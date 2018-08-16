#!/usr/bin/env bash

# Variables
BROWN=../brown.txt
BROWN_CLEAN=./brown_clean.txt


tr '[:upper:]' '[:lower:]' < $BROWN | # lowercase
    sed -r 's/[^a-z ]//g' | # remove non-ascii, non-period, non-space
    sed -r 's/ [ ]+/ /g' | # remove multiple consecutive space characters
    sed -r 's/^ //g' | # remove leading spaces
    sed -r 's/[ ]+$//g' | # remove trailing spaces
    awk 'NF' > $BROWN_CLEAN # remove blank lines