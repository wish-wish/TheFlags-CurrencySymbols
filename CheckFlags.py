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
import ipath as ip;   

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
    walk_files(ip.getCur()+"flag_sections",afiles);    
    for line in afiles:
        n=line.split(r"/");
        anames.append(n[len(n)-1]);

    frem=open(ip.getCur()+"forhumanremember.txt","r")

    f=open(ip.getCur()+"data/coin_sections.json","r")
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
    walk_files(ip.getCur()+"_currency",afiles);    
    for line in afiles:
        n=line.encode("gb2312").split(r"/");
        anames.append(n[len(n)-1]);
                
    f=open(ip.getCur()+"data/coin_sections.json","r")
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

def isMatchName(n1,n2list):    
    for n2 in n2list:
        n11=n1.lower()[:-4];
        n22=n2.lower()[:-4];
        if n11.find(n22)>=0 or n22.find(n11)>=0:
            return True,n2;
    return False,"";

def isMatchName2(n1,n2list):    
    for n2 in n2list:        
        if n1.replace("_","-").lower()==n2.lower():
            return True;
    return False;

def processCircle2():
    afiles=[];
    anames=[];
    walk_files(ip.getCur()+"flag_circle",afiles);
    for line in afiles:
        n=line.encode("gb2312").split(r"/");
        anames.append(n[len(n)-1]);
    idx=0;
    hitcount=0;
    f=open(ip.getCur()+"data/coin_sections.json","r")
    for line in f:
        arr=line.encode("gb2312").split(",")
        if len(arr)<3:
            continue;
        na=arr[2][1:-1];        
        if arr[3]=="" and isMatchName2(na,anames):
            arr[3]="2";
            hitcount=hitcount+1;
        #else: 
        #    break;
        nline="";
        arr[0]="["+str(idx);
        for a in arr:
            if a.lstrip()!="":
                nline=nline+a+",";
        print nline;
        idx=idx+1;
    print hitcount;
    

def processCircle():
    afiles=[];
    anames=[];
    walk_files(ip.getCur()+"flag_circle",afiles);
    for line in afiles:
        n=line.encode("gb2312").split(r"/");
        anames.append(n[len(n)-1]);
        #print(n[len(n)-1])

    f=open(ip.getCur()+"data/coin_sections.json","r")
    hitcout=0;
    symbols=[];
    nohits=[];
    hitmatchs=[];
    for line in f:
        arr=line.encode("gb2312").split(",")
        if len(arr)<3:
            continue;
        #arr.insert(2,"aa");
        #symbols.append(arr[2]);
        na=arr[2][1:-1].lower();  
        symbols.append(na);
        isMatch,gotn=isMatchName(na,anames);
        if na.lower() in anames:
            #arr.insert(3,'"1"');
            arr[3]='"1"'
            hitcout=hitcout+1;        
        elif isMatch:
            #arr.insert(3,'"'+gotn+'"');
            arr[3]='"'+gotn+'"'
            hitcout=hitcout+1;
            hitmatchs.append(gotn);        
        else:
            #arr.insert(3,'""');
            arr[3]='""'
            nohits.append(na);

        nline="";
        for a in arr:
            if a.lstrip()!="":        
                nline=nline+a+",";
        #print nline;

    '''
    print hitcout;
    for line in nohits:
        print line;
    print len(hitmatchs);
    for line in hitmatchs:
        print line;
    '''

    for line in anames:
        if line not in symbols:
            print line;

def processCircle3():
    afiles=[];
    anames=[];
    walk_files(ip.getCur()+"flag_circle",afiles);
    for line in afiles:
        n=line.encode("gb2312").split(r"/");
        anames.append(n[len(n)-1]);        

    f=open(ip.getCur()+"data/coin_sections.json","r")
    symbols=[];
    print "";
    print "not in 261";
    cou=0;
    for line in f:
        arr=line.encode("gb2312").split(",")
        if len(arr)<4:
            continue;        
        na="";
        if  len(arr[3])==3:
            na=arr[2][1:-1].lower();
        elif len(arr[3])>3:
            na=arr[3][1:-1].lower();
        else:
            print arr[2][1:-1].lower();
            cmd="copy "+ip.getCur()+"flag_sections/"+arr[2][1:-1]+" "+ip.getCur()+"tocheck/"+arr[2][1:-1];
            print cmd;
            #os.system(cmd.replace("/","\\"));            
        if len(na)>1 and na not in symbols:
            symbols.append(na);
        else:
            cou=cou+1;
    print cou;

    print "";
    print "not in 297";
    cou=0;
    for line in anames:
        if line not in symbols:
            print line;
            cmd="copy "+ip.getCur()+"flag_circle/"+line+" "+ip.getCur()+"tocheck/"+line;
            print cmd;
            #os.system(cmd.replace("/","\\"));
            cou=cou+1;
    print cou;
    f.close();

