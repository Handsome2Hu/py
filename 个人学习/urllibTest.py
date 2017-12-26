
#coding=utf-8
import urllib
import urllib.request
import urllib.parse

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_urllib2():
    response = urllib.request.urlopen(URL_IP)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response  Body:')
    print(''.join([str(line) for line in response.readlines()]))
    
def use_params_urllib2():
    params = urllib.parse.urlencode({'param1':'hello','param2':'你好','param3':'test'})
    print('Reuqest Params:')
    print(params)
    response = urllib.request.urlopen('?'.join([URL_GET,'%s'])%params)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Status Code:')
    print(response.getcode())
    print('>>>Response  Body:')
    print(''.join([str(line) for line in response.readlines()]))    

if __name__ == '__main__':
    print ('>>>Use simple urllib2:')
    use_params_urllib2()
    
    