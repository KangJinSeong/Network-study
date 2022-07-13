'''
Date: 2022.06.22
Title: 
By: Kang Jin Seong
'''

#client 모듈을 이용한 메시지 발행 프로그램

import paho.mqtt.client as paho

broker = "test.mosquitto.org"
port = 1883

#메시지가 성공적으로 발행되면 호출되는 콜백

def on_publish(client, user_data, result):
    print("data published: {} \n")
    pass

client1 = paho.Client() # 클라이언트 객체 생성
client1.on_publish = on_publish # on_publish 속성에 콜백 함수 연결
client1.connect(broker, port)   # 브로커와 연결
ret = client1.publish("mqtt/test", "Hello") #메시지 전송