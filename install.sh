#!/bin/bash

sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip git -y 

pip3 install -r /home/$USER/dotfiles/requirements.txt

python3 ./main.py
