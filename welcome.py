from Library.library import *
import tkinter as tk
from tkinter import ttk
import Library.theme.sv_ttk as sv_ttk
import os
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd

welcome_window = tk.Tk()

def welcome():
    welcome_window.option_add("*tearOff", False)
    welcome_window.overrideredirect(True)
    window_height = 400
    window_width = 600
    screen_width = welcome_window.winfo_screenwidth()
    screen_height = welcome_window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    welcome_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    welcome_window.columnconfigure(index=0, weight=1)
    welcome_window.columnconfigure(index=1, weight=1)
    welcome_window.columnconfigure(index=2, weight=1)
    welcome_window.rowconfigure(index=0, weight=1)
    welcome_window.rowconfigure(index=1, weight=1)
    welcome_window.rowconfigure(index=2, weight=1)
    welcome_window.resizable(False,False)
    sizegrip = ttk.Sizegrip(welcome_window)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))# Create a style

    welcome_frame = ttk.Frame()
    welcome_frame.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
    welcome_frame.columnconfigure(index=0, weight=1)

    Font = ("Comic Sans MS", 20, "bold")
    text1 = ttk.Label(welcome_frame, text='''Welcome''', font=Font, foreground="white")
    text1.grid(row=0, column=0, pady=50, columnspan=2)


    accentbutton = ttk.Button(welcome_frame, text="Load Program", style="Accent.TButton", command=lambda: NONE)
    accentbutton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

welcome()
sv_ttk.set_theme("dark")
welcome_window.mainloop()