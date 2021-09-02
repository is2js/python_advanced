# first-class functions = 일급함수
# - closure->파생되는 decorator의 관계
# - 이러한 것은 javascript나 다른 언어와 같이 < 일급함수 = 함수형 프로그래밍 = 일급 객체> 를 지원하기 때문에 사용할 수 있음.

# 1) 파이썬 변수 범위(global)
# - 인자를 받는 함수를 만들어 scope를 본다.

# 1-1) NameError: 함수내부도, 전역에도 없는 변수를 불렀음.
def func_v1(a):
    print(a)
    print(b) # 밖에 선언되거나, 인자로 받지 않아서 에러 남.
    # b를 출력을 하려면 인자로 받았어야함.
# 예외
# func_v1(5) # NameError: name 'b' is not defined


b=10 # 여기는 전역scope다. 함수내부에서 참조할 수있음. 에러 안남.
def func_v2(a):
    print(a)
    print(b) # 인자로 안받았다면, 전역에서 찾아서 쓴다.

func_v2(5) 


# 1-3) UnboundLocalError : 함수내부(local)에는 존재하지만, 할당하기 전에 호출(참조)했다.
# AAA 전역에 먼저 존재하더라도, **일단은 사용(참조) 뒤쪽이라도 내부local이 먼저다.**
# - 파이썬 runtime의 interpret는 참조 등의 실행이전에, local영역전체에 b가 있는 것만 체크를 함. 참조 뒤쪽에 있더라도 로컬에 있는 것임.
# AAA runtime의 interpreter는 있는지 체크만 하며, 지역변수가 우선이며, 지역에 존재한다면 전역변수는 아예 참조도 안됨.
b=10 # 여기는 전역scope다. 
def func_v3(a):
    print(a)
    print(b) # 인자로 안받았다면, 전역에서 찾아서 쓴다.
    b = 5

# func_v3(5) #UnboundLocalError: local variable 'b' referenced before assignment

# 1-4) dis : bytecode의 실행흐름을 보는 패키지
# - UnboundLocalError(지역에 존재안했거나 or 지역에 존재하지만 할당전참조)나는 함수를 집어넣어서 확인한다.
from dis import dis
# print('EX1-1 - ', dis(func_v3))
#  31           0 LOAD_GLOBAL              0 (print) : local print함수 로드
#               2 LOAD_FAST                0 (a)    : local a로드
#               4 CALL_FUNCTION            1    : print(a) 호출call
#               6 POP_TOP

#  32           8 LOAD_GLOBAL              0 (print) : local print 로드
#              10 LOAD_FAST                1 (b)    : local b 로드
#              12 CALL_FUNCTION            1    : print(b)호출 -> b가 아직 할당안되어있어서 에러
#              14 POP_TOP

#  33          16 LOAD_CONST               1 (5) : local 상수 5를 local b에 저장.
#              18 STORE_FAST               1 (b) : print(b)이후에야 b가 저장(할당)됨
#              20 LOAD_CONST               0 (None)
#              22 RETURN_VALUE


# 2) Closure
# AAA 반환되는 내부의 함수에 대하여, 선언된 연결 정보를 가지고 참조하는 방식
# AAA 반환 당시 함수의 유효범위를 벗어난 변수or메소드에 직접 접근 가능하다.

# 2-1) closure전에 누적을 해보자.
a = 10
print('EX2-1 - ', a+10)
print('EX2-2 - ', a+100) # 독립적으로 계산되어, 누적시킬 순 없다.

# 누적시키는 방법은??? reduce or sum()처럼 누적된 합을 구할 수있다.
print('EX2-3 - ', sum(range(1,51)))
print('EX2-4 - ', sum(range(51,101)))

# 2-2) 누적 함수를 class를 만들어 callable 객체()로 구현하고 싶다.  class 실습
# - 객체에 빈 list를 가지고, 거기서 계속 누적하며, call(variable)시 그 변수를 append한 뒤, 결과값은 print or return만 데이터만 보존시키도로록 하는 객체.
# - 객체가 1개만 있어도 다 하는 누적기능의 객체
# - 더할때마다 (평균을) 누적시키는 객체를 만들기 위한 class
# - 생성시 빈 list를 생성하여, 더해주고, 길이만큼 나눠주면 평균
class Averager():
    def __init__(self):
        self._series = []
    
    # callable메소드를 오버라이딩 해서, 객체를 (v)로 직접호출할 수 있게 한다.
    # - 객체를 직접호출할 땐, self외 먼가를 받아서 바로 처리할 수 있게끔 편하게??
    # - 값은 저장 : 객체마다 생기는... 빈 list에 값을 append해줄 수 있게 된다.
    # - 결과물은 print + return만!(저장X, 변수 계속 들어오니까) : append해놓고 결과는 print로 평균을 보여주면 된다.
    # - 빈 list의 데이터만 유지하자.
    def __call__(self, v):
        self._series.append(v)
        print("class >>> {} / {}".format(self._series, len(self._series)))
        return sum( self._series) / len(self._series)

