# coding: utf-8

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


# 读取csv文件
df = pd.read_csv('douban_moive.csv')

# 将dataframe转换为list
mark_list = df['mark'].values.tolist()
# 利用Counter统计每个评分的数量
num_count = Counter(mark_list)
print("各个星级的评论条数：\n", dict(num_count))

# 利用groupby求得各个星级评论的情感得分的均值
grouped = df.groupby('mark').describe().reset_index()
mark = grouped['mark'].values.tolist()
grouped1 = df.groupby('mark')['score'].mean()
average_score = grouped1.values
print("各个星级的评论情感得分的平均值：\n", dict(zip(mark, average_score)))

good = 0
bad = 0
for i in range(len(mark_list)):
    if df.score[i] > 0.5:
        good = good + 1
    else:
        bad = bad + 1
print("好评率", good / len(mark_list))

# 将数据集中的日期转换成datetime的模式
time = pd.to_datetime(df['time'], format="%Y/%m/%d")


def estimate_score(arr):
    good1 = 0
    score = arr.values.tolist()
    for j in range(len(score)):
        if score[j] > 0.5:
            good1 = good1 + 1
    return good1/len(score)


# 利用groupby处理每天的好评率（情感得分大于0.5称为好评）
grouped2 = df.groupby(time)['score'].apply(estimate_score)
print("每天的好评率如下\n", grouped2)

plt.figure(figsize=(50, 50), dpi=100)
# 把y轴的刻度间隔设置为0.1，并存在变量里
y_major_locator = MultipleLocator(0.1)
# ax为两条坐标轴的实例
ax = plt.gca()
# 把y轴的主刻度设置为0.1的倍数
ax.yaxis.set_major_locator(y_major_locator)

plt.plot(time, df.score, '*')
plt.show()
