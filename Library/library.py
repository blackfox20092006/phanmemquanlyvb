import os
main_path = os.getcwd()
database_path = main_path + '\\' + 'database'
def fCheckdb():
    try:
        os.chdir(database_path)
        os.chdir(main_path)
        return 0
    except:
        return 'MissingDatabase'
def fList(path, mode):
    mode = int(mode)
    f_list = os.listdir(path)
    f_list2 = []
    for i in range(len(f_list)):
        if len(f_list[i].split('.')) == 2 and (f_list[i].split('.'))[0] != '':
            f_list2.append(f_list[i])
    f_list2 = fSort(f_list2)
    if mode == 1:
        return f_list2
    elif mode == 2:
        rvalue = {}
        rvalue2 = []
        for i in range(len(f_list2)):
            rvalue = {}
            rvalue['num'] = i+1
            rvalue['filename'] = f_list2[i]
            if len(f_list2[i].split('__')) > 1:
                rvalue['type'] = (f_list2[i].split('__'))[0]
            else:
                rvalue['type'] = 'Chưa được phân loại'
            rvalue2 += [rvalue]
        return rvalue2
    else:
        return 'InvaildModeParam'
def fFilter(data, tag, mode):
    mode = int(mode)
    data = list(data)
    os.chdir(database_path)
    if mode == 1:
        temp = []
        key = tag + '__'
        for i in range(len(data)):
            if data[i].find(key) != -1:
                temp += [data[i]]
        return temp
    elif mode == 2:
        temp = []
        key = tag + '__'
        for i in range(len(data)):
            if data[i].find(key) != -1:
                temp += [data[i]]
        rvalue = {}
        rvalue2 = []
        for i in range(len(temp)):
            rvalue = {}
            rvalue['num'] = i+1
            rvalue['filename'] = temp[i]
            rvalue['type'] = (temp[i].split('.'))[len(temp[i].split('.'))-1] + ' File'
            rvalue2 += [rvalue]
        return rvalue2
    else:
        return 'InvailModeParam'
def fAdd_tag(old_name, tag):
    os.chdir(database_path)
    if fChecktag(tag) == -1:
        return 1
    if str(fList(database_path, 1)).find(old_name) != -1:
        if len(old_name.split('__')) > 1:
            return 2
        while old_name.find('__') != -1:
            old_name = old_name.replace('__', '_')
        new_name = tag + '__' + old_name
        try:
            os.rename(old_name, new_name)
            return 0
        except:
            return -1
    else:
        return -1
def fChecktag(tag):
    for i in tag:
        if i == ' ' or i == '_' or i == '?' or i == '/' or i == '+' or i == '-' or i == '_' or i == ')' or i == '(' or i == '|' or i == '{' or i == '}' or i == '[' or i == ']' or i == '"' or i == ':' or i == ';' or i == '>' or i == '<' or i == ',' or i == '.' or i == '~' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '\\':
            return -1
    else:
        return 0
def fChangetag(new_tag, file_name):
    if fChecktag(new_tag) == -1:
        return -1
    elif new_tag == (file_name.split('__'))[0]:
        return -2
    else:
        os.chdir(database_path)
        filelist = fList(database_path, 1)
        for i in range(len(filelist)):
            if filelist[i] == file_name:
                t = filelist[i].split('__')
                ans = new_tag + '__' + t[1]
                os.rename(file_name, ans)
                return 0
def fSort(list_file):
    list_file = list(list_file)
    no_tag = []
    other = []
    value = []
    for i in list_file:
        if len(i.split('__')) == 1:
            no_tag += [i]
        else:
            other += [i]
    return list(no_tag+other)
def fAddtags(list_file, tag): #return -1 file has already had tag
    #return 0 added tag successfully
    #return 1 do not have permission to change file or file is not available
    #return -2 tag is not available
    if fChecktag(tag) == -1:
        return -2
    for i in list_file:
        if i.split('__') > 1:
            return -1
    os.chdir(database_path)
    for i in list_file:
        try:
            os.rename(i, tag + '__' + i)
        except:
            return 1
temp = []
def fRemovetag(list_file):
    global temp
    #return -1 file do not have tag to remove :)) stupid user
    for i in list_file:
        if i.split('__') == 1:
            return -1
    for i in list_file:
        try:
            os.chdir(database_path)
            os.rename(i, (i.split('__'))[1:len(i.split('__'))])
            temp += [(i.split('__'))[1:len(i.split('__'))]]
        except:
            return -2
def fChangetags(list_file, new_tag):
    global temp
    if fChecktag(new_tag) == -1:
        return -3
    if fRemovetag(list_file) != -2 or fRemovetag(list_file) != -1:
        fAddtags(temp, new_tag)