'''
Date: 2022.06.17
Title: 
By: Kang Jin Seong
'''
#loop.create_server()를 이용한 TCP 에코 서버 프로그램
# 연결을 한번만 서비스한다.

import asyncio

#이벤트 콜백을 정의하는 protocol 클래스
class EchoServerProtocol(asyncio.Protocol):
    # 연결이 성공하면 호출되는 콜백
    #transport는 연결 소켓을 나타내고 이벤트 루프에서 전달된다.
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print(f"Connection from {peername}")
        self.transport = transport  #소켓

    #데이터를 수시하면 호출되는 콜백
    # data(수신된데이터)는 이벤트 루프에서 전달된다.
    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        self.transport.write(data)  #데이터 송신
        print("Close the client socket")
        # self.transport.close()  # 연속 서비스를 원하면 이 문장 삭제

async def main():
    #저수준 API를 사용하기 위해 현재 이벤트 루프를 가져온다.
    loop = asyncio.get_running_loop()

    #서버 객체 생성 및 실행 예약
    server = await loop.create_server(lambda: EchoServerProtocol(), '', 2500)

    #서버 실행
    async with server:
        await server.serve_forever()

asyncio.run(main()) 