#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Jone Chiang
# @file  : start.py 
# @time  : 2018/11/03 19:25:17

from scrapy import cmdline

cmdline.execute('scrapy crawl qiushi'.split())
