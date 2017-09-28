# coding=utf-8
import os
import sys
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

if __name__ == "__main__":
    # 存储读取语料 一行语料为一个文档
    corpus = []
    for line in open('lda_txt.txt', 'r',encoding='utf8').readlines():
        corpus.append(line.strip())

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    print(vectorizer)

    X = vectorizer.fit_transform(corpus)
    analyze = vectorizer.build_analyzer()
    weight = X.toarray()
    weight.dtype = 'int32'
    print(weight.dtype)

    print(len(weight))
    print(weight[:5, :5])

    # 训练LDA模型
    print('LDA:')
    import numpy as np
    import lda
    import lda.datasets
    model = lda.LDA(n_topics=5, n_iter=200, random_state=1)
    model.fit(np.asarray(weight))
    topic_word = model.topic_word_
    print(topic_word.shape)
    print(topic_word[0][0])

    # 文档-主题（Document-Topic）分布
    doc_topic = model.doc_topic_
    print("type(doc_topic): {}".format(type(doc_topic)))
    print("shape: {}".format(doc_topic.shape))

    # 输出主题中的TopN关键词
    word = vectorizer.get_feature_names()
    n = 3
    for i, topic_dist in enumerate(topic_word):
        print(i)
        print(topic_dist)
        # topic_words = np.array(word)[np.argsort(topic_dist)][:-(n + 1):-1]
        x1 = np.argsort(topic_dist)
        # print(x1.shape)
        x2 = np.array(word)
        # print(x2.shape)
        topic_words = x2[x1][:-(n+1):-1]
        print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

    #输出前20篇文章最可能的Topic
    label = []
    for n in range(10):
        topic_most_pr = doc_topic[n].argmax()
        label.append(topic_most_pr)
        print("doc: {} topic: {}".format(n, topic_most_pr))

    #计算文档主题分布图
    import matplotlib.pyplot as plt

    f, ax = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    for i, k in enumerate([0, 1, 2, 3, 4]):
        ax[i].stem(doc_topic[k, :], linefmt='r-',
                   markerfmt='ro', basefmt='w-')
        ax[i].set_xlim(0, 9)  # x坐标下标
        ax[i].set_ylim(0, 1.2)  # y坐标下标
        ax[i].set_ylabel("Prob")
        ax[i].set_title("Document {}".format(k))
    ax[5].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