# - 이름을 class라고 짓는다. 객체가 객체()로 callable하니까?
avg_cls = Averager() # 객체는 따로 뭘 안받는다. 내부  빈 list만 생성됨.
print('EX3-1 - ',avg_cls(15)) # EX3-1 -  10.0
# - 누적이 되는지 보자.
print('EX3-2 - ',avg_cls(35)) # EX3-2 -  25.0
print('EX3-3 - ',avg_cls(40)) # EX3-2 -  30.0 [15, 35, 40] / 3

# AAA 누적이 가능한 이유?
# - 객체의 인스턴스변수 안에 append로 값 누적
# - python에서는 class의 객체가  dict형태(key:values)로 attribute로 가지고 있기 때문
# AAA 가져다 쓰는 sum()함수도 내부적으로 이런식으로 구현되어있다. class->객체->callabe 객체() -> 내부에서 저장후 결과값 반환
# avg_cls.__dict__ # _series: -[ 15, 35, 40, ]



# 2-3) 내장함수, class가 아닌 closure(2중함수)로 구현
# AAA closure 패턴은 2개 이상의 함수로 구현되어있다.
# - [반환되는 내부함수] -> 함수안에 함수가 있는 구조다.
# - [함수 반환당시의 유효범위]를 넘어서서 사용할 수 있다.

# 2-3-1) 내장함수, class가 아닌 함수(함수반환-함수)를 선언한다.
def closure_avg1():
    # 2-3-2) 데이터를 저장하는 곳을 인스턴스변수가 아닌 local변수에 선언한다.
    series = []

    # 2-3-3) 함수를 반환해주는 함수를 선언한다.
    # - 이 안(2차함수)에서는 [가정]외부에서 받아올 변수(v)를 받아준다.
    # - 마치 __call__메서드에서 하듯이.. 외부받아 내부에 넣고 처리/반환까지 
    def averager(v):
        series.append(v) # - 함수내부에서는, 바깥 것(1차함수의 데이터저장변수)을 참조 가능하다!
        # - 외부변수v를 받아 처리할 로직을 다 처리한다.
        print("def >>> {} / {}".format(series, len(series)))
        # 2-3-4) 이제 2차함수의 scope를 벗어나기 위한 return을 해준다.
        # - 1차함수로 돌아와야함.
        return sum(series) / len(series)

    # 2-3-5) 1차함수(main함수)에서는 2차함수(내부함수)를 실행부없이 return해준다.
    # -> 실행부없는 [return 함수] -> 바깥에서 1차(main)호출시, return함수의 실행부()도 호출해야함.
    # -> average()가 return된 거이 아니라 아직 리턴안되었다.
    return averager


# 2-3-6) 메인함수를 호출해도, 아직 함수상태다. 내부함수의 실행부를 안 넣어줬기 때문
# - 내부함수에서는 메인함수의 변수(series) + 외부에서 들어올 가상인자(v)를 받아 처리할 수 있는 로직이 있다.
# - class로 구현한 누적-__call__(self, v)와 같은 역할이다.
# - 특히 내부함수라서.. <Locals>.함수다. return만 되어있고 진행은 안되어있음.
avg_closure1 = closure_avg1()
print('EX4-1 - ', avg_closure1) #  <function closure_avg1.<locals>.averager at 0x009E34F8>
print('EX4-2 - ', avg_closure1(15)) #  <function closure_avg1.<locals>.averager at 0x009E34F8>
print('EX4-3 - ', avg_closure1(35)) #  <function closure_avg1.<locals>.averager at 0x009E34F8>
print('EX4-4 - ', avg_closure1(40)) #  <function closure_avg1.<locals>.averager at 0x009E34F8>


