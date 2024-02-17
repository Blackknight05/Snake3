#!/bin/bash

# Install necessary packages
yum update -y
yum install -y python3

# Install Python dependencies
pip3 install --user -r requirements.txt

# Run the Python script
python3 snake.py
