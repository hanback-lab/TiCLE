# TiCLE

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/product_topview.png" width=25%>

TiCLE RP2350이 탑재된 Raspberry Pi Pico 2 W 확장 보드입니다. 안정적이고 신뢰성 높은 GPIO 확장을 넘어 풍부한 SDK 보장합니다. 이를 통해 접근성이 높고 확장성을 넓혀주는 개발 환경을 가질 수 있어 무궁무진한 상상력을 발휘할 수 있게 지원해줍니다.

# Features

- **강력한 MCU 보드 기반** : 탑재된 Raspberry Pi Pico 2 W 보드는 강력한 칩 RP2350이 탑재된 고성능 MCU 보드. 더 자세한 사양은 [이 링크](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)를 참조
- **소프트웨어 지원** : 사용하기 쉬우면서 강력한 기능을 가진 SDK 제공 및 지원
- **IO 확장** : 총 16개의 GPIO 핀 및 5V, 3.3V, GND 각각 6핀 확장 추가 제공
- **안정적인 전력 공급** : 각 GPIO 핀 및 전원 확장 핀에 안정적인 전력 공급 보장
- **CAN 통신 핀 제공** :  CAN 통신을 이용하여 다수의 주변장치 제어 가능
- **기본 탑재된 주변장치** : TiCLE 보드 위에 RGB LED, Switch, IMU 장치 탑재

# Provided platform

TiCLE은 Raspberry Pi 공식 micropython 펌웨어를 커스터마이징하여 설치되어 있습니다. 기존에 막강한 Micropython 기능을 넘어서 한백전자 고유의 기술을 이용해 제작한 SDK를 추가로 포함하여 제공됩니다. 이러한 개발환경은 사용자에게 유연하고도 강력한 성능을 발휘할 수 있도록 지원해줍니다.

<br>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/MicroPython_new_logo.svg/120px-MicroPython_new_logo.svg.png">
<br><br>

자세한 Micropython 문법은 [이 링크](https://docs.micropython.org/en/latest/rp2/quickref.html)에서 확인해볼 수 있습니다.

# Getting Started 🏎️

## Setting develop environment

TiCLE의 개발환경은 현존하는 가장 막강한 편집기 Visual Studio Code와 pip를 통해 간단한 방법으로 구축할 수 있습니다. 환경을 구축하게 되면 python 가상 환경 제공과 더불어 기존에 VSCode를 설치하였더라도 완전 독립적으로 동작합니다. 이러한 독립적인 구조는 환경 구축의 자유도를 높이고 재사용성을 높일 수 있습니다!

[이 링크](https://github.com/hanback-lab/TiCLE/wiki/Installation)를 통해서 설치하는 방법을 확인할 수 있습니다.

## Make a rainbow 🌈

<img src="https://github.com/hanback-lab/TiCLE/blob/main/pictures/ticle_rgb_led.png" width=25%>

위 사진처럼 TiCLE 우측 중단에 RGB LED가 설치되어 있고, Raspberry Pi Pico 보드의 GP0번에 연결되어 있습니다. [TiCLE API](https://github.com/hanback-lab/TiCLE/wiki/TiCLE-API)의 `ticle.PixelLed` 를 활용하여 이 RGB LED를 제어합니다.

```python
# rainbow.py
import ticle
import utime
pl = ticle.PixelLed(0, 1)

for i in range(255):
    pl.on((i,0,0))
    utime.sleep_ms(10)
for i in range(255):
    pl.on((255-i,i,0))
    utime.sleep_ms(10)
for i in range(255):
    pl.on((0,255-i,i))
    utime.sleep_ms(10)
```

터미널에 다음 명령어로 프로그램을 실행시킵니다.

```
upy run rainbow.py
```

## Switch Control 

<img src="https://github.com/hanback-lab/TiCLE/blob/main/pictures/ticle_sw.png" width=25%>

위 사진처럼 TiCLE 우측 중단에 Switch가 설치되어 있고, Raspberry Pi Pico 보드의 GP2번에 연결되어 있습니다. `machine.Pin` 을 사용하여 Switch의 입력을 받아봅니다.

다음은 Switch의 입력을 확인하고 Switch가 눌려졌을 시 'pressed' 라는 문구가 표시됩니다.

```python
# button.py
import machine
import utime

p = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if p.value() == 1:
        print("You pressed")
        utime.sleep(0.3)
```

# Tech Support 🛠️

자사의 장비를 이용해주셔서 감사합니다! 만일 제품 사용 시 불편한 점 및 문제가 발생하였을 때 최대한 빠르고 친절하게 기술지원을 보장해드립니다. 아래 주소로 편하게 연락주세요. 🤗

대한민국 : edu@hanback.co.kr   
해외 : support@hanback.co.kr
