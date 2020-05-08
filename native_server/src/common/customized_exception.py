# -*- coding: utf-8 -*-
# @Date     : 2020-04-01
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991


class InvalidKeyWord(Exception):
    """ 关键字寻找失败异常 """

    def __init__(self, error_msg=None):
        super().__init__()

        if error_msg is not None:
            self.error_msg = error_msg
        else:
            self.error_msg = "找不到指定的关键字"
        self.error_code = 101

    def __str__(self):
        return self.error_msg


class InvalidExtLibPath(Exception):
    """ 关键字寻找失败异常 """

    def __init__(self, error_msg=None):
        super().__init__()

        if error_msg is not None:
            self.error_msg = error_msg
        else:
            self.error_msg = "不合法的关键字扩展库路径"
        self.error_code = 102

    def __str__(self):
        return self.error_msg


class InvaildHttpMethod(Exception):
    """ http method 异常"""

    def __init__(self, error_msg=None):
        super().__init__()

        if error_msg is not None:
            self.error_msg = error_msg
        else:
            self.error_msg = "当前HTTP请求方法不支持"
        self.error_code = 101

    def __str__(self):
        return self.error_msg
