#!/bin/bash

#Docker Install
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

#Use docker without sudo
sudo groupadd docker
sudo usermod -aG docker vagrant 
newgrp docker

# Hadolint install
wget -O hadolint https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64
sudo mv hadolint /usr/local/bin/hadolint
sudo chmod +x /usr/local/bin/hadolint

# Install Python
sudo apt-get install -y python3

# Install pip (Python package installer)
sudo apt-get install -y python3-pip

# Install Flask using pip
pip3 install Flask



