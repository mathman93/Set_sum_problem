#!/bin/bash

for entry in `ls input/`
do
  python3 solution_basic.py < input/$entry > diff.txt
  echo "Diff Against Official - $entry"
  diff diff.txt output/$entry
  rm diff.txt
  echo
  echo
done