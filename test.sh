#!/usr/bin/env bash

if [[ "$#" -ne 3 ]]; then
    echo "usage : test.sh TEMPLATES_REPOSITORY ARGUMENTS_FILE OUTPUT_DIRECTORY"
    exit 1
fi

rm -rf $3
SCRIPT_DIR=$(dirname $(readlink -f $0))
${SCRIPT_DIR}/flexio-template-tool.sh --dir $1 --args $2 --out $3
