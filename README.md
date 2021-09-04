## 개요
 - python의 심화된 내용을 py파일에 주석으로 번호를 매기며 실습합니다.
 - 주석을 따라가면서 클론코딩 해보세요.
    - 개인적인 의문 or action 전의 행동 `QQQ`, 새롭게 알게 되거나  아차~! 싶은 내용들은 `AAA`로 표기되었습니다.

## 목차
 - 01~03 : 클래스/인스턴수 변수와 메서드, class 실습(Student)
 - 04 : 데이터모델-namedtuple
 - 05 : 데이터모델-magic method in class
 - 06 : advanced list-시퀀스/list comprehension/generator(like tuple comp) 
     - container(서로다른 자료형담기) : `list` `tuple` collections.deque
     - flat(1개 자료형만 담기) : str bytes bytearray `array.array` memoryview
     - mutable(원소들 재할당 가능) : `list`, bytearray, array.array, memoryview, deque
     - immutable(추가는되나 원소재할당시 에러) : `tuple` str bytes

 - 07 : advanced tuple-패킹, 언패킹/ 가변vs불변형/ list의 재할당 주의/ sort vs sorted
     - sorted(), sort() 주요인자 : reverse, key=len, key=str.lower, key=func(lambda)
 - 08 : sequence_dict : hash/dict comp(csv실습)/setdefault/사용자정의Dict class 실습(UserDict)/immutableDict(MappingProxyType)
     - dict.setdefault(있으면사용/없으면생성할 key, 없을때 초기값ex>[] ) 초기값 상태에서 할 행동(ex .append()) 

 - 09 : sequence_set : frozen_set / {a} >> set([a]) by dis / set comprehension
 - 10: first-class functions_higher-order function : 함수라는 객체의 dir(attributes) / 변수에 할당 / 고위함수(high-order func)에 인자에 함수를 대입, map, filter(lambda) / reduce / lambda / callable, class 실습(LottoGame, __call__ 오버라이딩 -> 호출가능한 객체) / 다양한 매개변수 / signature / partial
    - 일급함수 :  함수를 일종의 값으로, 객체로, 변수로 봄. -> 함수형 프로그래밍 가능. 아래와 같은 기능들을 가짐.
    - 런타임 초기화 = 실행시 초기화 가능
    - 함수도 다른class들의 객체처럼, 객체라 dir()로 attribute가 존재한다.
    - 함수를 변수 등에 할당 가능 ex> 데코레이터, 클로져
    - 함수를 함수인수로 전달 가능 ex> sorted( , key=len) (,key=lambda x:x[-1])
    - 함수를 함수 결과로 반환 가능 = return functions(재귀함수, 데코레이터 등)
 
 - 11: first-class functions_closure  : 파이썬 변수 범위 + dis / 누적을 위한 class 실습(Averager) / closure, clsoure 영역 출력(closure.__code__.co_freevars), 잘못된 예와 nonlocal /  
    - `LEGB` : 함수안에서 식별자 찾는 우선순위
        * **Local** : 함수내부의 x를 먼저 찾는다.
        * **Enclosing** : 함수를 감싸고 있는 것의 x
        * **Global** : 함수 밖의 x와 sync를 맺어서 찾아온다.
        * **Builit in** : 내장함수? Built in 영역까지 확인
    - My closure: Free variable영역의 데이터 보존(like 객체 생성자 속 인스턴수변수에서 데이터 생성후 보존) + 내부함수에서 외부변수(v)받으면서 데이터 처리 가능
    - closure의 list, tuple이 아닌 FreeVariable변수는 내부함수에서 nonlocal로 직전영역(FV영역)과 sync를 맞춰서 사용한다.

 - 12: first-class functions_decorator : @perf_clock deco실습 / @decorator 미사용 == closure처럼 사용 -> @decorator사용 비교 /  
    - 함수명 : func.__name__ / 매개변수들(튜플) : ', '.join( repr(arg) for arg in args)로 데코안에서 출력 가능.
    - closure와 비교시, 메인함수-FreeVaraible영역의 보존데이터 물고사용 대신 메인함수-func실행부없는 함수를 받아 -> 내부함수(클로져영역)에서 외부변수(*args 등)을 받아 실행과 동시에 추가작업후 func() 결과 return -> 메인함수에서는 내부함수 실행없이 return -> 밖에서 @데코만 붙여주면 알아서 func(v)만 실행 대신 데코함수+(v) 실행부 붙혀서 실행됨.

    ```python
    def 데코_이름( func ):
        def 내부_함수( *외부인자 ):
            # func실행전 작업
            result = func(*외부인자) # return해줘야할 원래함수 결과
            # func실행후 작업
            # 필요하다면 print로 추가작업 
            print(f"데코실행 >>> 실행 중 함수이름: {func.__name__}({ repr(arg) for arg in 외부인자}) -> result: {result}")
            return result
        return 내부_함수

    ```
 - 13: Object reference_reference : is vs __eq__ with tuple / copy vs deepcopy(class 실습(Basket))/ copy패키지(shallow, deep) /  함수 매개변수 전달 사용법(함수 내부에서도 전역변수라도, 원본이 변한다.) / 불변형 4가지의 deepcopy불가(같은 값-> 어떻게 생성하든 같은id 바라봄.)
    - 불변형 중 일부는(only tuple, string)으로 값 자체에 hash, id를 가지지 않는 이상 -> 같은값 할당:다른id / 같은값의 변수할당: 같은id for 효율성
    - 같은 값의 변수를 이용해서, deepcopy하고 싶다면 생성자(list(), dict())등을 활용하자. 생성자들은 iter변수를 받아도, 알아서 *언패킹 -> 패킹처리하여 값만 빼온다.
    - list안에 불변형(tuple)을 넣지말자. 데이터 변경시 새로운 객체를 생성(id달라짐)하는데 코스트가 많이 든다.
    - deepcopy의 목적 : 원본수정안되게 or 연결된 원본버리고 새로운 객체
    - deepcopy의 방법 : list()등의 원본+생성자활용 / copy패키지
    - shallow copy(얕은 복사)는 표면적인 객체id만 새로 생성하지만, 내부 속성들(.__dict__의 모든 것)들은 연결된 그대로의 id를 참조하고 있다.
    - 함수의 매개인자로 넘어갈때는, 가변형/불변형을 생각하자.
        - 가변형(list) : id가 그대로 넘어가서 함수내부에서 원본이 수정됨(할당 조심)
            - 원본이 변경되도 상관없을 경우 사용.
        - 불변형(tuple) : id, 객체가 복사되서 넘어가서 원본과 별개지만 코스트가 너무 클 수 있다.

    - 불변형은 값:id=1:1이다. 어떻게 생성을 하든 tuple,str,btye,frozenset은 같은 값-> 같은 객체를 바라본다.
        - 사본생성을 하지 않는다. 같은 값이면 다 원본이다.

 - 14: Class method advancded : private __x  + @property(getter)-> @(getter).setter class 실습(VectorP) / slot - 명령어, 반복시 걸린시간 (by timeit) 비교- class 실습(TestA, TestB) , repeat_outer + timeit deco실습 / 
    - 객체 생성시부터 인스턴스변수들에 조건을 걸고 싶은데, 생성자에서만 걸면 나중에 직접접근으로 변경/오염된다. -> 생성자에서 걸면 안좋다.
    - self._x 는 예의상 표시용이었다면 -> self.__x로 외부접근 막고 + @propery -> @p.setter로 -> setter에 조건에 맞는 데이터를 받고/getter로 꺼내기만 하자. 

 - 15: Class method advanced : __len__ __getitem__ for slicing  class 실습(Objects) / 추상클래스, abc 설명 / sequence관련 메소드를 가진 추상클래스 / 
    - 추상클래스는 수백가지 자식class들이 공통으로 정의한 변수,메서드들의 naming을 사용해서 정의되게 함. 

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

