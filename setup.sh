#!/bin/bash

if [ ! -d "env"  ]; then

  virtualenv env

fi

if [ -d "env" ]; then

  source ./env/bin/activate

  pip install -r ./requirements.txt

fi
