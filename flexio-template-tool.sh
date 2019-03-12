#!/usr/bin/env bash

OUTPUT_DIRECTORY=${PWD}

args=( "$@" )
if [[ "$1" = "--dir" || "$1" = "--args" ]]; then
    args[1]=$(realpath $2)
fi

if [[ "$3" = "--dir" || "$3" = "--args" ]]; then
    args[3]=$(realpath $4)
fi

SCRIPT_DIR=$(dirname $(readlink -f $0))
source ${SCRIPT_DIR}/venv/bin/activate
python3.7 ${SCRIPT_DIR}/src/main.py "${args[@]}" --out ${OUTPUT_DIRECTORY}
deactivate