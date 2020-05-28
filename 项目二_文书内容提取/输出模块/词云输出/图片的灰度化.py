# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from PIL import Image

def gray_picture():
    image_path ='J:\PyCharm项目\项目\项目二_文书内容提取\输出模块\parrot_new.png'
    image = Image.open(image_path)
#print(image)
    im_gray = image.convert('L')
    im_gray.save('gray_picture.png')#图片保存
    return im_gray
gray_picture()

