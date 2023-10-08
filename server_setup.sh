#!/bin/bash
sudo apt update -y
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3.10-venv -y
sudo apt install python3-pip -y
