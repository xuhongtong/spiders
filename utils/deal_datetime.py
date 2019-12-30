import datetime
import time


# 1.字符串转时间戳
def str_stamp(str_date):
    try:
        time_array = time.strptime(str_date, "%Y-%m-%d %H:%M:%S")
    except:
        time_array = time.strptime(str_date, "%Y-%m-%d")
    time_stamp = int(time.mktime(time_array))
    return time_stamp


# 时间戳转时间字符串
def stamp_str(time_stamp):
    timeArray = time.localtime(time_stamp)
    try:
        str_date = time.strftime("%Y-%m-%d", timeArray)
    except:
        str_date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return str_date


# utc格式转本地时间格式
def utc_localtime(utc):
    try:
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        utcTime = datetime.datetime.strptime(utc, UTC_FORMAT)
    except:
        UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
        utcTime = datetime.datetime.strptime(utc, UTC_FORMAT)
    localtime = utcTime + datetime.timedelta(hours=8)
    return localtime


# 获取当前本地时间(日期格式）
def str_now_date():
    str_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    date = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    return date


# 获取当前本地时间(日期格式）
def str_now_date_time():
    str_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    return date


# 获取当前本地时间(字符串格式）
def str_date():
    str_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return str_date


# 字符串转日期时间
def str_dates(times):
    try:
        date = datetime.datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    except:
        date = datetime.datetime.strptime(times, '%Y-%m-%d')
    return date


# 日期格式转字符串
def date_str(times):
    try:
        date_str = datetime.datetime.strftime(times, "%Y-%m-%d %H:%M:%S")
    except:
        date_str = datetime.datetime.strftime(times, "%Y-%m-%d")
    return date_str


# 获取当前utc时间
def str_date_utc():
    str_date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    date = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M') - datetime.timedelta(hours=8)
    return date


# 补数据（获取本地时间对应的utc时间）
def repair_date_utc(str_date):
    date = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=8)
    return date


# 获取当前utc时间
def get_now_utc():
    utc = datetime.datetime.utcnow()
    return utc


# 获取时间戳
def date_stamp(times):
    times = date_str(times)
    ts = int(time.mktime(time.strptime(times, "%Y-%m-%d %H:%M:%S")))
    return ts


# 取时间
def time_genertor(start_time, end_time, hours=24):
    temp = start_time
    while temp < end_time:
        temp = start_time + datetime.timedelta(hours=hours)
        yield start_time, temp
        start_time = temp
