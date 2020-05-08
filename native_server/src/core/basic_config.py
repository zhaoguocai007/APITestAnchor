# -*- coding: utf-8 -*-
# @Date     : 2020-03-17
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991

import os

# 项目目录
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def calc_inner_abs_path(inner_path):
    """计算框架内部文件绝对路径"""
    return os.path.join(project_dir, "output")

# 日志输出路径.默认输出到当前工程项目output下; 可修改此值自定义路径
log_path = calc_inner_abs_path("output")



