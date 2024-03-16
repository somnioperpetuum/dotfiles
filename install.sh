#!/bin/bash

sudo apt update && sudo apt upgrade -y


# Ensure python Install
sudo apt install python3 python3-pip git -y 

#Miniconda install
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

# Source profile
source ./.profile

#Ensure rust install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Source profile
source ./.profile


cd /home/$USER/dotfiles

pip3 install -r /home/$USER/dotfiles/requirements.txt

python3 /home/$USER/dotfiles/main.py
