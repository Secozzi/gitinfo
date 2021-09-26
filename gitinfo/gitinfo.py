from .utils import *
from anytree import RenderTree, ContRoundStyle
from rich.table import Table
from rich import print
import click


INFO_QUERY = """\
query($owner: String!, $repo: String!, $branch: String!) {
    repository(owner: $owner, name: $repo) {
    createdAt
    diskUsage
    forkCount
    isArchived
    isDisabled
    isFork
    isInOrganization
    isLocked
    isMirror
    isPrivate
    issues {totalCount}
    languages(
        first: 1
        orderBy: {field:SIZE direction:DESC}
    ) {nodes { name }}
    latestRelease {
      name
      url
    }
    licenseInfo { url spdxId }
    object(expression:$branch) {
    ... on Commit {
            history {
                totalCount
            }
        }
    }
    openIssues:issues(states:OPEN) { totalCount }
    owner { login url }
    closed_pr: pullRequests(states:CLOSED) {totalCount}
    merged_pr: pullRequests(states:MERGED) {totalCount}
    open_pr: pullRequests(states:OPEN) {totalCount}
    pushedAt
    stargazerCount
    updatedAt
    url
    watchers {totalCount}
    }
}
"""


LANG_QUERY = """\
query($owner: String!, $repo: String!) {
    repository(owner: $owner, name: $repo) {
        languages(
            first: 100
            orderBy: {field:SIZE direction:DESC}
        ){
            totalSize
            totalCount
            edges {
                node {name color}
                size
            }
        }
    }
}
"""


FILE_QUERY_1 = """\
query RepoFiles($owner: String!, $repo: String!, $path: String!) {
repository(owner: $owner, name: $repo) {
    defaultBranchRef { name }
    object(expression: $path) {
        ... on Tree {
            entries {
                name
                type
                object {
                    ... on Blob {
                        byteSize
                    }
"""


FILE_QUERY_2 = """\
                    }
                }
            }
        }
    }
}
"""


def Bool(input_bool: bool) -> str:
    if input_bool:
        return "[italic green]True[/]"
    else:
        return "[italic bright_red]False[/]"


def Number(input_num: int) -> str:
    return f"[magenta]{input_num}[/]"


def Date(input_date: str) -> str:
    return f"[#A9E190]{humanize_time(input_date)}[/]"


def Link(hyperlink: str, title: str) -> str:
    return f"[blue][link {hyperlink}]{title}[/]"


def Size(input_bytes: int) -> str:
    return f"[#3685B5]{human_size(input_bytes)}[/]"