def processReOrder():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    idx=0;
    for line in f:
        arr=line.encode("gb2312").split(",")
        if len(arr)<3:
            continue;
        nline="["+str(idx)+",";
        idx1=0;
        for a in arr:
            if idx1==0:
                idx1=idx1+1;
                continue;
            if len(a)>1:
                nline=nline+a+",";
            idx1=idx1+1;

        print nline;
        idx=idx+1;
    f.close();

def processSort():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    names=[];
    idx=0;
    newlist=[];
    for line in f:
        arr=line.encode("gb2312").split(",")
        if len(arr)<3:
            continue;
        names.append(arr[2][1:-1]);
        nline="["+arr[2]+","+str(idx)+","
        idx1=0;
        for a in arr:
            if(idx1==0 or idx1==2 or len(a)<2):
                idx1=idx1+1;
                continue;        
            nline=nline+a+",";
            idx1=idx1+1;
        #print nline;
        newlist.append(nline);
        idx=idx+1;
    newlist.sort();
    idx=0;
    for line in newlist:
        arr=line.split(",")
        arr[1]=str(idx);
        idx=idx+1;
        nline="";
        if len(arr)<3:
            continue;
        for a in arr:
            if(idx1==0 or len(a)<2):
                continue;
            nline=nline+a+",";
        print nline;
    f.close();

def getSame(na,blist):    
    for line in blist:
        brr=line.encode("gb2312").rstrip().split(",");        
        if na[1:-1]==brr[1]:
            return brr[4];
    #print arr[0][5:];
    return "";

def processGBT():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    ft=open(ip.getCur()+"data/GBT-2659-2000.csv","r")
    gbt=[];
    for line in ft:
        gbt.append(line);        
    for line in f:
        arr=line.encode("gb2312").rstrip().split(",")
        if len(arr)<3:
            continue;
        #arr.insert(0,getSame());        
        nline='["'+getSame(arr[4],gbt)+'",';
        idx1=0;
        for a in arr:
            if(len(a)<2):
                continue;            
            if idx1==0:
                nline=nline+a[5:]+",";
            else:
                nline=nline+a+",";
            idx1=idx1+1;
        print nline;
    ft.close();
    f.close();

def processNGBT():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    ft=open(ip.getCur()+"data/GBT-2659-2000.csv","r")
    hits=[];
    for line in f:
        arr=line.encode("gb2312").rstrip().split(",")
        if len(arr)<3:
            continue;
        if arr[0][2:-1]<>"":
            hits.append(arr[0][2:-1]);
    for line in ft:
        arr=line.encode("gb2312").rstrip().split(",")
        if arr[4] not in hits:
            print arr[1];
    ft.close();
    f.close();   


def processSort1():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    names=[];
    idx=0;
    newlist=[];
    for line in f:
        arr=line.encode("gb2312").lstrip().rstrip().split(",")
        if len(arr)<4:
            continue;
        names.append(arr[2][1:-1]);
        nline="["+arr[1]+","
        idx1=0;
        for a in arr:
            if(idx1==1 or a==""):
                idx1=idx1+1;
                continue;     
            if idx1==0:   
                nline=nline+a[1:]+",";
            else:
                nline=nline+a+",";            
            idx1=idx1+1;            
        #print nline
        newlist.append(nline);
        idx=idx+1;
    newlist.sort();
    idx=0;
    for line in newlist:
        arr=line.split(",")
        arr[2]=str(idx);
        del arr[2];
        idx=idx+1;
        nline="";
        if len(arr)<3:
            continue;
        for a in arr:
            if(idx1==0 or len(a)<1):
                continue;
            nline=nline+a+",";
        print nline;
    f.close();


