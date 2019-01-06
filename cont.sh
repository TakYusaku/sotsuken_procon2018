#!/bin/sh

python3 ./tools/initCSV.py random QL
python3 ./tools/initCSV.py zeros MCM
python3 Learning.py li.csv

python3 ./tools/initCSV.py zeros QL
python3 ./tools/initCSV.py random MCM
python3 Learning.py li.csv
