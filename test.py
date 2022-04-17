from snownlp import SnowNLP
from snownlp import sentiment

a = []
txt = ["这部剧还算行吧，部分演员的演技有待提高，剧情方面槽点不少，还有点悬浮假大空，叙事节奏也略慢，并且和原著小说出入还挺大的，总之，就是编剧既没改编好，导演也没把控到位。", "刘诗诗演技太差了，台词听着难受，像快断气一样，表情也是怎么摆怎么不合适。",
       "希望中国的影视，真正去关心平民，而不是描写一出上流社会的幻想，满足底层百姓的梦"]

# 训练前
for i in range(3):
    a.append(SnowNLP(txt[i]))
    print(a[i].sentiments)

# # 训练
# sentiment.train('E:\\python\\Lib\\site-packages\\snownlp\\sentiment\\neg1.txt', 'E:\\python\\Lib\\site-packages\\snownlp\\sentiment\\pos1.txt')
# sentiment.save('E:\\python\\Lib\\site-packages\\snownlp\\sentiment\\sentiment.marshal1')
