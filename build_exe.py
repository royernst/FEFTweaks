from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {"packages": ["tkinter"], "include_files": ["path/to/your/tkinter/files"]}

# Base set to "Win32GUI" to prevent a command prompt from appearing alongside the GUI (only on Windows).
base = None
if os.name == "nt":
    base = "Win32GUI"

setup(
    name="FEFTweaks",
    version="0.1",
    description="Fire Emblem Fates (FE14) Save Editor Tool",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
