# -*- coding: utf-8 -*-
# @Date     : 2020-04-22
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991


import json

a='{"a":"中国"}'
c=json.dumps(a,ensure_ascii=False)
print(type(c))
print(c)