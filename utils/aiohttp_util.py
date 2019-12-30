import asyncio

import aiohttp
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().random  # 随机生成UA
}


# 发送请求
async def fetch(session, url):  # async定义协程对象
    async with session.get(url) as response:
        return await response.text()  # await挂起耗时操作


# # 处理网页
async def download(url, parser):
    async with aiohttp.ClientSession(headers=headers) as session:
        html = await fetch(session, url)
        if parser:
            await parser(html)
        return html


# # 执行多个异步任务
def exec_aiohttp_book(urls, parser=None):
    loop = asyncio.get_event_loop()  # 创建事件循环
    tasks = [asyncio.ensure_future(download(url, parser)) for url in urls]  # 将协程包装成任务对象
    tasks = asyncio.wait(tasks)  # asyncio实现并发,使用wait来接收并发task列表
    loop.run_until_complete(tasks)  # 将任务对象注册到事件循环运行程序


def exec_aiohttp(urls):
    loop = asyncio.get_event_loop()  # 创建事件循环
    tasks = [asyncio.ensure_future(download(url, parser)) for url, parser in urls.items()]  # 将协程包装成任务对象
    tasks = asyncio.wait(tasks)  # asyncio实现并发,使用wait来接收并发task列表
    loop.run_until_complete(tasks)  # 将任务对象注册到事件循环运行程序
