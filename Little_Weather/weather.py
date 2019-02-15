#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import requests
import json

class Weather():
    # 天气类的构造函数
    def __init__(self,city):
        # 请求的网页
        self.url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak' \
              '=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?.' % city
        # 得到的天气数据
        self.data=[{},{},{},{}]
        # 请求是否成功的标志，0为成功，其他为失败
        self.error_code=0

    # 获取网页数据的函数，获取成功返回获取的网页数据
    def get_page(self):
        rs=requests.get(self.url)
        rs_dict=json.loads(rs.text)
        self.error_code = rs_dict['error']
        return rs_dict

    # 解析网页的函数，将获取到的页面解析并将数据写入data
    def parse_page(self):
        page=self.get_page()
        if self.error_code==0:  # 判断获取的信息是否有误
           results=page['results']
           info_dict = results[0]
           pm25 = info_dict['pm25']
           self.data[0]['pm25']=pm25  # 存入PM2.5
           weather_data = info_dict['weather_data']
           for i in range (0, 4):
               # 取出日期、天气、风级、温度
               self.data[i]['date']=weather_data[i]['date']   # 日期
               self.data[i]['weather']=weather_data[i]['weather'] # 天气
               self.data[i]['wind']= weather_data[i]['wind']   # 风向
               self.data[i]['temperature']= weather_data[i]['temperature']   # 温度范围

    # 改变天气类的函数，将改变的城市接入而改变天气类的信息
    def change_data(self,city):
        self.url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak' \
                   '=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?.' % city
        self.data = [{}, {}, {}, {}]
        self.parse_page()

