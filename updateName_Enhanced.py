#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 07/01/2017

'''
批量修改文件夹名字_加强版(包括子目录)
'''

import os

def renameFiles(cur_dir):
    # 列出某个目录下的文件和文件夹，可以是绝对和相对目录
    files = os.listdir(cur_dir)

    # 切换到这个路径作为工作目录,这句要放在listdir后面
    os.chdir(cur_dir)

    # 递归子文件夹
    for fileName in files:
        if os.path.isdir(fileName):
            renameFiles(fileName)
            # 切换到父目录
            os.chdir(os.pardir)

    # 对这个目录的文件重命名
    for i in range(0, len(files)):
        if files[i].rfind(']') >= 0:
            newName = files[i].split(']')[1]
            # oldPath = filePath + fileName
            # newPath = filePath + newName
            os.rename(files[i], newName)

if __name__ == '__main__':
    renameFiles("/Users/leo/Downloads/[www.zygx8.com-资源共享吧]实战-Vue.js高仿饿了么外卖App 2016最火前端框架/")