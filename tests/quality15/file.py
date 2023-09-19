# !/usr/bin/python3
# coding=utf-8
# -*- coding: utf-8 -*-
import string
import sys
from datetime import datetime, time
from ftplib import FTP

import paramiko


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


def conn_sftp(host, port, user, passwd, path):
    try:
        new_list: list = []
        transport = paramiko.Transport((host, port))
        transport.connect(username=user, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        listdir_attr = sftp.listdir_attr(path)
        sftp.close()

        i = 0
        while i < len(listdir_attr):
            file = listdir_attr[i]

            if file.longname.find("dr") < 0:
                print(file.longname)
                t_date = datetime.fromtimestamp(file.st_atime)
                file = {
                    "name": file.filename,
                    "date": t_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "time": t_date.strftime("%H:%M:%S"),
                    "size": file.st_size
                }
                new_list.append(file)

            i += 1

        return new_list
    except Exception as e:
        print(e)


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
            f_date = line[0:9].strip()
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

            f_date = f_date.replace("Jan", "01")
            f_date = f_date.replace("Feb", "02")
            f_date = f_date.replace("Mar", "03")
            f_date = f_date.replace("Apr", "04")
            f_date = f_date.replace("May", "05")
            f_date = f_date.replace("Jun", "06")
            f_date = f_date.replace("Jan", "07")
            f_date = f_date.replace("Aug", "08")
            f_date = f_date.replace("Sep", "09")
            f_date = f_date.replace("Oct", "10")
            f_date = f_date.replace("Nov", "11")
            f_date = f_date.replace("Dec", "12")

            f_time = line[50:55]
            if len(f_time) != 4:
                f_date = f_date + " " + str(datetime.today().year)

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


def file_date(f_list: [], last_date):
    """ 检查目录下文件更新时间数量 """
    last_date_new = datetime.strptime(last_date, "%Y-%m-%d %H:%M:%S")
    flag = 0
    i = 0
    while i < len(f_list):
        t = f_list[i]
        dt = t['date'] + " " + t['time']

        if dt.find('PM') >= 0 or dt.find('AM') >= 0:
            last = datetime.strptime(dt, "%m-%d-%y %H:%M%p")
        else:
            if len(t['time']) == 4:
                last = datetime.strptime(dt, "%m %d %Y")
            else:
                last = datetime.strptime(dt, "%m %d %Y %H:%M")

        if last > last_date_new:
            flag += 1

        i += 1

    print("文件更新时间检查完成")
    return "#date|"+str(flag)+"|"+str(f_list)+"#"


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
        if f_n.find(".") >= 0:
            tail = f_n.split(".")[1]
            if str(f_types).find(tail) >= 0:
                flag += 1
        i += 1

    print('文件类型检测完成')
    return "#type|"+str(flag)+"|"+str(f_list)+"#"


def file_data_count(f: FTP):
    print("file_data_count")


def timestamp_convert_str(str_format, timestamp):
    """
    时间戳 转 字符串
    :param timestamp: 1676554320
    :param str_format:"%Y-%m-%d %H:%M:%S"
    :return:
    """
    timestamp = int(timestamp) if isinstance(
        timestamp, str) and len(timestamp) == 10 else timestamp
    return time.strftime(str_format, time.localtime(timestamp))


def service_sftp(cmd, host, port: int, user, passwd, protocol: int, path, args: []):
    result = ""
    if "help" == cmd:
        print("仅支持命令: help|exist|size|count|type|date|data")
    elif "exist" == cmd:
        files = conn_sftp(host, port, user, passwd, path)
        f_name = args[0]
        result = file_exist(files, f_name)
    elif "count" == cmd:
        files = conn_sftp(host, port, user, passwd, path)
        f_name = args[0]
        result = file_count(files, f_name)
    elif "type" == cmd:
        files = conn_sftp(host, port, user, passwd, path)
        f_name = args[0]
        result = file_type(files, f_name)
    elif "size" == cmd:
        files = conn_sftp(host, port, user, passwd, path)
        f_name = args[0]
        result = file_size(files, f_name)
    elif "date" == cmd:
        files = conn_sftp(host, port, user, passwd, path)
        f_name = args[0]
        last_date_new = datetime.strptime(f_name, "%Y-%m-%d %H:%M:%S")

        flag = 0
        i = 0
        while i < len(files):
            f = files[i]
            f_date = f['date']
            if datetime.strptime(f_date, "%Y-%m-%d %H:%M:%S") >= last_date_new:
                flag += 1
            i += 1

        result = "#date|" + str(flag) + "|" + str(files) + "#"
    else:
        print("cmd: help|exist|size|sum|date|data")

    print("检查结果")
    return result


def service(cmd, host, port: int, user, passwd, protocol: int, path, args: []):
    if int(protocol) == 2:
        return service_sftp(cmd, host, port, user, passwd, protocol, path, args)

    result = ""
    if "help" == cmd:
        print("仅支持命令: help|exist|size|count|type|date|data")
    elif "exist" == cmd:
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
    elif "date" == cmd:
        ftp = conn(host, port, user, passwd)
        files = dir_file(ftp, path)
        close(ftp)
        result = file_date(files, args[0])
    else:
        print("cmd: help|exist|size|sum|date|data")

    print("检查结果")
    return result


f_cmd = "exist"  # exist
f_protocol = 2  # 1 ftp 2 sftp
f_host = "10.10.90.246"
f_port: int = 22
f_account = "root"
f_password = "Root1209."
f_path = "/root"
f_args = ['2.log']


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
    f_args.clear()
    f_args.append(sys.argv[8])

    print("read_argv:", f_cmd, f_host, f_port, f_account, f_password, f_protocol, f_path, f_args)


# python file.py "exist" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "hive规则模板修改"
# python file.py "exist" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "接口设计与表设计.xls"
# python file.py "count" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "2"
# python file.py "count" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "2"
# python file.py "type" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "xls,doc,txt"
# python file.py "type" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "xls,doc,txt"
# python file.py "size" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "398"
# python file.py "size" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "445"
# python file.py "date" "10.10.50.68" "198" "ftptest" "123456" "1" "222" "2023-12-09 06:34:45"
# python file.py "date" "10.10.50.156" "21" "ftptest" "123456" "1" "/var/ftp/test" "2023-09-14 06:14:45"


# python file.py "exist" "10.10.61.146" "22" "test" "test" "2" "/" "2.log"
# python file.py "count" "10.10.90.246" "22" "root" "Root1209." "2" "/root" "2"
# python file.py "size" "10.10.90.246" "22" "root" "Root1209." "2" "/root" "1201"
# python file.py "type" "10.10.61.146" "22" "test" "test" "2" "/" "log,zip,jar"
# python file.py "date" "10.10.61.146" "22" "test" "test" "2" "/" "2023-09-14 06:14:45"


if __name__ == '__main__':
    read_argv()
    resp = service(f_cmd, f_host, f_port, f_account, f_password, f_protocol, f_path, f_args)
    print(resp)
    exit(0)

