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

    accentbutton = ttk.Button(welcome_frame, text="CHẠY PHẦN MỀM", style="Accent.TButton", command=lambda: main_window())
    accentbutton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


def main_window():
    welcome_window.destroy()
    # root.state('zoomed')]
    root = tk.Tk()
    root.iconbitmap('img//appicon.ico')
    # Custom GUI
    root.title("Quản Lý Văn Bản Hành Chính v1.0")
    root.option_add("*tearOff", False)
    # Make the app responsive
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=2, weight=1)
    root.rowconfigure(index=0, weight=1)
    root.rowconfigure(index=1, weight=1)
    root.rowconfigure(index=2, weight=1)
    root.resizable(False, False)

    if fCheckdb() == 'MissingDatabase':
        messagebox.showerror("Lỗi", "Không tìm thấy cơ sở dữ liệu")
        root.destroy()
    h = tk.BooleanVar()
    # Create a Frame for the Menu
    menu_frame = ttk.LabelFrame(root, text="Quản lý tag", padding=(0, 0, 0, 10))
    menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), ipadx=30, sticky="nsew")
    menu_frame.columnconfigure(index=0, weight=1)
    # Separator
    separator = ttk.Separator(root)
    separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")
    # Create a Frame for the Radiobuttons
    radio_frame = ttk.LabelFrame(root, text="Chức năng khác", padding=(20, 10))
    radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
    radio_frame.columnconfigure(index=0, weight=1)
    # Create a Frame for input widgets
    # widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
    # widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
    # widgets_frame.columnconfigure(index=0, weight=1)

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
        treeview.insert(parent='', index='end', text=j, iid=j, values=item)
        j += 1

    # Select and scroll

    # treeview.selection_set(1)
    treeview.see(1)

    # function go in here ======================================================================================================
    # Get data in listbox----------------------------------------------------------------
    def get_data_listbox(event):
        file_name = ''
        for item_listbox in treeview.selection():
            item = treeview.item(item_listbox)
            record = ' '.join(item["values"])
            file_name = (record.split('.'))[0] + '.' + (((record.split('.'))[1]).split(' '))[0]
            root.clipboard_clear()
            root.clipboard_append(file_name)
            root.update()
            messagebox.showinfo("Thông báo", "Đã sao chép tên tệp tin")

    treeview.bind('<ButtonRelease-1>', get_data_listbox)

    def fRefresh():
        root.destroy()
        os.chdir(main_path)
        os.system('py main.py') # use when run as Py extension
        #os.system('main.exe') # use when run as application (*.exe)

    def about():
        tk.messagebox.showinfo('Thông tin phần mềm', '''
    Phần mềm quản lý văn bản hành chính (phiên bản 1.0).
    Đây là phần mềm hoàn toàn miễn phí và mã nguồn mở.
    Tác giả : Trần Thanh Trọng và Hoàng Quang Nhân
    ''')

    def calc():
        os.system('calc')

    def fExit_button():
        msg_box = tk.messagebox.askquestion('Thoát phần mềm', 'Bạn chắc chắn muốn thoát phần mềm?', icon='warning')
        if msg_box == 'yes':
            root.destroy()

    # ==============================================================================================================================

    # main menu go here
    def f_at():  # function add tag
        global _filename_, _tag_, _begin_, _end_
        filename = _str_filename_.get()
        tagename = _str_tag_.get()
        # begin = _int_begin_.get()
        # end = _int_end_.get()
        if fChecktag(tagename) != -1:
            if (filename.split('.')) != 1:
                fAdd_tag(filename, tagename)
                tk.messagebox.showinfo('Thành công', 'Thêm tag thành công !')
                return 0
            # elif end.isnumeric() == True and begin.isnumeric() == True:
            #    file_list2 = fList(database_path, 1)
            #    file_list2 = fSort(file_list2)
            #    i = 0
            #    while len(file_list2[i].split('__')) == 1:
            #        i += 1
            #    if len(file_list2) < end or begin < 1 or i < end:
            #        return -2
            #    status = fAddtags(file_list2[begin-1:i+1])
            #    return status
        else:
            return 'WrongTag'

    def f_change():
        global _filename_, _tag_, _begin_, _end_
        filename = _str_filename_.get()
        changetagename = _str_changetag_.get()
        begin = _int_begin_.get()
        end = _int_end_.get()
        if fChecktag(changetagename) != -1:
            if (filename.split('.')) != 1:
                fChangetag(changetagename, filename)

    def f_open():
        global _filename_, _tag_, _begin_, _end_
        filename = _str_filename_.get()
        os.chdir(database_path)
        os.startfile(filename)

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

    _str_filename_ = tk.StringVar()
    _str_tag_ = tk.StringVar()
    _str_changetag_ = tk.StringVar()
    _int_begin_ = tk.IntVar()
    _int_end_ = tk.IntVar()
    _str_keyword_ = tk.StringVar()
    # Menu

    # row 1
    _filename_ = ttk.Entry(menu_frame, textvariable=_str_filename_)
    _filename_.insert(0, "Tên file")
    _filename_.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew")

    addtag_button = ttk.Button(menu_frame, text='Mở', style="Accent.TButton", command=lambda: f_open())
    addtag_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # row 2
    '''
    _begin_ = ttk.Spinbox(menu_frame, textvariable=_int_begin_, from_=0, to=100)
    #_begin_.insert(0, "Input")
    _begin_.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="ew")
    #clicked_input = _begin_.bind('<Button-1>', delete_input)
    #
    _end_ = ttk.Spinbox(menu_frame, textvariable=_int_end_, from_=0, to=100)
    #_end_.insert(0, "Output")
    _end_.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="ew")
    #clicked_output = _end_.bind('<Button-1>', delete_output)
    '''
    # row 2

    # clicked_namefile = _filename_.bind('<Button-1>', delete_namefile)
    _tag_ = ttk.Entry(menu_frame, textvariable=_str_tag_)
    _tag_.insert(0, "Tag bạn muốn gán cho file")
    _tag_.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="ew")
    addtag_button = ttk.Button(menu_frame, text='Thêm tag', style="Accent.TButton", command=lambda: f_at())
    addtag_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # clicked_tag = _tag_.bind('<Button-1>', delete_tag)

    # row 3
    _changetag_ = ttk.Entry(menu_frame, textvariable=_str_changetag_)
    _changetag_.insert(0, "Tag bạn muốn đổi cho file")
    _changetag_.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="ew")

    changetag_button = ttk.Button(menu_frame, text='Thay đổi tag', style="Accent.TButton", command=lambda: f_change())
    changetag_button.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    # row 4

    def fFind_mini():
        keyword = _str_keyword_.get()
        result = fFind(keyword)
        if len(result) == 0:
            messagebox.showerror('Lỗi', 'Không tìm thấy bất kì kết quả phù hợp nào ! Vui lòng thử với từ khóa khác.')
        else:
            child_root = Toplevel(root)
            child_root.title('Kết quả tìm kiếm cho từ khóa "' + keyword + '"')
            child_root.resizable(0, 0)

            # Panedwindow
            paned = ttk.PanedWindow(child_root, height=500, width=500)
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
            treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2),
                                    height=25)
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

            treeview_data = []
            for i in result:
                treeview_data.append((i, (i.split('__'))[0]))
            j = 1

            for item in treeview_data:
                treeview.insert(parent='', index='end', text=j, iid=j, values=item)
                j += 1
            # treeview.bind('<<TreeviewSelect>>', get_data_listbox)
            child_root.minsize(treeview.winfo_width(), child_root.winfo_height())
            child_root.geometry("+{}+{}".format(0, 0))
            treeview.see(1)

            def get_data_listbox2(event):
                file_name = ''
                for item_listbox in treeview.selection():
                    item = treeview.item(item_listbox)
                    record = ' '.join(item["values"])
                    file_name = (record.split('.'))[0] + '.' + (((record.split('.'))[1]).split(' '))[0]
                    child_root.clipboard_clear()
                    child_root.clipboard_append(file_name)
                    child_root.update()
                    messagebox.showinfo("Thông báo", "Đã sao chép tên tệp tin")

            treeview.bind('<<TreeviewSelect>>', get_data_listbox2)
            # This is where the magic happens
            sv_ttk.set_theme("dark")

            def fClose():
                child_root.destroy()

            close_button = ttk.Button(child_root, text='Đóng cửa sổ', style="Accent.TButton", command=lambda: fClose())
            close_button.grid(row=5, column=1, padx=10, pady=(10, 10), sticky='ew')

    _keyword_ = ttk.Entry(menu_frame, textvariable=_str_keyword_)
    _keyword_.insert(0, "Từ khóa")
    _keyword_.grid(row=4, column=0, padx=10, pady=(10, 10), sticky="ew")

    find_button = ttk.Button(menu_frame, text='Tìm kiếm', style="Accent.TButton", command=lambda: fFind_mini())
    find_button.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    # open_button = ttk.Button(radio_frame, text='Open', style="Accent.TButton")
    # open_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    # Function

    def fAdd():
        filename = fd.askopenfilename()
        shutil.move(filename, database_path)
        fn = (filename.split('/'))[len(filename.split('/')) - 1]
        file_2 = database_path + '\\' + fn
        if os.path.exists(file_2):
            messagebox.showinfo('Thành công', 'Thêm tệp vào cơ sở dữ liệu thành công !')
        else:
            messagebox.showerror('Thất bại', 'Thêm tệp vào cơ sở dữ liệu thất bại !')

    calc = ttk.Button(radio_frame, text='Máy tính', command=calc, style="Accent.TButton")
    calc.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    refresh_button = ttk.Button(radio_frame, text="Làm mới danh sách", command=fRefresh, style="Accent.TButton")
    refresh_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    backup_button = ttk.Button(radio_frame, text='Sao lưu dữ liệu', command=fBackup, style="Accent.TButton")
    backup_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    add_button = ttk.Button(radio_frame, text='Thêm tệp vào cơ sở dữ liệu', command=fAdd, style="Accent.TButton")
    add_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    about_button = ttk.Button(radio_frame, text='Thông tin phần mềm', command=about, style="Accent.TButton")
    about_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    exit_button = ttk.Button(radio_frame, text='Thoát chương trình', command=fExit_button, style="Accent.TButton")
    exit_button.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    # Sizegrip
    sizegrip = ttk.Sizegrip(root)
    sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
    # Center the window, and set minsize
    root.update()
    # root.eval('tk::PlaceWindow . center')
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))
    sv_ttk.set_theme("dark")
    root.mainloop()


welcome()
welcome_window.mainloop()
