#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : monitor.py
# @Author : Norah C.IV
# @Time : 2022/4/21 10:37
# @Software: PyCharm
import re
import requests
import urllib3

from prettytable import PrettyTable

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
table = PrettyTable()

table.field_names = ['\033[0;32mOptions\033[0m', '\033[0;32mHref\033[0m']


class Monitor:
    @staticmethod
    def repo(keyword):
        keywords = None

        if ' ' in keyword:
            keywords = keyword.replace(' ', '+')
        else:
            keywords = keyword

        repo_url = "https://github.com/search?q=" + keywords + ""

        try:
            response = requests.get(url=repo_url, timeout=60, verify=False)
            response_data = response.content.decode('utf-8')
            repo_num_re = re.findall('Showing ([\d,]*?) available', response_data)
            if repo_num_re:
                repo_num = (repo_num_re[0].replace(',', ''))
            else:
                repo_num_re = re.findall('    ([\d,]*?) repository results', response_data)
                if repo_num_re:
                    repo_num = (repo_num_re[0].replace(',', ''))
                else:
                    repo_num = (0)
            repo_list = re.findall('py-4 public sou(.*?)</li>', response_data, re.S)
            repo_data = ''
            repo_num = 1
            for repo_re in repo_list:
                repo_path = re.findall('" href="(.*?)">', repo_re)[0]
                repo_url = "https://github.com" + repo_path
                repo_show = re.findall('<p class="mb-1">(.*?)</p>', repo_re, re.S)
                if repo_show:
                    repo_show = repo_show[0].replace(' ', '').replace('\n', ' ').replace('\'', ' ').replace('\r', ' ')
                else:
                    repo_show = ''
                table.add_row([repo_num, repo_url])
                repo_num += 1
                repo_data += repo_url + ' ' + repo_show + '\n'
            print(table)
        except Exception:
            print('\033[0;31m[-] Error: Some Error Occurred!Please Enter Again!\033[0m')
        finally:
            table.clear_rows()

    @staticmethod
    def commit(keyword):
        keywords = None

        if ' ' in keyword:
            keywords = keyword.replace(' ', '+')
        else:
            keywords = keyword

        commit_url = "https://github.com/search?q=" + keywords + "&type=Commits"

        try:
            response = requests.get(url=commit_url, timeout=60, verify=False)
            commit_data = response.content.decode('utf-8')
            commits_num_re = re.findall('Showing ([\d,]*?) available', commit_data)
            if commits_num_re:
                commits_num = (commits_num_re[0].replace(',', ''))
            else:
                commits_num_re = re.findall('    ([\d,]*?) commit results', commit_data)
                if commits_num_re:
                    commits_num = commits_num_re[0].replace(',', '')
                else:
                    commits_num = 0
            commit_list = re.findall('js-details-container Details py-(.*?)</relative-time>', commit_data,
                                     re.S)
            commit_data = ''
            commit_num = 1
            for commit_re in commit_list:
                commit_path = re.findall('" href="(.*?)">', commit_re)[0]
                commit_url = "https://github.com" + commit_path
                commit_show = re.findall('<a class="message js-navigation-open" aria-label="(.*?)" data-pjax="true"',
                                         commit_re, re.S)
                if commit_show:
                    commit_show = commit_show[0].replace(' ', '').replace('\n', ' ').replace('\'', ' ').replace('\r', ' ')
                else:
                    commit_show = ''
                commit_data += commit_url + ' ' + commit_show + '\n'
                table.add_row([commit_num, commit_url])
                commit_num += 1
            print(table)
        except Exception:
            print('\033[0;31m[-] Error: Some Error Occurred!Please Enter Again!\033[0m')
        finally:
            table.clear_rows()

    @staticmethod
    def issue(keyword):
        keywords = None

        if ' ' in keyword:
            keywords = keyword.replace(' ', '+')
        else:
            keywords = keyword

        issue_url = "https://github.com/search?q=" + keywords + "&type=Issues"

        try:
            response = requests.get(url=issue_url, timeout=60, verify=False)
            issue_data = response.content.decode('utf-8')
            issues_num_re = re.findall('Showing ([\d,]*?) available', issue_data)
            if issues_num_re:
                issues_num = (issues_num_re[0].replace(',', ''))
            else:
                issues_num_re = re.findall('<h3>\n    ([\d,]*?) issues', issue_data)
                if issues_num_re:
                    issues_num = (issues_num_re[0].replace(',', ''))
                else:
                    issues_num = (0)
            issues_list = re.findall('<div class="issue-list-item d-flex py-4 hx_hit-issue(.*?)</relative-time>', issue_data, re.S)
            issues_data = ''
            issue_num = 1
            for issues_re in issues_list:
                issues_path = re.findall('" href="(.*?)">', issues_re)[0]
                issues_url = "https://github.com" + issues_path
                issues_title = re.findall('<a title="(.*?)"', issues_re)[0]
                issues_show = re.findall('<p class="mb-0">(.*?)</p>', issues_re, re.S)
                if issues_show:
                    issues_show = issues_show[0].replace(' ', '').replace('\n', ' ').replace('\'', ' ').replace('\r', ' ')
                else:
                    issues_show = ''
                issues_data += issues_url + ' ' + issues_title + ' ' + issues_show + '\n'
                table.add_row([issue_num, issues_url])
                issue_num += 1
            print(table)
        except Exception:
            print('\033[0;31m[-] Error: Some Error Occurred!Please Enter Again!\033[0m')
        finally:
            table.clear_rows()

    @staticmethod
    def wiki(keyword):
        keywords = None

        if ' ' in keyword:
            keywords = keyword.replace(' ', '+')
        else:
            keywords = keyword

        wiki_url = "https://github.com/search?q=" + keywords + "&type=Wikis"

        try:
            response = requests.get(url=wiki_url, timeout=60, verify=False)
            wiki_data = response.content.decode('utf-8')
            wikis_num_re = re.findall('Showing ([\d,]*?) available', wiki_data)
            if wikis_num_re:
                wikis_num = (wikis_num_re[0].replace(',', ''))
            else:
                wikis_num_re = re.findall('    ([\d,]*?) wiki results', wiki_data)
                if wikis_num_re:
                    wikis_num = (wikis_num_re[0].replace(',', ''))
                else:
                    wikis_num = (0)
            wikis_list = re.findall('<div class="f4 text-normal">(.*?)</relative-time>', wiki_data, re.S)
            wikis_data = ''
            wiki_num = 1
            for wikis_re in wikis_list:
                wikis_path = re.findall('" href="(.*?)">', wikis_re)[0]
                wikis_url = "https://github.com" + wikis_path
                wikis_show = re.findall('<p class="mb-1 width-full">(.*?)</p>', wikis_re, re.S)
                if wikis_show:
                    wikis_show = wikis_show[0].replace(' ', '').replace('\n', ' ').replace('\'', ' ').replace('\r', ' ')
                else:
                    wikis_show = ''
                wikis_data += wikis_url + ' ' + wikis_show + '\n'
                table.add_row([wiki_num, wikis_url])
                wiki_num += 1
            print(table)
        except Exception:
            print('\033[0;31m[-] Error: Some Error Occurred!Please Enter Again!\033[0m')
        finally:
            table.clear_rows()
