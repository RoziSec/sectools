#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : port.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:43
# @Software: PyCharm
import sys

from main import begin
from prettytable import PrettyTable
from port.scan import Nmap

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m', '\033[0;32mNotes\033[0m']
table.add_row(['1', '\033[0;33mSimplify\033[0m', '\033[0;31m精简端口扫描\033[0m'])
table.add_row(['2', '\033[0;33mGeneral\033[0m', '\033[0;31m常规端口扫描\033[0m'])
table.add_row(['3', '\033[0;33mAll\033[0m', '\033[0;31m全端口扫描\033[0m'])
table.add_row(['0', '\033[0;33mGo Back\033[0m', '\033[0;31m\033[0m'])


class Portscan:
    @staticmethod
    def scan():
        print(table)
        while True:
            try:
                portscan_choices = input('\033[0;32mNorah C.IV\033[0m > ')
                if portscan_choices == '1':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    Nmap().scan(host, 'sim')

                elif portscan_choices == '2':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    Nmap().scan(host, 'oft')

                elif portscan_choices == '3':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    Nmap().scan(host, 'all')

                elif portscan_choices == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Scan Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
