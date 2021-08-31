# first-class functions = 일급함수
# - 모든 것을 객체로 다루는 python 뿐만 아니라 함수형 프로그래밍도 관련되어 있다.
# - 함수형 프로그래밍 = 함수를 객체 취급하는 프로그래밍.
# - higher-order function = 고(준)위 함수
#  = 함수를 인자로 전달하거나 함수를 결과로 return

# 1) 파이썬 함수의 특징
# 1-1) 런타임 초기화 = 실행시 초기화 가능
#      함수도 다른class들의 객체처럼, 객체라 dir()로 attribute가 존재한다.
# 1-2) 함수를 변수 등에 할당 가능 ex> 데코레이터, 클로져
# 1-3) 함수를 함수인수로 전달 가능 ex> sorted( , key=len) (,key=lambda x:x[-1])
# 1-4) 함수를 함수 결과로 반환 가능 = return functions(재귀함수, 데코레이터 등)


# 2) 함수 객체의 속성 vs class 객체 예제 (함수도 객체며, 부모 class의 attr를 가진다.)
def factorial(n):
    """Factorial Function -> n:int"""
    if n< 2:
        return 1
    return n * factorial(n-1)

print('EX1-1 - ', factorial(5))
print('EX1-2 - ', factorial.__doc__)
    
#  빈 class라도, 상속되는 magic method나 builtin method가 있다.
# - 내부에 정말 많은 메서드, 속성들을 출력해볼 수 있다.
class A:
    pass 

# - 함수와 class가 가진 속성들을 dir()로 볼 수 있다.
# - 먼저 타입을 보면 def function type도 class의 객체 취급을 한다.
# - 객체가 아닌 class Class의 type은.. CLass들의 부모=메타클래스=Type class라서 type으로 뜨는 것 같다.
# - my) class자체의 type은 type class다.
# - cf) 클래스내부의 속성값 + 메서드 싹다 합해서 python의 attribute라고 한다.
print('EX1-3 - ', type(factorial), type(A)) # <class 'function'> <class 'type'>

# 함수, class모두 class의 객체다 -> 해당 class의 attr를 살펴보자.
# print('EX1-4 - ', dir(factorial), dir(A)) # <class 'function'> <class 'type'>
# function attr:  ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# class  attr :  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weaef__']
# 차이점
# print('EX1-4 - ', set(dir(factorial))-set(dir(A))) # <class 'function'> <class 'type'>
# func - class:  {'__code__', '__defaults__', '__qualname__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__annotations__', '__call__', '__closure__'}
# class - func: {'__weakref__'}
# AAA class에는 없는 함수만 가지는 attribute로는 
# - __qualname____globals____annotations____call____closure__ 등이 있다.
# AAA sense list-list를 set으로 바꿔서 뺄땐, 각각을 미리 sorted해놓고 빼면 정렬된 빼기가 나온다?
print('EX1-4 - ', set(sorted(dir(factorial)))-set(sorted(dir(A)))) # <class 'function'> <class 'type'>
# -> 안됨..
# __code__', '__defaults__', '__qualname__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__annotations__', '__call__', '__closure__'}
# 이중에는 closure, callable, global 등을 공부할 것임.

# AAA name이라는 메서드는 함수이름을 string으로 제공해준다.
# cf) flask에서 __name__은 실행시 모듈실행시-> 모듈명 / script로 실행시 __main__이 넘어온다.
print('EX1-5 - ', factorial.__name__)
# AAA code이라는 메서드는 내부코드들 + python작업 경로
print('EX1-6 - ', factorial.__code__)
# <code object factorial at 0x000001B6F8560EA0, file "c:\python_advanced\10_일급함수_higher_order_function.py", line 14>




# 3) 함수를 변수에 할당해서 사용
# 인자가 없는 상태로 ()의 함수 실행부를 제외시키고 할당시킨다.
var_func = factorial
# - 찍어보면, 실행전 함수상태다.
# - 찍어보니, 같은값을 할당 = id도 같다.
print('EX2-1 - ', var_func, id(var_func), id(factorial)) # <function factorial at 0x0328A3D8>
print('EX2-2 - ', var_func(5)) # 
# - map함수의 첫번재 인자로 실행안한 함수를 받는다. 
# - 변수할당 함수를 넣어주자(할당안하고 원형 실행x상태로 넣어도 상관없음)
print('EX2-3 - ', map(var_func, range(1,6))) # <map object at 0x03B7B3F0>
# map은 list로 형변환 해야 나옴
# my) 어떤 함수의 실행결과들을 모으고 싶다면, list(map(func, ))으로 돌려서 모으자.
print('EX2-3 - ', list(map(var_func, range(1,6)))) 







