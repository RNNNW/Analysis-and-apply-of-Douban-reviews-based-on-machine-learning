# coding:utf-8
import re
from wordcloud import WordCloud
import jieba
import pandas as pd


def remove_punctuation(line):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    line = rule.sub('', line)
    return line


# 处理分词以后的文本
def new_cut(text):
    wordlist_jieba = jieba.cut(text, cut_all=False)
    space_wordlist = " ".join(wordlist_jieba)
    return space_wordlist


# 载入自定义词典
jieba.load_userdict("./newdict.txt")

# 自定义停用词合集
stop_words = set()
fd = open("stopwords.txt", "r", encoding='utf-8')
for item in fd.readlines():
    stop_words.add(item.strip())

df = pd.read_csv('douban_moive.csv')
comment_list = df['comment'].values.tolist()
mark_list = df['mark'].values.tolist()
score_list=df['score'].values.tolist()

# 将句子中的标点符号去掉
new_comment = []
for i in range(len(mark_list)):
    new_comment.append(remove_punctuation((comment_list[i])))

# text = ""
# for i in range(len(mark_list)):
#     text = text + new_cut(new_comment[i])
# print(text)
# 找出3星以下的差评和3星以上的好评
text = ""
text1 = ""
for i in range(len(mark_list)):
    if score_list[i] < 0.3:
        text = text + new_cut(new_comment[i])
    elif score_list[i] > 0.7:
        text1 = text1 + new_cut(new_comment[i])

# 调用包PIL中的open方法，读取图片文件，通过numpy中的array方法生成数组
# mask_pic = np.array(Image.open("background.jpg"))
wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",  # 设置字体
                      background_color="white",  # 设置背景颜色
                      max_font_size=200,  # 设置字体最大值
                      min_font_size=15,  # 设置字体最小值
                      max_words=1000,  # 设置最大显示的字数
                      stopwords=stop_words,  # 设置停用词，停用词则不再词云图中表示
                      width=800,
                      height=800
                      ).generate(text1)

image = wordcloud.to_image()
image.show()
# wordcloud1 = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",  # 设置字体
#                        # mask=mask_pic,  # 设置背景图片
#                        background_color="white",  # 设置背景颜色
#                        max_font_size=200,  # 设置字体最大值
#                        min_font_size=15,  # 设置字体最小值
#                        max_words=1000,  # 设置最大显示的字数
#                        stopwords=stop_words,  # 设置停用词，停用词则不再词云图中表示
#                        width=800,
#                        height=800
#                        ).generate(text1)
#
# image1 = wordcloud1.to_image()
# image1.show()
