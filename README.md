# ArtificalInt

工作记录：</br>
一：缩写去重（3285->2700）</br>
    缩写提取规则：对基金项目名称分割为word，如果一个len（word）>3 and word.isupper(),则 wrod 为缩写。
    同缩写去重！</br>
二：包含去重（2700->2262）</br>
    将项目名称去除标点、特色字符（如"\n"）、空格；并将其小写化。过滤规则为if str1.find(str2)!=-1,则去除。</br>
