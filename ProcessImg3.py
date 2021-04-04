#coding=utf-8
#__author__ = 'cclin'
#write by cclin 2021.4.5

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
from scipy import misc
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np;
import ipath as ip;
import argparse;
import base64;
import chardet;
import pip._vendor.chardet.jisfreq;

#BOM=ByteOrder Mark
def get_encoding(file):
    with open(file,'rb') as f:
        return chardet.detect(f.read())['encoding']

def  scaleFlags():
    fi=ip.getCur()+"coin_sections.json";
    enc=get_encoding(fi)
    print(enc)
    f=codecs.open(fi,"r","utf-8");
    lines=[];
    for line in f:
        a=line.encode("gb2312").lstrip().rstrip()
        if len(a)>3:
            lines.append(line);
    #scale 306
    for line in lines:
        a=line.lstrip().rstrip()         
        arr=a.split(",");        
        pp=ip.getCur()+"flag_sections/"+arr[0][2:-1]        
        scalePicture(pp,True);
    f.close();

def scaleGBTS():
    #scale gbt
    plist=[];
    ip.walk_files(ip.getCur()+"gbt-2659/gbt2659", plist);
    for line in plist:
        scalePicture(line,True);

#https://www.jb51.net/article/102981.htm
#https://www.cnblogs.com/skyfsm/p/8276501.html
#https://blog.csdn.net/zhangziju/article/details/79123275
def scalePicture(ppath,isbak):            
    im = Image.open(ppath)
    if isbak:
        sp=os.path.split(ppath);        
        np=sp[0]+"/bk/"
        ip.forceDir(np);
        im.save(np+sp[1]);
        print(np+sp[1]);
    #print(lena.shape[0],lena.shape[1],lena.shape[2]);
    #fig = plt.gcf()
    #print(plt.figure(1));
    #print(fig.get_size_inches()*fig.dpi());
    tosize=[166,99];
    scale=1.0;
    scale1=float(tosize[0])/float(im.size[0]);
    scale2=float(tosize[1])/float(im.size[1]);
    if scale1>scale2:
        scale=scale1;
    else:
        scale=scale2;   
    scale=scale*0.95; 
    imr=im.resize((int(im.size[0]*scale),int(im.size[1]*scale)));
    imr.save(ppath);

#https://www.jb51.net/article/181383.htm
#https://blog.csdn.net/zhangziju/article/details/79123275
'''
1:1位像素，黑和白，存成8位的像素
L:灰度，L=R*299/1000+G*587/1000+B*114/1000
P:8位彩色
RGBA:32位彩色
CMYK:32位彩色 RGB to cmyk:C=255-R/M=255-G/Y=255-B/k=0
YcbCr:24位彩色 RGB to YCbCr：Y= 0.257*R+0.504*G+0.098*B+16/Cb = -0.148*R-0.291*G+0.439*B+128/Cr = 0.439*R-0.368*G-0.071*B+128
I:32位整形灰色 RGB TO I:I = R * 299/1000 + G * 587/1000 + B * 114/1000
F:32位浮点 RGB TO F:F = R * 299/1000+ G * 587/1000 + B * 114/1000
'''
def converMode(ppath,isbak):
    f=open(ppath,"rb");    
    im = Image.open(ppath)
    if isbak:
        sp=os.path.split(ppath);
        np=sp[0]+"/bk/"
        ip.forceDir(np);
        #print(im.size[0]*1.5,im.size[1]*1.5);
        #imr=im.resize((int(im.size[0]*1.5),int(im.size[1]*1.5)));
        im.save(np+sp[1]);
        print(np+sp[1]);    
    print(im.mode);
    print(im.size);
    #print(base64.b64encode(f.read()).decode('utf-8'));
    f.close();

if __name__ == '__main__':
    #reload(sys) 
    #sys.setdefaultencoding( "utf-8" )  
    ss=u"请关注全国留守儿童，请关注全国城乡差距，请关注全国教育现状......"
    print(ss)
    cmd = "TITLE "+ss
    os.system(str(cmd.encode('gb2312')))    
    print("author cclin 2021.04.05")
    print("support:e-mail=12092020@qq.com")
    print("copyright 2015~2018 for anyone to use")
    print("")
    print(__file__,__name__)
    print("")
    #half autohand process

    #converMode(r"D:\World\TheFlags-CurrencySymbols\_currency\Albania_s_lek.png",True);
    print(get_encoding(ip.getCur()+"coin_sections.json"));
    scaleFlags();
    #scaleGBTS();
    #print os.path.splitext(r"D:\World\TheFlags-CurrencySymbols\_currency\Albania_s_lek.png");