# !/usr/bin/python3
# coding=utf-8

import os
import string
from ftplib import FTP

# author=Owen Jia
# email=owen-jia@outlook.com
# date=2023/9/14

print("规则<文件是否存在检测>")


def conn(host, port, user, passwd, p):
    f = FTP()
    f.encoding = 'UTF-8'
    f.connect(host, port)
    f.login(user, passwd)
    f.set_debuglevel(0)
    welcome = f.getwelcome()
    print(welcome)
    if welcome.find("Microsoft") >= 0:
        f.encoding = 'GBK'
    return f


def close(f: FTP):
    f.quit()


def print_line(line):
    print(line)


def line_file(os, lines: []):
    files = []

    i = 0
    while i < len(lines):
        line = lines[i].split(" ")

        if os:
            f_date = line[0]
            f_time = line[2]
            f_size = line[18]
            f_name = line[19]
            f = {
                "date": f_date,
                "time": f_time,
                "size": f_size,
                "name": f_name
            }
            files.append(f)
        else:
            f_date = line[20]+""+line[19]
            f_time = line[21]
            f_size = line[18]
            f_name = line[22]
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

    return line_file(f.encoding.find("GBK") >= 0, files)


def file_exist(f_list: [], f_name):
    """ 检查文件名文件是否存在 """
    flag = 0
    i = 0
    while i < len(f_list):
        t = f_list[i]
        if f_name == t['name'] or t['name'].find(f_name) >= 0:
            flag = 1
        i += 1

    print('file_exist', f_name, flag)
    return flag


def file_size(f_list: [], f_size):
    print("file_size")


def file_last_time(f: FTP):
    print("file_last_time")


def file_count(f_list: [], f_count):
    print("file_count", f_count, len(f_list))
    return len(f_list) >= f_count


def file_type(f_list: [], f_types):
    types = ""
    i = 0
    while i < len(f_list):
        types = f_list[i]
        i += 1

    print("file_type")


def file_data_count(f: FTP):
    print("file_data_count")


def service(cmd, host, port, user, passwd, p, path, *args):
    result = {}
    if "help" == cmd:
        print("cmd: help|exist|size|sum|date|data")
    elif "exist" == cmd:
        ftp = conn(host, port, user, passwd, p)
        files = dir_file(ftp, path)
        close(ftp)
        file_exist(files, args[0])
    elif "count" == cmd:
        ftp = conn(host, port, user, passwd, p)
        files = dir_file(ftp, path)
        close(ftp)
        file_count(files, args[0])
    else:
        print("cmd: help|exist|size|sum|date|data")

    print("done")
    return result


f_protocol = 1
f_host = "10.10.50.68"
f_port = 198
f_account = "ftptest"
f_password = "123456"
f_path = "222"


def test_data():
    ftp_linux: {
        "FTP_HOST": "10.10/.50/.156",
        "FTP_PORT": 21,
        "FTP_ACCOUNT": "ftptest",
        "FTP_PASSWD": "123456",
        "FTP_PATH": "var/ftp/test"
    }
    ftp_window: {
        "FTP_HOST": "10.10/.50/.68",
        "FTP_PORT": 198,
        "FTP_ACCOUNT": "ftptest",
        "FTP_PASSWD": "123456",
        "FTP_PATH": "222"
    }
    sftp_window: {

    }
    sftp_linux: {

    }


if __name__ == '__main__':
    resp = service("exist", f_host, f_port, f_account, f_password, f_protocol, f_path, 'hive规则模板修改')
    print(resp)
    resp = service("exist", "10.10.50.156", 21, f_account, f_password, f_protocol, "/var/ftp/test", '新建文本文档 (2)')
    print(resp)
    resp = service("count", "10.10.50.156", 21, f_account, f_password, f_protocol, "/var/ftp/test", 2)
    print(resp)
    exit("ys")

