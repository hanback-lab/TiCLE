# AI Speaker

Ticle 보드와 여러 주변 장치를 활용하여 음성인식으로 제어되는 인공지능 스피커를 제작합니다. 이 프로젝트를 완료하면 다음 기능을 얻는 스피커를 제작할 수 있습니다.

- 음성인식을 통한 스피커 기능 제어
- 주변장치 제어
  - WS2812 neopixel 제어
  - Servo 모터를 활용하여 원하는 각도로 스피커 방향 조절
  - 자동으로 곡을 전환하고, 음량을 조절하는 MP3 플레이어 

해당 프로젝트에 사용된 모든 코드는 아래 링크에서 확인할 수 있습니다.

https://github.com/hanback-lab/TiCLE/tree/main/examples/ai-speaker

## 환경 설정

### H/W

아래 리스트에 맞춰 주변장치를 TiCLE DiO 보드에 결선합니다.
- WS2812
  - 빨강 선 : 5V
  - 검정 선 : GND
  - 노랑 선 : GP07
- Servo Motor
  - 빨강 선 : 5V
  - 갈색 선 : GND
  - 주황 선 : GP06
- 오디오 앰프
  - 빨강 선 : 12V
  - 검정 선 : GND
  - 초록 선(Mode) : GP22
  - 하양 선(Scan) : GP26
  - 파랑 선(Down) : GP27
  - 노랑 선(Up) : GP28

### S/W
Host PC에서 VSCode를 실행한 뒤, 터미널을 열어 다음 명령어를 통해 실습에 필요한 패키지들을 설치합니다.

```
pip install SpeechRecognition 
pip install pyaudio 
pip install paho-mqtt
```

## Command를 이용한 Bluetooth 오디오 제어

음성인식을 사용하기에 앞서, TiCLE 장비를 활용해 Command를 이용하여 오디오 앰프를 제어해봅니다. 

### BtAudioAmp

우선, 오디오 앰프를 제어해줄 수 있는 클래스를 작성한 뒤, ticle 파일 시스템에 저장하여 재사용할 수 있도록 파일을 저장해봅니다.

아래 코드를 작성합니다.

```python
# btaudioamp.py

import machine
import utime


class BtAudioAmp:
    """
    Bluetooth Audio Amplifier Control
    """
    SHOT_HOLD = 50
    LONG_HOLD = 1300
    
    def __init__(self, mode, scan, down, up, shot_hold_ms=SHOT_HOLD, long_hold_ms=LONG_HOLD):
        """
        Initialize the Bluetooth Audio Amplifier control pins.
        :param mode: pin number for mode control
        :param scan: pin number for scan control
        :param down: pin number for down/previous control
        :param upn: pin number for up/next control
        """        
        self._mode = machine.Pin(mode, mode=machine.Pin.OUT, value=0)
        self._scan = machine.Pin(scan, mode=machine.Pin.OUT, value=0)
        self._down_prev = machine.Pin(down, mode=machine.Pin.OUT, value=0)
        self._up_next = machine.Pin(up, mode=machine.Pin.OUT, value=0)
        self._shot_hold_ms = shot_hold_ms
        self._long_hold_ms = long_hold_ms
        
    def __press(self, pin, hold_ms):
        """
        Press a button for a specified duration.
        :param pin: Pin to press
        :param hold_ms: Duration to press the button in milliseconds
        """
        pin.value(1)
        utime.sleep_ms(hold_ms)
        pin.value(0)
        utime.sleep_us(80)

    def down(self):
        """
        Press the down/previous button for a specified duration.
        """
        self.__press(self._down_prev, self._long_hold_ms)

    def up(self):
        """
        Press the up/next button for a specified duration.
        """
        self.__press(self._up_next, self._long_hold_ms)

    def prev(self):   
        """
        Press the down/previous button for a specified duration.
        """
        self.__press(self._down_prev, self._shot_hold_ms)        

    def next(self):
        """
        Press the up/next button for a specified duration.
        """
        self.__press(self._up_next, self._shot_hold_ms)

    def pause_resume(self):
        """
        Press the mode button for a specified duration.
        :param duration: Duration to press the button in milliseconds
        """
        self.__press(self._scan, self._shot_hold_ms)
```

다음 명령어를 이용해 클래스를 TiCLE 보드에 저장합니다.

```
upy put btaudioamp.py
```

### 오디오 앰프 제어

다음 코드를 작성합니다.

