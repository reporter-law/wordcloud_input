# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from jieba import posseg as psg
import jieba
from 项目.项目二_文书内容提取.提取模板模块.文档类型分流 import file_shunt as f
from 项目.项目二_文书内容提取.提取模板模块.停用词的去除 import stopword_manager as sm, stopword_database as sd
#print(help(psg))#作用就是可以有词性，进行词性选择

def jieba_cutword(path):
    word = f(path)
    #print(word)
    try:
        #print('这是停用词处理后的前十位词语的内容： ' + word[:10])  此内容已经过时，被修正后存在错误

        lst_words = []
        '''此处很关键，整体调整使用自定义词典导入'''
        jieba.load_userdict('J:\PyCharm项目\项目\项目二_文书内容提取\提取模板模块\刑事诉讼法词典.txt')

        # 部分调整，使用自定义词语的导入
        '''
        jieba.add_word("公诉机关")
        '''

        '''导出名词、人名之类的词语'''
        for x in psg.lcut(word.strip()):
            # 保留名词、人名、地名，长度至少两个字
            # psg导出的应该是字典
            if x.flag in ['n', 'nr', 'ns'] and len(x.word) > 1:
                lst_words.append(x.word)
        print('切词后停用词处理前状态： 顺利通过！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        if len(str(path)) <= 50:
            '''文档类型的停用词处理后待分词内容返回'''
            correct_words =  sm(lst_words)
            print('这是第三层处理，将txt文章进行分词，统计词语出现的频率-------------------------------------')
            return word_frequency(correct_words)
        else:
            '''数据库类型字符串停用词处理后内容返回'''
            correct_wprds = sd(lst_words)
            print('这是第三层处理，将txt文章进行分词，统计词语出现的频率-------------------------------------')
            return word_frequency(correct_wprds)

    except:
        print('           分词出错，请返回提取模块模块。jiebacut_word.py进行查看          ')






def word_frequency(lst_words):
    '''词频统计'''
    try:
        word_frequency = {}
        for word_ in lst_words:
            if word_ in word_frequency:
                word_frequency[word_] += 1
            else:
                word_frequency[word_] = 1
        '''排序'''
        word_sort = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        # print(word_sort)
        # return word_frequency
        return word_sort
    except:
        print('停用词处为None')
#path = 'I:\迅雷下载\捕诉\捕诉模式的博弈分析_曹旺.pdf'
#print(jieba_cutword(path))


