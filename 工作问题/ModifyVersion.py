#coding=utf8

############################################################
#                                                          #
#读取文件中的版本号，写入到rc文件中，达到编译出版本号的程序    #
#                                                          #
############################################################

#使用方法：

#VS 工程属性页面中 配置属性->生成事件->预先生成事件-> 命令行中添加：
#
#SubWCRev.exe "../" "../Template.Source.Version.h" "./Source.Version.h"
#python "../111.py" "$(ProjectDir)$(ProjectName).rc"
#
#SubWCRev.exe 是SVN自带工具，复制文件，并替换文件中的参数
#$WCREV$ 替换为SVN版本号
#运行该py 替换rc文件的版本号
import string
import re
import codecs
import os
import sys
import chardet

filepath = sys.argv[1]


f = codecs.open('Source.Version.h','r+','utf-8')
lines = f.readlines()
version1 = ''
version2 = ''
for line in lines:
    tmp = re.split('\s+',line)
    if len(tmp) > 2 and tmp[1] == 'VER_UMS_HQ_REVISION1':
        version1 = tmp[2]
    if len(tmp) > 2 and tmp[1] == 'VER_UMS_HQ_REVISION2':
        version2 = tmp[2]
f.seek(0)
f.close()


#rc 文件有utf 16 有 ascii，所以先判断文件的编码格式
tt = open(filepath,'rb')
enc = chardet.detect(tt.readline())
tt.seek(0)
tt.close()

if enc['encoding'] == 'ascii':
    ff = codecs.open(filepath,"r+")
else:  
    ff = codecs.open(filepath,"r+",enc['encoding'])

lines = ff.readlines()
data = []
for line1 in lines:
    tmp = re.split('\s+',line1)
    if len(tmp) >= 2 and (tmp[1] == 'FILEVERSION' or tmp[1] =='PRODUCTVERSION'):
        strtmp = tmp[0] +' ' + tmp[1] +' ' + version1 +  '\r\n'
        data.append(strtmp)
    elif len(tmp) >= 3 and (tmp[2] == '"FileVersion",' or tmp[2] =='"ProductVersion",'):
        strtmp = tmp[0] + '            ' + tmp[1] + ' ' +tmp[2] + ' ' + version2 + '\r\n'
        data.append(strtmp)
    else:
        data.append(line1)
ff.seek(0)
ff.writelines(data)
ff.close()