```python
# bt_ex.py
from btaudioamp import BtAudioAmp

bt = BtAudioAmp(mode=22, scan=26, down=27, up=28)
is_play = True

msg = """Bluetooth Audio Amplifier Control
Press 'mode' to switch be and smartphone pairing
smartphone audio play
"""

def setup():
    print(msg)

def loop():
    global is_play
    cmd = input("command: ").lower()

    if cmd == "down":
        bt.down()
    elif cmd == "up":
        bt.up()
    elif cmd == "next":
        if is_play:
            bt.next()
    elif cmd == "prev":
        if is_play:
            bt.prev()
    elif cmd == "pause":
        if is_play:
            bt.pause_resume()
            is_play = False
    elif cmd == "resume":
        if not is_play:
            bt.pause_resume()
            is_play = True
    else:
        print("Unknown command: {cmd}")

def cleanup():
    pass

if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except KeyboardInterrupt:
        cleanup()
```

프로그램을 실행하기에 앞서, 오디오 앰프의 모드를 Bluetooth Mode로 설정한 뒤, 휴대폰 및 노트북 등을 활용해 블루투스와 페어링 한 후 음악을 재생시킵니다. 이 상태가 실습의 기본 상태입니다.

그 후, 터미널에 다음 명령어를 입력하여 프로그램을 실행합니다.

```
upy bt_ex.py
```

프로그램을 실행한 후, 아래 리스트를 참조하여 원하는 동작에 맞는 명령어를 입력해 스피커를 제어해봅니다.

- up : 볼륨 1 올리기
- down : 볼륨 1 내리기
- next : 다음 곡 전환
- prev : 이전 곡 전환
- pause : 일시정지
- resume : 재개

## 음성인식을 활용한 스피커 제어

이 장에서는 음성인식으로 스피커의 여러 기능을 제어해 봅니다.

우선, 주변장치를 제어할 TiCLE 코드를 작성합니다. 이 때, 9번줄에서 `Wifi.connect_ap()` 함수 안에 들어갈 인자값을 현재 사용하고 있는 네트워크 장비에 맞춰 기입합니다. 

```python
# ticle.py
import utools
import ticle
from wifi import Wifi
from umqtt.robust2 import MQTTClient
import time
from btaudioamp import BtAudioAmp

ip = Wifi.connect_ap("ssid", "password")  # AP 이름과, 비밀번호를 변경해 주세요.
if ip:
    print(f"IP is {ip}")
else:
    print("Failed!!!")
    raise SystemExit(-1)

TOPIC_IOT_ACTION = "pbl/iot/action/+"
TOPIC_IOT_ACTION_LIGHT = "pbl/iot/action/light"
TOPIC_IOT_ACTION_MOVING = "pbl/iot/action/moving"
TOPIC_IOT_ACTION_AUDIO = "pbl/iot/action/audio"

pl = ticle.PixelLed(7, 10)  # Pin 7, Quantity: 10
servo = ticle.ServoMotor(6, 50)  # Pin 6
cmqtt = MQTTClient(client_id="NamE12q", server="mqtt.eclipseprojects.io")  # 고유한 이름(무작위)로 변경해 주세요

interval_20 = utools.intervalChecker(20)
interval_1000 = utools.intervalChecker(1000)

global command
command = None
global option
option = None
global do_act
do_act = False

# Bt audio
global bt
bt = BtAudioAmp(mode=22, scan=26, down=27, up=28)
global is_play
is_play = True

def on_message(topic, msg, retained, duplicate):
    topic = topic.decode()
    msg = msg.decode()
    print(msg)

    global command
    global option
    global do_act

    if topic == TOPIC_IOT_ACTION_LIGHT:
        command = "light"
        option = int(msg)
        do_act = True
    elif topic == TOPIC_IOT_ACTION_MOVING:
        command = "moving"
        option = int(msg)
        do_act = True
    elif topic == TOPIC_IOT_ACTION_AUDIO:
        command = "audio"
        option = msg
        do_act = True
    else:
        print(f">>>UNKNOWN<< topic: {topic}, message: {msg}")

def act():
    global command
    global option
    global bt
    global is_play
    
    if command is not None:
        if command == "light":
            if option <= 100:
                val = int(255/100*option)
                pl.on(list([val]*3))
        elif command == "moving":
            servo.angle(option)
        elif command == "audio":
            if option == "up":
                bt.up()
            elif option == "down":
                bt.down()
            elif option == "prev":
                if is_play:
                    bt.prev()
            elif option == "next":
                if is_play:
                    bt.next()
            elif option == "pause":
                if is_play:
                    bt.pause_resume()
                    is_play = False
            elif option == "resume":
                if not is_play:
                    bt.pause_resume()
                    is_play = True

def setup():
    print("Press 'Ctrl+C' to quit")
    
    cmqtt.connect()
    cmqtt.set_callback(on_message)
    cmqtt.subscribe(TOPIC_IOT_ACTION)

def loop():
    global do_act           
    if interval_20: 
        cmqtt.check_msg()
        if do_act:
            act()
            do_act = False
                         
    if interval_1000():
        cmqtt.ping()  # MQTT 서버와의 연결 유지

def cleanup():
    servo.angle(90)
    pl.off()
    print("Good-bye!!!")

if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()

```

