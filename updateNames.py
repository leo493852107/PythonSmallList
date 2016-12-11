#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 09/12/2016

'''
批量修改文件夹名字
'''

from os import rename, listdir

filePath = '/Users/leo/Downloads/实战-打造扛得住的MySQL数据库架构/第1章 实例和故事/'
fileList = listdir(filePath)

for fileName in fileList:
    if fileName.rfind(']') >= 0:
        newName = fileName.split(']')[1]
        oldPath = filePath + fileName
        newPath = filePath + newName
        rename(oldPath, newPath)
