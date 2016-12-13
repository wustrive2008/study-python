#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 遍历打印目录下的pdf文件
'''

import os, os.path
import re

def print_pdf (root, dirs, files):
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if re.search(r".*\.pdf", path):
            print(path)

for root, dirs, files in os.walk('/Users/wubaoguo/Documents/pdf文档'):
    print_pdf(root, dirs, files)

