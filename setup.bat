@echo off
REM Create virtual environment
python -m venv .venv

REM Activate virtual environment
call .venv\Scripts\activate

REM Install packages from requirements.txt
if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo requirements.txt not found. Please make sure it exists in the current directory.
)

REM Instructions to activate the virtual environment
echo To activate the virtual environment, run: .venv\Scripts\activate
