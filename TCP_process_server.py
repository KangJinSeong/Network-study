'''
Date: 2022.06.07
Title: 
By: Kang Jin Seong
'''
import socket
# 숫자에 대한 영어 사전
table = {'1':'one', '2':'two', '3':'three','4':'four','5':'five'}

s = socket.socket() # AF_INET, SOCK_STREAM
address = ('', 2500)
s.bind(address)
s.listen(1)
print('waiting...')
c_socket, c_addr = s.accept()
print('Connection:', c_addr)

while True:
    data = c_socket.recv(1024).decode() # 요청 수신
    try:
        resp = table[data]  # 데이터를 key로 사용하여 Value를 가져온다.
    except:
        c_socket.sendall('Try again'.encode())  # 오류가 있을때
    else:
        c_socket.sendall(resp.encode()) # 변환값을 전송

