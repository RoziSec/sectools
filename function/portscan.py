#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : port.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:43
# @Software: PyCharm
import sys

from main import begin
from begin.format_table import TableFormat
from port.scan import Nmap


class Portscan:
    @staticmethod
    def scan():
        print(TableFormat().port_format()[0])
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
