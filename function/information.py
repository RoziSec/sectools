#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : information.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:58
# @Software: PyCharm
import sys
import os
import platform

from main import begin
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m']
table.add_row(['1', '\033[0;33mRepositories\033[0m'])


class Information:
    @staticmethod
    def scan():
        os_platform = platform.platform()
        if 'Windows' in os_platform:
            os.system('cls')
        elif 'Linux' in os_platform:
            os.system('clear')
        print(table)
        while True:
            info_choices = input('\033[0;32mNorah C.IV\033[0m > ')
            if info_choices == '1':
                print(1)
            elif info_choices == '2':
                print(2)
            elif info_choices == '3':
                print(3)
            elif info_choices == '4':
                print(4)
            elif info_choices == '5':
                print(5)
            elif info_choices == '0':
                begin()
            else:
                sys.exit(0)
