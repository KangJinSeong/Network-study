'''
Date: 2022.06.20
Title: 
By: Kang Jin Seong
'''

#다중 메시지 발행 프로그램

import paho.mqtt.publish as publish

broker = "test.mosquitto.org"  

mgs = [{'topic':"mqtt/multiple", 'payload':"Hello"},("mqtt/multiple", "World", 0, False)]
publish.multiple(mgs, hostname= broker)