#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from weather import *
from tkinter import messagebox
import re

class GUI():
    def __init__(self):
        # 创立窗口
        self.windows=Tk()
        self.windows.title ("天气预报")
        self.windows.resizable (0, 0)  # 阻止Python GUI的大小调整

        # 页面的布局
        self.frmLT = Frame (width=700, height=150)  # 城市搜索板块
        self.frmLC = Frame (width=700, height=500)  # 今日天气显示板块
        self.frmLB = Frame (width=700, height=400)  # 未来三日天气显示板块

        # 将获取的天气信息的变量储存器

        # 第1天
        self.d00 = StringVar ()
        self.d01 = StringVar ()
        self.d02 = StringVar ()
        self.d03 = StringVar ()
        # 第2天
        self.d10 = StringVar ()
        self.d11 = StringVar ()
        self.d12 = StringVar ()
        self.d13 = StringVar ()
        # 第3天
        self.d20 = StringVar ()
        self.d21 = StringVar ()
        self.d22 = StringVar ()
        self.d23 = StringVar ()
        # 第4天
        self.d30 = StringVar ()
        self.d31 = StringVar ()
        self.d32 = StringVar ()
        self.d33 = StringVar ()

        self.PM25 = StringVar ()
        self.cityname = StringVar ()
        # 储存经GUI处理后weather传过来的数据
        self.weather_data = []

        # 初次设定为“北京”,并返回页面结果
        self.cityname.set ("北京")
        self.response = Weather (self.cityname.get ())
        self.response.parse_page ()
        self.set_weather_data ()

    def grid_widget(self):
        self.frmLT.grid (row=0, column=0, columnspan=10, rowspan=1)
        self.frmLC.grid (row=1, column=0, columnspan=10, rowspan=5)
        self.frmLB.grid (row=6, column=0, columnspan=10, rowspan=4)

        Label (self.frmLT, text="城市(区)名", font='Helvetica -18').grid (row=0, column=1)
        city = Entry (self.frmLT, bd=1, textvariable=self.cityname, font='Gotham -18 bold')
        city.grid (row=0, column=2)
        Button (self.frmLT, text="查询", command=self.set_weather).grid (row=0, column=3)

        # GUI界面中各个数据的摆放方式

        # 当前天气状况
        Label (self.frmLC, textvariable=self.d00, font='Gotham -64 bold').grid (row=1, column=1, columnspan=2)
        Label (self.frmLC, textvariable=self.d01, font='Gotham -36 bold').grid (row=2, column=1, columnspan=2)
        Label (self.frmLC, textvariable=self.d02, font='Gotham -36 bold').grid (row=3, column=1, columnspan=2)
        Label (self.frmLC, textvariable=self.PM25, font='Gotham -26 bold').grid (row=4, column=1, columnspan=2)
        Label (self.frmLC, textvariable=self.d03, font='Helvetica -20 bold').grid (row=5, column=1, columnspan=2)
        Label (self.frmLC, textvariable="  ", font='Helvetica -20 bold').grid (row=6, column=1, columnspan=2)

        # 明日的天气
        Label (self.frmLB, textvariable=self.d10, font='Gotham -26 bold').grid (row=7, column=0, columnspan=2)
        Label (self.frmLB, textvariable=self.d11, font='Gotham -26 bold').grid (row=8, column=0, columnspan=2)
        Label (self.frmLB, textvariable=self.d12, font='Gotham -26 bold').grid (row=9, column=0, columnspan=2)
        Label (self.frmLB, textvariable=self.d13, font='Helvetica -26 bold').grid (row=10, column=0, columnspan=2)

        # 后天的天气
        Label (self.frmLB, textvariable=self.d20, font='Gotham -26 bold').grid (row=7, column=4, columnspan=2)
        Label (self.frmLB, textvariable=self.d21, font='Gotham -26 bold').grid (row=8, column=4, columnspan=2)
        Label (self.frmLB, textvariable=self.d22, font='Gotham -26 bold').grid (row=9, column=4, columnspan=2)
        Label (self.frmLB, textvariable=self.d23, font='Helvetica -26 bold').grid (row=10, column=4, columnspan=2)

        # 大后天的天气
        Label (self.frmLB, textvariable=self.d30, font='Gotham -26 bold').grid (row=7, column=8, columnspan=2)
        Label (self.frmLB, textvariable=self.d31, font='Gotham -26 bold').grid (row=8, column=8, columnspan=2)
        Label (self.frmLB, textvariable=self.d32, font='Gotham -26 bold').grid (row=9, column=8, columnspan=2)
        Label (self.frmLB, textvariable=self.d33, font='Helvetica -26 bold').grid (row=10, column=8, columnspan=2)

    # 查询按钮事件响应函数
    def set_weather(self):
        self.response.change_data (self.cityname.get ())
        if self.response.error_code == 0:  # 判断是否得到有效的信息
            self.set_weather_data ()
        else:
            messagebox.showinfo (title='Error', message='请输入正确的城市名称！')

    # 回车事件响应函数
    def set_weather1(self,event):
        self.response.change_data (self.cityname.get ())
        self.response.parse_page ()
        if self.response.error_code == 0:
            self.set_weather_data ()
        else:
            messagebox.showinfo (title='Error', message='请输入正确的城市名称！')

    # 设置数据函数
    def set_weather_data(self):
        if self.response.get_page () != None:
            del self.weather_data[0:16]  # 将原先存的数据删除一次
            for i in range (0, 4):  # 将得到数据读入weather_data
                self.weather_data.append (self.response.data[i]['date'])
                self.weather_data.append (self.response.data[i]['weather'])
                self.weather_data.append (self.response.data[i]['wind'])
                self.weather_data.append (self.response.data[i]['temperature'])

            # 正则表达式匹配得到数据中的温度，考虑负度数的情况
            if re.search ('-\d*℃', self.weather_data[0]) == None:
                self.weather_data[0] = re.search ('\d*℃', self.weather_data[0]).group ()
            else:
                self.weather_data[0] = re.search ('-\d*℃', self.weather_data[0]).group ()

            # 将得到的数据与GUI中Label的textvarible值更新
            self.d00.set (self.weather_data[0])
            self.d01.set ("天气：" + self.weather_data[1])
            self.d02.set ("风向：" + self.weather_data[2])
            self.d03.set ("今日温度范围：" + self.weather_data[3])
            self.d10.set ("" + self.weather_data[4])
            self.d11.set (self.weather_data[5])
            self.d12.set (self.weather_data[6])
            self.d13.set (self.weather_data[7])
            self.d20.set (self.weather_data[8])
            self.d21.set (self.weather_data[9])
            self.d22.set (self.weather_data[10])
            self.d23.set (self.weather_data[11])
            self.d30.set (self.weather_data[12])
            self.d31.set (self.weather_data[13])
            self.d32.set (self.weather_data[14])
            self.d33.set (self.weather_data[15])

            # PM2.5的特殊情况处理，将没有监测点的城市信息提示出来
            if self.response.data[0]['pm25'] == "":
                self.PM25.set ("PM2.5: 无监测点！")
            else:
                self.PM25.set ("PM2.5: " + self.response.data[0]['pm25'])


