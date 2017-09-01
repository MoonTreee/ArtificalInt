import re
import numpy as np


# 对于基金的处理

# 读取文件并装换为小写,并去除：空格，括号，逗号
def readAndLow(path):
    file = open(path)
    foundList = file.readlines()
    founds = []
    for found in foundList:
        foundLow = found.lower()
        founds.append(foundLow)
    return founds


# 识别国家
def findCountry(founds):
    i = 0
    for found in founds:
        china = re.search(r'china', found)
        if china is not None:
            i += 1
    return i


# 去重
def removeDupli(lists, t):
    foundLists = []
    flag = False
    for found in lists:
        if len(foundLists) == 0:
            print("开始")
        else:
            for foundList in foundLists:
                if stringSim(foundList, found) < t:
                    flag = True
                    break
        if flag is False:
            print(found)
            foundLists.append(found)
            flag = False

    return foundLists


# 字符串的相似度--基于编辑距离
def stringSim(str1, str2):
    # d[i][j]表示字符串str1:1~i与字符串str2:1~j的最短编辑距离
    # 初始化临界值
    str1Len = len(str1)
    str2Len = len(str2)
    d = np.zeros((str1Len, str2Len))
    for i in range(str1Len):
        d[i][0] = i
    for j in range(str2Len):
        d[0][j] = j

    # 动态规划赋值
    for i in range(str1Len):
        for j in range(str2Len):
            # 如果相等
            if list(str1)[i] == (list(str2)[j]):
                d[i][j] = d[i - 1][j - 1]
            # 如果不想等,选取最小的编辑距离
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1
    return d[str1Len - 1][str2Len - 1]


# if A in B,包含规则
def mergeTwo(founds):
    foundLists = []
    i = 0
    for found in founds:
        found = found.replace(" ", '').replace("\n", '').lower()
        if len(foundLists)==0:
            foundLists = [found]
        else:
            for foundList in foundLists:
                LongStr = foundList if len(foundList)>len(found) else found
                ShortStr = found if len(foundList)>len(found) else foundList
                # 存在包含关系
                if LongStr.find(ShortStr)!=-1:
                    i+=1
                    print("LongString : " + LongStr + "*****ShortStr : "+ShortStr)
                    break
                else:
                    foundLists.append(found)
    print(i)
    return foundLists

# 提取缩写
# 0827 缩写长度最小为3
def getAbbreviation(found):
    fabb = ""
    for i in found.split():
        if len(i) > 2 and i.isupper():
            fabb = i
            break
    return fabb


# 缩写合并
def mergeOne(founds):
    foundDic = {}
    for found in founds:
        found = found.replace("(", ' ').replace(")", " ").replace(".", " ").replace("\n", '').replace(",", "").replace \
            (":", " ").replace('"', " ").strip()
        addre = getAbbreviation(found)
        keys = list(foundDic.keys())
        if len(addre)>0:
            if addre in keys:
                foundDic[addre].append(found)
            else:
                foundDic[addre] = [found]
        else:
            foundDic[found] = [found]
    return foundDic


if __name__ == '__main__':
    # path = "add_1.txt"
    # file = open(path)
    # foundLists = mergeTwo(file.readlines())
    # print(len(foundLists))
    # print("***********************现在输出结果*****************************")
    # f = open("contain_1.txt", "w+")
    # for key in foundLists:
    #     f.writelines(key+'\n')
    # f.close()
    file = open("test.txt")
    founds = mergeTwo(file.readlines())
    file.close()
    for f in founds:
        print(f+'\n')
