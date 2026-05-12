# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Setup

```sh
# Initialise git repo
git init

# Create and activate a virtual environment (example using pyenv)
pyenv virtualenv {{cookiecutter.python_version}} {{cookiecutter.repo_name}}
pyenv activate {{cookiecutter.repo_name}}

# Install all dependencies (runtime + dev) using uv
uv sync --group dev

# Or, without uv, install manually
pip install -r requirements.txt
pip install ruff ty pytest pytest-cov pytest-mock prek
```

## Run

```sh
./run_{{cookiecutter.repo_name}}.sh fib -n 23

# Or run directly with Python:
python -m {{cookiecutter.repo_name}} fib -n 23
```

## Test

```sh
pytest

# With coverage:
pytest --cov
```

## Lint & Format

```sh
ruff check .
ruff format .
```

## Git Hooks (optional)

[prek](https://github.com/fouladi/prek) wraps pre-commit for a simpler workflow:

```sh
prek install
prek run
```
