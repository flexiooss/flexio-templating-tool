#!/usr/bin/env bash

OUTPUT_DIRECTORY=${PWD}


declare -a args=()
while [[ $# -gt 0 ]]
do
key="$1"

case ${key} in
    --dir)
    args+=(${key})
    args+=($(realpath $2))

    shift
    shift
    ;;
    --git)
    args+=(${key})
    args+=($2)
    shift
    shift
    ;;
    --args)
    args+=(${key})
    args+=($(realpath $2))
    shift
    shift
    ;;
    --out)
    OUTPUT_DIRECTORY=($(realpath $2))
    shift
    shift
    ;;
    *)
    echo unknown option "$key"
    exit 0
    ;;
esac
done

echo ${args[@]}
SCRIPT_DIR=$(dirname $(readlink -f $0))
source ${SCRIPT_DIR}/venv/bin/activate
python3.7 ${SCRIPT_DIR}/src/main.py "${args[@]}" --out ${OUTPUT_DIRECTORY}
deactivate