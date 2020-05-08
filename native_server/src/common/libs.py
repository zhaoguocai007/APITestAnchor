# -*- coding: utf-8 -*-
# @Date     : 2020-04-01
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991

import os
from src.core.basic_config import project_dir

class Singleton(object):
    """ 单例模式工厂父类，继承此类则自动变为单例模式"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance