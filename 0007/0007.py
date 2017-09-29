import re
import os

def countline(path):
    blanks, comments, codelines, totallines = 0, 0, 0, 0
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.splitext(file)[1] == '.py':
            print(file)
            with open(file,'r',encoding='utf-8') as openfile:
                while True:
                    line = openfile.readline()
                    totallines += 1
                    if not line:
                        break
                    elif line.strip().startswith('#'):
                        comments += 1
                    elif line.strip().startswith("'''") or line.strip().startswith('"""'):
                        comments += 1
                        if line.count("'''") == 1 or line.count('"""') == 1:
                            while True:
                                line = openfile.readline()
                                totallines += 1
                                comments += 1
                                if ('"""' in line) or ("'''" in line):
                                    break
                    elif line.strip():
                        codelines += 1
                    else:
                        blanks += 1

    print('the number of total line is: '+str(totallines))
    print('the number of comments is '+str(comments))
    print('the number of codeline is '+str(codelines))
    print('the number of blank line is '+str(blanks))
    blanks, comments, codelines, totallines = 0, 0, 0, 0


if __name__ == '__main__':
    countline(".")