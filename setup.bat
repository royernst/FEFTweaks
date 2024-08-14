@echo off
REM Check if the virtual environment is already active
if defined VIRTUAL_ENV (
    echo Virtual environment is already active.
) else (
    REM Create and activate virtual environment
    python -m venv .venv
    call .venv\Scripts\activate
)

REM Install packages from requirements.txt
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Please make sure it exists in the current directory.
)
