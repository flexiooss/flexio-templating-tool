#!/usr/bin/env bash

if [[ "$#" -ne 2 ]]; then
    echo "usage : test.sh TEMPLATES_REPOSITORY ARGUMENTS_FILE"
fi

SCRIPT_DIR=$(dirname $(readlink -f $0))
${SCRIPT_DIR}/flexio-template-tool.sh --dir $1 --args $2