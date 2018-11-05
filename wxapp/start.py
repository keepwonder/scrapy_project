#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Jone Chiang
# @file  : start.py 
# @time  : 2018/11/05 22:46:19

from scrapy import cmdline

cmdline.execute('scrapy crawl wxapp_union'.split())
