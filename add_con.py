# 对包含合并之后的结果进行整理。统一为标准形式

#标准形式
f1 = open("add_1.txt")
addlist = f1.readlines()
f1.close()

# 因为要进行包含合并转换之后的形式（小写，空格等）
f2 = open('contain_1.txt')
containlist = f2.readlines()
conlist = []
for con in containlist:
    conlist.append(con.replace("\n", ''))
f2.close()
f3 = open("add_con.txt", "w+")
print(len(addlist))
i = 0
for found in addlist:
    found_con = found.replace(" ", '').replace("\n", '').lower()
    if found_con in conlist:
        i += 1
        print(found_con)
        f3.writelines(found)
        conlist.remove(found_con)
    else:
        f3.write("\n")

f3.close()
print(i)