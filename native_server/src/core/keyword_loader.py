# -*- coding: utf-8 -*-
# @Date     : 2020-03-18
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991

import importlib
import sys, os
import src.user_settings as s
from src.common.customized_exception import InvalidExtLibPath
from src.common.log_cat import Log


class KeyWordLoader:
    """关键字加载器"""

    def __init__(self):
        pass

    def _path_check(self, path):
        if os.path.isdir(path):
            return True
        else:
            raise InvalidExtLibPath()

    def get_ext_keyword_lib_path(self):
        lib_path = s.keyword_ext_lib_path
        if self._path_check(lib_path):
            return lib_path

    def load_ext_lib(self):
        """加载扩展类库"""
        #todo 别忘记需要添加目录下所有的item
        ext_lib_path = self.get_ext_keyword_lib_path()
        sys.path + self.pkg_path_scan(ext_lib_path)

    def pkg_path_scan(self, path):
        lib_sys_path = set()
        lib_sys_path.add(os.path.dirname(path)) #默认添加父级目录,增加容错性
        default_pck_name = os.path.basename(path)
        Log.debug("获取扩展包默认包名".format(default_pck_name))
        package_obj = importlib.import_module(default_pck_name)

        return lib_sys_path





    def load(self):
        """读取所有关键字并缓存"""
        built_in_keyword_pck = "keyword"