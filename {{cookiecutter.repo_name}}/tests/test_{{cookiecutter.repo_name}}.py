import pytest

from {{cookiecutter.repo_name}}.__main__ import fib
from {{cookiecutter.repo_name}}.util import arg_setup


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


def test_fib_negative() -> None:
    with pytest.raises(ValueError):
        fib(-1)


def test_arg_setup_fib() -> None:
    args = arg_setup(["fib", "-n", "7"])
    assert args.command == "fib"
    assert args.number == 7


def test_arg_setup_version() -> None:
    args = arg_setup(["version"])
    assert args.command == "version"
