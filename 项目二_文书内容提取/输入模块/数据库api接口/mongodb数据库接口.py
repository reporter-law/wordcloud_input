# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import pymongo
import pprint
from 项目.项目二_文书内容提取.输出模块.词云输出.词云 import database_ciyun as dbcy
from 项目.项目二_文书内容提取.提取模板模块.jiebacut_word import jieba_cutword as jb
import openpyxl

def database_connect(port):
    '''数据库连接与db选定'''
    print('1、数据库进入中-----------------------------------------------------------')
    client = pymongo.MongoClient(host = 'localhost',port=port)
    db = client.wenshuku
    Collection = db.caipanwenshu


    #print('2、以下：数据库全部内容---------------------------------------------------')
    results = Collection.find()
    index = 0
    '''
    for values in results[:10]:

        #pprint.pprint(values)
        index += 1
        print(index)

    '''


    '''数据库统计内容,数据库说明'''
    #print('2、以下：数据库统计内容---------------------------------------------------')
    #Collection.count_documents = Collection.count_documents
    #print(Collection.ount_documents)
    #print()


    '''1：数据导入词云:2：数据导出使用切词方法'''

    #print(results[0])
    print('以下为mongodb字典列表化的内容-------------------------------------------------------------')
    list_ = []
    deplicate = {}
    for results in results:
        for item in results.items():
            #print(item)
            list_.append(list(item))

    print('-----------------------------------------------------------------------')
    #print(list_[1][1])

    print('---------------------------------隔离线--------------------------------------')
    #print(len(list_[1][1].split(',')))
    jud_list = []
    for index in range(len(list_)):
        if index == 0:
            pass
        elif index % 2 != 0:#双数进入



            '''数据处理处：添加数据类型接口'''
            '''此处为方法调用,调用'''
            title = list_[index][1].split('[')[0].strip()



            #reason = list_[index][1].split('[')[3].strip()
            #crime = list_[index][1].split('[')[5].strip()
            #counrt = list_[index][1].split('[')[7].strip()
            #area = list_[index][1].split('[')[9].strip()
            #jud_counrt = list_[index][1].split('[')[11].strip()
            #jud_counrt_ = list_[index][1].split('[')[13].strip()
            #print(reason)
            #proxy = list_[index][1].split('[')[0].strip()
            yield {title:jb(list_[index][1])}


    '''客户端关闭'''
    #client.close()

    client.close()


#词云
'''
index = 0
for i in database_connect():
    print('词云:{name}'.format(name = i))
    print()
    index += 1
    print('这是第%d个词云' % index)
print('一共%d个词云----------------------------------------------------' % index)
'''

'''
index = 0
data_list = []
for i in database_connect(27017):
            #print('数据名称:{name}'.format(name=i))
    print()
    index += 1
    print('        这是第%d个整理后的数据！！！！！！！！！！！！！！！！！！！！！！！！' % index)
    print(i)
'''











'''
#训练数据
list_ = [[1,2],[2,1]]
print(list_[0][0])


dic = {'a':2,'b':3}
lis = []
for item in dic.items():
    print(type(item))
    lis.append(list(item))
print(lis[1])
for key ,value in dic.items():
    #print(key,value)
    print(type(key),type(value))
'''
