import re

from lxml import etree

from utils.aiohttp_util import exec_aiohttp
from utils.decorator_tools import take_time

# table表格用于储存ip代理
table = []


async def parse_ip66(html):
    pattern = '\d+\.\d+\.\d+\.\d+:\d+'
    table.extend(re.findall(pattern, html))
    return table


async def parse_freeip(html):
    html = etree.HTML(html)
    xpath_list = html.xpath('/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr')
    for xpath in xpath_list:
        ipproxy = f"{xpath.xpath('td')[0].text}:{xpath.xpath('td')[1].text}"
        table.append(ipproxy)
    return table


async def parse_xici(html):
    html = etree.HTML(html)
    xpath_list = html.xpath("//table[@id='ip_list']//tr[@class='odd']")
    for xpath in xpath_list:
        ipproxy = f"{xpath.xpath('td')[1].text}:{xpath.xpath('td')[2].text}"
        table.append(ipproxy)
    return table


proxy_dic = {
    'https://www.freeip.top/?page=1&anonymity=2': parse_freeip,
    'http://www.66ip.cn/mo.php?sxb=&tqsl=100': parse_ip66,
    'https://www.xicidaili.com/nn/': parse_xici
}


@take_time()
def get_ipproxy(proxy_dic):
    exec_aiohttp(proxy_dic)
    print(len(table))
    return table


get_ipproxy(proxy_dic)
