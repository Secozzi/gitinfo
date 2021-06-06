# gitinfo
Quickly get information about a Github repository

## Installation
`pip install gitinfo`

## Usage

```
Usage: gitinfo [OPTIONS] URL_OR_REPO_PATH

  Displays information on a Github repository.

  URL_OR_REPO_PATH must be either some form of Github Url or path starting
  with username and repo such as `user/repo/whatever`.

Options:
  --set-token                Sets `url` to personal access token.
  -l, --long                 View more information.
  -L, --lang                 Show all languages of repo.
  -f, --file-tree            Display files in a tree.
  -p, --path TEXT            Set starting path for file tree relative to root
                             (Github repo).  [default: ]

  -d, --depth INTEGER RANGE  Depth to traverse file tree.  [default: 1]
  -b, --branch TEXT          Enter branch name or commit hash to view files
                             from that specific branch/commit.  [default:
                             master]

  --help                     Show this message and exit.
```

## Examples:

### Quick overview of a repository
`gitinfo https://github.com/microsoft/vscode`

result:
```
                         microsoft/vscode - Ratelimit: 4941
╭──────────────────────────────────────────────────────────────────────────────────╮
│ Owner    - microsoft     Disk usage - 366.69 MB    Created at  - 5 Years ago     │
│ URL      - Link          Stars      - 116795       Updated at  - 54 Minutes ago  │
│ License  - MIT           Forks      - 19071        Pushed at   - 20 Minutes ago  │
│ Language - TypeScript    Watchers   - 3125         Open issues - 5337            │
╰──────────────────────────────────────────────────────────────────────────────────╯
```

### More detailed view:
`gitinfo microsoft/terminal -l`

```
                                    microsoft/terminal - Ratelimit: 4998
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Owner          - microsoft                       Created at     - 3 Years ago       Is archived - False  │
│ URL            - Link                            Updated at     - 49 Minutes ago    Is disabled - False  │
│ License        - MIT                             Pushed at      - 4 Hours ago       Is fork     - False  │
│ Latest Release - Windows Terminal v1.8.1444.0    Disk usage     - 92.08 MB          Is in org.  - True   │
│ Forks          - 6702                            Watchers       - 1313              Is locked   - False  │
│ Star count     - 74816                           Open Issues    - 1288              Is mirror   - False  │
│ Commit count   - 2274                            Closed Issues  - 6681              Is private  - False  │
│ Open p.r.      - 51                              Closed p.r.    - 260               Merged p.r. - 1973   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Language breakdown
`gitinfo https://github.com/torvalds/linux.git -L`

```
             torvalds/linux - Ratelimit: 4996
╭─────────────────────────────────────────────────────────╮
│ C - 98.15%            Assembly - 0.98%   Shell - 0.3%   │
│ Makefile - 0.23%      Perl - 0.12%       Python - 0.12% │
│ C++ - 0.02%           Roff - 0.02%       SmPL - 0.02%   │
│ Yacc - 0.01%          Lex - 0.01%        Awk - 0.0%     │
│ UnrealScript - 0.0%   Gherkin - 0.0%     Raku - 0.0%    │
│ M4 - 0.0%             Clojure - 0.0%     XS - 0.0%      │
│ sed - 0.0%                                              │
╰─────────────────────────────────────────────────────────╯
```

### Simple file tree query
`gitinfo secozzi/gitinfo/useless_path/2 -f`

```
./
├── gitinfo/
├── .gitignore (1.76 KB)
├── LICENSE (1.04 KB)
├── README.md (75 bytes)
╰── setup.py (309 bytes)
```

### Advanced file tree query
`gitinfo sympy/sympy -f --branch 1.7 --path sympy/integrals --depth 4`

