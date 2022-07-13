'''
Date: 2022.06.16
Title: 
By: Kang Jin Seong
'''
#open_connection()을 이용한 TCP  클라이언트 프로그램

import asyncio

async def tcp_echo_client(message, loop):
    #소켓을 생성하고 연결하는 코루틴
    reader, writer = await asyncio.open_connection('', 2500, loop = loop)

    #데이터 송신
    print('송신: {!r}'.format(message))
    writer.write(message.encode())  #코루틴이 아니므로 동기식 전송

    data = await reader.read(100)   #메시지 수신(코루틴)
    print('수신: {!r}'.format(data.decode()))

    print('연결 종료')
    writer.close()

message = 'Hello Server!'
loop = asyncio.get_event_loop()

#이벤트 루프에서 코루틴 실행
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()