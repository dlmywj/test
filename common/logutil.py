#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import logging


#实例化对象;加载日志器
log = logging.getLogger('log')
#针对所有输出的第一层过滤
log.setLevel(level=logging.DEBUG)
#生成日志文件(句柄)
handler = logging.FileHandler('log.txt')
#设置日志文件的格式
formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s ')
#把设置的文件日志格式添加至log.txt
handler.setFormatter(formatter)
#获取控制台句柄,并设置日志句柄
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
#为logger对象添加句柄
log.addHandler(handler)
log.addHandler(console)

log.debug('这是一个debug')
log.info('这是一个信息')
log.warning('这是一个警告')
log.error('这是一个错误')
log.critical('这是一个致命错误')




