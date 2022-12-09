from Library.library import *
import tkinter as tk
from tkinter import ttk
import Library.theme.sv_ttk as sv_ttk
import os
from tkinter import messagebox
from tkinter import *
root = tk.Tk()
root.resizable(0,0)
#root.state('zoomed')
if fCheckdb() == 'MissingDatabase':
    messagebox.showerror("Lỗi", "Không tìm thấy cơ sở dữ liệu")
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
# Create a Frame for the Menu
menu_frame = ttk.LabelFrame(root, text="Menu", padding=(0, 0, 0, 10))
menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), ipadx=30, sticky="nsew")
menu_frame.columnconfigure(index=0, weight=1)
# Separator
separator = ttk.Separator(root)
separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")
# Create a Frame for the Radiobuttons
radio_frame = ttk.LabelFrame(root, text="Function", padding=(20, 10))
radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
radio_frame.columnconfigure(index=0, weight=1)
#Create a Frame for input widgets
#widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
#widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
#widgets_frame.columnconfigure(index=0, weight=1)


# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=1, pady=(25, 5), ipadx=50, sticky="nsew", rowspan=3)

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
treeview.see(1)



#function go in here ======================================================================================================
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
        messagebox.showinfo("Thông báo", "Đã sao chép tên tệp tin")

treeview.bind('<<TreeviewSelect>>', get_data_listbox)

def fRefresh():
    root.destroy()
    os.chdir(main_path)
    os.system('py main.py')

def fOpen(file_name):
    #return -1, wrong file name or do not have permission to open
    try:
        os.chdir(database_path)
        os.system(file_name)
        return 0
    except:
        return -1


def about():
    tk.messagebox.showinfo('Thông tin phần mềm', '''
Phần mềm quản lý văn bản hành chính (phiên bản 1.0).
Đây là phần mềm hoàn toàn miễn phí và mã nguồn mở.
Tác giả : Trần Thanh Trọng và Hoàng Quang Nhân
''')


def backup():
    pass


def fExit_button():
    msg_box = tk.messagebox.askquestion('Thoát phần mềm', 'Bạn chắc chắn muốn thoát phần mềm?', icon='warning')
    if msg_box == 'yes':
        root.destroy()

#==============================================================================================================================

#main menu go here
def f_at(): #function add tag
    global _filename_, _tag_, _begin_, _end_
    _filename_ = str(_filename_)
    _tag_ = str(_tag_)
    #_begin_, _end_ = int(_begin_), int(_end_)
    if fChecktag(_tag_) != -1:
        if (_filename_.split('.')) != 1:
            fAdd_tag(_filename_, _tag_)
        elif _end_.isnumeric() == True and _begin_.isnumeric() == True:
            file_list2 = fList(database_path, 1)
            file_list2 = fSort(file_list2)
            i = 0
            while len(file_list2[i].split('__')) == 1:
                i += 1
            if len(file_list2) < _end_ or _begin_ < 1 or i < _end_:
                return -2
            status = fAddtags(file_list2[_begin_-1:i+1])
            return status
    else:
        return 'WrongTag'
'''
def delete_tag(event):
    _tag_.configure(state=NORMAL)
    _tag_.delete(0, END)
    _tag_.unbind('<Button-1>', clicked_tag)
def delete_input(event):
    _begin_.configure(state=NORMAL)
    _begin_.delete(0, END)
    _begin_.unbind('<Button-1>', clicked_input)
def delete_output(event):
    _end_.configure(state=NORMAL)
    _end_.delete(0, END)
    _end_.unbind('<Button-1>', clicked_output)
def delete_namefile(event):
    _filename_.configure(state=NORMAL)
    _filename_.delete(0, END)
    _filename_.unbind('<Button-1>', clicked_namefile)
'''
#Menu
_filename_ = ttk.Entry(menu_frame)
_filename_.insert(0, "Tên file")
_filename_.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")

#clicked_namefile = _filename_.bind('<Button-1>', delete_namefile)
#
_tag_ = ttk.Entry(menu_frame)
_tag_.insert(0, "Tag bạn muốn gán cho file")
_tag_.grid(row=0, column=1, padx=10, pady=(10, 10), sticky="ew")
#clicked_tag = _tag_.bind('<Button-1>', delete_tag)
#
_begin_ = ttk.Entry(menu_frame)
_begin_.insert(0, "Input")
_begin_.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="ew")
#clicked_input = _begin_.bind('<Button-1>', delete_input)
#
_end_ = ttk.Entry(menu_frame)
_end_.insert(0, "Output")
_end_.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="ew")
#clicked_output = _end_.bind('<Button-1>', delete_output)
#
ok_button = ttk.Button(menu_frame, text='Đổi tag', style="Accent.TButton", command=f_at())
ok_button.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")


#open_button = ttk.Button(radio_frame, text='Open', style="Accent.TButton")
#open_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

#Function

backup_button = ttk.Button(radio_frame, text='Backup (coming soon)', command=backup)
backup_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

refresh_button = ttk.Button(radio_frame, text="Làm mới danh sách", command=fRefresh)
refresh_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

exit_button = ttk.Button(radio_frame, text='Thoát chương trình', command=fExit_button)
exit_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

about_button = ttk.Button(radio_frame, text='Thông tin phần mềm', command=about)
about_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

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