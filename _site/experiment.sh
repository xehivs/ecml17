#!/bin/bash
# Script to do the experiment.
clear
filename=$1
if [ -f $filename ]
then
  prefix="${filename%.*}"

  # Run experiments
  START=$(date +%s)
  python -u $1 | tee logs/$prefix.log
  END=$(date +%s)
  DIFF=$(echo "$END - $START" | bc)
  echo "Processing took $DIFF seconds"

else
  echo "There is not such a file $1"
fi