```
./sympy/integrals/
├── benchmarks/
│   ├── __init__.py (0 bytes)
│   ├── bench_integrate.py (295 bytes)
│   ╰── bench_trigintegrate.py (241 bytes)
├── rubi/
│   ├── parsetools/
│   │   ├── tests/
│   │   │   ├── __init__.py (0 bytes)
│   │   │   ╰── test_parse.py (8.02 KB)
│   │   ├── __init__.py (0 bytes)
│   │   ├── generate_rules.py (2.77 KB)
│   │   ├── generate_tests.py (2.64 KB)
│   │   ├── header.py.txt (9.15 KB)
│   │   ╰── parse.py (26.99 KB)
│   ├── rubi_tests/
│   │   ├── tests/
│   │   │   ├── __init__.py (0 bytes)
│   │   │   ├── test_1_2.py (29.71 KB)
│   │   │   ├── test_1_3.py (59.75 KB)
│   │   │   ├── test_1_4.py (10.18 KB)
│   │   │   ├── test_exponential.py (245.08 KB)
│   │   │   ├── test_hyperbolic_sine.py (77.69 KB)
│   │   │   ├── test_inverse_hyperbolic_sine.py (63.64 KB)
│   │   │   ├── test_inverse_sine.py (82.23 KB)
│   │   │   ├── test_logarithms.py (431.76 KB)
│   │   │   ├── test_miscellaneous_algebra.py (513.84 KB)
│   │   │   ├── test_secant.py (91.21 KB)
│   │   │   ├── test_sine.py (160.52 KB)
│   │   │   ├── test_special_functions.py (47.21 KB)
│   │   │   ├── test_tangent.py (129.27 KB)
│   │   │   ╰── test_trinomials.py (1.44 MB)
│   │   ╰── __init__.py (293 bytes)
│   ├── rules/
│   │   ├── __init__.py (0 bytes)
│   │   ├── binomial_products.py (194.5 KB)
│   │   ├── exponential.py (61.4 KB)
│   │   ├── hyperbolic.py (212.89 KB)
│   │   ├── integrand_simplification.py (22.64 KB)
│   │   ├── inverse_hyperbolic.py (342.67 KB)
│   │   ├── inverse_trig.py (309.75 KB)
│   │   ├── linear_products.py (89.41 KB)
│   │   ├── logarithms.py (95.54 KB)
│   │   ├── miscellaneous_algebraic.py (227.17 KB)
│   │   ├── miscellaneous_integration.py (49.38 KB)
│   │   ├── miscellaneous_trig.py (184.83 KB)
│   │   ├── piecewise_linear.py (19.43 KB)
│   │   ├── quadratic_products.py (309.78 KB)
│   │   ├── secant.py (440.04 KB)
│   │   ├── sine.py (716.0 KB)
│   │   ├── special_functions.py (87.32 KB)
│   │   ├── tangent.py (306.98 KB)
│   │   ╰── trinomial_products.py (236.89 KB)
│   ├── tests/
│   │   ├── __init__.py (0 bytes)
│   │   ├── test_rubi_integrate.py (2.62 KB)
│   │   ╰── test_utility_function.py (79.7 KB)
│   ├── __init__.py (3.38 KB)
│   ├── constraints.py (288.21 KB)
│   ├── rubimain.py (7.91 KB)
│   ├── symbol.py (1.56 KB)
│   ╰── utility_function.py (262.95 KB)
├── tests/
│   ├── __init__.py (0 bytes)
│   ├── test_deltafunctions.py (3.41 KB)
│   ├── test_failing_integrals.py (6.7 KB)
│   ├── test_heurisch.py (10.96 KB)
│   ├── test_integrals.py (61.09 KB)
│   ├── test_intpoly.py (35.32 KB)
│   ├── test_lineintegrals.py (235 bytes)
│   ├── test_manual.py (25.3 KB)
│   ├── test_meijerint.py (29.49 KB)
│   ├── test_prde.py (15.56 KB)
│   ├── test_quadrature.py (19.45 KB)
│   ├── test_rationaltools.py (4.86 KB)
│   ├── test_rde.py (9.27 KB)
│   ├── test_risch.py (36.37 KB)
│   ├── test_singularityfunctions.py (1.14 KB)
│   ├── test_transforms.py (34.6 KB)
│   ╰── test_trigonometry.py (3.78 KB)
├── __init__.py (1.8 KB)
├── deltafunctions.py (7.18 KB)
├── heurisch.py (24.69 KB)
├── integrals.py (62.55 KB)
├── intpoly.py (41.56 KB)
├── manualintegrate.py (61.75 KB)
├── meijerint.py (76.11 KB)
├── meijerint_doc.py (1.0 KB)
├── prde.py (50.01 KB)
├── quadrature.py (16.26 KB)
├── rationaltools.py (10.15 KB)
├── rde.py (26.04 KB)
├── risch.py (64.95 KB)
├── singularityfunctions.py (2.24 KB)
├── transforms.py (61.87 KB)
╰── trigonometry.py (10.79 KB)
```