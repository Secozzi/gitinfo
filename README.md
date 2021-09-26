# gitinfo
Quickly get information about a Github repository

## Installation
Install via pip:
`pip install gitinfo`

Then set user token:
`gitinfo <token> --set-token`

If token is not set, the application will not work

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
  -c, --collapse             Collapse each file in file tree
  -b, --branch TEXT          Enter branch name or commit hash to view info or
                             files from that specific branch/commit. Default
                             is HEAD.

  --help                     Show this message and exit.
```

## Examples:

### Quick overview of a repository
`> gitinfo https://github.com/microsoft/vscode`

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
`> gitinfo microsoft/terminal -l`

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
`> gitinfo https://github.com/torvalds/linux.git -L`

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
`> gitinfo secozzi/gitinfo/useless_path/2 -f`

```
/secozzi/gitinfo
├── gitinfo/
├── .gitignore (1.76 KB)
├── LICENSE (1.04 KB)
├── README.md (9.21 KB)
├── requirements.txt (62 bytes)
╰── setup.py (1.08 KB)
```

### Collapsed file tree query
`> gitinfo microsoft/terminal -f -p src -c -d 3`

```
/microsoft/terminal/tree/main/src
├── buffer/
│   ├── out/
│   │   ├── lib/
│   │   ├── ut_textbuffer/
│   │   ╰── 40 Files (265.8 KB)
│   ╰── 1 Files (16 bytes)
├── cascadia/
│   ├── CascadiaPackage/
│   │   ├── ProfileIcons/
│   │   ├── Resources/
│   │   ╰── 5 Files (29.9 KB)
│   ├── inc/
│   │   ╰── 2 Files (13.5 KB)
│   ├── LocalTests_SettingsModel/
│   │   ╰── 13 Files (282.33 KB)
│   ├── LocalTests_TerminalApp/
│   │   ├── TestHostApp/
│   │   ╰── 11 Files (236.65 KB)
│   ├── PublicTerminalCore/
│   │   ╰── 6 Files (45.88 KB)
│   ├── Remoting/
│   │   ├── dll/
│   │   ├── Resources/
│   │   ╰── 29 Files (101.34 KB)
│   ├── ShellExtension/
│   │   ╰── 8 Files (15.39 KB)
│   ├── TerminalApp/
│   │   ├── dll/
│   │   ├── Resources/
│   │   ╰── 107 Files (767.14 KB)
│   ├── TerminalAzBridge/
│   │   ╰── 7 Files (11.67 KB)
│   ├── TerminalConnection/
│   │   ├── Resources/
│   │   ╰── 22 Files (92.95 KB)
│   ├── TerminalControl/
│   │   ├── dll/
│   │   ├── Resources/
│   │   ╰── 44 Files (337.36 KB)
│   ├── TerminalCore/
│   │   ├── lib/
│   │   ╰── 17 Files (160.0 KB)
│   ├── TerminalSettingsEditor/
│   │   ├── Resources/
│   │   ╰── 78 Files (362.91 KB)
│   ├── TerminalSettingsModel/
│   │   ├── dll/
│   │   ├── Resources/
│   │   ╰── 72 Files (577.3 KB)
│   ├── UnitTests_Control/
│   │   ╰── 8 Files (44.11 KB)
│   ├── UnitTests_Remoting/
│   │   ╰── 5 Files (113.24 KB)
│   ├── UnitTests_TerminalCore/
│   │   ╰── 12 Files (251.2 KB)
│   ├── ut_app/
│   │   ╰── 10 Files (97.22 KB)
│   ├── WindowsTerminal/
│   │   ╰── 20 Files (185.48 KB)
│   ├── WindowsTerminal_UIATests/
│   │   ├── Common/
│   │   ├── Elements/
│   │   ╰── 5 Files (17.22 KB)
│   ├── WindowsTerminalUniversal/
│   │   ├── Resources/
│   │   ╰── 9 Files (13.9 KB)
│   ├── WinRTUtils/
│   │   ├── inc/
│   │   ╰── 8 Files (9.62 KB)
│   ├── WpfTerminalControl/
│   │   ╰── 9 Files (52.29 KB)
│   ├── WpfTerminalTestNetCore/
│   │   ├── Properties/
│   │   ╰── 7 Files (8.45 KB)
│   ├── wt/
│   │   ╰── 4 Files (4.24 KB)
│   ╰── 1 Files (1.8 KB)
├── dep/
│   ├── fmt/
│   │   ╰── 2 Files (2.44 KB)
│   ╰── 1 Files (20 bytes)
├── host/
│   ├── exe/
│   │   ╰── 18 Files (69.7 KB)
│   ├── ft_fuzzer/
│   │   ╰── 2 Files (9.5 KB)
│   ├── ft_host/
│   │   ╰── 36 Files (1.98 MB)
│   ├── ft_integrity/
│   │   ╰── 7 Files (16.27 KB)
│   ├── ft_uia/
│   │   ├── Common/
│   │   ├── Elements/
│   │   ├── Properties/
│   │   ╰── 19 Files (170.31 KB)
│   ├── lib/
│   │   ╰── 3 Files (13.04 KB)
│   ├── proxy/
│   │   ╰── 7 Files (8.28 KB)
│   ├── ut_host/
│   │   ╰── 38 Files (860.07 KB)
│   ├── ut_lib/
│   │   ╰── 2 Files (1.72 KB)
│   ╰── 125 Files (1.26 MB)
├── inc/
│   ├── CppCoreCheck/
│   │   ╰── 1 Files (15.28 KB)
│   ├── test/
│   │   ╰── 1 Files (11.9 KB)
│   ├── til/
│   │   ╰── 17 Files (203.88 KB)
│   ╰── 21 Files (73.23 KB)
├── interactivity/
│   ├── base/
│   │   ├── lib/
│   │   ╰── 17 Files (52.91 KB)
│   ├── inc/
│   │   ╰── 13 Files (17.99 KB)
│   ├── onecore/
│   │   ├── lib/
│   │   ╰── 22 Files (60.92 KB)
│   ├── win32/
│   │   ├── lib/
│   │   ├── ut_interactivity_win32/
│   │   ╰── 45 Files (269.57 KB)
│   ╰── 1 Files (51 bytes)
├── internal/
│   ╰── 4 Files (2.84 KB)
├── propsheet/
│   ╰── 40 Files (325.37 KB)
├── propslib/
│   ╰── 14 Files (84.07 KB)
├── renderer/
│   ├── base/
│   │   ├── lib/
│   │   ╰── 14 Files (85.38 KB)
│   ├── dx/
│   │   ├── lib/
│   │   ├── ut_dx/
│   │   ╰── 17 Files (286.38 KB)
│   ├── gdi/
│   │   ├── lib/
│   │   ├── tool/
│   │   ╰── 9 Files (89.62 KB)
│   ├── inc/
│   │   ╰── 14 Files (25.69 KB)
│   ├── uia/
│   │   ├── lib/
│   │   ╰── 4 Files (18.44 KB)
│   ├── vt/
│   │   ├── lib/
│   │   ├── ut_lib/
│   │   ╰── 17 Files (131.63 KB)
│   ├── wddmcon/
│   │   ├── lib/
│   │   ╰── 8 Files (42.15 KB)
│   ╰── 1 Files (61 bytes)
├── server/
│   ├── lib/
│   │   ╰── 3 Files (8.52 KB)
│   ╰── 47 Files (253.16 KB)
├── staging/
│   ╰── 2 Files (443 bytes)
├── terminal/
│   ├── adapter/
│   │   ├── lib/
│   │   ├── ut_adapter/
│   │   ╰── 25 Files (231.67 KB)
│   ├── input/
│   │   ├── lib/
│   │   ╰── 8 Files (69.56 KB)
│   ├── parser/
│   │   ├── ft_fuzzer/
│   │   ├── ft_fuzzwrapper/
│   │   ├── lib/
│   │   ├── ut_parser/
│   │   ╰── 22 Files (207.95 KB)
│   ╰── 1 Files (45 bytes)
├── testlist/
│   ╰── 6 Files (2.18 KB)
├── til/
│   ├── ut_til/
│   │   ╰── 21 Files (202.93 KB)
│   ╰── 3 Files (1.87 KB)
├── tools/
│   ├── buffersize/
│   │   ╰── 3 Files (4.85 KB)
│   ├── closetest/
│   │   ╰── 5 Files (35.49 KB)
│   ├── ColorTool/
│   │   ├── ColorTool/
│   │   ├── schemes/
│   │   ├── signing/
│   │   ╰── 6 Files (11.73 KB)
│   ├── echokey/
│   │   ╰── 4 Files (12.87 KB)
│   ├── fontlist/
│   │   ╰── 3 Files (9.0 KB)
│   ├── integrity/
│   │   ├── exeuwp/
│   │   ├── exewin32/
│   │   ├── lib/
│   │   ├── packageuwp/
│   │   ╰── 1 Files (63 bytes)
│   ├── lnkd/
│   │   ╰── 5 Files (10.86 KB)
│   ├── MonarchPeasantPackage/
│   │   ├── Images/
│   │   ╰── 2 Files (6.03 KB)
│   ├── MonarchPeasantSample/
│   │   ╰── 18 Files (2.64 MB)
│   ├── nihilist/
│   │   ╰── 7 Files (4.91 KB)
│   ├── pixels/
│   │   ╰── 5 Files (13.66 KB)
│   ├── scratch/
│   │   ╰── 3 Files (2.29 KB)
│   ├── test/
│   │   ╰── 4 Files (3.44 KB)
│   ├── texttests/
│   │   ╰── 2 Files (568 bytes)
│   ├── U8U16Test/
│   │   ╰── 10 Files (59.96 KB)
│   ├── vtapp/
│   │   ├── Properties/
│   │   ╰── 8 Files (26.2 KB)
│   ├── vtpipeterm/
│   │   ╰── 7 Files (35.23 KB)
│   ├── vttests/
│   │   ╰── 4 Files (7.54 KB)
│   ╰── 1 Files (68 bytes)
├── tsf/
│   ╰── 19 Files (98.71 KB)
├── types/
│   ├── inc/
│   │   ╰── 12 Files (39.28 KB)
│   ├── lib/
│   │   ╰── 3 Files (9.73 KB)
│   ├── ut_types/
│   │   ╰── 6 Files (21.13 KB)
│   ╰── 38 Files (303.34 KB)
├── winconpty/
│   ├── dll/
│   │   ╰── 2 Files (3.02 KB)
│   ├── ft_pty/
│   │   ╰── 4 Files (20.42 KB)
│   ├── lib/
│   │   ╰── 1 Files (2.85 KB)
│   ╰── 5 Files (22.74 KB)
╰── 19 Files (64.4 KB)
```

### Complex file tree query
`> gitinfo sympy/sympy -f --branch 1.7 --path sympy/integrals --depth 4`

```
/sympy/sympy/tree/1.7/sympy/integrals
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