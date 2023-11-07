# git hooks

This directory contains all git hooks. 


# Installation

See Installation section in `../README.md`

## Usage

The commit hooks are build with a custom script `hooks-commitizen.py` and with the package [pre-commit](https://pre-commit.com/)

The `.pre-commit-config.yaml` contains the configuration for static code checks like yapf, pylint or isort.

The `hooks-commitizen.py` contains the interactive questioner to build the commit message


### Skip git hooks

You can skip a stage inside the commit hooks by setting the `SKIP` variable before the git commit command e.g.:
```bash
SKIP=pylint git commit
```
Additional information under https://pre-commit.com/#temporarily-disabling-hooks
