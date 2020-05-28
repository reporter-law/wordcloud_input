# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:










def stopword_manager(lst_words):
    """文档类型停用词处理"""
    index = 0
    path__ = 'J:\PyCharm项目\项目\项目二_文书内容提取\提取模板模块\stop_words_zh.txt'
    with open(path__, 'r', encoding='utf-8', )as f:
        stop_word = [stop_word.strip() for stop_word in f.readlines()]

        for i in lst_words:
            if i in stop_word:
                lst_words.remove(i)
                index += 1
    print('存在 %d 个停用词        ' % index)
    print('第二层停用词处理-------------------------------------------------------------------------')
    # with open('经过停用词处理的txt.txt','a+',encoding='utf-8',errors='ignore')as f:
    # f.write(str(word).replace('[','').replace(']','')

    return lst_words

    # pprint.pprint(word)


# path = 'I:\迅雷下载\捕诉\捕诉模式的博弈分析_曹旺.pdf'
# print(cancel_stopword(path))

def stopword_database(lst_words):
    """数据库分词的停用词处理"""
    index = 0
    path__ = 'J:\PyCharm项目\项目\项目二_文书内容提取\提取模板模块\stop_words_zh.txt'
    with open(path__, 'r', encoding='utf-8', )as f:
        stop_word = [stop_word.strip() for stop_word in f.readlines()]
        #print(stop_word)

        '''第一个需要解决的问题就是database传入的字符串的处理'''
        for i in range(3):
            for value in lst_words:
            #print(lst_words)
                if value in stop_word:
                    lst_words.remove(value)
                #本院没有完全去掉，是否是remove导致的
                    index += 1
                else:
                    pass
                    #print('第一次已经清理干净')


    print('存在 %d 个停用词        ' % index)
    print('第二层停用词处理-------------------------------------------------------------------------')
    # with open('经过停用词处理的txt.txt','a+',encoding='utf-8',errors='ignore')as f:
    # f.write(str(word).replace('[','').replace(']','')
    #print(lst_words)
    return lst_words