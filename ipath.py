#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2021.4.4

#from openpyxl import Workbook
#from openpyxl import load_workbook
#import xlrd

import sys
import os,os.path
import re
import xml.dom.minidom as minidom
from xml.etree import ElementTree as ET
import codecs
#import commands
from subprocess import Popen,PIPE
import subprocess
import time
   
def walk_dirs(dir,list,topdown=True):       
    for root, dirs, files in os.walk(dir, topdown):        
        for name in dirs:            
            path=os.path.join(root,name)+r"/"
            path=path.replace("\\","/")
            #pa=path.lower()
            list.append(path)
            #print path

def walk_files(dir,list,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            ext=os.path.splitext(name)[1]
            file=os.path.join(root,name)     
            file=file.replace("\\","/")
            #print file
            if file.find(".svn")==-1 and file not in list:                
                list.append(file)
                #print file;
    
def getCur():
    return os.path.split(os.path.realpath(__file__))[0]+r"/"

def forceDir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir);

