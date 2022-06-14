#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hashlib

class sign_util():

    #筛选传参数据(json格式)
    def info(self,data):
        try:
            dic = {}     #定义一个空字典
            for key ,value in data.items():
                if key != 'sign' and  value != 'null' and value != '':
                    dic[key] = value
            return  dic
        except:
            raise  Exception ('传参格式有误,请检查!!!')

    #将筛选后的传参数据生成md5加密格式的字符, 串参数名=参数值&....&参数名n=参数值n
    def signstring(self,data):
        dic1 = sign_util().info(data)
        str1 = ''
        list = dic1.keys()
        for i in list:
            str1 = str1 + i + '=' + str(dic1[i]) + '&'
        return str1[0:-1]

    # 根据MD5传参字符串格式进行加密,返回MD5加密后的大写字符串
    def getsign(self, data):
        signstring = sign_util().signstring(data)
        # 创建MD5
        md = hashlib.md5()
        # 对stringA字符串进行编码
        md.update(signstring.encode('utf-8'))
        # 数据加密
        signValue = md.hexdigest()
        # 把加密的结果，小写转换成大写，upper函数
        signValue = signValue.upper()
        return signValue





if __name__ == '__main__':
    alldata = {
        "content": "哦哦哦哦",
        "image": "http://static.rulin49.com/055ef6397ec8d2ef6308ee35acf4108b.jpg?w=1334&h=750 ",
        "labelId": "49",
        "locationId": "60a8c64c91a04c4d98ccf48ac51243d8",
        "sign": "00612E7A9FFDFF2C24284BC89E9A35DA",
        "type": "6",
        "bid": 'null',
        "num": "",
        'phone': 1571754405
    }
    a = sign_util().getsign(alldata)
    print(a)









