# -*- coding: utf-8 -*-
# @Date     : 2020-03-18
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991

import regex,re
s = "$sleep($sleep(tt, $str(qwe,$str(0)),ffg,$int(123), tr, $str(ett,rty),er))"
s1 = "$sleep(1,2)"

keyword_regex = regex.compile(r'\$\w+\((?R)*[^()]*\)[^()]*?')
param_list = regex.findall(keyword_regex, s1)
print(param_list)


def rule_execute(self, str_rule_expression: str):
    try:
        keyword_name = re.search(r"^\$(?P<keyword_name>\w+)\(", str_rule_expression).group("keyword_name")
        param = re.search(r"^\$\w+\((?P<param>[\s\S]*)\)$", str_rule_expression).group("param")
    except AttributeError:
        return str_rule_expression

    if param == "":
        return self.keyword_execute(keyword_name, [])
    keyword_regex = regex.compile(r'\$\w+\((?R)*[^()]*\)[^()]*?')
    nested_param_list = regex.findall(keyword_regex, param)
    if len(nested_param_list) == 0:
        return self.keyword_execute(keyword_name, list(map(lambda x: x.strip(), param.split(","))))
    all_param_list = regex.sub(keyword_regex, "$keyword$", param)
    all_param_list = list(map(lambda x: x.strip(), all_param_list.split(",")))

    k = 0
    for key, value in enumerate(all_param_list):
        if value == "$keyword$":
            if keyword_name in self.keep_origin_keyword_list:
                all_param_list[key] = nested_param_list[k]
            else:
                all_param_list[key] = self.rule_execute(nested_param_list[k])
            k += 1

    return self.keyword_execute(keyword_name, all_param_list)