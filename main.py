from Library.library import *
import tkinter as tk
from tkinter import ttk
import Library.theme.sv_ttk as sv_ttk
import os
from tkinter import messagebox
root = tk.Tk()
if fCheckdb() == 'MissingDatabase':
    messagebox.showerror("Lỗi", "Không tìm thấy cơ sở dữ liệu.")
    root.destroy()
#Custom GUI
root.title("Quản Lý Văn Bản Hành Chính v1.0")
root.option_add("*tearOff", False)
# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]
# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()
# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)
# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)

# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=25)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

# Treeview columns
treeview.column("#0", width=10)
treeview.column(1, anchor="w", width=120)
treeview.column(2, anchor="w", width=120)

# Treeview headings
treeview.heading("#0", text="Số Thứ Tự", anchor="center")
treeview.heading(1, text="Tên File", anchor="center")
treeview.heading(2, text="Loại Văn Bản", anchor="center")


file_list = fList(database_path, 2)
treeview_data = []
for i in file_list:
    treeview_data.append((i['filename'], i['type']))
j = 1
for item in treeview_data:
    treeview.insert(parent='', index='end', text = j, iid = j, values=item)
    j += 1

# Select and scroll
#treeview.selection_set(1)
treeview.see(2)

#Get data in listbox----------------------------------------------------------------
def get_data_listbox(event):
    file_name = ''
    for item_listbox in treeview.selection():
        item = treeview.item(item_listbox)
        record = ' '.join(item["values"])
        file_name = (record.split('.'))[0] + '.' +(((record.split('.'))[1]).split(' '))[0]
        root.clipboard_clear()
        root.clipboard_append(file_name)
        root.update()
        messagebox.showinfo("Thông báo", "Đã copy!")
treeview.bind('<<TreeviewSelect>>', get_data_listbox)
def fRefresh():
    root.destroy()
    os.chdir(main_path)
    os.system('py main.py')
refresh_button = ttk.Button(root, text="Refresh", command=fRefresh)
refresh_button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")
# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
# This is where the magic happens
sv_ttk.set_theme("dark")
root.mainloop()
