# -*- coding: utf-8 -*-
# @Date    : 2019-12-09
# @Author  : zhaoguocai

import logging, os, time, sys
from src.core.basic_config import log_path
from src.user_settings import log_level
from logging import handlers


# Todo 需要控制台log添加颜色

class LogCat:
    """ 日志处理模块 """

    _log_path = log_path
    _log_level = log_level
    _log_display_format = "%(asctime)s - %(name)s - %(levelname)s : %(message)s"

    def __init__(self):
        if not os.path.exists(LogCat._log_path):
            os.makedirs(LogCat._log_path)
        self.log_file = os.path.join(LogCat._log_path, "{}.log".format(time.strftime('%Y-%m-%d', time.localtime())))

    def get_loger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.NOTSET) #默认的root 设置的日志等级是Warning
        formatter = logging.Formatter(LogCat._log_display_format)
        console = logging.StreamHandler(sys.stdout)
        file_handler = handlers.TimedRotatingFileHandler(filename=self.log_file, when='D', interval=1,
                                                         backupCount=15, encoding='utf-8')
        console.setLevel(LogCat._log_level)
        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(LogCat._log_level)
        logger.addHandler(console)
        logger.addHandler(file_handler)
        return logging.getLogger()


Log = LogCat().get_loger()
