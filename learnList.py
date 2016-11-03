#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 03/11/2016


import urllib
from bs4 import BeautifulSoup

import sys

# 解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误
# http://wangye.org/blog/archives/629/
reload(sys)
sys.setdefaultencoding('utf-8')


html = urllib.urlopen('http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000').read()

soup = BeautifulSoup(html, 'html.parser')

arr = soup.select('#main .x-sidebar-left .uk-nav li a')


def getLearnListFun():
    count = 0
    word = ''
    for i in arr:
        count += 1
        label = i.text + ' ' + str(count) + '\n'
        word += label

    with open('LearnList.txt', 'w') as f:
        f.write(word)

if __name__ == '__main__':
    getLearnListFun()