def processSort2():
    f=open(ip.getCur()+"data/coin_sections.json","r")    
    idx=0;
    newlist=[];
    for line in f:
        a=line.encode("gb2312").lstrip().rstrip()   
        if len(a)>3:     
            newlist.append(a);
        #print a;
        idx=idx+1;
    newlist.sort();
    idx=0;
    gbt=[];
    for line in newlist:
        arr=line.lstrip().rstrip().split(","); 
        #del arr[2];      
        idx=idx+1;
        nline="";
        if len(arr)<3:
            continue;
        for a in arr:    
            if len(a)>0:        
                nline=nline+a+",";
        if arr[1]<>'""' and arr[1] not in gbt:
            gbt.append(arr[1]);
        print nline;
    print len(gbt),gbt;
    f.close();

def  generateGBT2659():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    #os.chdir((getCur()+"GBT-265").replace("/","\\"));
    ft=open(ip.getCur()+"data/GBT-2659-2000.csv","r")
    print os.getcwd();
    os.chdir("GBT");
    gbt=[];
    for line in f:
        a=line.encode("gb2312").lstrip().rstrip() 
        arr=a.split(",");
        if len(a)>3 and arr[2]<>'""':
            cmd="copy "+ip.getCur()+"flag_sections/"+arr[0][2:-1]+" "+arr[2][1:-1]+".png";
            cmd=cmd.replace("/","\\");
            #print cmd;
            gbt.append(arr[2][1:-1]);
            os.system(cmd);
    '''
    for line in ft:
        a=line.lstrip().rstrip().decode('utf-8').encode('gb2312').split(",")        
        if a[4] not in gbt:
            print a[4],'---------------------------------------------';            
    '''
    ft.close();
    f.close();

def processISO():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    ft=open(ip.getCur()+"data/GBT-2659-2000.csv","r")
    fo=open(ip.getCur()+"data/iso3166_cn.txt","r");
    gbt=[];
    iso=[];
    print "name splits:"
    for line in ft:
        gbt.append(line);
        a=line.lstrip().rstrip().decode('utf-8').encode('gb2312').split(",")        
        if a[2][0]=='"' and a[2][len(a[2])-1]<>'"':
            print line.lstrip().rstrip().decode('utf-8').encode('gb2312');

    for line in fo:
        iso.append(line);
    
    print "iso not in gbt:"
    for line in iso:
        a=line.lstrip().rstrip().decode('utf-8').encode('gb2312').split(",")
        hit=False;
        for bline in gbt:
            b=bline.split(",");
            if a[0].lower()==b[3].lower():
                hit=True;
        if not hit:
            print line.decode('utf-8').encode('gb2312').lstrip().rstrip();

    print "gbt not in iso:"
    for line in gbt:
        a=line.lstrip().rstrip().decode('utf-8').encode('gb2312').split(",")
        hit=False;
        for bline in iso:
            b=bline.split(",");
            if a[3].lower()==b[0].lower():
                hit=True;
        if not hit:
            print line.decode('utf-8').encode('gb2312').lstrip().rstrip();
          
    f.close();
    ft.close();
    fo.close();

def processISO_A2():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    ft=open(ip.getCur()+"data/GBT-2659-2000.csv","r")
    fo=open(ip.getCur()+"data/iso3166_cn.txt","r");
    gbt=[];
    iso=[];    
    for line in ft:
        if len(line.lstrip().rstrip())>2:
            gbt.append(line.lstrip().rstrip().decode('utf-8').encode('gb2312'));                

    for line in fo:
        if len(line.lstrip().rstrip())>2:
            iso.append(line.lstrip().rstrip().decode('utf-8').encode('gb2312'));
        
    for line in f:
        if len(line.lstrip().rstrip())<3:
            continue;
        a=line.lstrip().rstrip().decode('utf-8').encode('gb2312').split(",")
        hit="";
        for aline in gbt:
            b=aline.split(",");        
            if len(a[1])>2 and a[1][1:-1]==b[4]:
                hit=b[3];
        a[1]=a[1].upper();
        a.insert(1,'"'+hit.upper()+'"');
        cline=a[0]+",";
        d=0;
        for c in a:
            if d>0 and len(c)>0:
                cline=cline+c+","
            d=d+1;
        print cline;          
    f.close();
    ft.close();
    fo.close();

