# Upyboard

## Upyboard 소개

### Upyboard란?

Upyboard는 MCU 보드에 구축된 Micropython 환경에서의 프로그래밍을 보조하는 개발 툴입니다. 이 툴은 다양한 기능을 제공하고 빠른 속도로 동작하여 개발자로부터 하여금 편의성을 증진시켜줄 수 있습니다.

#### 기능

제공되는 기능은 다음과 같습니다.
- **간편한 프로그램 실행** : 높은 추상화 및 간편한 환경설정들로 인해 보드 위에서의 Micropython 프로그램 실행의 간편성을 대폭 높입니다.
- **사용자 맞춤 환경설정** : 사용자 맞춤 설정을 통해 필요한 설정값을 미리 저장해 편의성을 증가시킬 수 있습니다.
- **강력한 보드 제어** : Soft Reset, Repl 접속 등 보드를 간단하고도 강력하게 제어할 수 있습니다.
- **저장소 접근 및 관리** : 보드의 저장소에 접근하고 파일들을 관리할 있어 라이브러리 업로드 등 보드의 활용도를 대폭 높일 수 있습니다.
- **자동 업데이트** : 업데이트 버전 등록 시 자동으로 감지하고 설치를 진행합니다.

#### 지원 보드

현재 지원하는 보드는 다음과 같습니다.
- [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/)
- [TiCLE](https://github.com/hanback-lab/TiCLE)
- \<향후 추가 지원 예정\>

## Upyboard 설치 방법

Upyboard 툴은 파이썬 패키지로써 Pypi에 등록되어 있어, pip로 간편하게 설치할 수 있습니다. 단, 다음 조건을 충족해야 합니다.

- Windows 11 이상
- **Python 3.10 이상**

```
pip install upyboard
```

## Quick Start

Upyboard를 활용하기 위한 개발환경을 구축합니다. 

개발환경 구성을 위해 다음 준비 사항이 필요합니다.
- Visual Studio Code (이하 VSCode)
- Python (3.10 이상)
- upyboard 패키지
- Raspberry Pi Pico 2 or TiCLE

VSCode 및 Python 설치는 다음 내용을 참고하여 진행합니다. 
- 통합 설치 (추천) : https://github.com/hanback-lab/TiCLE/wiki/Installation
- 개별 설치
  - VSCode : https://code.visualstudio.com/Download
  - Python : https://python.org/downloads
---

우선, VSCode 상에서 작업할 위치에 폴더를 엽니다.

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/open_folder.png" width="50%"/>

<br>

보드와 PC간의 연결 상태를 확인합니다. 그 후 터미널에 다음 명령어를 입력하여 PC에 연결된 보드의 시리얼 포트를 확인합니다.

```
upy scan
```

![upy_scan](https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_scan.png)

<br>

시리얼 포트를 확인하였다면 다음 명령어를 입력하여 현재 Workspace에 보드의 시리얼 포트 정보를 저장합니다. 

```
upy -s <시리얼 포트> env
```

![upy_register](https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy._register_env.png)

<br>

<details>
<summary><b>TiCLE 보드 초기화</b></summary>
<br>

**지원 되는 보드 목록 이외 보드에서 아래 내용 진행으로 인한 문제에 대해 해결방안은 제시하지 않습니다.**

upy init 은 TiCLE 보드를 초기화 하는 작업으로 TiCLE 보드를 사용하기 위한 시스템 초기화 및 기본 라이브러리가 설치됩니다. 

```
upy init
```

![upy_init](https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_init.png)

초기화가 진행되면 앞의 그림처럼 업로드된 파일의 내용을 확인할 수 있으며, upy ls 를 통해 보드에 업로드된 내용들을 확인할 수 있습니다. 

```
upy ls
```
<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_ls.png" width="30%" />

<br>

lib 폴더 내부의 내용을 확인하고 싶다면, 다음과 같이 입력하여 내용을 확인합니다. 

```
upy ls lib
```

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_ls_lib.png" width="30%" />

</details>

---

### Hello World!

다음은 Micropython 프로그램을 작성하고 Pico에 업로드하는 실습입니다. 

먼저 간단한 프로그램을 작성합니다. VSCode 왼쪽 상단에 'New File' Icon을 눌러 새 파일을 생성한 다음, 'main.py' 라고 이름을 지정합니다.

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/create_file.png" width="40%" />   
<br>
<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/create_file_set_name.png" width="40%" />
<br><br>


파일을 아래와 같이 작성합니다.

```python
print("Hello World!")
```

<br>

다음 명령어를 입력하여 프로그램 동작 결과를 확인합니다.

```
upy run main.py
```

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_run.png" width="35%" />

## Commands

upyboard 명령의 옵션 종류 및 사용법이 담겨 있습니다. 

명령어의 기본 구조는 다음과 같습니다.

```sh
upy [OPTIONS] COMMAND [ARGS] ...
```

### scan
> 현재 PC 또는 랩탑에 연결된 보드를 검색합니다. 

연결된 보드의 포트 정보, Micropython 펌웨어 버전, 펌웨어 버전 등록 일자, 그리고 보드 명칭이 표시됩니다. 

```
upy scan
```

<details>
<summary>사용 예시</summary>
<br>
실행 결과

![scan_ex](res/scan_ex.png)
</details>

### env
> 현재 경로에 보드의 포트 정보 및 개발 편의 설정을 저장합니다. 

env 옵션을 실행할때 현재 사용자 경로에 연결된 포트 정보를 저장하여 이후 upy 명령을 통한 보드 작업에서 포트 정보를 일일이 기재하지 않아도 자동으로 설정되도록 합니다. 또한, VSCode의 Intellicode 및 Python extenstion에 Micropython 정보를 설정하여 VSCode에서 Micropython 개발을 편리하게 할 수 있도록 구성해줍니다.

upy의 명령은 '-s' 옵션을 통해 보드의 포트 정보를 직접 입력하여 활용할 수 있습니다. 하지만, env 명령을 통해 설정을 저장한다면 옵션을 매번 입력하지 않은 상태로 활용할 수 있습니다. 

환경 등록은 Workspace 에 최초 1회만 실행하면 됩니다. 또한, 초기 상태에는 등록된 포트 정보가 없기 때문에 '-s' 옵션을 사용하여 포트 정보를 명시해줍니다. 보드와 연결된 포트는 [scan](#scan) 명령어를 통해 확인할 수 있습니다.

```
upy -s <COM Port> env
```

<details>
<summary>사용 예시</summary>
<br>

[scan](#scan) 옵션을 활용해 연결된 포트를 확인 

![scan_ex](res/scan_ex.png)

'COM5' 포트를 설정에 저장

![env_ex](res/env_ex.png)
</details>

### init
> 보드를 초기화합니다. 

보드에 저장된 파일들을 모두 삭제한 후, 공장 초기화합니다. 이 때, 연결된 보드를 자동으로 감지하여 각 보드에 맞는 초기화 과정을 수행합니다.

```sh
upy init
```

<details>
<summary>사용 예시</summary>
<br>

TiCLE 보드 공장 초기화 진행

![init_ex](res/init_ex.png)
</details>

### sport

> Workspace 에 등록된 포트 정보를 변경합니다.

같은 Workspace에서 보드만 변경된 경우, 연결된 포트 정보가 달라질 수 있습니다. 이때 env 명령을 다시 수행하지 않고 sport 명령어를 사용하여 포트 정보를 변경해 기존과 동일하게 사용할 수 있습니다.

단, [env](#env) 를 활용해 관련 정보가 저장된 Workspace 에서만 동작됩니다.

인자값으로 변경할 포트를 입력합니다. 만약 인자값으로 아무것도 입력하지 않을시, 현재 Workspace 에 저장된 포트 정보를 출력합니다.

```sh
# Display port information
upy sport

# Change port
upy sport <COM PORT>
```

<details>
<summary>사용 예시</summary>

<br>
보드 변경 전

![scan_ex](res/scan_ex.png)

![sport_current_ex](res/sport_current_ex.png)

보드 변경 후 scan 시 'COM29' 표시됨

![sport_scan_ex](res/sport_scan_ex.png)

sport 명령어를 사용해 포트 변경

```sh
upy sport COM29
```

![sport_ex](res/sport_ex.png)

포트 변경 확인

```sh
upy sport
```

![sport_change_ex](res/sport_change_ex.png)

</details>

### run
> 현재 Workspace 에서 작성된 Micropython 프로그램을 실행시킵니다. 

이 옵션은 사용자가 작성한 Micropython 프로그램을 보드에 설치된 인터프리터를 사용하여 프로그램을 실행합니다. 실행하는 프로그램의 코드가 보드에 저장되지 않으며 1회성으로 실행하여 빠르게 결과를 확인하기에 용이합니다. 

인자값으로 실행할 파일 이름을 입력합니다.

```sh
upy run <File name>.py
```

<details>
<summary>사용 예시</summary>
<br>

Workspcae 에서 'hello_world.py' 파일 생성 후 다음과 같이 입력 및 저장

```python
print("hello world!")
```

<img src="res/run_file_ex.png" width=60%>

다음 명령어로 프로그램 실행 후 결과 확인

```sh
upy run hello_world.py
```

![run_ex](res/run_ex.png)
</details>

### df
> 보드 저장소의 현재 용량을 확인합니다.

```
upy df
```

<details>
<summary>사용 예시</summary>
<br>
실행 결과

![df_ex](res/df_ex.png)

</details>

### ls

> 보드 저장소의 특정 경로에 있는 모든 폴더/파일들을 출력합니다.

인자값으로 특정 경로를 입력하면 해당 경로의 모든 폴더/파일들을 출력합니다. 입력하지 않는다면 최상위 경로 ('/') 를 출력합니다.

```sh
upy ls

# Specific path
upy ls <path>
```

<details>
<summary>사용 예시</summary>
<br>
실행 결과

```sh
upy ls
```

![ls_ex](res/ls_ex.png)

\<TiCLE 전용\> library 폴더 내 파일 목록 출력

```sh 
# 보드에 탑재된 칩 종류에 따라 달라질 수 있음.
upy ls lib
```

![ls_lib_ex](res/ls_lib_ex.png)
</details>

### mkdir
> 보드 저장소 내에 폴더를 생성합니다.

파일들을 정리 및 분류하는데 용이하게 사용할 수 있습니다.

인자값으로 생성할 폴더의 경로를 입력합니다.

```sh
upy mkdir <path>
```

<details>
<summary>사용 예시</summary>
<br>
실행 결과

```sh
upy mkdir test
```

![mkdir_ex](res/mkdir_ex.png)

생성 확인

```sh
upy ls
```

![mkdir_ls_ex](res/mkdir_ls_ex.png)
</details>

### put
> 파일을 보드 저장소에 저장시킵니다.

Workspcae 에서 작성된 Micropython 프로그램을 보드 저장소에 저장시킵니다. 단순 파일 저장을 넘어 사용자 지정 라이브러리 저장, boot 및 main 프로그램도 등록할 수 있어 보드의 활용도를 높여줄 수 있습니다.

인자값을 총 두 개까지 입력할 수 있습니다.
- 첫 번째 인자 : 저장할 파일 이름
- 두 번째 인자 (선택) : 보드에 저장할 때 붙여질 새로운 이름 및 저장할 경로

```sh
# Use original file name
upy put <file name>

# Attach new name
upy put <file name> <new name or path>
```

<details>
<summary>사용 예시</summary>
<br>

[run](#run) 예시에서 생성한 'hello_world.py' 을 다음 명령어를 통해 보드 저장소에 파일 저장

```sh
upy put hello_world.py
```
![put_ex](res/put_ex.png)

만약, 새로운 이름 (예시 : temp.py)로 저장할 시 다음과 같이 입력

```sh
upy put hello_world.py temp.py
```

![put_temp_ex](res/put_other_name.png)

[ls](#ls) 명령어로 파일 저장 확인

```sh
upy ls
```

![put_ls](res/put_ls.png)

[mkdir](#mkdir) 예시에서 제작한 test 폴더 안에 'hello_world.py' 파일을 'hello.py' 이름으로 저장

```sh
upy put hello_world.py test/hello.py
```
![put_in_test](res/put_in_test.png)

[ls](#ls) 명령어로 파일 저장 확인

```sh
upy ls test
```

![put_ls_test](res/put_ls_test.png)
</details> 

### get
> 파일 내용을 읽고 출력합니다.

보드에 저장된 파일 내용을 읽고 터미널에 출력합니다. 보드 저장소 내에 저장된 파일의 원본이 손실되었거나 다른 작업자와 협업할 때 등 활용할 수 있습니다.

인자값을 총 두 개까지 입력할 수 있습니다.
- 첫 번째 인자 : 보드 저장소 경로
- 두 번째 인자 (선택) : 보드 저장소에서 특정 파일을 불러온 후 Workspace에 저장될 파일 이름 또는 경로
```sh
# Display file content on terminal
upy get <path>

# Load and save a file from the board with a specified name or path
upy get <path> <new name or path>
```

<details>
<summary>사용 예시</summary>
<br>
불러올 파일 확인

![check_the_file](res/put_ls.png)

get 명령어를 통해 파일 내용을 터미널에 출력

```sh
upy get hello_world.py
```
![get_ex](res/get_ex.png)

보드에 test 폴더 아래에 있는 'hello.py' 파일을 사용자 환경에 'hi.py'로 저장

![check_the_test](res/put_ls_test.png)

```sh
upy get test/hello.py hi.py
```

![get_test_hi](res/get_test_hi.png)

![check_get_the_file](res/get_the_file.png)
</details> 

### upload
> 파일을 컴파일하여 보드 저장소에 저장합니다.

Micropython 파일을 바이트코드 파일로 변환시켜 보드 저장소에 저장시키는 기능입니다. 경량화 및 은닉화 등의 목적으로 활용될 수 있습니다. 

인자값을 총 두 개까지 입력할 수 있습니다.
- 첫 번째 인자 : 저장할 파일 이름
- 두 번째 인자 (선택) : 보드 저장소에 저장할 때 붙여질 새로운 이름 및 경로

```sh
# Use original file name
upy upload <file name>.py

# Attach new name or path
upy upload <file name>.py <new_name or path>
```

<details>
<summary>사용 예시</summary>
<br>

[run](#run) 예시에서 생성한 'hello_world.py' 을 다음 명령어를 통해 보드 저장소에 파일을 컴파일한 후 저장

```sh
upy upload hello_world.py
```

![upload_ex](res/upload_ex.png)

만약, 새로운 이름 (예시 : temp.mpy)로 저장할 시 다음과 같이 입력

```sh
upy upload hello_world.py temp.mpy
```

![upload_temp_ex](res/upload_temp.png)

`ls` 명령어로 파일 저장 확인

```sh
upy ls
```

![upload_ls](res/upload_ls.png)

[mkdir](#mkdir) 예시에서 제작한 test 폴더 안에 'hello_world.py' 파일을 'hello.mpy' 이름으로 저장

```sh
upy upload hello_world.py test/hello.mpy
```
![upload_in_test](res/upload_in_test.png)

`ls` 명령어로 파일 저장 확인

```sh
upy ls test
```

![upload_ls_test](res/upload_ls_test.png)
</details> 

### rm

> 보드 저장소 내의 특정 폴더 및 파일을 삭제합니다.

인자값으로 삭제할 파일 및 폴더, 혹은 경로를 입력합니다.

```sh
upy rm <path>
```

<details>
<summary>사용 예시</summary>
<br>

[ls](#ls) 명령어로 현재 저장된 파일들 확인

![rm_ls_prev](res/upload_ls.png)

[put](#put) 예시에서 저장한 'temp.py' 파일 삭제

```sh
upy rm temp.py
```

![rm_ex](res/rm_ex.png)

삭제 확인

```sh
upy ls
```

![rm_ls_ex](res/rm_ls_ex.png)

[upload](#upload) 예시에서 저장한 'test/hello.mpy' 파일 삭제

```sh
upy rm test/hello.mpy
```

![rm_mpy_ex](res/rm_mpy_ex.png)

삭제 확인

```sh
upy ls test
```

![rm_mpy_ls_ex](res/put_ls_test.png)

</details>

### format
> 보드 저장소을 초기화합니다.

보드 저장소에 있던 파일들을 전부 삭제합니다. 저장소를 깔끔하게 정리하고 싶을 때 유용하게 사용할 수 있습니다.

```sh
upy format
```

<details>
<summary>사용 예시</summary>
<br>
실행 결과


![format_ex](res/format_ex.png)

(+) format 후 파일시스템 확인

```sh
upy ls
```

![format_ls_ex](res/format_ls_ex.png)

</details>

### reset 

> 보드를 Soft reset 시킵니다.

reset 옵션은 보드의 Micropython 인터프리터를 초기화시키는 기능입니다. 즉, RAM에 적재된 Micropython 코드 및 변수, 모듈 등을 초기화시킵니다.   

reset 시 보드는 자동으로 boot.py -> main.py 프로그램을 순차적으로 실행하는데, 이 시퀀스를 이용하여 보드에 전원을 처음 공급할때와 같은 상황을 구성할 수 있습니다.  

```sh
upy reset
```

<details>
<summary>사용 예시</summary>
<br>
Workspace 에서 'blink.py' 파일 생성 및 아래 내용 기재

```py
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)
while True:
    led.toggle()
    time.sleep_ms(1000)
```

![blink_code](res/blink_code.png)

[put](#put) 옵션을 사용하여 'main.py' 이름으로 보드 저장소에 저장

```sh
upy put blink.py main.py
```

![blink_put](res/blink_put.png)

upy reset 후 보드에 장착된 LED가 1초씩 점멸하는 지 확인

```sh
upy reset
```

![reset_ex](res/reset_ex.png)

![reset_ex_res](res/reset_ex.gif)

</details>

### repl

> 보드의 MicroPython REPL에 접속합니다.

REPL(Read Eval Pring Loop)이란 명령어 한 줄씩 입력받아 실행하고 그 결과를 즉시 출력해주는 대화형 인터프리터 환경입니다.

REPL은 대화형 실행 환경으로써 단순한 코드는 그 결과값을 즉시 확인해볼 수 있다는 특징을 가지고 있습니다. 이를 활용해 센서 값을 실시간으로 읽어보거나 특정 함수 및 라이브러리의 동작을 테스트해볼 수 있는 등 디버깅 및 실험에 있어서 아주 용이하게 쓰일 수 있는 기능입니다.

또한, Soft Reset 등의 단축키 기능이 담겨 있어 보드 저장소 및 전체 제어를 할 수 있습니다.

REPL에 접속하면 직전까지 실행되고 있던 프로그램은 자동으로 종료됩니다.

```sh
upy repl
```

<details>
<summary>사용 예시</summary>
<br>
REPL을 열고 단순 연산값을 출력해봅니다.

```sh
upy repl
>>> print(1+2)
```

실행 결과

![repl_ex](res/repl_ex.png)

REPL에서 Soft Reset을 걸어 [reset](#reset) 과정에서 넣었던 `main.py` 프로그램을 실행시켜봅니다.

```sh
>>> <Ctrl+D>
```

실행 결과

![repl_softreset_ex](res/repl_softreset_ex.png)

LED에 불이 점멸하는 것을 확인할 수 있습니다.

</details>

### shell

> 보드의 저장소 관리를 Shell 형태로 수행합니다.

보드에 접속하여 특정 기능을 제어할 수 있는 명령어 기반 인터페이스(Command Line Interface) 입니다.  

Linux의 Shell처럼 입력을 통해 명령어를 수행할 수 있지만, 아래에 명시된 명령어만 사용 할 수 있습니다. 보드 저장소 관리의 효율성을 증진시켜줄 수 있습니다.

```sh
upy shell
```

사용할 수 있는 명령어는 다음과 같습니다.

- clear : 화면 정리
- [ls](#ls)
- cd : 특정 경로 이동
- [get](#get)
- [put](#put)
- [rm](#rm)
- [mkdir](#mkdir)
- [df](#df)
- [repl](#repl)
- pwd : 현재 경로 출력
- help : shell 상에서 사용할 수 있는 명령어 출력

<details>
<summary>사용 예시</summary>
<br>

접속 화면

```sh
upy shell
```

![shell_ex](res/shell_ex.png)

'test' 폴더 이동 후 현재 경로 출력

```sh
cd test
pwd
```

![shell_cd_pwd](res/shell_ex_cdpwd.png)

[ls](#ls) 명령어로 test 폴더 내에 파일 확인

```sh
ls
```

![shell_ls](res/shell_ls_ex.png)

</details>
