#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import yaml

class yamlutil():

    # 读取extract.yaml文件
    def read_extract_yaml(self,key):
        with open(os.getcwd()+'\\extract.yaml',mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f.read(),Loader=yaml.FullLoader)
            return value[key];

    # 写入extract.yaml文件
    def write_extract_yaml(self,data):
        with open(os.getcwd()+'\\extract.yaml',mode='a',encoding='utf-8') as f:
            value = yaml.dump(data=data,stream=f,allow_unicode=True)
            return value

    # 清除extract.yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd()+'\\extract.yaml',mode='w',encoding='utf-8') as f:
            f.truncate()

    # 读取case_yaml.yml文件
    def read_ecase_yaml(self,filename):
        with open('D:\\soft\\test\\pycharm\\pycharm-project\\case\\'+filename, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            return value;

    # 读取一个yaml文件中多个接口用例的方法
    def read_ecase_more(self,filename,groupname):
        with open('D:\\soft\\test\\pycharm\\pycharm-project\\case\\'+filename, mode='r', encoding='utf-8') as f:
            info = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            value = info[groupname]
            return value;






