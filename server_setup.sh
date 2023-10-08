#!/bin/bash
sudo apt update -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3.10-venv -y
sudo apt install python3-pip -y
git clone https://github.com/sharhan-alhassan/ugmsc-thesis.git && cd upgmsc-thesis