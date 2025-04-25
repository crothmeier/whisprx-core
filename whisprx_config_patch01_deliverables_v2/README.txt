
Whisprx Config-Patch-01 Deliverables
====================================

Contents
--------
1. performance_presets.yaml  - New performance preset configuration file.
2. config_patch_01.diff      - Unified diff covering all modified / new files.
3. MR_description.md         - Merge request description / release notes.
4. test_tts_split.py         - Unit tests for the new sentence splitting helper.
5. README.txt                - This file.

Usage
-----
* Apply the diff on top of the 'staging' branch.
* Drop performance_presets.yaml into the `config/` directory.
* Run `pytest -q` to ensure all tests (including test_tts_split.py) pass.
* Run flake8 to verify zero lint warnings.
* Create the MR in GitLab and paste MR_description.md as the body.

Generated: 2025-04-25T01:24:32Z
