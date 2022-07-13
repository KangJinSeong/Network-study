'''
Date: 2022.06.09
Title: 
By: Kang Jin Seong
'''

#프레임 생성과 파싱 프로그램

import socket
import capsule

SIZE = 5    # 분할 크기
sock = socket.socket()
sock.connect(('30.0.1.16',2500))

HEAD = 0x05 #시작 문자
addr = 1    # 상대방 주소
seqNO = 1   # 순서 번호
frame_seq = ''
msg = 'hello world'
print("전송 메세지:", msg)
for i in range(0,len(msg), SIZE):    # 5문자씩 분할하여 프레임 구성
    start = i
    frame_seq += capsule.frame(HEAD, addr, seqNO, msg[start:start+SIZE])
    start += SIZE
    seqNO += 1

sock.sendall(frame_seq.encode())    # 프레임 전송
msg = sock.recv(2048).decode()  #프레임 다시 수신
print("수신 프레임:", msg)
r_frame = msg.split(chr(HEAD))  #프레임 분할
del r_frame[0]

p_msg = ''
for fr in r_frame:
    p_msg += fr[10:(11+int(fr[6:10]))]  #메세지 복원
print('복원 메세지:', p_msg)
sock.close()
