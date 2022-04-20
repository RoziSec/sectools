#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : github.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:53
# @Software: PyCharm
import sys

from main import begin
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m']
table.add_row(['1', '\033[0;33mRepositories\033[0m'])
table.add_row(['2', '\033[0;33mCommits\033[0m'])
table.add_row(['3', '\033[0;33mIssues\033[0m'])
table.add_row(['4', '\033[0;33mWikis\033[0m'])
table.add_row(['5', '\033[0;33mUsers\033[0m'])
table.add_row(['0', '\033[0;33mGo Back\033[0m'])


class GitHub:
    @staticmethod
    def scan():
        print(table)
        while True:
            github_choices = input('\033[0;32mNorah C.IV\033[0m > ')
            if github_choices == '1':
                print(1)
            elif github_choices == '2':
                print(2)
            elif github_choices == '3':
                print(3)
            elif github_choices == '4':
                print(4)
            elif github_choices == '5':
                print(5)
            elif github_choices == '0':
                begin()
            else:
                sys.exit(0)
