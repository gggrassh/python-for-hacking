import requests  # 发送HTTP请求获取网页内容
from bs4 import BeautifulSoup  # 解析HTML文档，提取所需信息

def get_page(url):
    response = requests.get(url)
    # 获取响应的HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # 查找并打印所有超链接
    print(soup.find_all("a"))

    # 找到a标签
    tag = soup.find_all('a')
    # 遍历每个标签
    for t in tag:
        # 获取href属性值，提取网址
        url2 = t.get('href')
        print(url2)

    # # 查找搜索按钮
    # var = soup.find(id="mw_searchButton")
    # print(var.string)
get_page(input('What url would you like to scrape? '))