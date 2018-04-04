#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseApp.py

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from tkinter import messagebox
import unittest, time
import HTMLTestRunner
import Public

class App_API(unittest.TestCase):
    '''应用 API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88'
        self.app = Public.APPApi(self.base_url)
      
    def test_list(self):                                     #+++++++++++++++++++APP列表
        '''APP列表'''
        response = self.app.APP_list()
        self.assertEqual(response.status_code,200)
    
    def test_get(self):                                      #+++++++++++++++++++APP查看
        '''APP查看'''
        response = self.app.APP_get()
        self.assertEqual(response.status_code,200)
        
    
    def test_add(self):                                       #+++++++++++++++++++APP增加
        '''APP增加'''
        response = self.app.APP_add()
        self.assertIn(response.status_code,[400,201])
    
        
    def test_update(self):                                   #+++++++++++++++++++APP更新
        '''APP更新'''
        response = self.app.APP_update()
        self.assertIn(response.status_code,[200,204])
            
    
    def test_delete(self):                                   #+++++++++++++++++++APP删除
        '''APP删除'''
        response = self.app.APP_delete()
        self.assertEqual(response.status_code,204)
        
    def test_importrevisions(self):                          #+++++++++++++++++++APP版本导入
        '''APP版本导入'''
        response = self.app.APP_importrevisions()
        self.assertEqual(response.status_code,201)
        
    def test_revisions(self):                                #+++++++++++++++++++APP版本列表
        '''APP版本列表'''
        response = self.app.APP_revisionslist()
        self.assertEqual(response.status_code,200)
    
    def test_getrevisions(self):                             #+++++++++++++++++++APP版本查看
        '''APP版本查看'''
        response = self.app.APP_getrevisions()
        self.assertEqual(response.status_code,200)
    
    
    def test_exportrevisions(self):                          #+++++++++++++++++++APP版本导出
        '''APP版本导出'''
        response = self.app.APP_exportrevisions()
        self.assertEqual(response.status_code,200)

    def test_deploy(self):                                   #+++++++++++++++++++APP版本部署
        '''APP版本部署'''
        response = self.app.APP_deploy()
        self.assertIn(response.status_code,[201,400])
        
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(App_API("test_add"))
    testunit.addTest(App_API("test_list"))
    testunit.addTest(App_API("test_update"))
    testunit.addTest(App_API("test_get"))
    testunit.addTest(App_API("test_importrevisions"))
    testunit.addTest(App_API("test_revisions"))
    testunit.addTest(App_API("test_getrevisions"))
    testunit.addTest(App_API("test_exportrevisions"))
    testunit.addTest(App_API("test_deploy"))
    testunit.addTest(App_API("test_delete"))
    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    