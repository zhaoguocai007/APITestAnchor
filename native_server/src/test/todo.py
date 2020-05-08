# -*- coding: utf-8 -*-
# @Date     : 2020-03-23
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991


# 添加缓存模型 pip install cacheout

import importlib.util
import importlib,sys,pkgutil,os
p="D:\\develop\\python"
sys.path.append(p)
keyword_fun_name="cc"
package_obj = importlib.import_module("k_test")
package_name = package_obj.__path__
print(package_name)
child_modules = pkgutil.iter_modules(package_name)

for mod in child_modules:
    mod_name = "k_test.{}".format(mod.name)
    print(mod_name)
    print(mod.ispkg)
    print(mod.module_finder.path)
    print("---")
    sys.path.append(mod.module_finder.path)
    views_item_object = importlib.import_module(mod_name)
    try:
        func = getattr(views_item_object, keyword_fun_name)
        break
    except AttributeError:
        continue
    except Exception:
        continue

print(func())
print("------")

print(sys.path)