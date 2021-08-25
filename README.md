## 파이썬 심화 학습
 - py파일에 주석으로 차근차근 작성되었습니다.
 - 주석을 따라가면서 클론코딩 해보세요.


## 환경설정
 - 찾기 쉬운 경로인 `C:\`안에 `python_advanced`로 폴더를 만든다.

### WSL로 인해 window의 python이 실행안된다면?
 - settings에서 `integrated default profile`을 검색하여, 기본 터미널을 새로 설치한 powershell7으로 설정해주자.
 
 ![image-20210824113209852](https://raw.githubusercontent.com/is3js/screenshots/main/image-20210824113209852.png)

### interpreter 선택

 - vscode palette를 열어서 `python select interpreter`를 선택하여, 설치한 default python을 선택해주자.

### task runner로 디버깅 없이 실행
 - 디버깅 or 디버깅없이 실행 : F5, ctrl+F5
     - 불필요한 경로 프린트 및 실행이 오래 걸림
     
 - 팔레트(F1, c+s+p) -> task 검색 -> task configure -> task.json만들기 -> 아래 내용 복붙
     - 실행 단축키: `ctrl+shift+b`
     - options env PYTHONENCODING : utf-8 : 한글설정
     - ${file} : 실행될 파일이 설정됨

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Project Label",
            "type": "shell",
            "command": "python",
            "args": [
                "${file}"
            ],
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "options": {
                "env": {
                    "PYTHONIOENCODING": "UTF-8"
                }
            },
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

### 가상환경 세팅
 - 작업폴더 직전 상위 폴더로 이동해주자.
     - 나는 c:\python_advanced이므로, c:\로 이동하면 된다.
     - 터미널에서 c:\로 바로 이동할 때는 `cd \`를 이용하면 된다.
 - `python -m venv .\python_advanced\`
     - python -m venv [가상환경파일들을 생성할 폴더]
     - 해당 폴더명으로 가상환경이 생성된다.
     - **만들고 싶은 가상환경이름의 폴더**를 여기서는 프로젝트 폴더에 넣어준 것이다.
 - 가상환경 실행을 위해 해당 폴더로 이동한 뒤, 실행시킨다.
     - 윈도우에서는 **SCripts폴더**, mac에서는 **bin폴더**에서 on/off파일이 있다.
     - 즉, Script폴더안의 act/deactivate를 실행시키면 된다.
 ```shell
 cd python_advanced
 dir
 cd scripts
 .\activate
 .\deactivate.bat
 ```
 
 - 뭔가 환경이 꼬였다면, **가상환경폴더 3개(include, lib, scripts)만 삭제하면된다.**
 
 
 - **vscode 후 activate라면,  팔레트를 열어서 scripts폴더에서 직접 지정해준다.**
     - 터미널 실행부터 한다면, activate후 code 를 치면, 자동으로 가상환경 -> **가상환경 안되어있는 것 같아도 pip list치면 가상환경 내용임.**
     
```shell
C:\Users\is2js> cd \
C:\> cd .\python_advanced\
C:\python_advanced> .\Scripts\activate
(python_advanced) PS C:\python_advanced>
(python_advanced) PS C:\python_advanced>
(python_advanced) PS C:\python_advanced> code .
```

### 가상환경 package 다루기

1. 설치된 것 들 확인 : `pip list`
2. 검색 : pip `search` simple* -> `현재 안됨`
3. 설치 : pip `install` pkg
    -  업그레이드 : pip `install --upgrade` pkg
4. 설치된 것을 확인 : pip `show` pkg 
5. 삭제 : pip `uninstall` pkg


## 목차
 - 01~03 : 클래스/인스턴수 변수와 메서드


