'''
Date: 2022.06.07
Title: 
By: Kang Jin Seong
'''

class TCPServer:
    # 소켓을 생성하고 바인드 후 연결 대기
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))  # 소켓과 주소 결합
        self.sock.listen(1) # 연결 대기

    #연결을 허용하고 클라이언트 소켓과 주소 반환
    def Accept(self):   # 연결 수락
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr

if __name__ == '__main__':
    sock = TCPServer(2500) 
    c, addr = sock.Accept()
    print('수신 메세지:', c.recv(1024).decode())
    msg = "Hello client"
    c.send(msg.encode())
    c.close()
