def longestStr(lists):
    length = []
    res = ""
    for l in lists:
        length.append(len(l))
    maxLen = max(length)
    for l in lists:
        if len(l)==maxLen:
            res = l
            break
    return res


file = open("0830_ADD")
resu = []
lists = file.readlines()
for l in lists:
    l = l.split(";")
    resu.append(longestStr(l))
f = open("add_1.txt", "w+")
for r in resu:
    f.writelines(r+"\n")
f.close()
