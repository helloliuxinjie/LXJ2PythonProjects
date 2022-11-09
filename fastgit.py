# -*- coding:utf-8 -*-
# @Time    ：2022/11/9 009 14:49
# @Author  ：Liu Xinjie
# @FileName: fastgit.py
# @Software: PyCharm
# @Gmail   ：liuxinjie533@gmail.com
# @AboutMe : SZU, coding just for fun!

"""
我的git用户设置
user.name=helloliuxinjie
user.email=484671483@qq.com
本项目目标旨在实现：将指定目录下的工程提交到github仓库上
仓库的状态：本地新增，git仓库在之前与本地保持一致
"""
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--add", help="add file path or dir", default="./*")
parser.add_argument("--comment", help="comment", default=":fire:update")
args = parser.parse_args()

if __name__ == "__main__":
    os.system("git status")
    # os.system("git add {}".format(args.add))
    # os.system("git commit -m {}".format(args.comment))
    # os.system("git push")
    print("git add {}".format(args.add))
    print("git commit -m {}".format(args.comment))

"""
1.git init 初始在文件夹中生成隐藏的.git 文件
2.git clone target_url 克隆远程仓库
3.git clone -b 分支名 target_url  克隆分支的代码到本地
4.git status 查看状态
5.git add target_file_name 将某个文件存入暂存区
6.git add file_b file_c 将文件b和c存入暂存区
7.git add . 将所有文件提交到暂存区
8.git add -p target_file_name 一个文件分多次提交
9.git config user.name "提交的用户名"
10.git config user.email "邮箱"

git stash -u -k  提交部分文件内容 到仓库 例如本地有3个文件 a b c 只想提交a b到远程仓库 git add a b 然后 git stash -u -k 再然后git commit -m "备注信息" 然后再push push之后 git stash pop 把之前放入堆栈的c拿出来 继续下一波操作
git commit -m "提交的备注信息"   提交到仓库
若已经有若干文件放入仓库，再次提交可以不用git add和git commit -m "备注信息" 这2步， 直接用
git commit -am "备注信息"  将内容放至仓库 也可用git commit -a -m "备注信息"
* git commit中的备注信息尽量完善 养成良好提交习惯 例如 git commit -m "变更(范围)：变更的内容"
git push     将本地仓库代码提交到远端仓库
git pull     从远端仓库中更新本地仓库代码
git clone 远端仓库地址
"""