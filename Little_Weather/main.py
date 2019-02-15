#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from GUIMethod import *

# 主函数
if __name__ == '__main__':
    # 创建一个GUI的实例化对象
    app=GUI()
    app.grid_widget()
    # 对回车事件回应
    app.windows.bind ("<Return>", app.set_weather1)
    # 消息机制开始循环
    app.windows.mainloop()