#coding=utf-8

import sys
import string
import re
reload(sys)
sys.setdefaultencoding('utf-8')

f = open(r'Source.Version.h','r+')
lines = f.readlines()
version = ''
for line in lines:
    tmp = re.split('\s+',line)
    if len(tmp) > 2 and tmp[1] == 'VER_UMS_HQ_REVISION':
        version = tmp[2]
f.seek(0)
f.close()

ff = open(r'resource.h','r+')
lines = ff.readlines()
data = []
for line1 in lines:
    #tmp = re.split('\s+',line1)
    #if len(tmp) >= 2 and tmp[0] == 'FILEVERSION':
    #    strtmp = tmp[0] + tmp[1] + ' ' + version + '\n'
    #    data.append(strtmp)
    #else:
        data.append(line1)
        data.append('\n')
ff.seek(0)
ff.writelines(data)
ff.close
