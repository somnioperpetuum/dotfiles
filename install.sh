#!/bin/bash

sudo apt update && sudo apt upgrade -y

sudo apt install python3 -y && sudo apt install python3-pip -y

source ~/.profile

# python3 -m venv dotfiles

# cd /home/$USER/dotfiles

# source dotfiles/bin/activate

pip3 install -r ./requirements.txt

python3 ./main.py
