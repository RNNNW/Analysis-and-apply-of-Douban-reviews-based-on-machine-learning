# coding:utf-8
import pandas as pd
from snownlp import SnowNLP

# 读取抓取的csv文件，评论在第3列，序号为2
df = pd.read_csv('douban_moive.csv', header=None, usecols=[2])
# 将dataframe转换为list
contents = df.values.tolist()
# 数据长度
print("一共有", len(contents), "条评论")
score = []

for content in contents:
    # noinspection PyBroadException
    try:
        s = SnowNLP(content[0])
        score.append(s.sentiments)
    except Exception as e:
        print("something is wrong")
        score.append(0.5)
# 显示情感得分长度，与数据长度比较
print("一共有", len(score), "条对应的情感得分")
# 存储
data2 = pd.DataFrame(score)
data2.to_csv('sentiment1.csv', header=False, index=False, mode='a+')