def  generateISO3166():
    f=open(ip.getCur()+"data/coin_sections.json","r")
    #os.chdir((getCur()+"GBT-265").replace("/","\\"));
    print os.getcwd();
    ip.forceDir(ip.getCur()+"ISO3166");
    os.chdir("ISO3166");
    cou=0;
    aaa=[]
    for line in f:
        a=line.encode("gb2312").lstrip().rstrip() 
        arr=a.split(",");
        if len(a)>3 and arr[1]<>'""':
            cmd="copy "+ip.getCur()+"flag_sections/"+arr[0][2:-1]+" "+arr[1][1:-1]+".png";
            cmd=cmd.replace("/","\\");
            #print cmd;
            os.system(cmd);
            cou=cou+1;
            if(arr[1][1:-1] not in aaa):
                aaa.append(arr[1][1:-1]);
            else:
                print arr[1][1:-1],'------------------------------------------------------------------';
    print cou;
    '''
    fo=open(ip.getCur()+"data/iso3166_cn.txt","r");
    iso=[];              
    for line in fo:
        if len(line.lstrip().rstrip())>2:
            iso.append(line.lstrip().rstrip().decode('utf-8').encode('gb2312'));
            c=line.lstrip().rstrip().decode('utf-8').encode('gb2312').split(',');
            if c[0] not in aaa:
                print c[0],line.lstrip().rstrip().decode('utf-8').encode('gb2312');
    '''         
    f.close();

def  findISOMissing():
    f=open(ip.getCur()+"data/Country_iso3166.csv","r")
    f1=open(ip.getCur()+"data/iso3166_cn.txt","r")
    iso=[];
    for line in f:
        a=line.decode('utf-8').encode('gb2312').split(",");
        iso.append(a[2]);

    iso1=[];
    print "iso3166_cn.txt not in Country_iso3166.csv";
    for line in f1:
        a=line.decode('utf-8').encode('gb2312').split(",");
        iso1.append(a[0]);
        if a[0] not in iso:
            print a[0];

    print "Country_iso3166.csv not in iso3166_cn.txt";
    for line in iso:
        if line not in iso1:
            print line;

    f1.close();
    f.close();



if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding( "utf-8" )  
    ss=u"???????????????????????????????????????????????????????????????????????????????????????......"
    print ss
    cmd = "TITLE "+ss
    os.system(cmd.encode('gb2312'))    
    print "author cclin 2021.04.05"
    print "support:e-mail=12092020@qq.com"
    print "copyright 2015~2018 for anyone to use"
    print ""
    print __file__,__name__
    print ""
    #half autohand process
    
    #processSymbols();
    #processFlags();
    #processCircle();
    #processCircle2();
    #processCircle3();
    #os.system('copy d:/World/TheFlags-CurrencySymbols/flag_circle/wallis-amp-futuna.png d:/World/TheFlags-CurrencySymbols/tocheck/wallis-amp-futuna.png');
    #processReOrder();
    #processSort();
    #processSort1();
    #processGBT();
    #processNGBT();
    #processSort2();
    #generateGBT2659();
    #processISO();
    #processISO_A2();
    generateISO3166();
    #findISOMissing();

    '''
    n1="aland-islands.png";
    n2="Aland.png"
    n11=n1.lower()[:-3];
    n22=n2.lower()[:-3];
    if n11.find(n22)>=0 or n22.find(n11)>=0:
            print "True";    
    print getCur();
    #a=u'[0,"","lt","Abkhazia.png","?????????????????????","Abkhazia","","",""],'.split(",");
    a=u'[18,"","three-h-pure","Austria.png","?????????","Austria","Austria_s_Euro.png","??????","coin_ouyuan","coin_aodilixianling"],'.split(",");
    print(len(a));
    for line in a:        
        print line;
    '''
    