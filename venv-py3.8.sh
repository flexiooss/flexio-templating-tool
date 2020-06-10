#!/usr/bin/env bash
set -e
if [ ! -f /usr/bin/python3.8 ]; then
    echo "Python 3.8 is required"
    exit 1
fi
python3.8 -m venv $PWD/venv
source $PWD/venv/bin/activate
python3.8 -m pip install --upgrade pip

set +e
python3.8 -m pip install -r requirements.txt
