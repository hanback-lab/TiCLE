"""
PC 또는 라즈베리파이5에서 실행하는 프로그램

1. 기본 구조
    Mic ---> Recognition API ---> Internet --> AI Recognition Server
                                                                |    
    Text <------------------------------------------------------|
      |  
      |----> text parsing (command, option) --> MQTT clinet ---> Internet --> MQTT Broker
    
2. 음성 인식, 오디오, MQTT 클라이언트 라이브러리 설치
> pip install SpeechRecognition
> pip install pyaudio
> pip install paho-mqtt
"""

import speech_recognition as sr
import paho.mqtt.client as mqtt
import re

#-----------------------------------------------------------
# MQTT 서버에 발생할 토픽을 정의합니다.
TOPIC_IOT_ACTION_LIGHT = "pbl/iot/action/light"
TOPIC_IOT_ACTION_MOVING = "pbl/iot/action/moving"
TOPIC_IOT_ACTION_AUDIO = "pbl/iot/action/audio"
#-----------------------------------------------------------

# 객체 정의
recognizer = sr.Recognizer()
cmqtt = mqtt.Client()

#-----------------------------------------------------------
# 문자열 파싱 함수 정의 (vibe 코딩 활용)
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
        # 밝기 숫자
        brightness_match = re.search(r'(\d+)\s*(?:으로)?\s*(?:설정|바꿔|해)', text)
        if brightness_match:
            option = int(brightness_match.group(1))
        # 밝기 0 (꺼줘)
        elif re.search(r'(꺼줘|꺼)', text):
            option = 0
        # 모드 설정
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
#-----------------------------------------------------------

#-----------------------------------------------------------
# MQTT 서버에 연결할 때 호출될 콜백 함수 정의
def on_connect(client, userdata, flags, reason_code):
    if reason_code != 0:
        raise SystemExit("MQTT 서버에 연결할 수 없습니다.")

#-----------------------------------------------------------

#-----------------------------------------------------------
# 아두이노와 같운 프로세싱 구조 사용
# 프로그램이 처음 실행될 때 수행할 작업 정의
def setup():
    cmqtt.on_connect = on_connect    
    cmqtt.connect("mqtt.eclipseprojects.io")
    cmqtt.loop_start()

# 프로그램이 반복적으로 수행할 작업 정의
def loop():
    try:
        input("<Enter>키를 누르면 음성 인식을 시작합니다.")
        
        # 마이크로부터 음성을 캡처해 오디오 데이터를 생성합니다.
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 1.2
            print("말씀하세요...")
            audio = recognizer.listen(source, phrase_time_limit=10)
        
        # AI 음성 인식 서버를 통해 사용자 음성을 텍스트로 변환합니다.
        text = recognizer.recognize_google(audio, language='ko-KR')
        print("Text: " + text)  # 디버깅 목적입니다. 필요없으면 삭제하세요.
        
        # 텍스트를 파싱해 명령와 옵션을 추출합니다.
        command, option = parse_command(text)
        
        if command is None or option is None:
            print("알 수 없는 명령입니다.")
            return
        
        print(f"Command: {command}, Option: {option}") # 디버깅 목적입니다. 필요없으면 삭제하세요.
        
        # MQTT 서버로 명령에 해당하는 토픽과 옵션을 메시지로 전송합니다.
        if command == 'light':
            topic = TOPIC_IOT_ACTION_LIGHT
        elif command == 'moving':
            topic = TOPIC_IOT_ACTION_MOVING
        elif command == "audio":
            topic = TOPIC_IOT_ACTION_AUDIO
            # 옵션은 up, down, prev, next 중 하나입니다.
        else:
            return
        
        cmqtt.publish(topic, option)

    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"음성 인식 서버에 문제가 있습니다; {e}") 
        return

# 프로그램이 종료할 때 수행할 작업 정의
def cleanup():
    cmqtt.loop_stop()
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