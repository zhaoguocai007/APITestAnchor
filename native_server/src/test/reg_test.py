# -*- coding: utf-8 -*-
# @Date     : 2020-03-23
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991


a=r'(\$\w+\((?>[^()]+|(?R))*\))'

import time
start_time = time.time()
print(1111)
end_time = time.time()
print(end_time - start_time)


import regex

s = '$a1($a2($a3($a99("dsd")),a4,$a5(1,2),a6),a7,$a8($a9()))'
keyword_regex = regex.compile(r'(\$\w+\((?>[^()]+|(?R))*\))')
keyword_list = regex.findall(keyword_regex, s)
print(keyword_list)