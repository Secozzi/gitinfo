from __future__ import annotations
from anytree import NodeMixin
from datetime import datetime, timezone
from dotenv import load_dotenv
from os import environ
from os.path import join, dirname
from typing import Tuple, List, Any, Dict, Optional
import re
import requests
from rich.box import Box


__all__ = [
    "get_data", "get_token", "get_url_info", "human_size", "humanize_time",
    "populate_tree", "ROUNDED_BORDER", "run_query", "set_token", "sort_entries"
]


ROUNDED_BORDER: Box = Box(
    """\
╭──╮
│  │
│  │
│  │
│  │
│  │
│  │
╰──╯
"""
)


def get_token() -> str:
    """
    Retrieves the Github Personal Access Token from .env file
    """
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    return environ.get("GITSORT_TOKEN")


def set_token(token: str) -> None:
    """
    Set your Github personal access token in order to access
    private repositories and extend the usage of the GraphQL API.
    """
    import os
    from dotenv import load_dotenv
    from os.path import join, dirname

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    gitsort_token = os.environ.get("GITSORT_TOKEN")
    if not gitsort_token:
        with open(dotenv_path, "w") as f:
            f.write(f"GITSORT_TOKEN={token}")
        print("Github Token set!")
    else:
        inp = input("Github token already set! Do you want to update it? [y/n] ").lower()
        while inp not in ["y", "n"]:
            print("Invalid answer")
            inp = input("Github token already set! Do you want to update it? [y/n] ").lower()
        if inp == "y":
            with open(dotenv_path, "w") as f:
                f.write(f"GITSORT_TOKEN={token}")
            print("Github Token updated!")


def run_query(
    query: str,
    token: str,
    variables: dict | None = None,
    headers: dict | None = None
) -> Tuple[dict, str]:
    """
    Runs a Github GraphQL query and returns the result

    :param query: str
        GraphQL query
    :param token: str
        The users Github Personal Access Token
    :param variables: dict
        GraphQL Variables
    :param headers: dict
        Request headers
    :return: tuple
        The response and rate limit
    """
    if not headers:
        headers = {"Authorization": f"Bearer {token}"}

    request = requests.post(
        'https://api.github.com/graphql',
        json={'query': query, 'variables': variables},
        headers=headers
    )
    if request.status_code == 200:
        return request.json(), request.headers["X-RateLimit-Remaining"]
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_data(
    query: str,
    token: str,
    query_variables: Dict[str, str]
) -> Tuple[bool, Any, str]:
    """
    Get data from query

    :param query: str
        Graphql Query
    :param token: str
        Github Personal Access Token
    :param query_variables: dict
        Variables used in query
    :return: tuple
        returns a tuple of tree items:
        0. bool: True if query failed and return error messages else False
        1. Any: Data returned from query
        2. str: Rate limit
    """
    data, rate_limit = run_query(query, token, query_variables)
    if list(data.keys())[0] == "errors":
        return True, data["errors"][0]["message"], rate_limit
    try:
        return False, data["data"]["repository"], rate_limit
    except TypeError:
        return True, "Query failed. Make sure path and branch is valid.", rate_limit


def get_url_info(url: str) -> Tuple[str, str] | List[str]:
    """
    Retrieves owner and repository from a string

    :param url: str
        Either some form of Github Url or path such as `user/repo/whatever`
    :return: tuple | list
        Tuple containing owner and repo
    """
    is_link = re.compile(r"^(git(hub)?|https?)")
    is_git_path = re.compile(r"^[a-zA-Z0-9\-_.]+/[a-zA-Z0-9\-_.]+")
    git_url_regex = re.compile(r"^(https|git)?(://|@)?([^/:]+)[/:](?P<owner>[^/:]+)/(?P<name>.+)(.git)?$")
    is_git_repo = re.compile(r"((.git)|/)$")

    if is_link.match(url):
        if is_git_path.match(url):
            return url.split("/")[:2]

        match = git_url_regex.match(url)
        if not match:
            raise Exception("Invalid path")

        name = match.group("name").split("/")[0]
        name = is_git_repo.sub("", name)
        owner = match.group("owner")

        return owner, name
    else:
        if url.count("/") > 0:
            return url.split("/")[:2]
        raise Exception("Link/path must contain both user and repo")


