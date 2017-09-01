
# 对基金项目名称进一步进行处理，使其标准化。
# abb_A_0901存放的是最终的标准数据，abb_B_0901存放的是未进行合并去重的标准数据。
# 目的：将B文件中的数据进行合并（以A作为基准）
# 最终使得 f_a为压缩之后的标准名称列表,f_b为别名列表

# 读取A文件
f_a = []
a = open("txts/abb_A_0901.txt").readlines()
for a_i in a:
    f_a.append(a_i.replace("\n", ''))
# 读取B文件
f_b =[]
b = open("txts/abb_B_0901.txt").readlines()
for b_i in b:
    f_b.append(b_i.replace("\n", ''))

# 进行处理.遍历f_a,f_b.
# 如果f_a[i]为空("\n")
length = len(f_a)
n = 0
for i in range(length):
    j = length-i-1
    if len(f_a[j]) == 0:
        n+=1
        f_b[j-1] = (f_b[j] + ";"+f_b[j-1]).replace(";;", ";")
        print(f_b[j-1])
        f_b.pop(f_b[j])
        f_a.pop(f_a[j])
print(n)

# 写入文件
f_s = open("txts/stand.txt", "w+")
for i in range(len(f_a)):
    f_s.writelines(f_a[i]+'\n')
f_s.close()




