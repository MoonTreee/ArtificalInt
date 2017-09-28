file = open("download_1.txt", "r", encoding="utf8")
lda_txt = open("lda_txt.txt", "w")

for line in file.readlines():
    if line.startswith("AB"):
        lda_txt.writelines(line[3:])

file.close()
lda_txt.close()