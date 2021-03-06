#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : vulscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:46
# @Software: PyCharm
import sys
import os

from scan_start.format_table import TableFormat
from main import begin


class Vulnerability:
    @staticmethod
    def scan(command, root_path):
        print(TableFormat().vuln_format())
        while True:
            try:
                vuln_choices = input('\033[0;32mNorah C.IV\033[0m (\033[0;31m漏洞扫描\033[0m) > ')
                if vuln_choices == '1':
                    poc_name = input('\033[0;33m[+] Please enter poc name\033[0m：')
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/pocs/" + poc_name + ".py --verify --plugins html_report")

                elif vuln_choices == '2':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + " -r " + root_path +
                              "/pocsuite3/pocs/ --plugins html_report")

                elif vuln_choices == '3':
                    print(TableFormat().poc_format())

                elif vuln_choices == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Vulnerability Scan Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
