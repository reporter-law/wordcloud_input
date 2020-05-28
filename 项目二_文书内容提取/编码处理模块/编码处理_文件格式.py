# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
# 收获:#编码 --自动编码 --文件查找内容---error='ignore'-----文件格式
import chardet
import docx
from win32com import client as wc
import os
import glob
import time
'''
def chardets():
    path = 'C:\\Users\\Administrator\\Desktop\\案例二.docx'
    with open(path, 'rb') as f:
        print(chardet.detect(f.read()))
        return chardet.detect(f.read())['encoding']
#chardets()
#with open('C:\\Users\\Administrator\\Desktop\\案例二.docx','rb', encoding=chardets(), errors='ignore')as f:
    #contents = f.read()
    #print(contents)
'''



class Docx():
    def __init__(self,path):
        self.path = path



    '格式转化'
    def change_docx(self):

        for path_ in glob.glob(os.path.join(self.path, "*")):
            # print(path_)
            if path_.split('.')[1] == 'doc':

                w = wc.Dispatch('Word.Application')  # 实例化
                # w = wc.DispatchEx('Word.Application')另一种方法，但是似乎不好用
                '''win32打开并保存而不能直接保存'''
                doc = w.Documents.Open(path_)

                '''验证是否已经存在了！！！！！！'''
                type = path_.split('.')[0] + ".docx"
                # print('------------------------------------------...........................')
                # print(style)
                if type not in glob.glob(os.path.join(self.path, "*")):

                    doc.SaveAs(path_.split('.')[0] + ".docx", 16)  # 必须有参数16，否则会出错.
                    print('变更成功-----------------------------------------------------------')
                    doc.Close()
                else:
                    continue
            else:
                print('文件格式为%s, 可以直接进行读取-------------------------------------------------' % path_)



    '''输出docx格式的现在'''
    def return_file_types(self):
        docx_pool = []
        other_filetype = []
        for path in glob.glob(os.path.join(self.path, "*")):
            print(path)
            if path.split('.')[1] == 'docx':
                docx_pool.append(path)

            else:
                other_filetype.append(path)
        demand = input('输入自己需要的文件类型，只有docx与非docx两种格式，其中docx为1，而非docx为2： ')
        if demand == 1:
            return docx_txt
        elif demand == 2:
            return other_filetype

    def docxfile_to_txt(self):
        """
        docx转为txt
        """
        test_docx_pool = []
        for path in glob.glob(os.path.join(self.path, "*")):
            if path.split('.')[1] == 'docx':
                file = docx.Document(path)
                for para in file.paragraphs:
                    with open(self.path + '.txt', 'a',encoding='utf-8')as f:
                        f.write(para.text)
                        test_docx_pool.append(self.path + '.txt')
                file.close()

        return test_docx_pool
path = 'C:\\Users\\Administrator\\Desktop\\测试'

print(Docx(path).docxfile_to_txt())












'''
存在问题，但是问题不明,问题在style处path少了_，导致style=E:\桌面文件\作业.docx
for path in check_doc():
    print(path)
'''
