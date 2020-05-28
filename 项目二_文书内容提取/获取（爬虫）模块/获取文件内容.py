# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
import time
import random
from selenium.webdriver.chrome.options import Options
from threading import Thread as t


sec = random.randint(1,2)
'''randint生成整数'''
class Cnki():

    def __init__(self):
        pass

    def login(self):
        sec = random.randint(1, 5)
        ops = Options()
        # driver = webdriver.Chrome(r'd:\xxx\chromedriver.exe')
        # 原因：可能是chrome未在系统盘注册
        ops.binary_location = r'D:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
        '''opt = webdriver.ChromeOptions(),已经导入options不用'''
        #ops.add_argument('--headless')
        browser = webdriver.Chrome(options=ops)
        browser.implicitly_wait(1)
        browser.get('https://portal2020.xtu.edu.cn/cas/login?service=https%3A%2F%2Fzwidp.xtu.edu.cn%2Fidp%2FAuthn%2FExternal%3Fconversation%3De1s1&entityId=https%3A%2F%2Ffsso.cnki.net%2Fshibboleth')
        input_1 = browser.find_element_by_xpath('//*[@id="username"]')
        input_1.send_keys('201821030920')
        input_2 = browser.find_element_by_xpath('//*[@id="ppassword"]')
        input_2.send_keys('cao43100')
        time.sleep(2)

        time.sleep(50)
        browser.close()
#报错：Sorry, it looks like there is a problem finding your session. This can happen if you waited too long on the login page, or if you were redirected to a different server that issued the original request. This error usually goes away if you try accessing your desired application again.

    def cnki(self):
        sec = random.randint(1, 5)
        ops = Options()
        # driver = webdriver.Chrome(r'd:\xxx\chromedriver.exe')
        # 原因：可能是chrome未在系统盘注册
        ops.binary_location = r'D:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
        '''opt = webdriver.ChromeOptions(),已经导入options不用'''
        ops.add_argument('--headless')
        browser = webdriver.Chrome(options=ops)
        browser.implicitly_wait(1)
        browser.get('https://blog.csdn.net/python__reported')
        button1 = browser.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a["href"]')
        button1.click()
        browser.switch_to.window(browser.window_handles[1])
        browser.close()

Cnki().login()