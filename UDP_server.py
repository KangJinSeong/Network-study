'''
Date: 2022.06.09
Title: 
By: Kang Jin Seong
'''

import socket

port = 2500
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP 소켓
sock.bind(('',port))
print('수신 대기중')

while True:
    data, addr = sock.recvfrom(BUFFER)  # 데이터와 상대방 종단점 주소 수신
    print('Received message:', data.decode())
    print(addr)
    sock.sendto(data, addr)