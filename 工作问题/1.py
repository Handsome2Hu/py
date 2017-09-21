#coding=utf-16

import string
import re
import codecs

f = codecs.open('Source.Version.h','r+','utf-8')
lines = f.readlines()
version = ''
for line in lines:
    tmp = re.split('\s+',line)
    if len(tmp) > 2 and tmp[1] == 'VER_UMS_HQ_REVISION':
        version = tmp[2]
f.seek(0)
f.close()

ff = codecs.open("QU2D_Main.rc","r+","utf-16")
lines = ff.readlines()
data = []
for line1 in lines:
    tmp = re.split('\s+',line1)
    if len(tmp) >= 2 and (tmp[1] == 'FILEVERSION' or tmp[1] =='PRODUCTVERSION'):
        strtmp = tmp[0] +' ' + tmp[1] +' ' + version +  "\r\n"
        data.append(strtmp)
    else:
        data.append(line1)
ff.seek(0)
ff.writelines(data)
ff.close()
