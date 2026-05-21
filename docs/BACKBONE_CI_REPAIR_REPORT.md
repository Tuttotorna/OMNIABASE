# Backbone CI Repair Report

Repository: OMNIABASE

Timestamp UTC: 2026-05-21T19:05:35Z

Purpose:
Repair remaining red GitHub Actions caused by missing online backbone package installation.

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
      "id": 26246925546,
      "name": "CI",
      "status": "completed",
      "conclusion": "failure",
      "html_url": "https://github.com/Tuttotorna/OMNIABASE/actions/runs/26246925546",
      "created_at": "2026-05-21T19:00:34Z",
      "updated_at": "2026-05-21T19:00:58Z",
      "head_sha": "8f028aea40143d7ac0628a7185e8d4ba2d595a0f"
    }
  ]
}

Patch:
{
  "ci_changed": true,
  "legacy_non_dot_github_removed": [],
  "duplicate_test_workflows_removed": [],
  "python_version_policy": "3.12 only",
  "backbone_installs": {
    "OMNIA": true,
    "omnia-limit": true,
    "OMNIA-INVARIANCE": true
  },
  "required_omnia_doi_command_present": null
}

Local tests:
{
  "status": "pass",
  "passed": 9,
  "failed": 0,
  "errors": 0,
  "returncode": 0,
  "summary": "9 passed in 1.76s"
}

Push:
null

After online check:
null

After failed logs:
null
