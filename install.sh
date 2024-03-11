#!/bin/bash

sudo apt update && sudo apt upgrade -y

sudo apt install python3 -y && sudo apt install pip3 -y

source ~/.profile

python3 -m venv .dotfiles

cd .dotfiles

source .dotfiles/bin/activate

pip3 install -r ./requirements.txt

python3 ./install.py
