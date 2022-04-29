#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : passwdscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:51
# @Software: PyCharm
import os
import sys
import platform

from prettytable import PrettyTable
from main import begin

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os_platform = platform.platform()
if 'Windows' in os_platform:
    command = 'python '
elif 'Linux' in os_platform:
    command = 'python3 '
table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mContents\033[0m', '\033[0;32mDefault Port\033[0m',
                     '\033[0;32mDirection of Attack\033[0m']
table.add_row(['1', '\033[0;33mFTP\033[0m', '\033[0;33m21\033[0m', '\033[0;31m允许匿名的上传、下载、爆破和嗅探操作\033[0m'])
table.add_row(['2', '\033[0;33mLdap\033[0m', '\033[0;33m389\033[0m', '\033[0;31m注入、允许匿名访问、弱口令\033[0m'])
table.add_row(['3', '\033[0;33mMemCache\033[0m', '\033[0;33m11211\033[0m', '\033[0;31m未授权访问\033[0m'])
table.add_row(['4', '\033[0;33mMongoDB\033[0m', '\033[0;33m27017\033[0m', '\033[0;31m爆破、未授权访问\033[0m'])
table.add_row(['5', '\033[0;33mMssql\033[0m', '\033[0;33m1433\033[0m', '\033[0;31m注入、提权、SA弱口令、爆破\033[0m'])
table.add_row(['6', '\033[0;33mMysql\033[0m', '\033[0;33m3306\033[0m', '\033[0;31m注入、提权、爆破\033[0m'])
table.add_row(['7', '\033[0;33mPostgreSQL\033[0m', '\033[0;33m5432\033[0m', '\033[0;31m爆破、注入、弱口令\033[0m'])
table.add_row(['8', '\033[0;33mRedis\033[0m', '\033[0;33m6379\033[0m', '\033[0;31m未授权访问、弱口令爆破\033[0m'])
table.add_row(['9', '\033[0;33mSSH\033[0m', '\033[0;33m22\033[0m', '\033[0;31mSSH隧道及内网代理转发、文件传输\033[0m'])
table.add_row(['10', '\033[0;33mTelnet\033[0m', '\033[0;33m23\033[0m', '\033[0;31m爆破、嗅探、弱口令\033[0m'])
table.add_row(['11', '\033[0;33mVNC\033[0m', '\033[0;33m5900\033[0m', '\033[0;31m弱口令爆破\033[0m'])
table.add_row(['0', '\033[0;33mGo Back\033[0m', '\033[0;33m\033[0m', '\033[0;31m\033[0m'])


class WeakPassword:
    @staticmethod
    def scan():
        print(table)
        print('\033[0;33m[*] Choose The Brute Type\033[0m')
        while True:
            try:
                brute_choice = input('\033[0;32mNorah C.IV\033[0m > ')
                if brute_choice == '1':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/ftp_burst.py --verify")

                elif brute_choice == '2':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/ldap_burst.py --verify")

                elif brute_choice == '3':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/memcache_burst.py --verify")

                elif brute_choice == '4':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/mongodb_burst.py --verify")

                elif brute_choice == '5':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/mssql_burst.py --verify")

                elif brute_choice == '6':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/mysql_burst.py --verify")

                elif brute_choice == '7':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/postgresql_burst.py --verify")

                elif brute_choice == '8':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/redis_burst.py --verify")

                elif brute_choice == '9':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/ssh_burst.py --verify")

                elif brute_choice == '10':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/telnet_burst.py --verify")

                elif brute_choice == '11':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + root_path + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/vnc_burst.py --verify")

                elif brute_choice == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Brute Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
