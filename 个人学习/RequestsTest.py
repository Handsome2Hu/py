#coding=utf-8
'''
#import urllib
#import urllib.request
#import urllib.parse
import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print('>>>Response Headers:')
    print(response.headers)
    print('>>>Response  Body:')
    print(response.text)

def use_params_requests():
    params = {'param1':'hello','param2':'你好','param3':'test'}
    response = requests.get(URL_GET,params=params)
    print('>>>Response Headers:')
    print(response.headers)
    print('>>>Status Code:')
    print(response.status_code)
    print('>>>Status Code reason:')
    print(response.reason)
    print('>>>Response  Body:')
    #print(response.json)    
    print(response.text) 

if __name__ == '__main__':
    print ('>>>Use simple urllib2:')
    use_params_requests()

'''
'''
内置高阶函数
一：
def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

二：

例如，编写一个f函数，接收x和y，返回x和y的和：

def f(x, y):
    return x + y

调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：

先计算头两个元素：f(1, 3)，结果为4；
再把结果和第3个元素计算：f(4, 5)，结果为9；
再把结果和第4个元素计算：f(9, 7)，结果为16；
再把结果和第5个元素计算：f(16, 9)，结果为25；
由于没有更多的元素了，计算结束，返回结果25。

三：
filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
例如，要从一个list [1, 4, 6, 7, 9, 12, 17]中删除偶数，保留奇数，首先，要编写一个判断奇数的函数：

def is_odd(x):
    return x % 2 == 1

然后，利用filter()过滤掉偶数：

filter(is_odd, [1, 4, 6, 7, 9, 12, 17])

结果：[1, 7, 9, 17]

'''

import json
import requests
from requests import exceptions
URL = 'https://api.github.com'

def build_url(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_url('user/emails'),auth=('imoocdemo','imoocdemo123'))
    #print(response.text)
    print(better_print(response.text))
    
def params_request():
    response = requests.get(build_url('users'),params={'since':11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)

def json_request():
    response = requests.patch(build_url('user'),auth=('imoocdemo','imoocdemo123'),json={'name':'baby'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def timeout_request():
    try:
        response = requests.get(build_url('user/emails'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        print(response.text)
        print(response.status_code)
        
def hard_requests():
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'hys1.3.1'}
    req = Request('GET',build_url('user/emails'),auth=('imoocdemo','imoocdemo123'),headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)
    
    resp = s.send(prepped,timeout=10)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)

def error_request():
    response = requests.get('http://api.github.com')
    print(response.history)
    
def download_image():
    URL = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1508684596337&di=85cabd3af35d7b47e65de12719c7564a&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F16%2F42%2F96%2F56e58PICAu9_1024.jpg'
    response = requests.get(URL,stream=True)
    print(response.status_code,response.reason)
    print(response.content)
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

def download_image_improved():
    URL = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1508684596337&di=85cabd3af35d7b47e65de12719c7564a&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F16%2F42%2F96%2F56e58PICAu9_1024.jpg'
    response = requests.get(URL,stream=True)    
    from contextlib import closing
    with closing(requests.get(URL,stream=True)) as response:
        with open('demo1.jpg','wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)        
    
if __name__ == '__main__':
    download_image_improved()