# coding=utf-8
import re

import paramiko
from paramiko.channel import Channel


def conn_ssh():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('10.10.50.68', 22, 'ftptest', '123456')
    ssh_client.exec_command("cd 222")
    std_in, std_out, std_err = ssh_client.exec_command("ls -l")
    for line in std_out:
        print(line.strip("\n"))
    ssh_client.close()


def conn():
    try:
        # transport = paramiko.Transport(("10.10.90.246", 22))
        # transport.connect(username="root", password="Root1209.")
        transport = paramiko.Transport(("10.10.61.146", 22))
        transport.connect(username="test", password="test")
        sftp = paramiko.SFTPClient.from_transport(transport)
        put_local_path = "D:\\temp\\22-3.log"
        get_remote_path = "exp_2023_02_22_17_18_20.log"
        sftp.get(get_remote_path, put_local_path)
        listdir = sftp.listdir("/")
        print(listdir)
        listdir_attr = sftp.listdir_attr("/")
        print(listdir_attr)
        sftp.close()
    except Exception as e:
        print(e)


def match():
    s = "<SFTPAttributes: [ size=58792921 mode=0o100777 atime=1695094419 mtime=1672042114 ]>"
    p = r'size=\d+'
    print(re.findall(p, s)[0])

    p = r'atime=\d+'
    print(re.findall(p, s)[0])

    p = r'mtime=\d+'
    print(re.findall(p, s)[0])


if __name__ == '__main__':
    match()

