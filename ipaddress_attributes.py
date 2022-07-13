'''
Date: 2022.06.03
Title: 
By: Kang Jin Seong
'''

# impaddress 모듈의 속성
import binascii
import ipaddress as ipa

# Addresses = ['192.168.0.144']

# for ipaddr in Addresses:
#     addr = ipa.ip_address(ipaddr)
#     print(f'IP address: {addr!r}')
#     print('IP version:', addr.version)
#     print('Packed addr:', binascii.hexlify(addr.packed))
#     print('Integer addr:', int(addr))
#     print('Is private:', addr.is_private)
#     print()

# # 네트워크 주소갹체에서 사용 가능한 호스트 주소를 반복적으로 알아보려면 다음과 같이 반복문 사용

# net4 = ipa.ip_network('192.168.0.0/24')
# for x in net4.hosts():
#     print(x)

'''
네트워크 주소 객체를 만들면 객체는 네트워크에 포함된 호스트 주소를 포함하고 있다.
'''

net = ipa.ip_network('192.168.0.0/30')
print(type(net))
print(list(net.hosts()))