# 4) higher-order function = 고(준)위 함수
#  = 함수(실행부빼고)를 인자로 전달하거나 함수를 결과로 return
# 4-1) 함수를 인자로 전달할 수 있다.
# AAA filter(lamdba x:x조건문True, 데이터)를 통해 한번 필터링 시킨 데이터를 사용
# - map함수의 인자에는 함수가 들어간다.
# AAA filter함수의 인자에는 T(0이외값)/F(0)반환하여 필터링해주는 lambda함수가 들어간다.
# - my) 0이 나오는 lambda식은 필터링 된다. 
# AAA 홀수 필터링 -> 짝수는 0나오게 -> by x % 2
# - my) A만 필터링하고 싶다 -> 나머지를 제외하고 싶다 -> 나머지=(전체-A)가 0을 반환하도록 lambda를 짜자.
print('EX3-1 - ', list(map( var_func, filter(lambda x: x%2, range(1,6)))))
# AAA list comp의 if로 필터링해도된다. if A(홀수)만 고르기 or A제외한 부분(짝수)들이 0나오게 짜기
# - list comp가 효율이 더 좋다.
print('EX3-2 - ', [ var_func(i) for i in range(1, 6) if i % 2])

# 번외) 필터링 방법 : if A 만족조건 or A제외가 0을 반환하게 조건짜기

# 4-2) reduce(): 누적
# AAA 어려워한다. deprecated되어서 권장되지 않는다.
# AAA 하지만 다른 언어들이 많이 사용하고 있는 개념이기 때문에 알아야함.
# - 많이 안쓰여서 별로도 불리되었다.
# - 함수를 인자로 받는 map, filter와는 다르게 내장함수X
from functools import reduce
from operator import add 
# +대신 add(,,,)로 실행해서 사용 -> 인자에 +를 넣을순 없으니, 인자에 함수는 가능하니.
# - 누적되는 것이, 직전 누적값을 가지면서(for문 위 변수처럼), 값을 하나씩 돌아가며 인자함수에 넣어준다. 
print('EX3-3 -', reduce(add, range(1,11)))
# - sum()으로 모든 요소를 다 더할 수도 있는데, 
print('EX3-4 -', sum(range(1,11)))
# AAA 함수를 인자로 받는 상황(내가 만든 연산함수) + 누적해서 함수인자의 연산을 해야만 할 때 쓴다.

# 5) 익명함수(lambda)
# AAA 가급적 주석을 달아라
# AAA 가급적 함수를 사용해라.
# -  리팩토링(이름 붙이기)를 권장
# AAA 익명함수를 비실행 함수를 인자로 받는 고위함수에서 사용한다.
# - x에는 직전계산값이, t에는 새로운 값이 들어가면서 연산한다.
print('EX3-5 - ',reduce(lambda x, t : x+t , range(1, 11)))


# 6) Callable(핵심) : 호출 연산자 -> 메소드 형태로 호출가능한지 확인하는 것
# __call__ 매직메소드로서 func이라는 객체의 attr에 포함되어있다.
# ()로 실행부로 호출할 수 있다.

# 6-1실습) 로또 추첨기
# - reduce( , 데이터 ) x에 누적되면서, t값에 할당되는 데이터는 1개씩 줄여간다고 생각하자.
# - my) 데이터를 1개씩 줄여가면서 누적 계산한다.
import random # 랜덤이 필요하니 모듈 

# - class에는 내부 메소드를 가질 수 있고, 객체가 호출해서 사용
class LottoGame:
    # - 받아줄 게 없이 내부 자동 생성이니 self만 있으면 된다.
    def __init__(self):
        # - 뭔가를 안받아도 내부 속성을 데이터로 생성할 수 있다.
        # - list comp로 데이터를 생성해서 속성으로 만들어준다.
        self._balls = [ n for n in range(1, 46)]
    
    # - 뽑는 메소드 : 랜덤으로뽑고 -> 정렬해준다.
    def pick(self):
        random.shuffle(self._balls) # 객체 직접변환인가보다. 객체안에 있으니 오히려 좋을 듯
        # 반복용 list comp + for
        return sorted([random.choice(self._balls) for i in range(6)])

    # 6-4)
    def __call__(self):
        return self.pick()


