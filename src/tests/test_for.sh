#!/usr/bin/env bash

SCRIPT_DIR=$(dirname $(readlink -f $0))
ROOT=${SCRIPT_DIR}/../..
${ROOT}/test.sh ${ROOT}/src/tests ${ROOT}/src/tests/templates/template_test_for/test/test.json ${ROOT}/src/tests/templates/template_test_for/test/output
