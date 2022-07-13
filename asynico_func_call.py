'''
Date: 2022.06.14
Title: 
By: Kang Jin Seong
'''
# 일반 함수를 비동기로 실행하면 동시처리가 가능하다.

import asyncio as aio
import time


async def coro1():  #5초마다 출력
    i = 1
    while True:
        print(i)
        i = i + 1
        await aio.sleep(5)

async def coro2(loop):  #키보드 입력을 다시 출력
    while True:
        msg = await loop.run_in_executor(None, input, ':')
        print('->', msg)

async def main():
    loop = aio.get_event_loop()
    task1 = loop.create_task(coro1())
    task2 = loop.create_task(coro2(loop))

    await task1
    await task2

aio.run(main())