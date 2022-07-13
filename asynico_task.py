'''
Date: 2022.06.15
Title: 
By: Kang Jin Seong
'''
#Python 3.7이상에서 실행
import asyncio
import time

async def say(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    #태스크 생성 및 실행
    task1 = asyncio.create_task(say(1,'Hello'))
    task2 = asyncio.create_task(say(2,'World'))
    print(f"Started at {time.strftime('%X')}")

    await task1 # task1 완료 대기
    await task2 # task2 완료 대기

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())