'''
Date: 2022.06.03
Title: 
By: Kang Jin Seong
'''

import ipaddress as ipa

NETWORK = ['192.168.0.0/24']

for n in NETWORK:
    net = ipa.ip_network(n) # 네트워크 주소 객체 생성
    print('{!r}'.format(net))
    for i, ip in zip(range(10), net):
        print(i, ":", ip)
    print()