#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : start.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:40
# @Software: PyCharm
import sys

from function.vulscan import Vulnerability
from function.portscan import Portscan
from function.passwdscan import WeakPassword
from function.github import GitHub
from main import begin


class start:
    @staticmethod
    def loop():
        while True:
            try:
                choose = input('\033[0;32mNorah C.IV\033[0m > ')
                if choose == '1':
                    Vulnerability.scan()
                elif choose == '2':
                    Portscan.scan()
                elif choose == '3':
                    WeakPassword.scan()
                elif choose == '4':
                    GitHub.scan()
                elif choose == '0':
                    print('[-] Exited By User')
                    sys.exit(0)
                else:
                    print('[-] Error Param!')
            except KeyboardInterrupt:
                print('')
                exit_command = input('[+] Enter Y/n to exit(Default is Y)：')
                if exit_command == '' or exit_command.lower() == 'y':
                    sys.exit(0)
                elif exit_command.lower() == 'n':
                    begin()
