#项目说明
一、使用的爬虫技术
- 1.第三方异步请求库（协程）：aiohttp
- 2.第三方同步请求库（多线程）：requests
- 3.爬虫框架（分布式）：scrapy


二、实现功能
-1.日志
- 1.1.日志打印控制台开关，默认关闭
- 1.2.日志打印至文件，文件名：自定义名称+日期后缀，打印内容前缀
- 1.3.保留日期时间，默认为一周


2.装饰器功能
- 2.1.http请求重试次数
- 2.2.程序耗时统计

3.mongo数据库
- 3.1.单条或批量插入记录（以字典形式传入需要存储的数据，指定文档名称）
- 3.2.更新指定记录（通过字段筛选需要更新的记录、通过传入字典更新该条记录、指定文档名称）
- 3.3.指定字段判断数据库是否存在该记录，进行去重



免费ip代理网站
- 66代理：http://www.66ip.cn/mo.php?sxb=&tqsl=100
- freeip:https://www.freeip.top/?page=1&anonymity=2
- 西刺代理（高匿）:https://www.xicidaili.com/nn/1