@click.command()
@click.argument(
    "url", type=click.STRING, required=True, metavar="URL_OR_REPO_PATH"
)
@click.option(
    "--set-token", is_flag=True, default=False,
    help="Sets `url` to personal access token."
)
@click.option(
    "-l", "--long", is_flag=True, default=False,
    help="View more information."
)
@click.option(
    "-L", "--lang", is_flag=True, default=False,
    help="Show all languages of repo."
)
@click.option(
    "-f", "--file-tree", is_flag=True, default=False,
    help="Display files in a tree."
)
@click.option(
    "-p", "--path", type=click.STRING, default="", show_default=True,
    help="Set starting path for file tree relative to root (Github repo)."
)
@click.option(
    "-d", "--depth", type=click.IntRange(min=1), default=1, show_default=True,
    help="Depth to traverse file tree."
)
@click.option(
    "-c", "--collapse", is_flag=True, default=False,
    help="Collapse each file in file tree"
)
@click.option(
    "-b", "--branch", type=click.STRING, default="",
    help="Enter branch name or commit hash to view info or files from that specific branch/commit. Default is HEAD."
)
def main(url: str, **options) -> None:
    """
    Displays information on a Github repository.

    URL_OR_REPO_PATH must be either some form of Github Url or path
    starting with username and repo such as `user/repo/whatever`.
    """
    if options["set_token"]:
        set_token(url)

    token = get_token()
    owner, repo = get_url_info(url)
    query_variables = {
        "owner": owner,
        "repo": repo,
        "branch": f"{options['branch'] if options['branch'] else 'HEAD'}"
    }
    if options["file_tree"]:
        depth = ""
        for i in range(options["depth"] - 1):
            depth = f"... on Tree {{ entries {{ name type object {{... on Blob {{ byteSize }} {depth} }} }} }}"

        query_variables["path"] = f"{options['branch'] if options['branch'] else 'HEAD'}:{options['path']}"

        error, data, _ = get_data(FILE_QUERY_1 + depth + FILE_QUERY_2, token, query_variables)
        if error:
            print(data)
            return

        if not data["object"]:
            print("No files available")
            return
        entries = data["object"]["entries"]
        branch_name = data["defaultBranchRef"]["name"]

        entries = sort_entries(entries)
        path = (
            f"/{owner}"
            f"/{repo}"
            f"/tree"
            f"/{options['branch'] if options['branch'] else branch_name}"
            f"/{options['path']}"
        ) if options["path"] else f"/{owner}/{repo}"
        root = populate_tree(
            f"[blue link https://github.com{path}]{path}[/]",
            entries,
            options["collapse"]
        )

        for pre, fill, node in RenderTree(root, style=ContRoundStyle()):
            tree = "%s%s" % (pre, node.name)
            print(tree)

    elif options["lang"]:
        error, data, rate_limit = get_data(LANG_QUERY, token, query_variables)
        if error:
            print(data)
            return

        data = data["languages"]
        if not data["edges"]:
            print("Languages not available")
            return

        total_size = data["totalSize"]
        total_count = data["totalCount"]

        grid = Table(
            show_header=False,
            header_style=None,
            box=ROUNDED_BORDER,
            title=f'[green]{owner}/{repo}[/] - Ratelimit: [blue]{rate_limit}[/]'
        )

        langs = []
        matrix = []
        for lang in data["edges"]:
            langs.append(
                f"[{lang['node']['color'] if lang['node']['color'] else '#FFFFFF'}]"
                f"{lang['node']['name']}[/] - "
                f"{Number(round(100 * lang['size'] / total_size, 2))}%"
            )

        start = 0
        end = 3

        for i in range(total_count // 3 + 1):
            matrix.append(langs[start:end])
            start += 3
            end += 3

        for row in matrix:
            grid.add_row(*row)

        print(grid)
    else:
        error, data, rate_limit = get_data(INFO_QUERY, token, query_variables)
        if error:
            print(data)
            return

        grid = Table(
            show_header=False,
            header_style=None,
            box=ROUNDED_BORDER,
            title=f'[green]{owner}/{repo}[/] - Ratelimit: [blue]{rate_limit}[/]'
        )

        latestRelease = data["latestRelease"] or {
            "url": "",
            "name": "None"
        }

        licenseInfo = data["licenseInfo"] or {
            "url": "",
            "spdxId": "None"
        }

        if data['languages']['nodes']:
            language = data['languages']['nodes'][0]['name']
        else:
            language = "Not available"

        disk_usage = data["diskUsage"] or 0

        if data["object"]:
            commit_count = data['object']['history']['totalCount']
        else:
            commit_count = "Not available"

        if options["long"]:
            grid.add_row(
                f"Owner          - {Link(f'https://github.com/{owner}', owner)} ",
                f"Created at     - {Date(data['createdAt'])} ",
                f"Is archived - {Bool(data['isArchived'])} "
            )
            grid.add_row(
                f"URL            - {Link(data['url'], 'Link')} ",
                f"Updated at     - {Date(data['updatedAt'])} ",
                f"Is disabled - {Bool(data['isDisabled'])} "
            )
            grid.add_row(
                f"License        - {Link(licenseInfo['url'], licenseInfo['spdxId'])} ",
                f"Pushed at      - {Date(data['pushedAt'])} ",
                f"Is fork     - {Bool(data['isFork'])} "
            )
            grid.add_row(
                f"Latest Release - {Link(latestRelease['url'], latestRelease['name'])} ",
                f"Disk usage     - {Size(disk_usage * 1024)} ",
                f"Is in org.  - {Bool(data['isInOrganization'])} "
            )
            grid.add_row(
                f"Forks          - {Number(data['forkCount'])} ",
                f"Watchers       - {Number(data['watchers']['totalCount'])} ",
                f"Is locked   - {Bool(data['isLocked'])} "
            )
            grid.add_row(
                f"Star count     - {Number(data['stargazerCount'])} ",
                f"Open Issues    - {Number(data['openIssues']['totalCount'])} ",
                f"Is mirror   - {Bool(data['isMirror'])} "
            )
            grid.add_row(
                f"Commit count   - {Number(commit_count)} ",
                f"Closed Issues  - {Number(data['issues']['totalCount'] - data['openIssues']['totalCount'])}",
                f"Is private  - {Bool(data['isPrivate'])} "
            )
            grid.add_row(
                f"Open p.r.      - {Number(data['open_pr']['totalCount'])} ",
                f"Closed p.r.    - {Number(data['closed_pr']['totalCount'])} ",
                f"Merged p.r. - {Number(data['merged_pr']['totalCount'])} ",
            )
        else:
            grid.add_row(
                f"Owner    - {Link(f'https://github.com/{owner}', owner)} ",
                f"Disk usage - {Size(disk_usage * 1024)} ",
                f"Created at  - {Date(data['createdAt'])} ",
            )
            grid.add_row(
                f"URL      - {Link(data['url'], 'Link')} ",
                f"Stars      - {Number(data['stargazerCount'])} ",
                f"Updated at  - {Date(data['updatedAt'])} ",
            )
            grid.add_row(
                f"License  - {Link(licenseInfo['url'], licenseInfo['spdxId'])} ",
                f"Forks      - {Number(data['forkCount'])} ",
                f"Pushed at   - {Date(data['pushedAt'])} ",
            )
            grid.add_row(
                f"Language - [green]{language}[/] ",
                f"Watchers   - {Number(data['watchers']['totalCount'])} ",
                f"Open issues - {Number(data['openIssues']['totalCount'])} "
            )
        print(grid)
