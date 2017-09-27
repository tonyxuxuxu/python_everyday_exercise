"""
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re


def findword(data):
    words = re.compile('[a-zA-Z0-9]+')
    dict = {}
    for word in words.findall(data):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

if __name__ == "__main__":
    with open('./python.txt','r') as file:
        data = file.read()
        wordlist = findword(data)
        print(wordlist)
        file.close()
