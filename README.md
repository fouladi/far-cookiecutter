# Python far Cookiecutter

This Cookiecutter template creates Python projects from the project
templates.

## Features

* Supports `Python 3.7` and higher.
* Testing with [pytest](https://docs.pytest.org/en/latest/)
* Formatting with [yapf](https://github.com/google/yapf)
* Import sorting with [isort](https://github.com/timothycrosley/isort)
* Linting with [flake8](http://flake8.pycqa.org/en/latest/)

## Prerequisites

* Create projects swiftly from cookiecutters [cookiecutter](https://github.com/cookiecutter/cookiecutter)

## How to use it

Here you have to install first of all the `cookiecutter`. The following
steps are necessary:

```sh
# Install pipx if pipenv and cookiecutter are not installed
python -m pip install pipx
python -m pipx ensurepath

# Install cookiecutter using pipx
pipx install cookiecutter

# Use cookiecutter to create project from this template
cookiecutter gh:fouladi/far-cookiecutter

# Or

pipx run cookiecutter far-cookiecutter

# Enter project directory
cd <repo_name>

# Initialise git repo
git init

# Creating Virtual Environments with pyenv
pyenv virtualenv <python-version> <repo_name>

# Install requirements
pip install  -r requirements-dev.txt
```
