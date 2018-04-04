#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseSSH.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class SSHkey_API(unittest.TestCase):
    '''SSH私钥  API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.SshkeyApi(self.base_url)

    def test_list(self):                                       #+++++++++++++++++++Sshkey列表
        '''Sshkey列表'''
        response = self.app.Sshkey_list()
        self.assertEqual(response.status_code,200)
    
    def test_get(self):                                        #+++++++++++++++++++Sshkey查看
        '''Sshkey查看'''
        response = self.app.Sshkey_get()
        self.assertEqual(response.status_code,200)
    
    def test_add(self):                                        #+++++++++++++++++++Sshkey增加
        '''Sshkey增加'''
        response = self.app.Sshkey_add()
        self.assertIn(response.status_code, [400,201])
    
    def test_update(self):                                     #+++++++++++++++++++Sshkey更新
        '''Sshkey更新'''
        response = self.app.Sshkey_update()
        self.assertIn(response.status_code, [200,204])
         
    def test_remove(self):                                      #+++++++++++++++++++Sshkey删除
        '''Sshkey删除'''
        response = self.app.Sshkey_remove()
        self.assertEqual(response.status_code,204)
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(SSHkey_API("test_add"))
    testunit.addTest(SSHkey_API("test_list"))
    testunit.addTest(SSHkey_API("test_update"))
    testunit.addTest(SSHkey_API("test_remove"))
    testunit.addTest(SSHkey_API("test_get"))
      
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    