#Toàn bộ project được phát triển bởi Trần Thanh Trọng (Frontend) và Hoàng Quang Nhân (Backend)
#Vui lòng ghi ra đầy đủ nguồn khi sao chép và đăng lại trên các forum khác.
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
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    welcome_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    welcome_window.columnconfigure(index=0, weight=1)
    welcome_window.columnconfigure(index=1, weight=1)
    welcome_window.columnconfigure(index=2, weight=1)
    welcome_window.rowconfigure(index=0, weight=1)
    welcome_window.rowconfigure(index=1, weight=1)
    welcome_window.rowconfigure(index=2, weight=1)
    welcome_window.resizable(False, False)
    sizegrip = ttk.Sizegrip(welcome_window)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))  # Create a style

    s = ttk.Style()
    s.theme_use('clam')
    a = '#333333'
    Frame(welcome_window, width=600, height=400, bg=a).place(x=0, y=0)
    welcome_frame = ttk.Frame()
    welcome_frame.grid(row=0, column=1, padx=0, pady=(50, 10), sticky="nsew", rowspan=3)
    welcome_frame.columnconfigure(index=0, weight=1)
    Frame(welcome_frame, width=600, height=600, bg=a).place(x=0, y=0)

    Font = ("Comic Sans MS", 40, "bold")
    text1 = ttk.Label(welcome_frame, text='''Welcome''', font=Font, foreground="white", background=a)
    text1.grid(row=0, column=0, pady=50, columnspan=2)

    def des():
        welcome_window.destroy()
        os.system('py main.py')
    accentbutton = ttk.Button(welcome_frame, text="CHẠY PHẦN MỀM", style="Accent.TButton", command=lambda: des())
    accentbutton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

welcome()
welcome_window.mainloop()
