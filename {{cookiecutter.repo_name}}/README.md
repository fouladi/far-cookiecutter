# {{cookiecutter.project_name}}

## Setup

```sh
# Initialise git repo
git init

# Creating Virtual Environments with pyenv
pyenv virtualenv <python-version> {{cookiecutter.repo_name}}

# Install requirements
pip install  -r requirements-dev.txt
```

## Start Program

```sh
./run_{{cookiecutter.repo_name}}.sh feb -n 23

# Or if you want to run with Python directly:

python -m {{cookiecutter.repo_name}} feb -n 23
```

## Start Unit Tests

```sh
pytest
```

## Credits

* Farhad Fouladi
