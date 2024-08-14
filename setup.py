import os
import subprocess
import sys

def run_script(script_name):
    """Run the specified script."""
    try:
        subprocess.check_call([script_name])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")
        sys.exit(1)

def main():
    if os.name == 'nt':
        # Windows
        script_name = 'setup_env.bat'
    else:
        # macOS/Linux
        script_name = 'setup_env.sh'
    
    if not os.path.exists(script_name):
        print(f"{script_name} not found. Please make sure it exists in the current directory.")
        sys.exit(1)
    
    run_script(script_name)

if __name__ == '__main__':
    main()
