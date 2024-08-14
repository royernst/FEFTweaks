import os
import subprocess
import sys

def run_script(script_name):
    """Run the specified setup script."""
    try:
        subprocess.check_call([script_name])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")
        sys.exit(1)

def main():
    if not os.path.exists('requirements.txt'):
        # Exit if no requirements.txt file found -- it is needed for both setup scripts
        print("No requirements.txt file found. Please make sure it exists in the current directory.")
        return
        
    if os.name == 'nt':
        # Windows
        script_name = 'setup.bat'
    else:
        # macOS/Linux
        script_name = 'setup.sh'
    
    if not os.path.exists(script_name):
        print(f"{script_name} not found. Please make sure it exists in the current directory.")
        sys.exit(1)
    
    run_script(script_name)

if __name__ == '__main__':
    main()
