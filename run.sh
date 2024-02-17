#!/bin/bash

# Install Xvfb
sudo apt-get update
sudo apt-get install -y xvfb

# Set up the virtual display
export SDL_VIDEODRIVER=x11
export DISPLAY=:0

# Run your Python script
python snake.py
