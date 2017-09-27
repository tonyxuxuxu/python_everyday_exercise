"""
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

"""

import re
import os

def cmp(x, y):
    """
    Replacement for built-in funciton cmp that was removed in Python 3

    Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == y
    and strictly positive if x > y.
    """

    return (x > y) - (x < y)

def findword(data):
    words = re.compile('[a-zA-Z0-9]+')
    dict = {}
    for word in words.findall(data):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict


def fileword(path):
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.splitext(file)[1] == ".txt":
            with open(file) as txtfile:
                data = txtfile.read()
                wordlist = findword(data)
                print(wordlist)
#TODO get max value in dictionary in python 3

if __name__ == "__main__":
    fileword(".")
