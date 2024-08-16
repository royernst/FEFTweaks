import tkinter as tk
from menu import create_menu
from file_list import FileList
from config.config import Config

try:
    # Main application window
    root = tk.Tk()
    root.title("Chapter Files Explorer")

    # Configuration handler
    config = Config()

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Get window size from config
    window_size = config.get_window_size()
    window_width = int(screen_width * window_size["width_percentage"])
    window_height = int(screen_height * window_size["height_percentage"])

    # Center the window on the screen
    x_position = int((screen_width / 2) - (window_width / 2))
    y_position = int((screen_height / 2) - (window_height / 2))

    # Set the geometry of the main window
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create the menu
    create_menu(root, config)

    # Create the file list frame
    files_frame = tk.Frame(root)
    files_frame.pack(pady=20)

    # Initialize the FileList object with the directory from config
    directory = config.get_directory()
    file_list = FileList(root, files_frame, directory)

    # Store file_list in root so it can be accessed in other modules
    root.file_list = file_list

    # Start the application
    root.mainloop()

except Exception as e:
    print(f"Error initializing the application: {e}")
