#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2015.5.10

#from openpyxl import Workbook
#from openpyxl import load_workbook
#import xlrd

import sys
import os,os.path
import re
import xml.dom.minidom as minidom         
from xml.etree import ElementTree as ET   
import codecs
import commands
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

def getRemember(rfiles,fname):
    for line in rfiles:
        n=line.split("/");
        if(n[len(n)-1]==fname and n[len(n)-2]<>"flag_world-remembe"):            
            return n[len(n)-2];
    return "";

def processFlags():
    #half autohand process
    afiles=[];
    anames=[];
    walk_files(getCur()+"flag_sections",afiles);    
    for line in afiles:
        n=line.split(r"/");
        anames.append(n[len(n)-1]);

    frem=open(getCur()+"forhumanremember.txt","r")

    f=open(getCur()+"coin_sections.json","r")
    idx=0;
    icount=0;
    for line in f:        
        if line.strip()!="" and line.strip()!="[" and line.strip()!="]":
            arr=line.encode("gb2312").split(",");
            if len(arr)-1<7:
                arr[len(arr)-2]=arr[len(arr)-2][:-1];                
                '''
                while len(arr)-1<7:                
                    arr.append('"",');
                arr[len(arr)-2]=arr[len(arr)-2]+'""]'
                '''
            name=arr[1][1:-1];
            remember=getRemember(frem,name);
            if remember=="flag_world-remember":
                remember="";
            nline="["+str(idx)+","+'"'+remember+'",';
            idx1=0;
            for a in arr:                
                if idx1>0 and idx1<len(arr) and len(a)>1:
                    nline=nline+a+",";
                idx1=idx1+1;
            idx=idx+1;
            if len(arr)==5:
                nline=nline+'"","",""],';
            narr=nline.split(',');
            if len(narr)>10:
                print len(nline.split(',')),nline;
                icount=icount+1;
            #else:
                #print nline;
    print 'hit',icount;
    f.close()

def processSymbols():
    #half autohand process
    afiles=[];
    anames=[];
    walk_files(getCur()+"_currency",afiles);    
    for line in afiles:
        n=line.encode("gb2312").split(r"/");
        anames.append(n[len(n)-1]);
                
    f=open(getCur()+"coin_sections.json","r")
    symbols=[]
    for line in f:
        arr=line.encode("gb2312").split(",")
        if len(arr)<3:
            continue;      
        if arr[5] not in symbols:  
            symbols.append(arr[5][1:-1]);
    f.close();

    for n in anames:
        if n not in symbols:
            print n;


if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding( "utf-8" )  
    ss=u"请关注全国留守儿童，请关注全国城乡差距，请关注全国教育现状......"
    print ss
    cmd = "TITLE "+ss
    os.system(cmd.encode('gb2312'))    
    print "author cclin 2015.04"
    print "support:e-mail=12092020@qq.com"
    print "copyright 2015~2018 for anyone to use"
    print ""
    print __file__,__name__
    print ""

    #processSymbols();
    processFlags();
    
    print getCur();
    #a=u'[0,"","lt","Abkhazia.png","阿伯卡茨共和国","Abkhazia","","",""],'.split(",");
    a=u'[18,"","three-h-pure","Austria.png","奥地利","Austria","Austria_s_Euro.png","欧洲","coin_ouyuan","coin_aodilixianling"],'.split(",");
    print(len(a));
    for line in a:        
        print line;

    #half autohand process