"""
TiCLE (pico2w)에서 실행할 프로그램

1. 기본 구조
    MQTT Broker ---> Internet ---> MQTT clinet --> HW control
                                                                |    
2. Wifi와 MQTT 클라이언트 라이브러리는 TiCLE 초기화(init) 과정에서 설치됨됨
"""

import utools
import ticle
from wifi import Wifi
from umqtt.robust2 import MQTTClient
import time

#-----------------------------------------------------------
# TiCLE Wi-Fi를 인터넷이 가능한 AP에 연결합니다.
ip = Wifi.connect_ap("", "")  # AP 이름과, 비밀번호를 변경해 주세요.
if ip:
    print(f"IP is {ip}")
else:
    print("Failed!!!")
    raise SystemExit(-1)
#-----------------------------------------------------------

#-----------------------------------------------------------
# MQTT 서버로부터 구독할 토픽을 정의합니다.
TOPIC_IOT_ACTION = "pbl/iot/action/+"
TOPIC_IOT_ACTION_LIGHT = "pbl/iot/action/light"
TOPIC_IOT_ACTION_MOVING = "pbl/iot/action/moving"
TOPIC_IOT_ACTION_AUDIO = "pbl/iot/action/audio"
#-----------------------------------------------------------

# 객체 생성
pl = ticle.PixelLed(7, 10)  # Pin 7, Quantity: 10
servo = ticle.ServoMotor(6, 50)  # Pin 6
cmqtt = MQTTClient(client_id="NamE12q", server="mqtt.eclipseprojects.io")  # 고유한 이름(무작위)로 변경해 주세요

# 주기 시간 검사 함수 정의 (단위는 밀리초)
interval_20 = utools.intervalChecker(20)
interval_1000 = utools.intervalChecker(1000)

# 명령어 및 옵션
global command
command = None
global option
option = None

#-----------------------------------------------------------
# 구독한 토픽이 수신될 때 호출될 콜백 함수 정의
def on_message(topic, msg, retained, duplicate):
    topic = topic.decode()
    msg = msg.decode()
    print(msg)

    global command
    global option

    if topic == TOPIC_IOT_ACTION_LIGHT:
        command = "light"
        option = int(msg)
    elif topic == TOPIC_IOT_ACTION_MOVING:
        command = "moving"
        option = int(msg)
    elif topic == TOPIC_IOT_ACTION_AUDIO:
        if msg == 'up':
            pass
        elif msg == 'down':
            pass
        elif msg == 'prev':
            pass
        elif msg == 'next':
            pass
    else:
        print(f">>>UNKNOWN<< topic: {topic}, message: {msg}")

#-----------------------------------------------------------
# 주변장치 제어 코드
global servo_angle
servo_angle = 0
global servo_oppset
servo_oppset = 1

def act():
    global command
    global option
    global servo_angle
    global servo_oppset
    if command is not None:
        if command == "light":
            if option <= 100:
                val = int(255/100*option)
                pl.on(list([val]*3))
        elif command == "moving":
            servo.angle(option)

#-----------------------------------------------------------
# 아두이노와 같운 프로세싱 구조 사용
# 프로그램이 처음 실행될 때 수행할 작업 정의
def setup():
    print("Press 'Ctrl+C' to quit")
    
    cmqtt.connect()
    cmqtt.set_callback(on_message)
    cmqtt.subscribe(TOPIC_IOT_ACTION)

# 프로그램이 반복적으로 수행할 작업 정의 (주기 검사를 통해 주기 시간 단위로 수행)
def loop():           
    if interval_20: # MQTT 서버로부터 토픽 메시지 수신 처리
        cmqtt.check_msg()
        act()
             
    if interval_1000():
        cmqtt.ping()  # MQTT 서버와의 연결 유지

# 프로그램이 종료할 때 수행할 작업 정의
def cleanup():
    servo.angle(90)
    pl.off()
    print("Good-bye!!!")
#-----------------------------------------------------------

if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
