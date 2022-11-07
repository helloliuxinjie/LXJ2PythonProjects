# -*- coding: utf-8 -*-
# Author: Liuxinjie
# date：2022年11月7日

"""
本函数功能：
    更新所有python包
    而不用一个一个去点
手动更新包命令：pip install --upgrade packageName
"""

import os  # 导入os模块
command_list = 'pip list'  # 定义pip list命令
command_install = 'pip install '  # 定义pip install 命令前缀
data = os.popen(command_list)  # 返回一个可遍历的包的列表（内容又pip list得到）
info = data.readlines()  # 读取命令行的输出到一个list
# 删除表头信息
del info[0]
del info[0]
for line in info:  #按行遍历
    # 用" "分割每行，列表的第一个就是包名
    package = line.split(" ")[0]
    print("",end="")
    print("\033[1;32;40m%s\033[0m"%("正在检查更新"+package))
    os.system(command_install+package+" --upgrade")
print("更新完毕")