### 참고) interpreter관련 에러가 난다면
 - https://github.com/microsoft/vscode-python/issues/11924
```
For anyone running into this issue, you can add this to your settings to workaround the problem:
"python.experiments.optOutFrom": ["pythonDiscoveryModule", "pythonDiscoveryModuleWithoutWatcher"],

Also, for folks running into this problem, before you optout, can you do the following so we can narrow down the issue. Using the CPU profiles here we addressed few of the problems. But it is not enough for some of the cases.

Remove any "python.experiments.optOutFrom" setting.
Set this in your user settings: "python.logging.level": "info".
Reload VS code and open a python file.
Extension causes high CPU problem or Loading takes too long or loading fails.
Copy the "Output" > "Python" log contents and share (redact any username or data that you don't want to share).
Remove the "python.logging.level": "info"
Use this optOut "python.experiments.optOutFrom": ["pythonDiscoveryModule", "pythonDiscoveryModuleWithoutWatcher"],
```


### 가상환경 package 다루기

1. 설치된 것 들 확인 : `pip list`
2. 검색 : pip `search` simple* -> `현재 안됨`
3. 설치 : pip `install` pkg
    -  업그레이드 : pip `install --upgrade` pkg
4. 설치된 것을 확인 : pip `show` pkg 
5. 삭제 : pip `uninstall` pkg


