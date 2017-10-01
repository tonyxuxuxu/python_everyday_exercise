"""

第 0008 题： 一个HTML文件，找出里面的正文。

"""

from bs4 import BeautifulSoup

def searchhtml(path):
    with open(path, 'r', encoding='utf-8') as readhtml:
        text = BeautifulSoup(readhtml, 'lxml')
        content = text.get_text().split('\n')
    print(content)

if __name__ == "__main__":
    searchhtml("./0008.html")