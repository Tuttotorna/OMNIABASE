# Second-Pass Online CI Repair Report

Repository: OMNIABASE

Timestamp UTC: 2026-05-21T18:58:19Z

Purpose:
Repair remaining red GitHub Actions after first ecosystem CI repair.

No release was created.
No tag was created.
Only CI workflow files and this repair report were changed.

Boundary:
measurement != inference != decision

Before:
{
  "green": false,
  "status": "failed",
  "reason": "At least one Actions run for current HEAD failed.",
  "runs": [
    {
      "id": 26246552081,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIABASE/actions/runs/26246552081",
      "created_at": "2026-05-21T18:53:16Z",
      "updated_at": "2026-05-21T18:53:39Z",
      "head_sha": "610834542708eeedea45a9818adf493829068e45"
    }
  ]
}

Failed online log samples before repair:
{
  "ok": true,
  "failed_runs": [
    {
      "id": 26246552081,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIABASE/actions/runs/26246552081",
      "created_at": "2026-05-21T18:53:16Z",
      "updated_at": "2026-05-21T18:53:39Z",
      "head_sha": "610834542708eeedea45a9818adf493829068e45"
    }
  ],
  "samples": [
    {
      "run_id": 26246552081,
      "download_ok": true,
      "html_url": "https://github.com/Tuttotorna/OMNIABASE/actions/runs/26246552081",
      "samples": [
        {
          "file": "0_test _ python-3.11.txt",
          "lines": [
            "2026-05-21T18:53:23.4370071Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:24.7583267Z Collecting pytest",
            "2026-05-21T18:53:24.8130874Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:25.1908035Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:25.2093117Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:25.2258391Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:25.2481728Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:26.1221634Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:26.5038676Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:32.2315330Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0",
            "2026-05-21T18:53:34.4955383Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:35.1519423Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:35.1520156Z _______________ ERROR collecting tests/test_backbone_adapter.py ________________",
            "2026-05-21T18:53:35.1521262Z ImportError while importing test module '/home/runner/work/OMNIABASE/OMNIABASE/tests/test_backbone_adapter.py'.",
            "2026-05-21T18:53:35.1522915Z Traceback:",
            "2026-05-21T18:53:35.1528983Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:35.1530139Z ERROR tests/test_backbone_adapter.py",
            "2026-05-21T18:53:35.1530708Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:35.1531289Z 1 error in 0.17s",
            "2026-05-21T18:53:35.1727214Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "1_test _ python-3.12.txt",
          "lines": [
            "2026-05-21T18:53:23.1412996Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:26.3892053Z Collecting pytest",
            "2026-05-21T18:53:26.4514613Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:26.8406517Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:26.8587648Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:26.8747364Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:26.8967398Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:27.7780277Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:28.1844705Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:34.6540731Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0",
            "2026-05-21T18:53:37.1653056Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:37.7694108Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:37.7694894Z _______________ ERROR collecting tests/test_backbone_adapter.py ________________",
            "2026-05-21T18:53:37.7695958Z ImportError while importing test module '/home/runner/work/OMNIABASE/OMNIABASE/tests/test_backbone_adapter.py'.",
            "2026-05-21T18:53:37.7698910Z Traceback:",
            "2026-05-21T18:53:37.7708348Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:37.7710258Z ERROR tests/test_backbone_adapter.py",
            "2026-05-21T18:53:37.7711185Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:37.7712145Z 1 error in 0.14s",
            "2026-05-21T18:53:37.7953354Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "test _ python-3.11/4_Install tooling.txt",
          "lines": [
            "2026-05-21T18:53:23.4370060Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:24.7583207Z Collecting pytest",
            "2026-05-21T18:53:24.8130841Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:25.1907992Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:25.2093072Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:25.2258348Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:25.2481686Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:26.1221622Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:26.5038631Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:32.2314982Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0"
          ]
        },
        {
          "file": "test _ python-3.11/6_Run tests when tests exist.txt",
          "lines": [
            "2026-05-21T18:53:34.4955380Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:35.1519417Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:35.1520151Z _______________ ERROR collecting tests/test_backbone_adapter.py ________________",
            "2026-05-21T18:53:35.1521256Z ImportError while importing test module '/home/runner/work/OMNIABASE/OMNIABASE/tests/test_backbone_adapter.py'.",
            "2026-05-21T18:53:35.1522911Z Traceback:",
            "2026-05-21T18:53:35.1528979Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:35.1530134Z ERROR tests/test_backbone_adapter.py",
            "2026-05-21T18:53:35.1530697Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:35.1531284Z 1 error in 0.17s",
            "2026-05-21T18:53:35.1727195Z ##[error]Process completed with exit code 2."
          ]
        },
        {
          "file": "test _ python-3.12/4_Install tooling.txt",
          "lines": [
            "2026-05-21T18:53:23.1412983Z \u001b[36;1mpython -m pip install pytest numpy matplotlib jsonschema\u001b[0m",
            "2026-05-21T18:53:26.3891955Z Collecting pytest",
            "2026-05-21T18:53:26.4514572Z   Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)",
            "2026-05-21T18:53:26.8406491Z Collecting iniconfig>=1.0.1 (from pytest)",
            "2026-05-21T18:53:26.8587624Z Collecting packaging>=22 (from pytest)",
            "2026-05-21T18:53:26.8747329Z Collecting pluggy<2,>=1.5 (from pytest)",
            "2026-05-21T18:53:26.8967374Z Collecting pygments>=2.7.2 (from pytest)",
            "2026-05-21T18:53:27.7780261Z Downloading pytest-9.0.3-py3-none-any.whl (375 kB)",
            "2026-05-21T18:53:28.1844683Z Installing collected packages: typing-extensions, six, rpds-py, pyparsing, pygments, pluggy, pillow, packaging, numpy, kiwisolver, iniconfig, fonttools, cycler, attrs, referencing, python-dateutil, pytest, contourpy, matplotlib, jsonschema-specifications, jsonschema",
            "2026-05-21T18:53:34.6540445Z Successfully installed attrs-26.1.0 contourpy-1.3.3 cycler-0.12.1 fonttools-4.63.0 iniconfig-2.3.0 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 kiwisolver-1.5.0 matplotlib-3.10.9 numpy-2.4.6 packaging-26.2 pillow-12.2.0 pluggy-1.6.0 pygments-2.20.0 pyparsing-3.3.2 pytest-9.0.3 python-dateutil-2.9.0.post0 referencing-0.37.0 rpds-py-0.30.0 six-1.17.0 typing-extensions-4.15.0"
          ]
        },
        {
          "file": "test _ python-3.12/6_Run tests when tests exist.txt",
          "lines": [
            "2026-05-21T18:53:37.1653053Z \u001b[36;1m  python -m pytest -q\u001b[0m",
            "2026-05-21T18:53:37.7694101Z ==================================== ERRORS ====================================",
            "2026-05-21T18:53:37.7694876Z _______________ ERROR collecting tests/test_backbone_adapter.py ________________",
            "2026-05-21T18:53:37.7695952Z ImportError while importing test module '/home/runner/work/OMNIABASE/OMNIABASE/tests/test_backbone_adapter.py'.",
            "2026-05-21T18:53:37.7698905Z Traceback:",
            "2026-05-21T18:53:37.7708343Z E   ModuleNotFoundError: No module named 'omnia'",
            "2026-05-21T18:53:37.7710254Z ERROR tests/test_backbone_adapter.py",
            "2026-05-21T18:53:37.7711180Z !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!",
            "2026-05-21T18:53:37.7712140Z 1 error in 0.14s",
            "2026-05-21T18:53:37.7953338Z ##[error]Process completed with exit code 2."
          ]
        }
      ]
    }
  ]
}

Patch:
{
  "ci_changed": true,
  "legacy_non_dot_github_removed": [],
  "duplicate_test_workflows_removed": [],
  "python_version_policy": "3.12 only",
  "omnia_required_doi_command_present": null
}

Local tests:
{
  "status": "pass",
  "passed": 9,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "9 passed in 1.79s"
}

Push:
null

After online check:
null
