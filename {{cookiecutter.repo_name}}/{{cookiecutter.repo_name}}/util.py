"""utilities for logging and parameters setup"""
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
from logging.handlers import RotatingFileHandler


def log_setup(fname, logger):
    """Logging setup for a rotating logger in 'log/' directory

    Arguments:
    fname   : name of log file
    logger  : name of logger
    """

    filename = "log/" + fname
    _log = logging.getLogger(logger)
    _log.setLevel(logging.INFO)
    handler = RotatingFileHandler(filename,
                                  mode='a',
                                  maxBytes=50 * 1024 * 1024,
                                  backupCount=10)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(module)s:%(funcName)s:%(lineno)d] %(threadName)s'
    )
    handler.setFormatter(formatter)
    _log.addHandler(handler)
    return _log


def arg_setup():
    """Parse all input arguments."""

    pars = ArgumentParser('{{cookiecutter.repo_name}}.py',
                          usage='%(prog)s  {version} [options]',
                          formatter_class=RawTextHelpFormatter,
                          description="""
        Usage Examples:
        ---------------
            run_{{cookiecutter.repo_name}}.sh feb --number 5
            """)
    subparsers = pars.add_subparsers(dest='command')

    _ = subparsers.add_parser('version', help='Version')
    feb_parser = subparsers.add_parser('feb', help='Version')
    feb_parser.add_argument('-n',
                            '--number',
                            help='Calculate Fibonnaci Number',
                            required=True)
    return pars.parse_args()


log = log_setup("{{cookiecutter.repo_name}}.log", "{{cookiecutter.repo_name}}")
argpars = arg_setup()
