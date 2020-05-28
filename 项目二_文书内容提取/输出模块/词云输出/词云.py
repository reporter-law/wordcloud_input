# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
import wordcloud
#import matplotlib.pyplot as plt
from 项目.项目二_文书内容提取.提取模板模块 import jiebacut_word as jb
from wordcloud import  STOPWORDS#, ImageColorGenerator
import os
import glob


def pdf_ciyun(path):
    """
    pdf转化的词云
    :param path:
    :return:
    """
    aims = jb.jieba_cutword(path)
    sentence = dict(aims)
    print('这是第四层处理，将词频进行可视化为词云-----------------------------------------')

    '''词云实例化'''
    #backgroud_Image = np.array(Image.open(path.join('J:\PyCharm项目\项目\项目二_文书内容提取\提取模板模块\parrot_new.png')))
    #backgroud_Image = plt.imread('J:\PyCharm项目\项目\项目二_文书内容提取\输出模块\词云输出\gray_picture.png')

    '''I盘读不了'''
    '''
    必须是白色的背景色
    '''
    wc = wordcloud.WordCloud(
        background_color='black',
        font_path='msyh.ttc',
        #mask=backgroud_Image,
        random_state=100,
        width= 800,
        height = 1000,
        stopwords=STOPWORDS,
        #中文必须设置，否则方框
    )

    '''文本传入'''

    wc.generate_from_frequencies(sentence)
    # 不能有空格？

    '''图片保存'''
    wc.to_file(''.join(sentence)[:20]+'.png')
    print('词云制作成功--------------------------------------------------')
    return ''.join(sentence)[:20]+'.png'
#path = 'I:\迅雷下载\捕诉\捕诉模式的博弈分析_曹旺.pdf'
#print(len(path))
#print(path[-15:-5])
#txt_ciyun(path)



def database_ciyun(path):
    """
    数据库的词云绘制，与上面一样
    :param path:
    :return:
    """
    try:
        aims = jb.jieba_cutword(path)
        sentence = dict(aims)
        print('这是第四层处理，将词频进行可视化为词云-----------------------------------------')

        '''词云实例化'''
        # backgroud_Image = np.array(Image.open(path.join('J:\PyCharm项目\项目\项目二_文书内容提取\提取模板模块\parrot_new.png')))
        # backgroud_Image = plt.imread('J:\PyCharm项目\项目\项目二_文书内容提取\输出模块\词云输出\gray_picture.png')

        '''I盘读不了'''
        '''
        必须是白色的背景色
        '''
        wc = wordcloud.WordCloud(
            background_color='white',
            font_path='msyh.ttc',
            # mask=backgroud_Image,
            random_state=100,
            width=800,
            height=1000,
            stopwords=STOPWORDS,
            # 中文必须设置，否则方框
        )

        '''文本传入'''

        wc.generate_from_frequencies(sentence)
        # 不能有空格？

        '''图片查重'''
        path_ciyun = "J:\PyCharm项目\项目\项目二_文书内容提取\输入模块（启动端）\数据库api接口\mongodb词云\{name}".format(
            name=''.join(sentence)[:20] + '.png')
        if path_ciyun in glob.glob(os.path.join('J:\PyCharm项目\项目\项目二_文书内容提取\输入模块（启动端）\数据库api接口\mongodb词云', "*")):
            print('词云图片出现重复，正在跳过----------------------------------------------------')

        else:
            '''图片保存'''
            wc.to_file("J:\PyCharm项目\项目\项目二_文书内容提取\输入模块（启动端）\数据库api接口\mongodb词云\{name}".format(
                name=''.join(sentence)[:20] + '.png'))

            print('词云制作成功--------------------------------------------------')
            return ''.join(sentence)[0:20] + '.png'
    except:
        pass