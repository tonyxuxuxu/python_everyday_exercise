"""

第 0009 题： 一个HTML文件，找出里面的链接。

"""

from bs4 import BeautifulSoup

def findurl(path):
    with open(path,'r',encoding="utf-8") as openfile:
        text = BeautifulSoup(openfile,'lxml')
        url = text.findAll('a')
        for u in url:
            print(u['href'])

if __name__ =="__main__":
    findurl("./0009.html")

