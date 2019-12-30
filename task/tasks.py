import platform
import sys
import time
from WhatTheFuck import schedule
# 上线后需添加的路径
# import schedule

from aiohttp_spider.spider_ipproxy import get_ipproxy
from setting import plan_log_clear, plan_get_ipproxy
from utils.deal_datetime import str_now_date
from utils.log_tools import remain_recent_log

if not platform.system() == 'Windows':
    sys.path.append('/www/server/python/single_task_financial')

# ##注册任务
# 每天指定时间执行指定任务
schedule.every().day.at(plan_log_clear).do(remain_recent_log)

# 定时执行的爬取任务（每十分钟获取一次ip代理）
while True:
    if str_now_date() == plan_get_ipproxy:
        # 每10分钟执行一次
        schedule.every(10).minutes.do(get_ipproxy)
        print('开始计划任务')
        break
    time.sleep(1)

# 执行任务
while True:
    schedule.run_pending(max_worker=20)  # 最多20个计划任务
    time.sleep(1)
