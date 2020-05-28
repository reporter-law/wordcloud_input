# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import os


def re_name(dir_path, old_file, new_file):
    """
    os转docx
    :param dir_path:
    :param old_file:
    :param new_file:
    """
    os.renames(dir_path + "/" + old_file, dir_path + "/" + new_file)
dir_path = 'C:\\Users\\Administrator\\Desktop\\测试'
old_file = '啧啧啧.doc'
new_file = '啧啧啧.docx'
#re_name(dir_path,old_file,new_file)


import docx
path = 'C:\\Users\\Administrator\\Desktop\\测试\\啧啧啧.docx'
file = docx.Document(path)
for para in file.paragraphs:
    print(para.text)

'一样打不开'
