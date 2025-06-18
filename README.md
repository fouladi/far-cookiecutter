# Python far Cookiecutter

This Cookiecutter template creates Python projects from the project
templates.

## Features

* Supports `Python 3.7` and higher.
* Testing with [pytest](https://docs.pytest.org/en/latest/)
* Formatting and Linting with [ruff](https://github.com/astral-sh/ruff)

## Prerequisites

* Create projects swiftly from cookiecutters [cookiecutter](https://github.com/cookiecutter/cookiecutter)

## Install and run `far-cookiecutter`

### Option 1: Using `uv`

Navigate to the directory on your local machine in which you want to
create a project directory, and then run the following command:

```sh
uvx cookiecutter https://github.com/fouladi/far-cookiecutter
```

### Option 2: Using `pipx`

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
```

## How to use it

Follow the on-screen prompts to configure your project. Once you have
finished, a new directory containing your project will be created.

* Enter project directory

```sh
cd <repo_name>
```

* Initialise git repo

```sh
git init
```

* Creating Virtual Environments with `pyenv`

```sh
pyenv virtualenv <python-version> <repo_name>
```

* Install requirements

```sh
pip install  -r requirements-dev.txt
```
