import os
import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk  # Importing Pillow for image resizing
from new_interface import open_new_interface

class FileList:
    def __init__(self, root, frame, directory):
        self.root = root
        self.frame = frame
        self.directory = directory
        self.file_icon = None
        self.load_image()
        self.populate_files()

    def load_image(self):
        try:
            # Load the image from the assets folder and resize it to 100x100 pixels
            original_image = Image.open("assets/file_icon.png")
            resized_image = original_image.resize((100, 100), Image.ANTIALIAS)
            self.file_icon = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            print(f"Error loading or resizing image: {e}")

    def list_chapter_files(self, directory):
        try:
            return [f for f in os.listdir(directory) if f.startswith("Chapter")]
        except OSError as e:
            print(f"Error listing files in directory: {e}")
            return []

    def on_file_double_click(self, event):
        try:
            open_new_interface(self.root)
        except Exception as e:
            print(f"Error handling file double-click: {e}")

    def populate_files(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()

            if self.directory:
                chapter_files = self.list_chapter_files(self.directory)

                for file in chapter_files:
                    # Create a frame for each button and label pair
                    file_frame = tk.Frame(self.frame)

                    # Create the button with the image
                    btn = tk.Button(
                        file_frame,
                        image=self.file_icon,
                        width=100,
                        height=100,
                        command=lambda f=file: self.on_file_double_click(f)
                    )
                    btn.pack()

                    # Create a label for the file name
                    lbl = Label(file_frame, text=file, wraplength=100)
                    lbl.pack()

                    # Pack the frame
                    file_frame.pack(padx=5, pady=5, side=tk.LEFT)

        except Exception as e:
            print(f"Error populating files: {e}")

    def update_file_list(self, directory):
        try:
            self.directory = directory
            self.populate_files()
        except Exception as e:
            print(f"Error updating file list: {e}")
