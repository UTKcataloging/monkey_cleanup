#!/usr/bin/env bash

git clone https://github.com/markpbaggett/py_update_solr_with_gsearch || exit
cd py_update_solr_with_gsearch
python pygrabfedoraobjects.py -l porter.lib.utk.edu -f monkey-pids -p "scopes"

