#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : vulscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:46
# @Software: PyCharm
import sys
import os
import platform

from begin.get_file import find_file
from main import begin
from prettytable import PrettyTable

os_platform = platform.platform()
poc_table = PrettyTable()
poc_table.field_names = ['\033[0;32mNumber\033[0m', '\033[0;32mPoc File\033[0m']

scan_table = PrettyTable()
scan_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mScan Type\033[0m']
scan_table.add_row(['1', '\033[0;33m指定加载POC\033[0m'])
scan_table.add_row(['2', '\033[0;33m批量加载POC\033[0m'])
scan_table.add_row(['3', '\033[0;33m查看所有POC\033[0m'])
scan_table.add_row(['0', '\033[0;33mGo Back\033[0m'])

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = find_file(root_path + "/pocsuite3/pocs", filter_strs=[".pyc", "__init__"])

if 'Windows' in os_platform:
    command = 'python '
elif 'Linux' in os_platform:
    command = 'python3 '

i = 1
for items in f:
    file_name = ''
    if 'Windows' in os_platform:
        file_name = items.replace(root_path + "\pocsuite3\pocs\\", '')
    elif 'Linux' in os_platform:
        file_name = items.replace(root_path + "/pocsuite3/pocs/", '')
    poc_table.add_row([i, file_name])
    i += 1


class Vulnerability:
    @staticmethod
    def scan():
        print(scan_table)
        while True:
            try:
                vuln_choices = input('\033[0;32mNorah C.IV\033[0m > ')
                if vuln_choices == '1':
                    poc_name = input('\033[0;33m[+] Please enter poc name\033[0m：')
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/pocs/" + poc_name + ".py --verify --plugins html_report")

                elif vuln_choices == '2':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + " -r " + root_path +
                              "/pocsuite3/pocs/ --plugins html_report")

                elif vuln_choices == '3':
                    print(poc_table)

                elif vuln_choices == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Vulnerability Scan Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
