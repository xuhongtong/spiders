import pandas as pd
from bs4 import BeautifulSoup

from utils.aiohttp_util import exec_aiohttp_book
from utils.decorator_tools import take_time

table = []


# 解析网页
async def parser_dangdang(html):
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(html, "lxml")
    # 获取网页中的畅销书信息
    book_list = soup.find('ul', class_="bang_list clearfix bang_list_mode")('li')

    for book in book_list:
        info = book.find_all('div')

        # 获取每本畅销书的排名，名称，评论数，作者，出版社
        rank = info[0].text[0:-1]
        name = info[2].text
        comments = info[3].text.split('条')[0]
        author = info[4].text
        date_and_publisher = info[5].text.split()
        publisher = date_and_publisher[1] if len(date_and_publisher) >= 2 else ''

        # 将每本畅销书的上述信息加入到table中
        table.append([rank, name, comments, author, publisher])


@take_time()
def get_dangdang():
    dangdang_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d' % i for i in
                     range(1, 26)]
    exec_aiohttp_book(dangdang_urls, parser_dangdang)
    df = pd.DataFrame(table, columns=['rank', 'name', 'comments', 'author', 'publisher'])
    df.to_csv('dangdang.csv', index=False)
