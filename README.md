# OLDDRIVER
***
This is a simple module designed for scrapying pictures from [ptt-beauty](https://www.ptt.cc/bbs/Beauty/index.html) to your local machine.  
After importing the module,trying out diffrent parameters in your code makes it possible to get various types of pictures.This is, however, a very basic practice of web scrapying with python.   There is still much room for improvement in aspect of versatility of the module.
***
## Features

### scraping pitures from [ptt-beauty](https://www.ptt.cc/bbs/Beauty/index.html)
![img](https://github.com/majic0626/olddriver/blob/master/img2.PNG)
### easy use dependening on 3 main parameters : index,keyword,pushtag
![img](https://github.com/majic0626/olddriver/blob/master/img3.PNG)


***
## Environment
***
### development environment
* windows 10
* python 3.6.2

### suggestion
(suggestion: python 3.x and also on windows 7.8.10.)

***
## Usage
***
### about the module
* module : ```olddriver.py```
    * Class : ```newcar()```
        * Method
            * ```__init__(self,INI_INDEX=None)```
                * INDEX : the index of the page.
            * ```__store(self,sub_link)```
                * sub_link : url of sublink in the page.
            * ```__collecting(self,now_page,bso_main)```
                * now_page : url of the now page.
                * bso_main : beautifulsoup object of the now page.
            * ```drive(self,DOWN=True,DISTANCE=1)```
                * DOWN : scraping with index going up or down.
                * DISTANCE : the difference between index of first page                                                        and last page. 
        * Attribute
            * ```index``` [int] : index of page in which we are scrapying.
            * ```keyword`` [str]` : type of subpage("正妹","神人","帥哥"(not recommended))
            * ```match_linker``` [list] : all matched url of subpage will be stored here.
            * ```max_index``` [int] : max index of the  url of        [ptt-beauty](https://www.ptt.cc/bbs/Beauty/index.html) 
            * ```sto``` [boolean] : store pictures or not.
            * ```sto_path``` [str] : path where stores pictures.
            
        
### basic example
* import class in the module
```from olddriver import newcar```
* create an instance of newcar
if url="https://www.ptt.cc/bbs/Beauty/index2620.html"
index = 2620
```car = newcar(2620)```
* start to drive
```car.drive()```
Scraping all sub_pages whose subject is ['正妹'] and push number higher than 50 at https://www.ptt.cc/bbs/Beauty/index2620.html. Moreover,all files will be store in D:\beauty\XXXXX(based on system time).

### why not try out diffrent parameters?
Let's take a look at some interesting example.
```python
>>> from olddriver import newcar
>>> car = newcar(2620)
2620 assigned as ini_index.
>>> car.Plimit
50
>>> car.Plimit = 30
>>> car.keyword
'[正妹]'
>>> car.drive(DOWN=False,DISTANCE=3) # index goes up for 3 steps.
we are collecting at https://www.ptt.cc/bbs/Beauty/index2620.html... # collecting
the sub_pages matching the condition will be showed for you...
fucking exception happened..but under my control haha!
fucking exception happened..but under my control haha!
fucking exception happened..but under my control haha! 
no push tag was found.
fucking exception happened..but under my control haha!
no push tag was found.

# some exception always happens including "push_tag not found!" or
# "subject of subpage not found!" or "cannot recognize the number of push_tag!"
# BUT THEY ARE UNDER THE CONTROL.

matching subpage at https://www.ptt.cc/bbs/Beauty/index2620.html are :

['/bbs/Beauty/M.1534835860.A.27B.html', '/bbs/Beauty/M.1534841759.A.9B1.html', '/bbs/Beauty/M.1534844388.A.442.html', '/bbs/Beauty/M.1534850750.A.EC0.html']

# and then save pictures from those four subpages into our local machine (sto_path)
got a JPEG file
got a JPEG file
got a JPEG file
got a JPEG file
got a JPEG file
got a JPEG file
got a JPEG file
got a GIF file # this version don't save gif files.should have next version.
got a JPEG file
got a JPEG file
...
# this is ONLY subpages in the https://www.ptt.cc/bbs/Beauty/index2620.html
# the script will keep scraping in next two pages respectively
# https://www.ptt.cc/bbs/Beauty/index2621.html
# https://www.ptt.cc/bbs/Beauty/index2622.html
```
## NOW!IT'S YOUR TURN.










