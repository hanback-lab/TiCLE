# Upyboard

## Upyboard 소개

### Upyboard란?

Upyboard는 MCU 칩에 구축된 Micropython 환경에서의 프로그래밍을 보조하는 개발 툴입니다. 이 툴은 다양한 기능을 제공하고 빠른 속도로 동작하여 개발자로부터 하여금 편의성을 증진시켜줄 수 있습니다.

#### 기능

제공되는 기능은 다음과 같습니다.
- **간편한 프로그램 실행** : 높은 추상화 및 간편한 환경설정들로 인해 칩 위에서의 Micropython 프로그램 실행의 간편성을 대폭 높입니다.
- **사용자 맞춤 환경설정** : 사용자 맞춤 설정을 통해 필요한 설정값을 미리 저장해 편의성을 증가시킬 수 있습니다.
- **강력한 칩 제어** : Soft Reset, Repl 접속 등 칩을 간단하고도 강력하게 제어할 수 있습니다.
- **파일 시스템 접근 및 관리** : 칩의 파일시스템에 접근하고 파일들을 관리할 있어 라이브러리 업로드 등 칩의 활용도를 대폭 높일 수 있습니다.
- **자동 업데이트** : 업데이트 버전 등록 시 자동으로 감지하고 설치를 진행합니다.

#### 지원 보드

