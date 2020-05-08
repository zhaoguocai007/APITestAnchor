# -*- coding: utf-8 -*-
# @Date     : 2020-04-23
# @Author   : zhaoguocai
# @QQ       : 30516864
# @使用交流群 :685096991

import datetime, json
from src.common.log_cat import Log
from src.common.customized_exception import InvaildHttpMethod
import requests
import urllib3

urllib3.disable_warnings()


class RequestBean:
    def __init__(self):
        self.method = ""
        self.url = ""
        self.request_data = ""
        self.content_type = ""
        self.files = ""
        self.query_param = {}
        self.json = ""
        self.headers = {}
        self.cookies = {}

class ResponseBean:
    def __init__(self):
        self.response_data = ""
        self.duration_ms = 0


class HttpClient:
    __defined_http_methods = ("GET", "POST", "DELETE", "HEAD", "PUT", "PEATCH") #定义目前支持的http方法，后续支持新增

    def __init__(self):
        self.session_client = requests.session()
        self.request_bean = RequestBean()
        self.response_bean = ResponseBean()

    def __check_http_medthod(self, method):
        if method in HttpClient.__defined_http_methods:
            return True
        else:
            return False

    def get_request_bean(self):
        return self.request_bean

    def get_response_bean(self):
        return self.response_bean

    def request(self, url, method, params_dict=None, data=None, files=None, header_dict=None, cookies_dict=None):

        if not self.__check_http_medthod(method):
            raise InvaildHttpMethod

        # record
        self.request_bean.method = method
        self.request_bean.url = url
        self.request_bean.request_data = json.dumps(data, ensure_ascii=False)
        self.request_bean.query_param = params_dict
        Log.info("Host:{} , 请求方法类型:{}".format(url, method))

        if isinstance(data, str):
            req_record.json = json  # data 是字符串时，意味着是json
        req_record.data = data  # data 是字典类型则提交是form表单，data是json字符串类型提交的是json
        if data is not None:
            if isinstance(data, dict):
                Log.info("请求数据:{}".format(data))
            else:
                Log.info("请求数据:{}".format(data.decode("utf-8")))
        req_record.param = params_dict
        if params_dict is not None:
            Log.info("请求查询数据:{}".format(params_dict))

        req_record.files = files
        req_record.cookies = cookies_dict
        req_record.headers = header_dict
        self.request_record = req_record

        start_time = datetime.datetime.now()
        response = self.session_client.request(url=url,
                                               method=method,
                                               params=params_dict,
                                               data=data,
                                               files=files,
                                               headers=header_dict,
                                               cookies=cookies_dict,
                                               verify=False)

        end_time = datetime.datetime.now()
        time_sep = (end_time - start_time).microseconds / 1000
        Log.info("执行接口消耗时间{}ms".format(str(time_sep)))
        # 记录response
        resp_record.duration = time_sep
        resp_record.response = response
        Log.info("返回数据:{}".format(response.text))

        self.response_record = resp_record

# testing
# c = HttpClient()
# url = "http://yfyb-fusion-grab-fusion-edge.test.za-tech.net/mall/goods/queryChannelGoodsList"
#
#
# header = {"token": "3d7c3e837cdb64f8086b69f10770bf01", 'channelId': '103434503260602369', 'Content-Type': 'application/json'}
# json1 ='{"pageIndex":1,"pageSize":10,"statusList":[1],"categoryList":null}'
#
# import json
# c.request(url=url, method="POST", header_dict=header,data=json1)
# x = c.get_request_record()
# print(x.headers)
# y = c.get_response_record()
# print(y.duration)
# print(y.response.text)
#
# r = requests.post(url=url,json=json,headers=header)
# print(r.text)