# 객체 생성
game = LottoGame() # 내부에서 속성_balls 생성
# 게임 실행
print('EX4-1 - ', game.pick()) # 같은 것도 뽑힌다.

# 6-2) callable로 객체의  호출가능성 확인
print('EX4-2 - ', callable(str), callable(list), callable(factorial), callable(3.14))
print('EX4-3 - ', callable(game), callable(game.pick)) # False, True
# 객체는 호출할 수 없다. 객체의 인스턴스 메소드는 호출할 수 있다.
# - 객체()형태로 실행할 수 있다면, 즉 객체 = 인스턴스메소드가 되어버린다면 매우 편할 듯 하다.
# - game.pick()메소드를 game() 만으로 자동으로 호출 할 수 있다면? 매우 편할 듯.
# AAA 객체를 객체()로 호출가능하다면? -> 고위함수의 인자에 함수 - ()  대신 객체 -()를 넘겨서 객체()가 내부적으로 실행될 텐데
# print(game()) # TypeError: 'LottoGame' object is not callable
# - but 일반적으로는 객체()가 안된다.

# 6-3) __call__ 매직메소드 오버라이딩으로 
# AAA 객체 -> 객체() 가능 + return 원하는 객체의 메소드 호출()
# def __call__(self):
#     return self.pick()
# return시 원하는 작업(메소드-> 값 or 그냥 값 반화 등)을 걸어준다. 결과값이 나오면 될 듯.
# my) __call__ 오버라이딩만 해주면,, 객체를 callable한 상태로 업데이트시킨다.
# class의 __magic__ 메소드 오버라이딩은 객체끼리의 연산 뿐만 아니라.. 호출가능한 상태로 만들어주기도 한다.
# 6-5) 
print('EX4-3 - ', game())
print('EX4-4 - ', callable(game))


# 6-6) 
# AAA 객체를 호출가능한 상태로 만들었다? like 함수
# - Higher-order func의 함수인자 처럼, 변수/객체도 실행부뺀 함수의 인자/
# cf) class 잘짜놓으면 -> 객체가 함수처럼 취급(__call__), 객체가 변수처럼(인스턴스 속성, 클래스변수), class자체취급, class내부의 메소드들의 화력지원(인스턴스, 클래스, 스태틱)



# 7) 다양한 매개변수 입력받는 파이썬 특성(*args, **kwargs)
# - 혼란을 주기 위해 섞어서 배정함. 픽스된 인수, 패킹 등 4개를 받고 
# - 그대로 4개를 찍어서 어떻게 받는지 확인한다.
def  args_test(name, *contents, point=None, **attrs):
    return '<args_test> - ({})({})({})({})'.format(name, contents, point, attrs)

# 7-1) 1개만 넘겼을 때
# - 맨앞에 일반인수는 무조건 채춰야하며, 제일 처음 1개를 강제로 받아간다
# - 픽스된 변수 point는 앞에 것이 없어도, 들어가 있다.
# - *contents는 <<콤마로 연결된 값 1or2개>>가 패킹해서 넘기기 때문에, tuple로 들어온다.
# - 내부에서는 *를 빼고 사용하며, tuple이라 생각하고 처리한다.
# - **는 <<키워드=를 지정해준 인자들만 모아서>> 패킹하여 dict 형태로 넘겨준다.
# **- AAA 안넘어오면 빈 퓨틀(), 빈 dict {}가 찍힌다.**
# **my) 패킹 매개변수는 빈튜플, 빈dict가 default값이 있다!!**
print('EX5-1 - ', args_test('test1'))

# 7-2) 2개 넘겼을 때
# - 일반변수 name은 1개만 강제로 받는다.
# **- *패킹은 튜플로 넘어오는데, 1개의 값이라도 받아서 튜플 ('test2', )로 만들어서 넘어온다.**
# - 픽스된 인자(keyword방식)는 point=라는 keyword없으면 못받는다.
# **- **패킹은 dict가 넘어오는데, 인자들이 <<키워드='방식'>>로 들어가야한다.**
print('EX5-2 - ', args_test('test1', 'test2'))