def humanize_time(time_str: str) -> str:
    """
    Convert datetime into a more human-friendly format

    :param time_str: str
        Time string in the ISO 8601 format
    :return: str
        Human friendly format: <number> <time_period> ago
    """
    if not time_str:
        return "null"

    now = datetime.now()
    date = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    date = date.replace(tzinfo=timezone.utc)

    diff = int(now.timestamp() - date.timestamp())
    times = [
        1, 60, 3600, 86400, 604800, 2629746, 31556925
    ]
    times_str = [
        "Second", "Minute", "Hour", "Day", "Week", "Month", "Year"
    ]
    temp = [diff // t for t in times][::-1]
    for i, t in enumerate(temp):
        if t != 0:
            return f"{t} {times_str[6-i]}{'' if t == 1 else 's'} ago"


def human_size(bytes: int | float, units: Optional[List[str]] = None) -> str:
    """
    Convert bytes into a more human-friendly format

    :param bytes: int
        Number of bytes
    :param units: Optional[List[str]]
        units used
    :return: str
        Return size in human friendly format: <number> <size_unit>
    """
    if units is None:
        units = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']
    return f"{round(bytes, 2)} " + units[0] if bytes < 1024 else human_size(bytes / 1024, units[1:])


class FileEntry(NodeMixin):
    def __init__(
        self,
        name: str,
        size: str | int = None,
        parent=None,
        children=None
    ) -> None:
        super(FileEntry, self).__init__()

        if size != None:
            self.name = f"{name} ([green]{human_size(size)}[/])"
        else:
            self.name = f"[blue]{name}/[/]"

        self.parent = parent
        if children:
            self.children = children


class FileEntryRoot(NodeMixin):
    def __init__(self, name: str, parent=None, children=None):
        super(FileEntryRoot, self).__init__()

        self.name = name
        self.parent = parent
        if children:
            self.children = children


def populate_tree(
    root_name: str,
    data: list,
    collapse_blobs: bool = False
) -> "anytree.Node":
    """
    Populate the tree
    :param root_name: str
        Name of root node
    :param data: dict
        Data
    :param collapse_blobs: bool
        Collapse files or not
    :return: anytree.node
    """
    root = FileEntryRoot(root_name)

    def edges(tree: FileEntry | FileEntryRoot, parent=None):
        collapsed_count = 0
        collapsed_size = 0

        for entry in tree:
            if entry["type"] == "blob":
                if collapse_blobs:
                    collapsed_size += entry["object"]["byteSize"]
                    collapsed_count += 1
                else:
                    _ = FileEntry(entry["name"], entry["object"]["byteSize"], parent=parent)
            else:
                node = FileEntry(entry["name"], parent=parent)
                if entry["object"]:
                    edges(entry["object"]["entries"], parent=node)

        if collapse_blobs:
            _ = FileEntry(f"[orange1]{collapsed_count}[/] Files", collapsed_size, parent=parent)

    edges(data, root)
    return root


class Reversor:
    def __init__(self, obj: Any) -> None:
        self.obj = obj

    def __eq__(self, other: Any) -> bool:
        return other.obj == self.obj

    def __lt__(self, other: Any) -> bool:
        return other.obj < self.obj


def sort_entries(entries: List[Any]) -> List[Any]:
    """
    Recursively sort the data first based on type
    then alphabetically

    :param entries: list
        Entries
    :return: list
        Entries but sorted
    """
    entries = sorted(
        entries, key=lambda x: (
            Reversor(x["type"]),    # First sort by type (reversed)
            x["name"].lower()       # Then sort by alphabetical
        )
    )
    for entry in entries:
        if entry["type"] == "tree" and entry["object"]:
            entry["object"]["entries"] = sort_entries(entry["object"]["entries"])
    return entries
