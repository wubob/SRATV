#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@date: 2018年4月3日
@author: wuxb  2683904575@qq.com 
@file: D:/workspace/SRATV4/src/CaseNode.py

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
import unittest, time
import HTMLTestRunner
import Public

class Node_API(unittest.TestCase):
    '''节点API'''
    def setUp(self):
        self.base_url = 'http://192.168.1.241:88' 
        self.app = Public.NodeApi(self.base_url)   

    def test_list(self):                               #+++++++++++++++++++节点列表
        '''节点列表'''
        response = self.app.Node_list()
        self.assertEqual(response.status_code,200)
        
    def test_get(self):                                #+++++++++++++++++++节点查询
        '''节点查询'''
        response = self.app.Node_get()
        self.assertIn(response.status_code, [200,400])
    
    def test_add(self):                                #+++++++++++++++++++节点增加
        '''节点增加'''
        response = self.app.Node_add()
        self.assertIn(response.status_code,[400,500,200])
    
    def test_set(self):                                #+++++++++++++++++++节点设置
        '''节点设置'''
        response = self.app.Node_set()
        self.assertEqual(response.status_code,200)
        
    def test_batchset(self):                           #+++++++++++++++++++批量设置 
        '''批量设置'''
        response = self.app.Node_batchSet()
        self.assertIn(response.status_code,[409,200])
        
        
#     def test_watch(self):                               #+++++++++++++++++++监听事件 xxx
#         '''监听事件'''
#         response = self.app.Node_watch()  
#         self.assertEqual(response.status_code,200)
    
    def test_exec(self):                                #+++++++++++++++++++远程命令
        '''远程命令'''
        response = self.app.Node_exec()  
        self.assertEqual(response.status_code,200)
    
    def test_delete(self):                              #+++++++++++++++++++节点删除
        '''节点删除'''
        response = self.app.Node_delete()  
        self.assertIn(response.status_code, [204,500,423])
        
    
    def test_upgrade(self):                             #+++++++++++++++++++节点升级
        '''节点升级'''
        response = self.app.Node_upgrade()
        self.assertIn(response.status_code, [200,500,403])
     
    def test_alabel(self):                              #+++++++++++++++++++设置标签
        '''设置标签'''
        response = self.app.Node_alabel()
        self.assertIn(response.status_code, [200,400])
           
    def test_ulabel(self):                              #+++++++++++++++++++删除标签
        '''删除标签'''
        response = self.app.Node_ulabel()
        self.assertIn(response.status_code, [200,400])
           
    def test_lyum(self):                                #+++++++++++++++++++列出YUM
        '''列出YUM'''
        response = self.app.Node_lyum()
        self.assertIn(response.status_code, [200])
        
    def test_ayum(self):                                #+++++++++++++++++++增加YUM
        '''增加YUM'''
        response = self.app.Node_ayum()
        self.assertIn(response.status_code, [200])
    
    def test_dyum(self):                                #+++++++++++++++++++删除YUM
        '''删除YUM'''
        response = self.app.Node_dlabel()
        self.assertIn(response.status_code, [200])  
        return response
    
    def tearDown(self):
        pass
      
if __name__ == '__main__':
    nowtime = "Solar API testing "+time.strftime("%Y-%m-%d-%H_%M_%S")
    testunit=unittest.TestSuite()
    testunit.addTest(Node_API("test_add"))
    testunit.addTest(Node_API("test_list"))
    testunit.addTest(Node_API("test_get"))
    testunit.addTest(Node_API("test_set"))
    testunit.addTest(Node_API("test_batchset"))
#     testunit.addTest(Node_API("test_watch"))
    testunit.addTest(Node_API("test_exec"))
    testunit.addTest(Node_API("test_upgrade"))
    testunit.addTest(Node_API("test_alabel"))
    testunit.addTest(Node_API("test_ulabel"))
    testunit.addTest(Node_API("test_ayum"))
    testunit.addTest(Node_API("test_lyum"))
    testunit.addTest(Node_API("test_dyum"))
    testunit.addTest(Node_API("test_delete"))
    
    filename = 'D:\\test_object\\report\\'+nowtime+'.html'
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Solar API V0.3-beta1测试报告',description='用例执行情况：')
    runner.run(testunit) 
    fp.close()
    