# 7-3) 4개 넘겼을 때
# - 일반변수 name은 1개만 강제로 받는다.
# **- *패킹은 안으로는 튜플로 넘어오는데, <<2개의 콤,마>>를 스스로 묶어서 받는다.
# **AAA 튜플로 직접 묶어서 넘겨줘도 또다시 튜플로 내부패킹 하니, 절대 하지말 것**
# - 픽스된 인자(keyword방식)는 point=라는 keyword없으면 못받는다.
# ** **해킹은 keyword를 달고 있는 인자를 받아서 dict로 만들어 받는다.** -> {'id': 'admin'}
print('EX5-3 - ', args_test('test1', 'test2', 'test3', id='admin'))
# print('EX5-3 - ', args_test('test1', ('test2', 'test3'), id='admin'))
# args_test('test1', ('test2', 'test3'), asdf) -> (('test2', 'test3'),) 로 튜플이어도 1개의 인자로 인식하여 1개짜리 튜플로 받는다.


# 7-4) pix된 keyword방식 인수는, 순서에 상관없다.
print('EX5-4 - ', args_test('test1', 'test2', 'test3', id='admin', point=7))
# EX5-4 - (test1)(('test2', 'test3'))(7)({'id': 'admin'})

# 7-5) pix된 keyword방식 인수는, 순서에 상관없다.
# - **의 keyword=는 픽스된 keyword와 섞여도 순서에 상관없다. 중간에 픽스된 인자의 keyword가 있어도 상관없이 dict로 잘 들어간다.
# id='admin', <<point=7>>, password='1234'
# - 하지만, *패킹 변수 사이로 들어간다거나 하면 안된다.
print('EX5-5 - ', args_test('test1', 'test2', 'test3', id='admin', point=7, password='1234'))
# EX5-5 - (test1)(('test2', 'test3'))(7)({'id': 'admin', 'password': '1234'})




# 8) Signatrues
# - 2점 후반~3점대 부터 나온 기능이다.
# - 함수의 인자 정보를 표시하는 class형태 메소드
# - 딥러닝, flask 등... 함수의 인자를 signature로 조사를 한번 해본다.
# - 공식문서를 보는게 더 편하지만, inspect에는 유용한 패키지들이 많다.
from inspect import signature

sg = signature(args_test)
print('EX6-1 - ',sg) # (name, *contents, point=None, **attrs)
print('EX6-2 - ',sg.parameters) 
# OrderedDict([('name', <Parameter "name">), ('contents', <Parameter "*contents">), ('point', <Parameter "point=None">), ('attrs', <Parameter "**attrs">)])

# 8-1) 모든 정보 출력
# - 튜플형태의 orderdict를 풀어서 다 출력한다.
# - 2번쨰 인자 param이라는 class의 객체들은 .kind와 .default값을 확인할 수 있다.
for name, param in sg.parameters.items():
    print('EX6-3 - ', name, param.kind, param.default) 
# EX6-3 -  name POSITIONAL_OR_KEYWORD <class 'inspect._empty'>
# EX6-3 -  contents VAR_POSITIONAL <class 'inspect._empty'>
# EX6-3 -  point KEYWORD_ONLY None
# EX6-3 -  attrs VAR_KEYWORD <class 'inspect._empty'>



# 9) partial : 인수를 고정해서 새로운 함수를 return
# - 주로 특정인수고정 -> 콜백함수에 사용함
from operator import mul # add, mul 메소드는 함수의 인자에  연산자 대신 넣는 메소드들이다. ex> reduce(add, data)
# AAA operator 패키지의 모듈들은, 함수를 인자로 받는 함수들(고위함수)에 연산자 넣기 위해 만들어놨다.
from functools import partial # 좀 덜쓰이는, 일급함수들은 functions에 있다. ex> reduce, partial

print('EX7-1 - ', mul(10, 100)) # mul함수는 인자 2개만 받는다.

# 9-1) mul함수의 2개인자 중 인수1개(5)를 partial로 고정시켜보자.
five = partial(mul, 5) # mul(a,b)에서 5는 고정으로 넣어놨으니 하나만 더 주면 된다.
print('EX7-2 - ', five(100)) # 5*가 고정 -> # 500

# 9-2) 고정1개 된 것에 다시 추가 고정
five_six = partial(five, 6)
print('EX7-3 - ', five_six() ) # mul(5,6)2개 풀로 고정 -> 빈 인자로 실행해야됨. # 30

# 9-3) parital 활용 -> 상수 1개를 고정시킨 체, list comp에서 데이터 생성
print('EX7-4 - ', [ five(i) for i in range(1, 11)])

# 9-4) partial 활용2 -> 고위함수의 인자로 사용하기
print('EX7-5 - ', list(map(five, range(1, 11))))


# __call__ -> 객체를 호출가능하도록 한다. by 내부 메소드들 활용 / map, filter / lambda는 주석 잘 달 것. / 다양한 매개변수 매핑