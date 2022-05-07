#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : format_table.py
# @Author : Norah C.IV
# @Time : 2022/5/7 14:13
# @Software: PyCharm
import os
import platform

from prettytable import PrettyTable
from begin.get_file import find_file


class TableFormat:
    def __init__(self):
        self.main_table = PrettyTable()
        self.vuln_table = PrettyTable()
        self.port_table = PrettyTable()
        self.passwd_table = PrettyTable()
        self.github_table = PrettyTable()
        self.poc_table = PrettyTable()
        self.monitor_table = PrettyTable()
        self.port_results = PrettyTable()

    def main_format(self):
        self.main_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mContents\033[0m',
                                       '\033[0;32mChinese Name\033[0m']
        self.main_table.add_row(['1', '\033[0;33mVulnerability Detection\033[0m', '\033[0;31m漏洞扫描\033[0m'])
        self.main_table.add_row(['2', '\033[0;33mNmap Port Scan\033[0m', '\033[0;31mNmap端口扫描\033[0m'])
        self.main_table.add_row(['3', '\033[0;33mWeak Password Attack\033[0m', '\033[0;31m弱口令攻击\033[0m'])
        self.main_table.add_row(['4', '\033[0;33mGitHub Spider\033[0m', '\033[0;31mGitHub爬虫\033[0m'])
        self.main_table.add_row(['0', '\033[0;33mExit The Program\033[0m', '\033[0;31m退出程序\033[0m'])

        return self.main_table

    def vuln_format(self):
        self.vuln_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mScan Type\033[0m']
        self.vuln_table.add_row(['1', '\033[0;33m指定加载POC\033[0m'])
        self.vuln_table.add_row(['2', '\033[0;33m批量加载POC\033[0m'])
        self.vuln_table.add_row(['3', '\033[0;33m查看所有POC\033[0m'])
        self.vuln_table.add_row(['0', '\033[0;33mGo Back\033[0m'])

        return self.vuln_table

    def poc_format(self):
        os_platform = platform.platform()

        self.poc_table.field_names = ['\033[0;32mNumber\033[0m', '\033[0;32mPoc File\033[0m']
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        f = find_file(root_path + "/pocsuite3/pocs", filter_strs=[".pyc", "__init__"])
        i = 1
        for items in f:
            file_name = ''
            if 'Windows' in os_platform:
                file_name = items.replace(root_path + "\pocsuite3\pocs\\", '')
            elif 'Linux' in os_platform:
                file_name = items.replace(root_path + "/pocsuite3/pocs/", '')
            self.poc_table.add_row([i, file_name])
            i += 1

        return self.poc_table

    def port_format(self):
        self.port_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m',
                                       '\033[0;32mNotes\033[0m']
        self.port_table.add_row(['1', '\033[0;33mSimplify\033[0m', '\033[0;31m精简端口扫描\033[0m'])
        self.port_table.add_row(['2', '\033[0;33mGeneral\033[0m', '\033[0;31m常规端口扫描\033[0m'])
        self.port_table.add_row(['3', '\033[0;33mAll\033[0m', '\033[0;31m全端口扫描\033[0m'])
        self.port_table.add_row(['0', '\033[0;33mGo Back\033[0m', '\033[0;31m\033[0m'])

        self.port_results.field_names = ['\033[0;32mIP\033[0m', '\033[0;32mPort\033[0m', '\033[0;32mProtocol\033[0m',
                                         '\033[0;32mStatus\033[0m']

        return self.port_table, self.port_results

    def passwd_format(self):
        self.passwd_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mContents\033[0m',
                                         '\033[0;32mDefault Port\033[0m', '\033[0;32mDirection of Attack\033[0m']
        self.passwd_table.add_row(['1', '\033[0;33mFTP\033[0m', '\033[0;33m21\033[0m',
                                   '\033[0;31m允许匿名的上传、下载、爆破和嗅探操作\033[0m'])
        self.passwd_table.add_row(['2', '\033[0;33mLdap\033[0m', '\033[0;33m389\033[0m',
                                   '\033[0;31m注入、允许匿名访问、弱口令\033[0m'])
        self.passwd_table.add_row(['3', '\033[0;33mMemCache\033[0m', '\033[0;33m11211\033[0m',
                                   '\033[0;31m未授权访问\033[0m'])
        self.passwd_table.add_row(['4', '\033[0;33mMongoDB\033[0m', '\033[0;33m27017\033[0m',
                                   '\033[0;31m爆破、未授权访问\033[0m'])
        self.passwd_table.add_row(['5', '\033[0;33mMssql\033[0m', '\033[0;33m1433\033[0m',
                                   '\033[0;31m注入、提权、SA弱口令、爆破\033[0m'])
        self.passwd_table.add_row(['6', '\033[0;33mMysql\033[0m', '\033[0;33m3306\033[0m',
                                   '\033[0;31m注入、提权、爆破\033[0m'])
        self.passwd_table.add_row(['7', '\033[0;33mPostgreSQL\033[0m', '\033[0;33m5432\033[0m',
                                   '\033[0;31m爆破、注入、弱口令\033[0m'])
        self.passwd_table.add_row(['8', '\033[0;33mRedis\033[0m', '\033[0;33m6379\033[0m',
                                   '\033[0;31m未授权访问、弱口令爆破\033[0m'])
        self.passwd_table.add_row(['9', '\033[0;33mSSH\033[0m', '\033[0;33m22\033[0m',
                                   '\033[0;31mSSH隧道及内网代理转发、文件传输\033[0m'])
        self.passwd_table.add_row(['10', '\033[0;33mTelnet\033[0m', '\033[0;33m23\033[0m',
                                   '\033[0;31m爆破、嗅探、弱口令\033[0m'])
        self.passwd_table.add_row(['11', '\033[0;33mVNC\033[0m', '\033[0;33m5900\033[0m', '\033[0;31m弱口令爆破\033[0m'])
        self.passwd_table.add_row(['0', '\033[0;33mGo Back\033[0m', '\033[0;33m\033[0m', '\033[0;31m\033[0m'])

        return self.passwd_table

    def github_format(self):
        self.github_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mDescription\033[0m']
        self.github_table.add_row(['1', '\033[0;33mRepositories\033[0m'])
        self.github_table.add_row(['2', '\033[0;33mCommits\033[0m'])
        self.github_table.add_row(['3', '\033[0;33mIssues\033[0m'])
        self.github_table.add_row(['4', '\033[0;33mWikis\033[0m'])
        self.github_table.add_row(['0', '\033[0;33mGo Back\033[0m'])

        return self.github_table

    def monitor_format(self):
        self.monitor_table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mHref\033[0m']

        return self.monitor_table
