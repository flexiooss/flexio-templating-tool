#!/usr/bin/env bash

SCRIPT_DIR=$(dirname $(readlink -f $0))
ROOT=${SCRIPT_DIR}/../..

${ROOT}/test.sh ${ROOT} ${ROOT}/templates/new_template/test/test.json