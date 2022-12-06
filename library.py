#sử dụng đường dẫn thư mục khi gọi hàm, vui lòng sử dụng theo định dạng sau : ví dụ : C:\\Users\\DELL
import os
main_path = os.getcwd()
database_path = main_path + '\\' + 'database'
def fList(path): #return danh sách các file ở trong <path>
    f_list = os.listdir(path)
    f_list2 = []
    for i in range(len(f_list)):
        if len(f_list[i].split('.')) == 2 and (f_list[i].split('.'))[0] != '':
            f_list2.append(f_list[i])
    return f_list2
def fFilter(data, tag): #lọc các file theo tag trong  thư mục database
    data = list(data)
    os.chdir(database_path)
    temp = []
    key = tag + '__'
    for i in range(len(data)):
        if data[i].find(key) != -1:
            temp += [data[i]]
    return temp
def fAdd_tag(old_name, tag):
    #exitcode = 0 => add tag to file successfully
    #exitcode = -1 => add tag to file unsuccessfully
    os.chdir(database_path)
    if fList(database_path).find(old_name) != -1:
        new_name = tag + '__' + old_name
        os.rename(old_name, new_name)
        return 0
    else:
        return -1
def fChecktag(tag):
    for i in tag:
        if i == ' ' or i == '_' or i == '?' or i == '/' or i == '+' or i == '-' or i == '_' or i == ')' or i == '(' or i == '|' or i == '{' or i == '}' or i == '[' or i == ']' or i == '"' or i == ':' or i == ';' or i == '>' or i == '<' or i == ',' or i == '.' or i == '~' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '\\':
            return -1
    else:
        return 0
def fChangetag(new_tag, file_name): #exicode = -1 => invaild tag
    #exitcode = -2 => exist tag
    #exitcode = 0 => change tag successfully
    #exitcode = 1 => change tag unsuccessfully => not found filename or do not have premission
    if fChecktag(new_tag) == -1:
        return -1
    elif new_tag == (file_name.split('__'))[0]:
        return -2
    else:
        os.chdir(database_path)
        filelist = fList(database_path)
        for i in range(len(filelist)):
            if filelist[i] == file_name:
                t = filelist[i].split('__')
                ans = new_tag + '__' + t[1]
                os.rename(file_name, ans)
                return 0
def fAddtags (list_file, begin, end, tag): #exitcode = -2 => tag is not allow
    #exitcode = 0 => add tags successfully
    #exitcode = -3 => invail param for end
    #exitcode = 1 => file has already had tag, use fChangetags to change tag for many files
    begin = int(begin)
    end = int(end)
    list_file = list(list_file)
    os.chdir(database_path)
    if fChecktag(tag) == -1:
        return -2
    elif end > len(list_file) or end < begin:
        return -3
    else:
        for i in range(begin-1, end, 1):
            if len(list_file[i].split('__')) != 1:
                return 1
            else:
                temp = list_file[i].split('.')
                newname = tag + '__' + temp[0] + '.' +temp[1]
                os.rename(list_file[i], newname)
    return 0
def fChangetags(list_file, begin, end, tag, new_tag): #change from begin-th file to end-th file with new tag
    # exitcode = -2 => tag is not allow
    #exitcode = -3 => invail param for end
    #exitcode = 0 => successfully rename
    #list_file is a list which contains all files in database directory, this function will automatically filt the specific tag
    begin = int(begin)
    end = int(end)
    list_file = list(list_file)
    if fChecktag(tag) == -1:
        return -1
    elif end > len(list_file) or end < begin:
        return -3
    else:
        os.chdir(database_path)
        data = fFilter(list_file, tag)
        for i in range(begin, end+1):
            s = new_tag + '__' + (data[i].split('__'))[1]
            os.rename(data[i], s)
        return 0