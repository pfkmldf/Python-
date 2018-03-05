# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 00:01:18 2018

@author: yuan
"""

import requests
#处理xml文件信息
import xml.etree.ElementTree as ET

from xml.parser.expat import ParserCreate

class DefaultSaxHandler(object):
    def __init__(self,provinces):
        self.provinces = provinces
    
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))
    
    def end_element() 