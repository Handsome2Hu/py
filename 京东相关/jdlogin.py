#coding=utf-8
import requests
from bs4 import BeautifulSoup
import time
import os
import random
import re
import json

def login_by_QR():
    #模拟头
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                        'ContentType': 'text/html; charset=utf-8',
                            'Accept-Encoding':'gzip, deflate, sdch',
                            'Accept-Language':'zh-CN,zh;q=0.8',
                            'Connection' : 'keep-alive',
    }
    
    #几个登录url
    urls = (
                'https://passport.jd.com/new/login.aspx',
                'https://qr.m.jd.com/show',
                'https://qr.m.jd.com/check',
                'https://passport.jd.com/uc/qrCodeTicketValidation'
            )
    
    session = requests.session()
    #获取登录界面的cookies
    response = session.get(urls[0],headers=headers)
    if response.status_code != requests.codes.OK:
        print("获取登录页面失败：%s" % response.status_code)
        return
    cookies = {}
    for k,v in response.cookies.items():
        cookies[k]=v
    
    #获取二维码
    response = session.get(
        urls[1],
        headers=headers,
        cookies=cookies,
        params = {'appid': 133,
                'size': 147,
                't': (time.time() * 1000)
                                     }
                           )
    for k,v in response.cookies.items():
        cookies[k]=v
    
    #保存二维码图片
    image_file = 'qr.png'
    with open (image_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    
    ## scan QR code with phone
    os.system('start ' + image_file)
    
    #等待扫二维码登录
    headers['Host'] = 'qr.m.jd.com' 
    headers['Referer'] = 'https://passport.jd.com/new/login.aspx'
    
    qr_ticket = None
    retry_times = 100 #等待时间
    
    while retry_times:
        retry_times -= 1
        response = session.get(urls[2],headers=headers,cookies=cookies,params = {'callback':'jQuery%u'%random.randint(100000,999999),'appid':133,'token':cookies['wlfstk_smdl'],'_':(time.time()*1000)})
        
        if response.status_code != requests.codes.OK:
            continue
        
        rs = json.loads(re.search(r'\{[\s\S]*\}',response.text).group())
        if rs['code'] == 200:
            print('{} : {}'.format(rs['code'],rs['ticket']))
            qr_ticket = rs['ticket']
            break
        else:
            print('{} : {}'.format(rs['code'],rs['msg']))
            time.sleep(3)
            
    if not qr_ticket:
        print('二维码登录失败')
        return False
        
        
login_by_QR()