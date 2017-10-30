import csv
from nltk.stem import WordNetLemmatizer
from nltk.book import *


# 读取文件，并返回所有频数大于1的keyword列表
def readFiles(path):
    ky_list = list()
    ky_set = set()
    csv_reader = csv.reader(open(path, encoding='utf8'))
    # csv_writer = csv.writer(open('collo_result_0.csv', "w", newline=''), dialect='excel')
    lenm = WordNetLemmatizer()
    for row in csv_reader:
        words = row[0].replace('"', '').replace('-'," ").split()
        line = ''
        for w in words:
            if w.startswith("("):
                continue
            word = lenm.lemmatize(w)
            line = line + ' ' +word
        ky_list.append(line[1:])
        new_row = [str(line[1:]), str(row[1])]
        # csv_writer.writerow(new_row)
    fdist = FreqDist(ky_list)
    for l in ky_list:
        if fdist[l] >= 3:
            ky_set.add(l)
    print(len(ky_set))
    return ky_set


# 生成共现矩阵
def collocating(list):
    csv_writer = csv.writer(open('collo_result_1.csv', "w", newline=''), dialect='excel')
    length = len(list)
    for i in range(length):
        for j in range(i, length):
            result = collocateNum("collo_result_0.csv", list[i], list[j]).split('\t')
            if int(result[2]) >= 1:
                csv_writer.writerow(result)
                print(result)


# 计算共现次数
def collocateNum(path, word_1, word_2):
    csv_reader = csv.reader(open(path, encoding='gbk'))
    wos_1 = []
    wos_2 = []
    for row in csv_reader:
        if word_1 == row[0]:
            wos_1.append(row[1])
        if word_2 == row[0]:
            wos_2.append(row[1])
    # 求交集
    list_col = [i for i in wos_1 if i in wos_2]
    result = word_1 + '\t' + word_2 + '\t' + str(len(list_col))
    return result


# 构建索引 word1:wosxxxx;wosxxxx……
def indexBuildder(path):
    csv_reader = csv.reader(open(path, encoding='gbk'))
    # txt_writer = open("word_index.txt", "w", encoding='utf-8')
    result = {}
    for row in csv_reader:
        if row[0] not in result.keys():
            result[row[0]] = row[1]
        else:
            result[row[0]] = result[row[0]] + ";" + row[1]
    # for key in result.keys():
    #     txt_writer.writelines(str(key) + '\t' + str(result[key]) + '\n')
    # txt_writer.close()
    return result


# 利用索引生成共现矩阵
def collocatingTwo(list):
    dic = indexBuildder("collo_result_0.csv")
    txt_writer = open("cllocatingTwo.txt", "w", encoding='utf-8')
    length = len(list)
    for i in range(length):
        for j in range(i, length):
            values_1 = dic[list[i]].split(';')
            values_2 = dic[list[j]].split(';')
            collocate_count = len([i for i in values_1 if i in values_2])
            if collocate_count >= 1:
                txt_writer.writelines(str(list[i]) + '\t' +str(list[j]) + '\t' + str(collocate_count) + '\n')
    txt_writer.close()


if __name__ == '__main__':
    collocatingTwo(list(readFiles("ky.csv")))