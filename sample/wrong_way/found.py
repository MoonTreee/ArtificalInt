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


# 识别国家:USA(3559),PEOPLES R CHINA(2861),ENGLAND(1283),SPAIN(1227),
#         FRANCE(792),CANADA(773),ITALY(736),GERMANY(719),BRAZIL(648),
#         IRAN(603),AUSTRALIA(578),JAPAN(557),POLAND(539),TAIWAN(489)...
def findCountry(founds):
    country_list=[]
    i_0=0;i_1=0;i_2=0;i_3 =0;i_4=0;i_5=0;i_6=0;i_7=0;i_8=0;i_9=0
    # 制定国家识别规则
    for found in founds:
        if re.search(r'[Cc]hin|[Bb]eijing|[Jj]iangsu|[Zz]hejiang|Natural Science Foundation|973|863'
                     r'|[sS]hanghai|[Ss]handong', found):
            country_list.append("China")
            i_1+=1
        elif re.search(r'[Aa]merican|US|U S|Mexico|Stanford|Indian', found):
            country_list.append("USA")
            i_2+=1
        elif re.search(r'(.*)[Ee]ngland|UK|U K(.*)', found):
            country_list.append("England")
            i_3+=1
        elif re.search(r"(.*)[Ff]rance(.*)|Perlis", found):
            country_list.append("France")
            i_4+=1
        elif re.search(r'[Cc]anad', found):
            country_list.append("CANADA")
            i_5+=1
        elif re.search(r"[Ii]taly",found):
            country_list.append("ITALY")
            i_6+=1
        elif re.search(r'[Gg]erman', found):
            country_list.append("Germany")
            i_7+=1
        elif re.search(r'[Bb]razil', found):
            country_list.append("BRAZIL")
            i_8+=1
        elif re.search(r'[Ii]ndia', found):
            country_list.append("INDIAN")
            i_9+=1
        else:
            country_list.append(" ")
            i_0+=1
    print("中国：" + str(i_1))
    print("美国：" + str(i_2))
    print("英国：" + str(i_3))
    print("法国： "+ str(i_4))
    print("加拿大：" + str(i_5))
    print("意大利：" + str(i_6))
    print("德国：" + str(i_7))
    print("巴西：" + str(i_8))
    print("印度：" + str(i_9))
    print("未识别： "+ str(i_0))

    return country_list


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
                # LongStr = foundList if len(foundList)>=len(found) else found
                # ShortStr = found if len(foundList)>=len(found) else foundList
                # 存在包含关系
                if foundList.find(found) > -1 | found.find(foundList) >-1:
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
    file = open("txts/stand.txt")
    countries = findCountry(file.readlines())
    file.close()
