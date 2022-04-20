#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : start.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:40
# @Software: PyCharm
import sys

from function.information import Information
from function.vulscan import Vulnerability
from function.portscan import Portscan
from function.passwdscan import WeakPassword
from function.github import GitHub


class start:
    @staticmethod
    def loop():
        while True:
            try:
                choose = input('\033[0;32mNorah C.IV\033[0m > ')
                if choose == '1':
                    Information.scan()
                elif choose == '2':
                    Vulnerability.scan()
                elif choose == '3':
                    Portscan.scan()
                elif choose == '4':
                    WeakPassword.scan()
                elif choose == '5':
                    GitHub.scan()
                elif choose == '0':
                    print('[-] Exited By User')
                    sys.exit(0)
                else:
                    print('[-] Error Param!')
            except KeyboardInterrupt:
                print('')
                print('[-] Exited By Ctrl-C')
                sys.exit(0)
