#! /bin/bash
# Description: Wrapper script for '{{cookiecutter.repo_name}}'
# application. See help with -h
SCRIPT_DIR=$(cd $(dirname $0) && pwd)
cd "$SCRIPT_DIR"

if ! python -m {{cookiecutter.repo_name}} "$@" ; then
    echo "Error in {{cookiecutter.repo_name}} - System stopped!"
    exit 1  # application ended unsuccessfully
fi
