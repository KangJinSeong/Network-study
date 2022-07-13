'''
Date: 2022.06.17
Title: 
By: Kang Jin Seong
'''
#loop.create_server()를 이용한 TCP 에코 클라이언트 프로그램

import asyncio

#이벤트 콜백을 정의하는 protocol 클래스
class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost, loop):
        self.message = message
        self.loop = loop    #이벤트 루프
        self.on_con_lost = on_con_lost  #퓨처 객체, 콜백의 완료 여부 확인

    def connection_made(self, transport):
        while True:
            transport.write(self.message.encode())  #메세지 전송
            print(f"Data sent: {self.message!r}")

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))
    
    def connection_lost(self, exc):
        print("The server closed the connection")
        #연결이 종료되면 퓨처를 완료로 설정하고 True 변환
        self.on_con_lost.set_result(True)
    
async def say(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    #저수준 API를 사용하기 위해 현재 이벤트 루프를 가져온다.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()  #퓨처 생성
    message = 'Hello world'

    transport, protocol = await loop.create_connection(lambda: EchoServerProtocol(message,
    on_con_lost, loop), '',2500)

    # protocol이 연결 종료를 알릴 때까지 대기한 후에 연결을 닫는다.
    try:
        await on_con_lost   #퓨처 완료 대기
    finally:
        transport.close()   #연결을 닫는다.

asyncio.run(main()) 