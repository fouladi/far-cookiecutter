from functools import lru_cache

from . import __version__ as _version
from .util import arg_setup, get_logger


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth Fibonacci number (memoized).

    Args:
        n (int): Non-negative integer index.

    Returns:
        int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main() -> None:
    log = get_logger()
    argpars = arg_setup()

    log.info(f"... Start with version: {_version}")

    if argpars.command == "fib":
        print(fib(argpars.number))
    elif argpars.command == "version":
        print(_version)
    else:
        print("\t\tUsage: run_{{cookiecutter.repo_name}}.sh -h\n")


if __name__ == "__main__":
    main()
