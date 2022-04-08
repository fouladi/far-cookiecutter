# Python far Cookiecutter

This Cookiecutter template creates Python projects from project
templates.

## Features
- Supports Python 3.7 and higher.
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [yapf](https://github.com/google/yapf)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)

## How to use it
```sh
# Install pipx if pipenv and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

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
