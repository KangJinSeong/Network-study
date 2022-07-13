'''
Date: 2022.06.17
Title: 
By: Kang Jin Seong
'''

# GET request 보내기와 서버 응답 출력 프로그램

from urllib import request

URL = 'https://www.dongyang.ac.kr/' #URL
response = request.urlopen(URL)   # GET request와 서버 응답
print('Response:', response)
print('URL:', response.geturl())    #URL 정보

headers = response.info()   #응답 헤더 정보
print('DATE:', headers['date'])
print('HEADERS:')
print('--------------')
print(headers)

data = response.read().decode('utf-8')  #응답 내용 읽기
print('Length:', len(data))
print('DATA:')
print('--------------')
print(data)