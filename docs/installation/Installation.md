# 개발환경 구축

## Visual Studio Code

Visual Studio Code(VSCode) 란 MS에서 Electron 프레임워크를 기반으로 개발된 무료 프로그램으로으로 추가로 원하는 확장 기능을 설치해야 IDE로 사용 가능합니다. 윈도우를 비롯해 리눅스 Mac을 모두 지원하며 파이썬을 비롯해 다양한 언어와 부가 기능을 수 많은 확장 기능으로 지원합니다.

### VSCode 설치 및 세팅

상술하였듯 VSCode 편집기를 IDE로 사용하기 위해선 다양한 Extension들을 설치해주고 직접 설정해주어야 하는 불편함이 있습니다. 한백전자에서는 이러한 불편함을 해소시키기 위해 Windows에서 VSCode 및 pwsh 등 여러 편리한 개발환경들을 자동으로 설치해주는 스크립트를 제공합니다. 설치하는 방법은 다음과 같습니다.

1. 위 링크에 접속한 후 설치에 필요한 zip 파일을 다운로드 받습니다. 그 후, 압축을 해제합니다.

<img src="https://github.com/hanback-lab/TiCLE/blob/main/pictures/download_guide.png" width=100%>

&nbsp; [Installation files](https://github.com/hanback-lab/TiCLE/blob/main/tools/Environment_Install.zip)

2. 파일 탐색기를 열어 배치파일을 설치한 위치로 이동한 뒤, 탐색기 주소창에 'cmd' 라고 입력하여 명령 프롬프트 창을 띄웁니다.

![turnon_cmd](https://github.com/hanback-lab/TiCLE/blob/main/pictures/turnon_cmd.png)

<br>

3. 다음 명령어들을 순차적으로 실행합니다.

```
.\PrePkgInst.cmd
.\VSCodeInst.cmd
.\PostPkgInst.cmd
```

![pre](https://github.com/hanback-lab/TiCLE/blob/main/pictures/execute_pre.png)

![vscode inst](https://github.com/hanback-lab/TiCLE/blob/main/pictures/execute_vscodeinst.png)

![post](https://github.com/hanback-lab/TiCLE/blob/main/pictures/execute_post.png)

<br>

이 후, 파일 탐색기를 열어 다음 경로로 이동합니다.

```
C:\VSCode\
```

Code.exe 파일을 실행시켜 VSCode를 실행시킵니다.

## Upyboard

다음 링크를 참고바랍니다.

- https://github.com/hanback-lab/TiCLE/blob/main/docs/upyboard/upyboard.md