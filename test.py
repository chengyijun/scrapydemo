# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test.py
@time: 2021/1/19 20:03
@desc:
"""
import re


def main():
    sss = 'abc123def'
    res = re.findall(r'\d+', sss)
    print(type(res[0]))


if __name__ == '__main__':
    main()
