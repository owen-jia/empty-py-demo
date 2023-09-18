# !/usr/bin/python3
# coding=utf-8

import os
import string
import sys
from ftplib import FTP

# author=Owen Jia
# email=owen-jia@outlook.com
# date=2023/9/14


def conn(host, port: int, user, passwd):
    print(host, port, user, passwd)
    f = FTP()
    f.encoding = 'UTF-8'
    f.connect(host, port)
    f.login(user, passwd)
    f.set_debuglevel(0)
    welcome = f.getwelcome()
    print(welcome)
    if welcome.find("Microsoft") >= 0:
        f.encoding = 'GBK'
    print("ftp连接成功")
    return f


def close(f: FTP):
    f.quit()


def print_line(line):
    print(line)


def line_file(win: int, lines: []):
    files = []

    if win:
        i = 0
        while i < len(lines):
            line = lines[i]
            f_date = line[0:8]
            f_time = line[10:17]
            f_size = line[18:38].strip()
            f_name = line[39:len(line)]
            f = {
                "date": f_date,
                "time": f_time,
                "size": f_size,
                "name": f_name
            }
            files.append(f)
            i += 1
    else:
        i = 0
        while i < len(lines):
            line = lines[i]

            f_date = line[43:49]
            f_time = line[50:55]
            f_size = line[30:42].strip()
            f_name = line[56:len(line)]
            f = {
                "date": f_date,
                "time": f_time,
                "size": f_size,
                "name": f_name
            }
            files.append(f)
            i += 1

    print(files)

    return files


def dir_file(f: FTP, path: string = ''):
    lines: list = []
    files: list = []
    f.cwd(path)
    f.retrlines('LIST', lines.append)

    i = 0
    while i < len(lines):
        file: string = lines[i]
        if file.find("DIR") < 0 and file.find("dr") < 0:
            files.append(file)
            print(file)
        i += 1

    print("目录查询成功")
    return line_file(f.encoding.find("GBK") >= 0, files)


def file_exist(f_list: [], f_name):
    """ 检查文件名文件存在数量 """
    flag = 0
    i = 0
    while i < len(f_list):
        t = f_list[i]
        if f_name == t['name'] or t['name'].find(f_name) >= 0:
            flag += 1
        i += 1

    print('文件名检测完成')
    return "#exist|"+str(flag)+"|"+str(f_list)+"#"


def file_size(f_list: [], f_size: int):
    """ 检查目录下文件大小数量 """
    flag = 0
    i = 0
    while i < len(f_list):
        t = f_list[i]
        if int(t['size']) >= int(f_size):
            flag += 1
        i += 1

    print("文件大小检查完成")
    return "#size|"+str(flag)+"|"+str(f_list)+"#"


def file_last_time(f: FTP):
    print("file_last_time")


def file_count(f_list: [], f_count):
    """ 检查目录下文件数量 """
    print("file_count", f_count, len(f_list), f_list)

    flag = len(f_list)

    print('文件数量检测完成')
    return "#count|"+str(flag)+"|"+str(f_list)+"#"


def file_type(f_list: [], f_types):
    """ 检查符合条件文件类型的数量 """
    flag = 0
    i = 0
    while i < len(f_list):
        t = f_list[i]
        f_n = t['name']
        print("name--",f_n)
        tail = f_n.split(".")[1]
        if str(f_types).find(tail) >= 0:
            flag += 1
        i += 1

    print('文件类型检测完成')
    return "#type|"+str(flag)+"|"+str(f_list)+"#"


def file_data_count(f: FTP):
    print("file_data_count")


def service(cmd, host, port: int, user, passwd, protocol: int, path, args: []):
    result = ""
    print("args:",args)
    if "help" == cmd:
        print("仅支持命令: help|exist|size|count|type|date|data")
    elif "exist" == cmd:
        print("规则<文件是否存在检测>")
        ftp = conn(host, port, user, passwd)
        files = dir_file(ftp, path)
        close(ftp)
        result = file_exist(files, args[0])
    elif "count" == cmd:
        ftp = conn(host, port, user, passwd)
        files = dir_file(ftp, path)
        close(ftp)
        result = file_count(files, args[0])
    elif "type" == cmd:
        ftp = conn(host, port, user, passwd)
        files = dir_file(ftp, path)
        close(ftp)
        result = file_type(files, args[0])
    elif "size" == cmd:
        ftp = conn(host, port, user, passwd)
        files = dir_file(ftp, path)
        close(ftp)
        result = file_size(files, args[0])
    else:
        print("cmd: help|exist|size|sum|date|data")

    print("检查结果")
    return result


f_cmd = "count"  # exist
f_protocol = 1  # 1 ftp 2 sftp
f_host = "10.10.50.156"
f_port: int = 21
f_account = "ftptest"
f_password = "123456"
f_path = "/var/ftp/test"
f_args = ['2']


def read_argv():
    if len(sys.argv) < 2:
        exit(-1)

    global f_cmd
    f_cmd = sys.argv[1]
    if f_cmd == "":
        exit(-1)

    global f_host
    f_host = sys.argv[2]
    global f_port
    f_port = int(sys.argv[3])
    global f_account
    f_account = sys.argv[4]
    global f_password
    f_password = sys.argv[5]
    global f_protocol
    f_protocol = int(sys.argv[6])
    global f_path
    f_path = sys.argv[7]
    global f_args
    f_args = []
    if f_cmd == "exist":
        f_args.append(sys.argv[8])
    elif f_cmd == "count":
        f_args.append(sys.argv[8])
    elif f_cmd == "type":
        f_args.append(sys.argv[8])
    elif f_cmd == "size":
        f_args.append(sys.argv[8])

    print("read_argv:", f_cmd, f_host, f_port, f_account, f_password, f_protocol, f_path, f_args)


# python fileRules.py "exist" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "hive规则模板修改"
# python fileRules.py "exist" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "接口设计与表设计.xls"
# python fileRules.py "count" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "2"
# python fileRules.py "count" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "2"
# python fileRules.py "type" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "xls,doc,txt"
# python fileRules.py "type" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "xls,doc,txt"
# python fileRules.py "size" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "398"
# python fileRules.py "size" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "445"


if __name__ == '__main__':
    read_argv()
    resp = service(f_cmd, f_host, f_port, f_account, f_password, f_protocol, f_path, f_args)
    print(resp)
    exit(0)

