# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from 项目.项目二_文书内容提取.输出模块.词云输出.词云 import pdf_ciyun as pdf


def simple_pdf(path):
    """单个pdf文档传入"""
    pdf(path)
path = ''
simple_pdf(path)


def _file(path):
    """文件夹"""
    pdf(
        path
    )
path = ''
_file(path)