import logging
import os
import shutil
from setting import BASE_DIR, recent_week_stamp, console
from utils.deal_datetime import str_stamp, stamp_str, str_date


# 生成日志
def get_logger(logname):
    everyday_log_dir()
    logger = logging.getLogger(logname)
    # 每次清空handlers
    logger.handlers = []
    # 设置日志打印级别
    logger.setLevel(logging.INFO)
    # 设置日志文件名称及路径
    logname_info = f'{logname}_info.{new_log()}.log'
    logname_error = f'{logname}_error.{new_log()}.log'
    logfile_info = os.path.join(everyday_log_dir(), logname_info)
    logfile_error = os.path.join(everyday_log_dir(), logname_error)
    # 将日志写入到文件
    fh_info = logging.FileHandler(logfile_info, mode='a+', encoding='utf-8')
    fh_error = logging.FileHandler(logfile_error, mode='a+', encoding='utf-8')
    # 设置过滤等级
    info_filter = logging.Filter()
    info_filter.filter = lambda record: record.levelno < logging.WARNING
    err_filter = logging.Filter()
    err_filter.filter = lambda record: record.levelno >= logging.WARNING
    # 过滤设置应用到addFilter
    fh_info.addFilter(info_filter)
    fh_error.addFilter(err_filter)
    fh_info.setLevel(logging.INFO)
    fh_error.setLevel(logging.ERROR)
    # 设置日志打印格式
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh_info.setFormatter(formatter)
    fh_error.setFormatter(formatter)
    # 将日志打印格式应用到addHandler
    logger.addHandler(fh_info)
    logger.addHandler(fh_error)
    # 是否打印日志到控制台
    if console:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger


# 获取最新日期的日志
def new_log():
    log_dir_list = os.listdir(os.path.join(BASE_DIR, 'log'))
    log_date_stamp_list = []
    if log_dir_list:
        for log_dir in log_dir_list:
            log_date_stamp = str_stamp(log_dir.strip('.txt')[-10:])
            log_date_stamp_list.append(log_date_stamp)
        new_logfile = stamp_str(max(log_date_stamp_list))
        return new_logfile


# 生成每日日志目录名称
def everyday_log_dir():
    # 日志路径配置
    times = str_date()[:10]
    log = os.path.join(BASE_DIR, 'log')
    LOG_DIR = os.path.join(log, f'log.{times}')
    # 创建每日目录
    isExists = os.path.exists(LOG_DIR)
    if not isExists:
        os.mkdir(LOG_DIR)
        LOG_DIR = os.path.join(log, f'log.{times}')
    return LOG_DIR


# 保留近期日志
def remain_recent_log():
    # 当日时间戳
    current_day_stamp = str_stamp(str_date()[:10])
    log_dir_list = os.listdir(os.path.join(BASE_DIR, 'log'))
    for log_dir in log_dir_list:
        logfile_path = os.path.join(os.path.join(BASE_DIR, 'log'), log_dir)
        log_date_stamp = str_stamp(log_dir.strip('.txt')[-10:])
        # 小于一周的日志文件
        if current_day_stamp - recent_week_stamp > log_date_stamp:
            shutil.rmtree(logfile_path)
    return ''
