"""Utilities for logging and parameters setup"""

import logging
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from logging import Logger
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("log")


def log_setup(fname: str, logger_name: str) -> Logger:
    """Set up and return a configured logger with a rotating file
    handler.

    Args:
        fname (str): The name of the log file (e.g., 'app.log').
        logger_name (str): The name of the logger instance.

    Returns:
        Logger: A logger instance configured with a rotating file handler and formatter.
    """
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    log_path = LOG_DIR / fname
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        filename=log_path,
        mode="a",
        maxBytes=50 * 1024 * 1024,
        backupCount=10,
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s "
            "[%(module)s:%(funcName)s:%(lineno)d] %(threadName)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def arg_setup() -> Namespace:
    """Set up and parse command-line arguments using argparse.

    Returns:
        argparse.Namespace: The parsed arguments as a Namespace object.
    """
    pars = ArgumentParser(
        "{{cookiecutter.repo_name}}.py",
        usage="%(prog)s  {version} [options]",
        formatter_class=RawTextHelpFormatter,
        description="""
        Usage Examples:
        ---------------
            run_{{cookiecutter.repo_name}}.sh fib --number 5
        """,
    )

    subparsers = pars.add_subparsers(dest="command")

    subparsers.add_parser("version", help="Display version information")

    fib_parser = subparsers.add_parser("fib", help="Calculate Fibonacci number")
    fib_parser.add_argument("-n", "--number", help="Calculate Fibonacci number", required=True)

    return pars.parse_args()


log = log_setup("{{cookiecutter.repo_name}}.log", "{{cookiecutter.repo_name}}")
argpars = arg_setup()
