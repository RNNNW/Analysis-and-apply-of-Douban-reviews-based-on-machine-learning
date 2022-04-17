import re
import html
import time
import requests


def crawl_joke(page=1):
    url = "https://www.qiushibaike.com/text/page/" + str(page)
    res = requests.get(url)
    # 处理html中的转义字符
    body = html.unescape(res.text).replace("<br/>", "")
    # 处理整块内容
    pattern = re.compile("<div class=\"article block untagged mb15 typs_hot.*?<div class=\"content\">.*?</div>",
                         re.S)
    m = pattern.findall(body)
    # 处理评论
    comment_pattern = re.compile("<div class=\"content\"><span>(.*?)</div>", re.S)
    # 处理昵称
    name_pattern = re.compile("<div class=\"author clearfix\">.*?<h2>(.*?)</h2>", re.S)
    for i in m:
        output = []
        name = name_pattern.findall(i)
        if len(name) > 0:
            output.append(name[0])
        comment = comment_pattern.findall(i)
        if len(comment) > 0:
            output.append(comment[0])
        print("\t".join(output))
    time.sleep(1)


if __name__ == '__main__':
    for j in range(1, 10):
        crawl_joke(j)
