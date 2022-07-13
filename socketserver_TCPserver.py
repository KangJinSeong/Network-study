'''
Date: 2022.06.14
Title: 
By: Kang Jin Seong
'''

# socketserver 모듈을 이용한 TCP 에코 서버 프로그램
import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):   #데이터가 수신되면 한 번만 실행
        # self.request는 클라이언트와 연결된 소켓
        self.data = self.request.recv(1024).strip()
        print(("{} wrote:".format(self.client_address[0])))
        print((self.data))
        # 수신 문자 반송
        self.request.sendall(self.data.lower())

if __name__ == "__main__":
    host, port = '', 2500
    # 서버 생성
    server = socketserver.TCPServer((host,port), TCPHandler)
    #서버 실행
    server.serve_forever()