from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import fib
from {{cookiecutter.repo_name}}.util import log
from . import __version__ as _version
from .util import argpars, log

def main():
    log.info(f"... Start with version: {_version}")
    if argpars.command == 'feb':
        n = int(argpars.number)
        print(fib(n))
    elif argpars.command == 'version':
        print(_version)
    else:
        print("\t\tUsage: run_{{cookiecutter.repo_name}}.sh -h\n")

if __name__ == "__main__":
    main()
