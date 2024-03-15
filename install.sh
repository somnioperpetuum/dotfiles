#!/bin/bash

sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip git -y 

source ~/.profile

pip3 install -r ./requirements.txt

python3 ./main.py
