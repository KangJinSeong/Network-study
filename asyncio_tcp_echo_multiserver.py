'''
Date: 2022.06.17
Title: 
By: Kang Jin Seong
'''
# 다수의 클라이언트를 반복 서비스하는 에코 서버 프로그램
# start_server() 사용

import asyncio

# 연결되면 실행되는 코루틴
# (reader, writer)는 이벤트 루프가 전달

async def handle_echo(reader, writer):
    while True: #연결된 클라이언트를 계속 서비스한다.
        data = await reader.read(100)   #넌블록킹으로 동작하므로 무족건 리턴됨

        if data:    # 수신데이터가 있으면
            message = data.decode()
            addr = writer.get_extra_info('peername')    # 상대방 주소
            print("Received %r from %r" %(message, addr))

            print("Send: %r" %message)
            writer.write(data)  #메세지 송신
            await writer.drain()    #모두 송신 될때까지 대기

svr = ''
port = 2500
loop = asyncio.get_event_loop()

#클라이언트가 연결되면 handle_echo callback이 실행된다
coro = asyncio.start_server(handle_echo, svr, port, loop = loop)
server = loop.run_until_complete(coro)  #코루틴이 완료될 때까지 기다린다.
# 서버 주소를 읽어 표시한다.
print("Serving on {}".format(server.sockets[0].getsockname()))

try:
    loop.run_forever()  #계속 연결 서비스
except KeyboardInterrupt:
    pass

#서버 객체를 닫는다.
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()