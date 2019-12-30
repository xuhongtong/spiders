import os

# 上线Mongodb数据库连接信息
import platform

if platform.system() == 'Windows':
    # 测试Mongodb数据库连接信息
    mongo_info = {
        'host': '192.168.199.129',
        'username': '',
        'password': '',
        'authSource': ''
    }
else:
    mongo_info = {
        'mongodb_name':'xxx',
        'host': 'xxx',
        'username': 'xxx',
        'password': 'xxx',
        'authSource': 'xxx'
    }

# 日志是否打印到控制台
console = False

# 保留最近一周的日志
recent_week_stamp = 7 * 24 * 3600

# 请求异常重试次数
attempt = 3

# 创建基本目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ========计划任务=======#
# 每日中午12：00清除日志（默认一周前）
plan_log_clear = '12:00'

# 从当日或下一日10：00获取ip代理
plan_get_ipproxy='10:00'

