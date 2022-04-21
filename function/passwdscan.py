#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : passwdscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:51
# @Software: PyCharm
import sys
import os
import platform

from prettytable import PrettyTable
from main import begin

table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mContents\033[0m', '\033[0;32mDirection of Attack\033[0m']
table.add_row(['1', '\033[0;33mFTP\033[0m', '\033[0;31m允许匿名的上传、下载、爆破和嗅探操作\033[0m'])
table.add_row(['2', '\033[0;33mLdap\033[0m', '\033[0;31m注入、允许匿名访问、弱口令\033[0m'])
table.add_row(['3', '\033[0;33mMemCache\033[0m', '\033[0;31m未授权访问\033[0m'])
table.add_row(['4', '\033[0;33mMongoDB\033[0m', '\033[0;31m爆破、未授权访问\033[0m'])
table.add_row(['5', '\033[0;33mMssql\033[0m', '\033[0;31m注入、提权、SA弱口令、爆破\033[0m'])
table.add_row(['6', '\033[0;33mMysql\033[0m', '\033[0;31m注入、提权、爆破\033[0m'])
table.add_row(['7', '\033[0;33mPostgreSQL\033[0m', '\033[0;31m爆破、注入、弱口令\033[0m'])
table.add_row(['8', '\033[0;33mRedis\033[0m', '\033[0;31m未授权访问、弱口令爆破\033[0m'])
table.add_row(['9', '\033[0;33mSSH\033[0m', '\033[0;31mSSH隧道及内网代理转发、文件传输\033[0m'])
table.add_row(['10', '\033[0;33mTelnet\033[0m', '\033[0;31m爆破、嗅探、弱口令\033[0m'])
table.add_row(['11', '\033[0;33mVNC\033[0m', '\033[0;31m弱口令爆破\033[0m'])
table.add_row(['0', '\033[0;33mGo Back\033[0m', '\033[0;31m\033[0m'])


class WeakPassword:
    @staticmethod
    def scan():
        os_platform = platform.platform()
        if 'Windows' in os_platform:
            os.system('cls')
        elif 'Linux' in os_platform:
            os.system('clear')
        print(table)
        print('\033[0;33m[*] Choose The Brute Type\033[0m')
        while True:
            brute_choice = input('\033[0;32mNorah C.IV\033[0m > ')
            if brute_choice == '1':
                print('ssh brute')
            elif brute_choice == '2':
                print('ftp brute')
            elif brute_choice == '0':
                begin()
            else:
                sys.exit(0)
