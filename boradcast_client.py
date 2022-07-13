'''
Date: 2022.06.10
Title: 
By: Kang Jin Seong
'''
# 브로드 캐스트 송신 프로그램

from socket import *

addr = ('<broadcast>', 10000)   # 브로드캐스트 주소

#브로드캐스팅을 위한 소켓 설정

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)   #브로드캐스트 옵셜 설정

while True:
    smsg = input('Broadcast Message:')
    s.sendto(smsg.encode(), (addr))  #브로드캐스팅 메세지 전송