현재 지원하는 보드는 다음과 같습니다.
- [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/)
- [TiCLE](https://github.com/hanback-lab/TiCLE)
- \<향후 추가 지원 예정\>

## Upyboard 설치 방법

Upyboard 툴은 파이썬 패키지로써 Pypi에 등록되어 있어, pip로 간편하게 설치할 수 있습니다. 단, 다음 조건을 충족해야 합니다.

- Windows 11 이상
- Python 3.10 이상

```
pip install upyboard
```

## Quick Start

이 목차에서는 upyboard를 활용한 간단한 예시로 개발환경을 구축하고 간단한 프로그램을 실행시켜보는 실습을 진행해 보겠습니다.   

이 실습을 진행하기 위해 다음 준비 사항이 필요합니다.
- Visual Studio Code (이하 VSCode)
- Python (3.10 이상)
- upyboard 패키지
- Raspberry Pi Pico 2 or TiCLE

참고로, VSCode 및 Python 설치는 다음 링크를 참조해주시길 바랍니다.
- 통합 설치 (추천) : https://github.com/hanback-lab/TiCLE/wiki/Installation
- 개별 설치
  - VSCode : https://code.visualstudio.com/Download
  - Python : https://python.org/downloads
---

우선, VSCode 상에서 작업할 위치에 폴더를 엽니다.

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/open_folder.png" width="50%"/>

<br>

장비와 PC간의 연결을 확인합니다. 그 후 터미널에 다음 명령어를 입력하여 장비에 연결된 시리얼 포트를 확인합니다.

```
upy scan
```

![upy_scan](https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_scan.png)

<br>

시리얼 포트를 확인하였다면 다음 명령어를 입력하여 현재 Workspace에 장비 Serial Port를 등록시킵니다.

```
upy -s <시리얼 포트> env
```

![upy_register](https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy._register_env.png)

<br>

이 후, 다음 명령어를 입력하여 장비를 초기화 및 라이브러리들을 설치합니다.

```
upy init
```

![upy_init](https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_init.png)

초기화가 끝났다면 다음 명령어를 통해 파일 시스템을 확인해봅니다. 초기화가 잘 끝났다면 'lib' 라는 폴더가 Pico 안에 설치되어 있습니다.

```
upy ls
```
<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_ls.png" width="30%" />

<br>


명령어 인자값으로 폴더명을 넣어준다면 해당 폴더 내에 파일들도 확인할 수 있습니다.

```
upy ls lib
```

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_ls_lib.png" width="30%" />

<br><br>

### Hello World!

다음은 micropython 프로그램을 작성하고 Pico에 업로드하는 실습입니다. 

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

다음 명령어로 프로그램 동작 결과를 확인합니다.

```
upy run main.py
```

<img src="https://github.com/hanback-lab/TiCLE/raw/main/pictures/upy_run.png" width="35%" />

## Commands

upyboard 명령어들의 종류 및 사용법이 담겨 있습니다. 명령어들은 크게 5가지로 나뉘어져 있습니다.

- Workspace : 사용자 환경을 설정해줍니다.
- Run : 칩 위에서 Micropython 프로그램을 실행시킵니다.
- File : 파일 저장 및 불러오기 등 파일에 관련된 기능들입니다.
- File System : 칩의 파일 시스템을 관리해주는 기능들입니다. 이는 리눅스의 파일시스템과 유사합니다. 
- Chip Control : 실질적으로 칩을 제어합니다. (예시: Soft Reset) 

명령어의 기본 구조는 다음과 같습니다.

```sh
upy [OPTIONS] COMMAND [ARGS] ...
```

대부분의 upyboard 명령어는 사용자 환경이 upyboard 프로그램에 등록 되어 있어야 원활히 동작하며, 이는 `env` 명령어를 통해 진행할 수 있습니다. 만약 등록 되지 않은 경우 기능 사용에 제약이 되지만, `-s` 옵션을 붙여주어 일시적으로 기능을 활용할 수 있습니다.

### Workspace
#### env
> 실행 시 현재 경로를 사용자 환경으로 등록하고 구성합니다.

현재 경로에 .vscode 폴더를 생성합니다. 이 폴더는 칩과 연결된 포트 정보를 저장하며 프로그램 실행 시 포트 정보를 일일이 기입하지 않아도 자동으로 불러와 실행되게끔 설정해줍니다. 또한  VSCode의 Intellicode 및 Python extenstion에 관련 정보를 등록하여 VSCode에서도 Micropython 개발을 편리하게 할 수 있도록 구성해줍니다.

환경 등록은 해당되는 경로에 최초 1회만 실행하면 됩니다. 또한, 초기 상태에는 등록된 포트 정보가 없기에 '-s' 옵션을 사용하여 포트 정보를 명시해줍니다. 

```
upy -s <COM Port> env
```

<details>
<summary>사용 예시</summary>

실행 결과

![run_ex](res/env_ex.png)
</details>

#### init
> 칩을 초기화시킵니다.

칩 파일시스템의 저장된 파일들을 모두 삭제한 후, 라이브러리들을 설치하여 칩의 초기 상태로 만들어줍니다. 쓸모없는 파일들들 모두 한 번에 정리해야할 때 사용되는 기능입니다. 

```sh
upy init
```

<details>
<summary>사용 예시</summary>

실행 결과

![init_ex](res/init_ex.png)
</details>

#### scan
> 연결된 칩을 찾아 정보를 출력합니다.

연결된 칩의 연결 포트, Micropython 펌웨어 버전, 펌웨어 버전 등록 일자, 그리고 칩 이름이 표시됩니다. 이 명령어를 통해 칩과 연결된 포트 및 정보를 손쉽게 확인할 수 있습니다.

```
upy scan
```

<details>
<summary>사용 예시</summary>

실행 결과

![scan_ex](res/scan_ex.png)
</details>

#### sport

> 사용자 환경 설정에 등록된 포트 정보를 변경합니다.

같은 사용자 환경에서 칩만 달라질 경우, 연결된 포트 정보가 달라질 수 있습니다. 이에 이 명령어를 사용하여 포트 정보를 변경 후 기존과 동일하게 사용할 수 있습니다.

단, `env` 명령어로 사용자 환경이 등록된 경로에서만 동작합니다.

인자값으로 변경할 포트를 입력합니다.

```
upy sport <COM PORT>
```

<details>
<summary>사용 예시</summary>

기존 포트에서 'COM5'로 포트 변경 진행.

실행 결과

![sport_ex](res/sport_ex.png)
</details>

### Run
#### run
> 사용자 환경에서 작성된 Micropython 프로그램을 실행시킵니다. 

이 명령어는 사용자가 작성한 Micropython 프로그램을 칩에 설치된 인터프리터를 사용하여 프로그램을 동작시킨다는 것이 가장 큰 특징입니다. 사용자 환경과 칩의 환경을 분할시켜 주어 독립적으로 동작시킴과 동시에 즉시 프로그램을 실행시키기 용이합니다.

```sh
upy run <File name>.py
```

<details>
<summary>사용 예시</summary>

'hello_world.py' 파일 생성 후 다음과 같이 입력 및 저장

```python
print("hello world!")
```

실행 결과

![run_ex](res/run_ex.png)
</details>

### File
#### put
> 파일을 칩에 저장시킵니다.

사용자 환경에서 작성된 Micropython 프로그램을 칩의 파일시스템에 저장시킵니다. 단순 파일 저장을 넘어 사용자 지정 라이브러리 등록, boot 및 main 프로그램도 등록할 수 있어 칩의 활용도를 높여줄 수 있습니다.

인자값을 총 두 개까지 입력할 수 있습니다
- 첫 번째 인자 : 저장할 파일 이름
- 두 번째 인자 (선택) : 칩에 저장할 때 붙여질 새로운 이름

```sh
# Use original file name
upy put <file name>.py

# Attach new name
upy put <file name>.py <new name>.py
```

<details>
<summary>사용 예시</summary>

사용자 환경에서 'test.py' 파일 생성 후 다음과 같이 입력 및 저장

```python
print("hello world!")
```

다음 명령어를 통해 칩에 파일 저장

```sh
upy put test.py
```

만약, 새로운 이름 (예시 : temp)로 저장할 시 다음과 같이 입력

```sh
upy put test.py temp.py
```

실행 결과

![put_ex](res/put_ex.png)
</details> 

#### get
> 파일 내용을 읽고 출력합니다.

칩에 저장된 파일 내용을 읽고 터미널에 출력합니다. 칩 내에 저장된 파일의 원본이 소실되었거나 다른 작업자와 협업할 때 등 활용할 수 있습니다.

인자값으로 칩 내에서 불러올 파일 이름을 입력합니다.

```sh
upy get <file name>
```

<details>
<summary>사용 예시</summary>

사용자 환경에서 'test.py' 파일 생성 후 다음과 같이 입력 및 저장

```python
print("hello world!")
```

다음 명령어를 통해 칩에 파일 저장

```sh
upy put test.py
```

get 명령어를 통해 파일 내용 확인

```sh
upy get test.py
```

실행 결과

![get_ex](res/get_ex.png)
</details> 

#### upload
> 파일을 컴파일하여 칩에 저장합니다.

Micropython 파일을 바이트코드 파일로 변환시켜 칩에 저장시키는 기능입니다. 경량화 및 은닉화 등의 목적으로 활용될 수 있습니다. 

인자값을 총 두 개까지 입력할 수 있습니다
- 첫 번째 인자 : 저장할 파일 이름
- 두 번째 인자 (선택) : 칩에 저장할 때 붙여질 새로운 이름

```sh
# Use original file name
upy upload <file name>.py

# Attach new name
upy upload <file name>.py <new name>.mpy
```

<details>
<summary>사용 예시</summary>

사용자 환경에서 'test.py' 파일 생성 후 다음과 같이 입력 및 저장

```python
print("hello world!")
```

다음 명령어를 통해 칩에 파일 저장

```sh
upy upload test.py
```

만약, 새로운 이름 (예시 : temp)로 저장할 시 다음과 같이 입력

```sh
upy upload test.py temp.mpy
```

실행 결과

![upload_ex](res/upload_ex.png)
</details> 


### File System 

#### df
> 칩 파일시스템의 현재 용량을 확인합니다.

```
upy df
```

<details>
<summary>사용 예시</summary>

실행 결과

![df_ex](res/df_ex.png)

</details>

#### ls

> 칩 파일시스템의 현재 경로에 있는 모든 폴더/파일들을 출력합니다.

인자값으로 특정 경로를 입력하면 해당 경로의 모든 폴더/파일들을 출력합니다. 입력하지 않는다면 최상위 경로 ('/') 를 출력합니다.

```sh
upy ls

# Specific path
upy ls path
```

