#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : Github.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:53
# @Software: PyCharm
import sys

from main import begin
from prettytable import PrettyTable
from Github.monitor import Monitor

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m']
table.add_row(['1', '\033[0;33mRepositories\033[0m'])
table.add_row(['2', '\033[0;33mCommits\033[0m'])
table.add_row(['3', '\033[0;33mIssues\033[0m'])
table.add_row(['4', '\033[0;33mWikis\033[0m'])
table.add_row(['0', '\033[0;33mGo Back\033[0m'])


def keywords_input():
    keyword = input('[*] 输入关键词(多个关键词按空格分隔)\n'
                    '[*] 程序暂定只爬取第一页内容\n'
                    '\033[0;32mKeywords\033[0m : ')
    return keyword


class GitHub:
    @staticmethod
    def scan():
        print(table)
        print('\033[0;31m[+] 部分链接过长导致界面不美观，建议全屏运行\033[0m')
        while True:
            try:
                github_choices = input('\033[0;32mNorah C.IV\033[0m > ')

                if github_choices == '1':
                    keyword = keywords_input()
                    Monitor.repo(keyword)

                elif github_choices == '2':
                    keyword = keywords_input()
                    Monitor.commit(keyword)

                elif github_choices == '3':
                    keyword = keywords_input()
                    Monitor.issue(keyword)

                elif github_choices == '4':
                    keyword = keywords_input()
                    Monitor.wiki(keyword)

                elif github_choices == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Spider Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
