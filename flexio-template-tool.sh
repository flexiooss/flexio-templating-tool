#!/usr/bin/env bash

OUTPUT_DIRECTORY=${PWD}

args=( "$@" )
if [[ "$1" = "--dir" ]]; then
    args[1]=$(realpath $2)
fi

SCRIPT_DIR=$(dirname $(readlink -f $0))
cd ${SCRIPT_DIR}
python3 ${SCRIPT_DIR}/src/main.py "${args[@]}" --out ${OUTPUT_DIRECTORY}
