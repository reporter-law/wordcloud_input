# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获: 需要函数值需要return，不能仅仅只执行函数，这样函数不会将值返回
from 项目.项目二_文书内容提取.编码处理模块 import 全部转为txt as tx
import pprint

#文件类型判断及其处理
def file_shunt(path_):
    """
    依据传入的path的类型的不同而进行不同处理，传入字符串的进行直接切词，非字符串的先进行格式处理转为字符串
    :param path_:
    :return:
    此处不能进行文件类型判断，因为文件需要继续向上传入以进行格式转化，暂时不想改了
    """
    if len(path_) <= 10:
        print('可能为空集----------------------------------------------------------------')


    elif len(path_) <= 50 :
        try:
            path = tx.check_file_types(path_)  # 'I:\迅雷下载\捕诉\我国_捕诉合一_模式的正当性及其限度_洪浩.pdf.txt'
            return path

        except:
            pprint.pprint('这里出错：可能原因为传入数据库的内容为空或者pdf地址超过50个字符串长度或者原因不明')


        '''对传入的是字符串的内容进行初步处理'''
    else:
        '''使用数据库的停用词处理方法，普通的文档处理方法缺乏字符串处理'''
        print('此处为字符串直接传入的接口---------------------------------------------------------')
        words = str(path_).replace('[','').replace(']','').strip()

        print('文档类型分流处状态：顺利通过！！！！！！！！！！！！！！！！！！！！！！！！')
        return words

