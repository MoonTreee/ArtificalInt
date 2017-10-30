from os import listdir
import nltk
from nltk.stem import WordNetLemmatizer

# DE：作者关键字
# ID：扩展关键字（大写）
# 弃用

# 读取文件，并将DE和ID字段提取出来
def readFiles(path):
    files = listdir(path)
    result = open("result_0.txt", "w")
    de_id_list = []
    for file in files:
        lines = open(path + "/" + file, encoding='utf8').readlines()
        num_lines = len(lines)
        for i in range(num_lines):
            line = lines[i]
            de = ""
            id0 = ''
            if line.startswith("DE"):
                de = line.replace("\n", ' ')[2:]
                j = i + 1
                while lines[j][:2] == "  ":
                    de += lines[j][2:].replace("\n", " ")
                    j += 1
            elif line.startswith("ID"):
                id0 = line.replace("\n", ' ')[2:]
                j = i + 1
                while lines[j][:2] == "  ":
                    id0 += lines[j][2:].replace("\n", ' ')
                    j += 1
            item = de + id0
            if len(item) >= 1:
                print(item)
                result.writelines(item.strip() + "\n")
                de_id_list.append(item)
    return de_id_list


# 对得到的所需字段的文本进行处理
# 转小写，去除括号里面的内容
# 词形还原
def wordLemmatizing(path):
    lem = WordNetLemmatizer()
    lines = open(path, encoding='utf8').readlines()
    result = open("result_1.txt", "w")
    for line in lines:
        row = ""
        words = line.split(";")
        for p in words:
            # 小写化
            phrase = p.strip().lower().replace("\n", '')
            result_phr = ''
            for w in phrase.split(" "):
                # 去除括号里面的内容
                if w.startswith("(") or w.endswith("0"):
                    break
                # 词形还原
                word = lem.lemmatize(w)
                result_phr = result_phr + "_" +word.strip()
            result_phr = result_phr[1:]
            row = row + ";" +result_phr
        result.writelines(row[1:].strip()+'\n')
    result.close()
    return "词形处理完毕"



if __name__ == "__main__":
    # readFiles('D:\cp\\top-5\CarnegieMellowUniv\data_2057')
    # print(wordLemmatizing('result_0.txt'))




