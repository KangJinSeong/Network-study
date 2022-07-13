'''
Date: 2022.06.17
Title: 
By: Kang Jin Seong
'''

from urllib import parse
from urllib import request

data = {'tempeature':'25C', 'humidity':'60%'}   #POST 내용
encoded_data = parse.urlencode(data).encode('utf-8')    #POST query구성(서브URL)

# url = 'https://httpbin.org/post'    #베이스 url
url = 'http://192.168.0.144:8080'
resp = request.urlopen(url, encoded_data)   #POST request 서버 응답
print(resp.read().decode('utf-8'))  #응답 내용 출력