'''
Date: 2022.06.07
Title: 
By: Kang Jin Seong
'''
import MyTCPServer as mt # 사용자 정의 모듈을 불러온다
import sys

port = 2500

if len(sys.argv) > 1:   # 명령 실행시 포트를 지정하면 지정 포트 사용
    port - int(eval(sys.argv[1]))

s_sock = mt.TCPServer(port) # 서버 소켓 생성
c_sock, addr = s_sock.Accept()  # 클라이언트 연결

while True:
    print('Connected by:', addr[0], addr[1])    # 클라이언트 주소와 포트
    data = c_sock.recv(1024)
    if not data:    #데이터가 없으면 종료
        break
    print('Received message :', data.decode())
    c_sock.sendall(data)    # 데이터 재전송

c_sock.close()