# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import docx

import pdfplumber
import pprint
from 项目.项目二_文书内容提取.编码处理模块.编码处理_文件格式 import Docx as D


class Docx_To_Txt():

    def __init__(self,path):
        self.path = path

    def open_docx(self):
        file=docx.Document(self.path)
        for para in file.paragraphs:
            yield para.text


    def to_txt(self):
        for content in self.open_docx():
            path_ = path.split('.')[0] + '.txt'
            with open(path_, 'a+')as f:
                f.write(content)
        print('任务全部完成。。。。。。。。。。。。。。。。。。。。。')
        return path_


class Pdf_To_Txt():

    def __init__(self,path):
        self.path = path

    def to_txt(self):
        print('这是第一层处理，将pdf转为txt格式一遍后续分词-----------------------------')
        pdf = pdfplumber.open(self.path)

        for page in pdf.pages:
            '''pages为函数？'''
            #pprint.pprint(page.extract_text())
            with open(self.path +'.txt', 'a', encoding='utf-8')as f:
                '''需要进行编码,r+用utf-8为乱码？r+用gbk写入正确，但是与w效果一样'''
                f.write(page.extract_text())
        print('任务全部完成。。。。。。。。。。。。。。。。。。。。。')
        path_ =self.path +'.txt'
        return  path_


'''对传入的文件格式进行判断'''
def check_file_types(path):
    """被调用的主函数"""
    if '.docx' in path:
        print('这是docx文件')
        return Docx_To_Txt(path).to_txt()
    elif '.pdf' in path:
        print('这是pdf文件')
        return Pdf_To_Txt(path).to_txt()
    elif path.split('.')[1] == 'doc':
        D(path).change_docx()
        for file_path in D(path).return_file_types():
            return file_path
    elif '.txt' in path:
        return path
    else:
        try:
            for file_path in glob.glob(os.path.join(path, "*")):
                check_file_types(file_path)

        except:

            print('不是pdf、doc、docx、txt、的格式，也不是一个文件夹： ')
            print()
            print('文件类型无法判断，需要人工负阅---------------------------------------------------')


#print(check_file_types(path))
#Pdf_change_to_txt(path).to_txt()
