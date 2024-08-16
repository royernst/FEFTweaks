import tkinter as tk
from tkinter import ttk

def open_new_interface(root):
    try:
        new_window = tk.Toplevel(root)
        new_window.title("New Interface")

        # Create tabs
        tab_control = ttk.Notebook(new_window)

        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='Tab 1')
        tab_control.add(tab2, text='Tab 2')

        tab_control.pack(expand=1, fill="both")

        # Dummy buttons in Tab 1
        btn1 = ttk.Button(tab1, text="Button 1")
        btn2 = ttk.Button(tab1, text="Button 2")

        btn1.pack(pady=10)
        btn2.pack(pady=10)

        # Dummy buttons in Tab 2
        btn3 = ttk.Button(tab2, text="Button 3")
        btn4 = ttk.Button(tab2, text="Button 4")

        btn3.pack(pady=10)
        btn4.pack(pady=10)

    except Exception as e:
        print(f"Error opening new interface: {e}")
