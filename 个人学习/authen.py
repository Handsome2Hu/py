#coding=utf-8
import requests
import base64
BASE_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL,end_point])

def basic_auth():
    response = requests.get(construct_url('user'),auth=('imoocdemo','imoocdemo123'))
    print(response.text)
    print(response.request.headers)
    
    #
    print(base64.b64decode('aW1vb2NkZW1vOmltb29jZGVtbzEyMw=='))
    
basic_auth()