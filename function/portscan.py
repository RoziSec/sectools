#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : portscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:43
# @Software: PyCharm
import sys

from main import begin
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m', '\033[0;32mNotes\033[0m']
table.add_row(['1', '\033[0;33mSimplify\033[0m', '\033[0;33m精简端口扫描\033[0m'])
table.add_row(['2', '\033[0;33mGeneral\033[0m', '\033[0;33m常规端口扫描\033[0m'])
table.add_row(['3', '\033[0;33mAll\033[0m', '\033[0;33m全端口扫描\033[0m'])
table.add_row(['0', '\033[0;33mGo Back\033[0m', '\033[0;33m\033[0m'])


class Portscan:
    @staticmethod
    def scan():
        print(table)
        while True:
            github_choices = input('\033[0;32mNorah C.IV\033[0m > ')
            if github_choices == '1':
                print('精简端口')
            elif github_choices == '2':
                print('常规端口')
            elif github_choices == '3':
                print('全端口')
            elif github_choices == '0':
                begin()
            else:
                sys.exit(0)
