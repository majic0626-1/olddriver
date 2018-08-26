# -*- coding: utf-8 -*-

import requests as req
from bs4 import BeautifulSoup as BS
import re
import io
from PIL import Image
import time
import os



class newcar(object):

    def __init__(self,INI_INDEX=None):
        self.Plimit = 50
        self.keyword = '[正妹]'
        self.sto = True
        self.match_linker = {}
        

        self.__r_main = req.get("https://www.ptt.cc/bbs/Beauty/index.html")
        self.__bso_main = BS( self.__r_main.text,'lxml')
        self.max_index = int(re.search('(\d)+',self.__bso_main.find_all('a',{'class':"btn wide"})[1]['href']).group())+1

        if INI_INDEX == None:
            print ("no ini_index assigned.max_index was ini_index!")
            self.ini_index = self.max_index
            
        elif (INI_INDEX < 1) or INI_INDEX > self.max_index:
            print ("error when ini_index assigned.max_index was ini_index!")
            self.ini_index = self.max_index

        else:
            self.ini_index = INI_INDEX
            print ("{} assigned as ini_index.".format(self.ini_index))

        self.__now_page = "https://www.ptt.cc/bbs/Beauty/index"+str(self.ini_index)+".html"
        self.__r_main = req.get(self.__now_page)
        self.__bso_main = BS(self.__r_main.text,'lxml')

        
        

        

        
    def __store(self,sub_link):

        self.sto_path = 'D:\\beauty\\'+(time.asctime().replace(":"," ").replace(" ",""))
    
        try:
            os.mkdir(self.sto_path)
        except FileExistsError as e:
            print ("FILE EXISTS.STILL WORKING.")
    
        for i in sub_link: # find all .jpg pics
            r = req.get("https://www.ptt.cc"+i)
            bso = BS(r.text,'lxml')
            for l in bso.find_all(href=re.compile('.jpg$'),target='_blank'):
                file_name = l['href'].split("/")[-1] # XXX.jpg
                rr = req.get(l['href'])
                img = Image.open(io.BytesIO(rr.content))
                print ("got a "+img.format+" file")
                if  img.format == 'JPEG':
                    img.save(self.sto_path+'\\'+file_name)
                
        
            






    def __collecting(self,now_page,bso_main): # private method for instance of my_car class.
        sub_link = []
    

        print ("we are collecting at "+now_page+"...")
        print ("the sub_pages matching the condition will be showed for you...")
    

        for i in bso_main.find_all('div',{'class':"r-ent"}):

            link = i.find_all('div', {'class':'nrec'})[0]
            try:
                push = link.span.string # push tag's number
                try:
                    
                    if (push =='爆') or (int(str(push)) >= self.Plimit):
                        print ("fucking exception happened..but under my control haha!")
                        try:
                            sub_title = link.next_sibling.next_sibling.a.string
                            page = link.next_sibling.next_sibling.a['href']
                            
                            if re.search(self.keyword, sub_title) != None:
                                sub_link.append(page)
                        except TypeError as e:
                            print ("fail to get url.")
        
                except ValueError as e:
                    print ('have push tag.but cannot recognize number.')
                    
            except AttributeError as e:
                print ("no push tag was found.")


        print ("matching subpage at {} are : \n".format(now_page))       
        print (sub_link)
        return sub_link






    def drive(self,DOWN=True,DISTANCE=1): # STO:save or not
    

        if DOWN:
            direction = -1
        else:
            direction = 1 

        
    

        for i in range(DISTANCE):

            if ((self.ini_index > 0) or (self.ini_index <= self.max_index)):
                self.__now_page = "https://www.ptt.cc/bbs/Beauty/index"+str(self.ini_index)+".html"
                self.__r_main = req.get(self.__now_page)
                self.__bso_main = BS(self.__r_main.text,'lxml')
        
        
    
                self.__sub_link = self.__collecting(self.__now_page,self.__bso_main)
                self.match_linker[self.ini_index] = self.__sub_link

                if self.sto:
                    self.__store(self.__sub_link)

            else:
                print ("out of index limit.")
                break

            self.ini_index += direction

        print ("all process finish!!!老司機上車嘍")










    
        
