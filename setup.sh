#!/bin/bash

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install packages from requirements.txt
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please make sure it exists in the current directory."
fi

# Instructions to activate the virtual environment
echo "To activate the virtual environment, run: source .venv/bin/activate"
