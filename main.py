#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : main.py
# @Author : Norah C.IV
# @Time : 2022/4/18 10:27
# @Software: PyCharm
import os
import platform

from begin import start
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mContents\033[0m', '\033[0;32mChinese Name\033[0m']
table.add_row(['1', '\033[0;33mInformation Collection\033[0m', '\033[0;31m信息收集\033[0m'])
table.add_row(['2', '\033[0;33mVulnerability Detection\033[0m', '\033[0;31m漏洞扫描\033[0m'])
table.add_row(['3', '\033[0;33mNmap Port Scan\033[0m', '\033[0;31mNmap端口扫描\033[0m'])
table.add_row(['4', '\033[0;33mWeak Password Attack\033[0m', '\033[0;31m弱口令攻击\033[0m'])
table.add_row(['5', '\033[0;33mGitHub Spider\033[0m', '\033[0;31mGitHub爬虫\033[0m'])
table.add_row(['0', '\033[0;33mExit The Program\033[0m', '\033[0;31m退出程序\033[0m'])


def begin():
    print(table)
    print('\033[0;33m[*] Choose The Attack Module\033[0m')
    start.start().loop()


if __name__ == '__main__':
    os_platform = platform.platform()
    if 'Windows' in os_platform:
        os.system('cls')
    elif 'Linux' in os_platform:
        os.system('clear')
    program_logo = '''\033[0;31m
███████╗███████╗ ██████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████╗█████╗  ██║        ██║   ██║   ██║██║   ██║██║     ███████╗
╚════██║██╔══╝  ██║        ██║   ██║   ██║██║   ██║██║     ╚════██║
███████║███████╗╚██████╗   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚══════╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝\033[0m'''
    print(program_logo)
    begin()
