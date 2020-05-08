# -*- coding: utf-8 -*-
# @Date     : 2020-03-24
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991

"""本地缓存模块"""

from cacheout import Cache

from cacheout import CacheManager


class CacheAdapter():
    __maxsize = 1000
    __ttl = 0

    def __init__(self):
        pass

    def source(self):
        ca = CacheManager(
            {
                "a": {"maxsize": CacheAdapter.__maxsize},
                "b": {"maxsize": CacheAdapter.__maxsize}
            }
        )


CacheAdapter()

from cacheout import CacheManager


class C:
    a = 0
    b = 100


ca = CacheManager({"a": {"maxsize": 100},
                   "b": {"maxsize": 100}})

ca["a"].set("name", "andy")
ca["a"].set("name1", C())
x = ca.caches()[1].get("name1").a
print(x)
