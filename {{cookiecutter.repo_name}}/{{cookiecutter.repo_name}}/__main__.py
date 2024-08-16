from . import __version__ as _version
from .util import argpars, log


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def main() -> None:
    log.info(f"... Start with version: {_version}")
    if argpars.command == 'fib':
        n = int(argpars.number)
        print(fib(n))
    elif argpars.command == 'version':
        print(_version)
    else:
        print("\t\tUsage: run_{{cookiecutter.repo_name}}.sh -h\n")


if __name__ == "__main__":
    main()
