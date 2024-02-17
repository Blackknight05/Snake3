#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install -y python3-pip xvfb

# Install Python dependencies
pip install -r requirements.txt

# Set up virtual display with Xvfb
export SDL_VIDEODRIVER=x11
export DISPLAY=:0

# Run the Python script
python3 snake.py
