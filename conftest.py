#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pytest

from common.yaml_util import yamlutil


@pytest.fixture(scope="function")
def conn_database():
    print('连接数据库成功')
    yield
    print('数据库已经关闭')

@pytest.fixture(scope='session',autouse=True)
def clear_extract_yaml():
    yamlutil().clear_extract_yaml()