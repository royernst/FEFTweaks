#!/bin/bash

# Check if the virtual environment is already active
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment is already active."
else
    # Create and activate virtual environment
    python3 -m venv .venv
    source .venv/bin/activate
fi

# Install packages from requirements.txt
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please make sure it exists in the current directory."
fi
