'''
Date: 2022.06.03
Title: 
By: Kang Jin Seong
'''

import struct
import socket
import time

conn = ('30.0.1.16', 9000)  #라즈베리파이
# socket(family, type, proto = 0)
# family : AF(address family), AF_INET: IPV4
# type : TCP 소켓, SOCK_STREAM
# proto : Can 소켓 일반적으로 디폴트 0 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(conn)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# data = 1
# buf = struct.pack("i", data)
# client_socket.sendall(buf)

while True:
    r = client_socket.recv(1024)
    if not r:
        break
    # print(r)
    for i in range(int(len(r)/4)):
        print(r)
        b_data = b''
        b_data += r[i*4:(i*4)+4]
        print(struct.unpack('i',b_data))
    # time.sleep(1)

    
client_socket.close()