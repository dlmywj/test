#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import requests
from common.yaml_util import yamlutil
import pytest


class Test_request():

    @pytest.mark.parametrize('caseinfo',yamlutil().read_ecase_more('case_yaml.yml','get_code'))
    def test_code(self,caseinfo):
        mothod= caseinfo['request']['mothod']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        rep = requests.request(mothod,url=url,json=data)
        # 获取验证码code
        print(rep.json())
        assert 'code' in rep.json()

        # try:
        #     yamlutil().write_extract_yaml({'code':rep.json()['data']['code']['code']})
        #
        # except:
        #     raise FileNotFoundError('验证频繁，请稍后再试')

    # @pytest.mark.parametrize('caseinfo',yamlutil().read_ecase_more('case_yaml.yml','get_token'))
    # def test_post_token(self,caseinfo):
    #     mothod = caseinfo['request']['mothod']
    #     url = caseinfo['request']['url']
    #     # data = {}
    #     # data.update(caseinfo['request']['data'])
    #     # data.update({'code':yamlutil().read_extract_yaml("code")})
    #     data=dict(**caseinfo['request']['data'],**{'code':yamlutil().read_extract_yaml("code")})
    #     rep = requests.request(mothod,url=url,json=data)
    #     # 前端登录，获取token
    #     print(rep.json()["data"]["token"])
    #
    #     try:
    #         yamlutil().write_extract_yaml({'token': rep.json()["data"]["token"]})
    #         # a=yamlutil().read_extract_yaml('token')
    #         # print(a)
    #     except:
    #         raise  FileNotFoundError('未获取到token')
    #
    #
    # @pytest.mark.parametrize('caseinfo',yamlutil().read_ecase_more('case_yaml.yml','login'))
    # def test_get(self,caseinfo,conn_database):
    #         url = caseinfo['request']['url']
    #         mothod = caseinfo['request']['mothod']
    #         headers={
    #             'x-token':yamlutil().read_extract_yaml('token')
    #         }
    #         rep = requests.request(mothod,url=url,headers=headers)
    #         # 获取用户信息
    #         print(rep.json())


# url='http://101.133.235.37:9970/api/user/login'
# data={
#     "username":"15233385253",
#     "code":"0663"
# }
# rep=requests.post(url=url,json=data)
# print(rep.json())
#
# # 请求
# requests.post()
# requests.get()
# requests.delete()
# requests.put()
# requests.request()
# # # 响应
# rep=requests.request()
# print(rep.json())
# print(rep.text)
# print(rep.content)
# print(rep.status_code)
# print(rep.cookies)
# print(rep.encoding)
# print(rep.headers)