# 3) 어떻게 이런 일이 가능할까? 이중함수구조-> 실행하지않은 외부변수사용 내부함수반환 -> 메인() + (v, 내부함수실행부)
# AAA python에서는 def 메인(외부)함수<-->  def 내부함수 사이 공간을 < Free variable 영역>이라고 한다.
# - class에서는 객체라면 계속 참조가능한 인스턴수변수에 [] list를 보관하고 업데이트 해줬지만,
# - function에서는 <Free variable영역의 변수는 > global변수도 아닌데 데이터를 물고 + 외부변수와 함께 누적되서처리가 가능해진다.
# - 메인함수를 이용해 <실행되지않는 내부함수>를 호출 할때마다 데이터가 보존되어있다.
# AAA 원래는 함수가 끝나면, 자기영역의 변수는 소멸되야 정상이다.
# AAA 소멸되지 않고 내부함수에서 계속 참조가능한, Free variable영역(=반환함수의 유효범위를 벗어난)의 변수를 활용하기 위해
# AAA 누적, 지속가능하도록 처리하는 것이 클로져다.

#  def closure_avg1():
# ** Free variable영역**
#     series = []
# 
# ** 클로저 영역**
#    def averager(v):
#       ...
#   return average

# - 만약, 내부함수안에 series = []를 선언하면? Free variable영역X + local우선이므로 그변수를 참조 -> 호출시 
# - 일급객체 = 실행부X함수를 객체, 변수, 함수처럼 사용

# AAA 마우스 클릭 횟수등, 누적횟수를 체크할 때 closure를 많이 사용한다.
# AAA title저장, 웹에서의 로그 에서 많이 사용된다.
# AAA 전역변수를 감소 + 전역series=[]에 선언할거를 은닉화 + 디자인 패턴 적용 + 


# BUT 프로그램 종료직전까지 물고 있으니, 조심해야한다.

# my) 데이터를 물고 있어야하면서 & 외부입력에 대한 처리가 필요할 때
# -> class의 객체로 가지고 다닌다. or closure로 만든다.



# 4) Free variable 영역 출력해보기
# - closure는 함수라서, dir() -> __code__ -> co_freevars 출력해보기
print('EX5-1 - ', dir(avg_closure1))
print('EX5-2 - ', dir(avg_closure1.__code__))
print('EX5-3 - ', avg_closure1.__code__.co_freevars) # EX5-3 -  ('series',) 튜플형태로 내부함수영역 밖에 변수를 가지고 있다.
# print('EX5-4 - ', dir(avg_closure1.__closure__[0])) # 클로져자체도.. 함수? 
# print('EX5-5 - ', dir(avg_closure1.__closure__[0].cell_contents)) # 클로져 자체도 함수며, 명령어를 보니 튜플이나 리스트로... 보관?


# 5) 잘못된 closure 사용 예

# 5-1) Free variable영역에 데이터를 list가 아닌 int형 변수 사용
def closure_avg2():
    # Free vairable
    # - 평균을 똑같이 계산하는데, list형태의 데이터가 아닌, 갯수와 총합만 저장
    cnt = 0
    total = 0
    # list_ =[]
    tuple_ =tuple()
    str_=''
    def average(v):
        # - 일단... 변수가 사용안된 표시가 나는.. 에디터..
        # list_. 사용시는.. 사용했다는 불이 들어오는 에디터..
        # 5-2) 클로저에게 Freevairable 영역 변수 사용하는 예약어로 알려준다.
        nonlocal cnt, total
        cnt += 1 # 호출되어 , 뭐가 하나(v) 들어올 때마다 자유변수에 +1
        total += v
        # str_+=v # string도 nonlocal 없으면 데이터 사용 불가.
        # tuple은 list처럼 사용 가능.
        print('def2 >>> {} / {}'.format(total, cnt))
        return total / cnt
    return average

# - 위에것과 똑같음(자유영역에 변수 + 내부함수 실행부없이 return + 내부함수는 외부실행시받을 변수+ FV영역 보존 변수 처리항목)

avg_closure2 = closure_avg2()
print('EX5-6 - ', avg_closure2(10)) # UnboundLocalError: local variable 'cnt' referenced before assignment
print('EX5-7 - ', avg_closure2(15)) # UnboundLocalError: local variable 'cnt' referenced before assignment
# my) 전역변수에 관련해서는 없는 걸 부르면 NameError
# my) local 참조시 변수가 없거나 변수할당전에 부르면 UnboundLocalError
# -> 예약어 nonlocal은 내부함수에, Freevaraible변수(int형..) 을 사용할 수 있게 알려주는 것이다.


# closure는 언제 사용할까?
# 1. 누적치
# 2. 함수형 프로그래밍 중에, 영역밖 데이터를 snapshot수 보존하여 물고 다니면서 처리해야할 때
# - 공통으로 사용하는 데이터보존 누적/처리시
# 3. closure를 모를 땐, class로 객체인스턴스변수에 데이터 보존