다음으로, Host PC에서 사용할 코드를 작성합니다.

```python
# speech.py
import speech_recognition as sr
import paho.mqtt.client as mqtt
import re

TOPIC_IOT_ACTION_LIGHT = "pbl/iot/action/light"
TOPIC_IOT_ACTION_MOVING = "pbl/iot/action/moving"
TOPIC_IOT_ACTION_AUDIO = "pbl/iot/action/audio"

recognizer = sr.Recognizer()
cmqtt = mqtt.Client()

def parse_command(text):
    """
    Parse the command and option from the text.
    :param text: The input text to parse.
    :return: A tuple containing the command and option.
    """
    
    text = text.strip()
    command = None
    option = None

    # ===== LIGHT =====
    light_keywords = ['조명', '밝기', '형광등', '등']
    light_mode_map = {
        '그라데이션': 200,
        '무드등': 300,
        '진자': 400
    }
    if any(keyword in text for keyword in light_keywords):
        command = 'light'
        brightness_match = re.search(r'(\d+)\s*(?:으로)?\s*(?:설정|바꿔|해)', text)
        if brightness_match:
            option = int(brightness_match.group(1))
        elif re.search(r'(꺼줘|꺼)', text):
            option = 0
        else:
            for mode in light_mode_map:
                if mode in text:
                    option = light_mode_map[mode]
                    break

    # ===== MOVING =====
    elif '움직' in text or '방향' in text:
        command = 'moving'
        if '왼쪽' in text:
            option = 30
        elif '오른쪽' in text:
            option = 150
        elif '전 방향' in text:
            option = 500
        else:
            angle_match = re.search(r'(\d+)\s*도', text)
            if angle_match:
                option = int(angle_match.group(1))
            else:
                # 명확한 방향이나 숫자 없을 시 무효
                command = None
                option = None

    # ===== AUDIO =====
    elif '볼륨' in text or '곡' in text:
        command = 'audio'
        if '올려' in text or '크게' in text:
            option = 'up'
        elif '내려' in text or '작게' in text:
            option = 'down'
        elif '다음' in text:
            option = 'next'
        elif '이전' in text or '앞' in text:
            option = 'prev'
        elif '일시정지' in text or '정지' in text:
            option = 'pause'
        elif '재생' in text or '다시' in text:
            option = 'resume'

    # ===== SPECIAL CASE: 무드등 언급만 =====
    elif '무드등' in text:
        command = 'light'
        option = 300

    return [command, option]

def on_connect(client, userdata, flags, reason_code):
    if reason_code != 0:
        raise SystemExit("MQTT 서버에 연결할 수 없습니다.")

def setup():
    cmqtt.on_connect = on_connect    
    cmqtt.connect("mqtt.eclipseprojects.io")
    cmqtt.loop_start()

def loop():
    try:
        input("<Enter>키를 누르면 음성 인식을 시작합니다.")
        
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 1.2
            print("말씀하세요...")
            audio = recognizer.listen(source, phrase_time_limit=10)
        
        text = recognizer.recognize_google(audio, language='ko-KR')
        print("Text: " + text)  
        
        command, option = parse_command(text)
        
        if command is None or option is None:
            print("알 수 없는 명령입니다.")
            return
        
        print(f"Command: {command}, Option: {option}") 
        
        if command == 'light':
            topic = TOPIC_IOT_ACTION_LIGHT
        elif command == 'moving':
            topic = TOPIC_IOT_ACTION_MOVING
        elif command == "audio":
            topic = TOPIC_IOT_ACTION_AUDIO
        else:
            return
        
        cmqtt.publish(topic, option)

    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"음성 인식 서버에 문제가 있습니다; {e}") 
        return

def cleanup():
    cmqtt.loop_stop()

if __name__ == "__main__":
    try:
        setup()
        while True:
            loop()
    except KeyboardInterrupt:
        pass
    finally:    
        cleanup()
```

두 코드 작성이 완료되었다면, 터미널에서 두 창을 분할시키고, 한 쪽은 TiCLE 코드를, 다른 한 쪽은 Host PC에서 음성인식 코드를 실행합니다.

```
# Terminal 1
upy ticle.py
```

```
# Terminal 2
python speech.py
```

이 후, 원하는 동작을 음성으로 말하여 스피커 기능을 제어해봅니다.