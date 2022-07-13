'''
Date: 2022.06.09
Title: 
By: Kang Jin Seong
'''

# 메세지를 입력받고 제어필드를 추가하여 프레임을 구성하는 캡슐화 프로그램

def frame(start_ch, addr, seqNo, msg):  # 프레임 구성 함수
    addr = str(addr).zfill(2)   # addr을 문자열로 변환하고 길이가 1이면 앞쪽에 0을채워 2바이트가 되게 한다.
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch) + addr + seqNo + length + msg  #헤더 변환

if __name__ == '__main__':
    start_ch = 0x05 # 시작 문자
    addr =2
    seqNo = 1 #순서 번호

    msg = input('your message :')
    capsule = frame(start_ch, addr, seqNo, msg)
    print(capsule)