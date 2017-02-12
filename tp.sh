#!/bin/bash

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -a|--algo)
    ALGO="$2"
    shift
    ;;
    -e|--ex_path)
    EX_PATH="$2"
    shift
    ;;
    -s|--seuil)
    SEUIL="$2"
    shift
    ;;
    -p|--print|-t|--time|-h|--help)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

python3 ./tp1_inf4XXX.py $EX_PATH $ALGO $SEUIL $OPTIONS
