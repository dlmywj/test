#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  os
class path_util():

    #获取项目路径
    def get_path(self):
        porject_path=os.path.dirname(os.path.dirname(__file__))
        return porject_path