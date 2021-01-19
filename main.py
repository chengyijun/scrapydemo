# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: main.py
@time: 2021/1/19 16:35
@desc:
"""
from scrapy.cmdline import execute


def main():
    execute('scrapy crawl qsbk'.split())


if __name__ == '__main__':
    main()
