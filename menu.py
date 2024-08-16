import tkinter as tk
from tkinter import filedialog

def create_menu(root, config):
    try:
        # Menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Directory", command=lambda: open_directory(root, config))
        file_menu.add_command(label="Exit", command=root.quit)

        # Configure menu
        configure_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Configure", menu=configure_menu)
        configure_menu.add_command(label="Set Directory", command=lambda: set_directory(config, root))

    except Exception as e:
        print(f"Error creating menu: {e}")

def open_directory(root, config):
    try:
        directory = filedialog.askdirectory()
        if directory:
            config.set_directory(directory)
            root.file_list.update_file_list(directory)
    except Exception as e:
        print(f"Error opening directory: {e}")

def set_directory(config, root):
    try:
        directory = filedialog.askdirectory(initialdir=config.get_directory())
        if directory:
            config.set_directory(directory)
            root.file_list.update_file_list(directory)
    except Exception as e:
        print(f"Error setting directory: {e}")
