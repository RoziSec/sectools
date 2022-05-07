#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : main.py
# @Author : Norah C.IV
# @Time : 2022/4/18 10:27
# @Software: PyCharm
import os
import platform

from scan_start import start
from scan_start.format_table import TableFormat


def begin():
    try:
        print(TableFormat().main_format())
        print('\033[0;33m[*] Choose The Attack Module\033[0m')
        start.start().loop()
    except KeyboardInterrupt:
        print('Ctrl-C')


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
