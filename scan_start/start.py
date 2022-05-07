#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : start.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:40
# @Software: PyCharm
import os
import sys
import platform

from scan_func.vulscan import Vulnerability
from scan_func.portscan import Portscan
from scan_func.passwdscan import WeakPassword
from scan_func.github import GitHub
from main import begin

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os_platform = platform.platform()
if 'Windows' in os_platform:
    command = 'python ' + root_path
elif 'Linux' in os_platform:
    command = 'python3 ' + root_path


class start:
    @staticmethod
    def loop():
        while True:
            try:
                choose = input('\033[0;32mNorah C.IV\033[0m > ')
                if choose == '1':
                    Vulnerability.scan(command, root_path)

                elif choose == '2':
                    Portscan.scan()

                elif choose == '3':
                    WeakPassword.scan(command, root_path)

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
