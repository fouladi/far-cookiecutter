# Python far Cookiecutter

This Cookiecutter template creates Python projects from the project
templates.

## Features

* Supports `Python 3.12` and higher (configurable).
* Testing with [pytest](https://docs.pytest.org/en/latest/)
* Formatting and linting with [ruff](https://github.com/astral-sh/ruff)
* Type checking with [ty](https://github.com/astral-sh/ty)
* Git hooks via [pre-commit](https://pre-commit.com/) and [prek](https://github.com/fouladi/prek)
* Dev dependencies managed in `pyproject.toml` (`[dependency-groups]`)

## Prerequisites

* [cookiecutter](https://github.com/cookiecutter/cookiecutter)
* [jinja2-time](https://github.com/hackebrot/jinja2-time) — used to stamp the date in `CHANGELOG.md`

```sh
pip install jinja2-time
```

## Install and run `far-cookiecutter`

After installing [uv](https://github.com/astral-sh/uv), navigate to the
directory where you want to create your project and run:

```sh
uvx cookiecutter https://github.com/fouladi/far-cookiecutter
```

## Template variables

| Variable          | Default                  | Description                              |
|-------------------|--------------------------|------------------------------------------|
| `project_name`    | `Far Project`            | Human-readable project name              |
| `repo_name`       | *(derived)*              | Snake-case package/directory name        |
| `author`          | `John Doe`               | Author full name                         |
| `email`           | `j.doe@somewhere.com`    | Author email                             |
| `description`     | `A nice project…`        | Short project description                |
| `version`         | `0.1.0`                  | Initial version string                   |
| `python_version`  | `3.12`                   | Minimum Python version                   |
| `license`         | `MIT`                    | SPDX license identifier                  |
| `github_username` | `my-github-username`     | GitHub username for the homepage URL     |

## How to use it

Follow the on-screen prompts to configure your project. Once finished, a
new directory containing your project will be created.

```sh
# Enter project directory
cd <repo_name>

# Initialise git repo
git init

# Activate virtual environment
source .venv/bin/activate

# Install dependencies with uv
uv sync --group dev

# Optional: activate git-hook scripts
prek install
prek run
```
