import os
import subprocess
import sys
import stat

def run_script(script_name):
    """Run the specified setup script."""
    try:
        subprocess.check_call([script_name])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")
        sys.exit(1)

def make_executable(script_name):
    """Make provided script executable."""
    st = os.stat(script_name)
    os.chmod(script_name, st.st_mode | stat.S_IEXEC)

def main():
    try:
        if not os.path.exists('requirements.txt'):
            # Exit if no requirements.txt file found -- it is needed for both setup scripts
            print("No requirements.txt file found. Please make sure it exists in the current directory.")
            sys.exit(1)
            
        if os.name == 'nt':
            # Windows
            script_name = './setup.bat'
        else:
            # macOS/Linux
            script_name = './setup.sh'
            
            # Check if the script is executable
            if not os.access(script_name, os.X_OK):
                print(f"Setup script is not executable - modifying permissions...")
                make_executable(script_name)
                print("Done.")

            print("Virtual environment setup complete. Run 'source setup.sh' to complete setup.")
        
        if not os.path.exists(script_name):
            print(f"{script_name} not found. Please make sure it exists in the current directory.")
            sys.exit(1)
        
    except RuntimeError as rte:
        print(f"Runtime error in main execution block: {rte}")
    except Exception as ex:
        print(f"General exception in main execution block: {ex}")

if __name__ == '__main__':
    main()
