#!/usr/bin/env bash
set -e

CURRENT_PWD=$PWD
SCRIPT_DIR=$(dirname $(readlink -f $0))

if [ ! -f /usr/bin/python3.8 ]; then
    echo "Python 3.8 is required"
    exit 1
fi

cd ${SCRIPT_DIR}

python3.8 -m venv ${SCRIPT_DIR}/venv
source ${SCRIPT_DIR}/venv/bin/activate
python3.8 -m pip install --upgrade pip

set +e
python3.8 -m pip install -r ${SCRIPT_DIR}/requirements.txt

cd ${CURRENT_PWD}
