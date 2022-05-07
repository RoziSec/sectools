#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : passwdscan.py
# @Author : Norah C.IV
# @Time : 2022/4/19 23:51
# @Software: PyCharm
import os
import sys


from main import begin
from begin.format_table import TableFormat


class WeakPassword:
    @staticmethod
    def scan(command, root_path):
        print(TableFormat().passwd_format())
        print('\033[0;33m[*] Choose The Brute Type\033[0m')
        while True:
            try:
                brute_choice = input('\033[0;32mNorah C.IV\033[0m > ')
                if brute_choice == '1':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/ftp_burst.py --verify")

                elif brute_choice == '2':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/ldap_burst.py --verify")

                elif brute_choice == '3':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/memcache_burst.py --verify")

                elif brute_choice == '4':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/mongodb_burst.py --verify")

                elif brute_choice == '5':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/mssql_burst.py --verify")

                elif brute_choice == '6':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/mysql_burst.py --verify")

                elif brute_choice == '7':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/postgresql_burst.py --verify")

                elif brute_choice == '8':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/redis_burst.py --verify")

                elif brute_choice == '9':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/ssh_burst.py --verify")

                elif brute_choice == '10':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/telnet_burst.py --verify")

                elif brute_choice == '11':
                    host = input('\033[0;33m[+] Please enter host\033[0m：')
                    port = input('\033[0;33m[+] Please enter port\033[0m：')
                    os.system(command + "/pocsuite3/cli.py -u " + host + ':' + port + " -r " + root_path +
                              "/pocsuite3/brute/vnc_burst.py --verify")

                elif brute_choice == '0':
                    begin()

                else:
                    print('\033[0;31m[-] Error: Invalid Brute Type!Please Retype It!\033[0m')

            except KeyboardInterrupt:
                print('')
                print('[-] Exited By User')
                sys.exit(0)
