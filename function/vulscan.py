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
table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mPoc File\033[0m']
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = find_file(root_path + "/pocsuite3/pocs", filter_strs=[".pyc", "__init__"])
i = 1
for items in f:
    file_name = ''
    if 'Windows' in os_platform:
        file_name = items.replace(root_path + "\pocsuite3\pocs\\", '')
    elif 'Linux' in os_platform:
        file_name = items.replace(root_path + "/pocsuite3/pocs/", '')
    table.add_row([i, file_name])
    i += 1


class Vulnerability:
    @staticmethod
    def scan():
        print(table)
        while True:
            try:
                vuln_choices = input('\033[0;32mNorah C.IV\033[0m > ')
                if vuln_choices == '1':
                    print(1)

                elif vuln_choices == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Brute Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
