'''
Date: 2022.06.20
Title: 
By: Kang Jin Seong
'''

#requests 모듈을 이용한 GET request 프로그램

import requests

while True:
    setting = input("LED On? or OFF?:")
    #서버로 GET request 전송
    #라즈베리파이 주소 = 30.0.1.16
    resp = requests.get("http:30.0.1.16/", params={"led": setting})
    print(resp.text)    #라즈베리파이 응답