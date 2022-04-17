import requests
import re
from bs4 import BeautifulSoup


def get_one_page(url):
    response = requests.get(url)
    # response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def parse_page(soup):
    # 待存储的信息列表
    return_list = []
    # 起始位置
    grid = soup.find('div', attrs={"class": "interns"})
    if grid:
        # 找到所有的岗位列表
        job_list = soup.find_all('div', attrs={"class": "job-list"})

        # 匹配各项内容
        for job in job_list:
            # find()是寻找第一个符合的标签
            company = job.find('h3', attrs={"class": "name"}).get_text().strip()  # 返回类型为string，用strip（）可以去除空白符，换行符
            title = job.find('div', attrs={"class": "detail-top-title"}).get_text()
            salary = job.find('span', attrs={"class": "red"}).get_text().strip()
            # 将信息存到列表中并返回
            return_list.append(company + " " + title + " " + salary)
    return return_list


def write_to_file(content):
    # 以追加的方式打开，设置编码格式防止乱码
    with open("shixi.csv", "w", encoding="gb18030")as f:
        f.write("\n".join(content))


def main(page):
    url = 'https://www.zhipin.com/c100010000/?query=Java&page=' + str(page)+'&ka=-'+str(page)
    soup = get_one_page(url)
    return_list = parse_page(soup)
    write_to_file(return_list)


if __name__ == "__main__":
    main(3)
