#!/bin/bash

# Check if the virtual environment is already active
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment is already active."
else
    # Check if .venv directory does not exist
    if [ ! -d ".venv" ]; then
        # Create the virtual environment
        echo "Virtual environment not found. Creating a new one..."
        python -m venv .venv
    fi
    # Activate the virtual environment
    echo "Activating the virtual environment..."
    source .venv/bin/activate
fi

# Install packages from requirements.txt
if [ -f requirements.txt ]; then
    echo "Installing packages from requirements.txt..."
    python -m pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please make sure it exists in the current directory."
fi
