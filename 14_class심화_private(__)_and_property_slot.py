# 파이썬 클래스 관련 메소드 심화
# 1. private 속성 실습 : 객체에 설계된 속성들을 @데코로 보호?
# 2. __slot__ : 성능이 더 좋아서 쓰는 것을 추천하는 
# 3. 객체 슬라이싱, 인덱싱
# 4. ABC, 상속, 오버라이딩 : abc메타클래스를 상속받아 추상화, 오버라이딩을 배움
# - 디자인 패턴


# 1) pritvate속성(__x)와 프로퍼티(@property->method.setter)
# class는 설계도다. 
# - 설계도를 잘 만들어야 중복X 일관성O 이해쉽게 사용할 수 있다.
class VectorP(object):
    # python 3.점대부터는 metaclass를 기본적으로 상속받기 때문에 (), (object) 다 생략해도 된다.

    # 1-1) 언더바2개로 만들면, python에서는 보호역할을 자동으로 한다.
    # - 외부에서 인스턴스변수를 조회못하게 된다.
    def __init__(self, x, y):
        self.__x = float(x) # 첫번재 인자는 float으로 받겠다. 5->5.0
        self.__y = float(y)

    
    # AAA __iter__를 오버라이딩하면
    # - next() for문으로 순회할 수 있다.
    # - 내 생각엔 __x, __y로 감춰둔 변수를 내어줄 때 쓸 것 같다.
    def __iter__(self):
        # tuple comp는 없다. genetrator를 만든다.
        # return은 generator로 만들어서 반환해준다.
        # - list comp로 list를 보내도 된다. 하지만 데이터가 많을 때는 generator로 반환해주는게 좋다.
        return (i for i in (self.__x, self.__y))

    # 1-4) 프로퍼티 코딩
    # - @property : 데코레이터의 함수property()가 선행작업을 한 뒤, 우리 함수 func이 작동할 것이다.
    # - 데코레이터 : 콜백으로 선행하는 함수가 먼저 동작하고, 우리가 만든 메소드가 거기로 들어가서 작업하고 결과물이 return된다.
    # - 함수이름은 보통 (언더바를 뺀) 변수이름으로 한다.
    # - 각 __인스턴스 변수마다 작업을 해줘야하나보다.
    @property
    def x(self):
        # 값을 읽을려고 만든 것이니 변수를 내부에서 return(외부에서 접근안되니 method-return으로 내어준다.)
        print('Called property x')
        return self.__x

    # 1-6) 반드시 @property로 만든 x(getter)가 있어야 setter를 만든다.
    # @(getter).setter + 메서드명도 def (getter)(self, v)
    # - setter를 정의해주면, 객체.x(getter)에 할당이 가능해진다.
    # - 객체.x = v
    @x.setter
    def x(self, v): 
        # 변경을 원하는 값인 v를 받는다고 가정하고, 할당해주자.
        print('Called property x Setter')
        self.__x = float(v)

    # 1-8) y도 똑같이 만들어준다.
    # AAA 값을 넣을 때의 조건을 생성자가 아닌 setter에서 건다.
    # - 생성자에서 첫값은 의식해서 잘 넣어줘야하나??/
    # - 생성자에서 도 한번은 cut해줘야한다.
    @property
    def y(self):
        print('Called property y')
        return self.__y

    @y.setter
    def y(self, v):
        print('Called property y')
        if v<30:
            raise ValueError('30 below is not possible')
        self.__y = float(v)





# 1-1) 
v = VectorP(20, 40) #  x=20.0, y=40.0
# print(v.__x) # AttributeError: 'VectorP' object has no attribute '__x'
# 아에 attr가 없다고 뜬다. 사실은 내부 보호중.

# 1-2) iter method에서 구현을 해놔야 for문에 넣을 수 있다.
# -> next()나 for1개씩 돌아가면서 호출될 때 next()가 호출되는데, 
# -> 이 때, iter mehod에 return되는 부분이 값을 내어놓는다.
for val in v:
    print(val)


# 1-3) 생성자에서 데이터를 받을 때, if 안되는조건 raise Error를 일으킬 수 도 있다.
#   def __init__(self, x, y):
#         self.__x = float(x)
#         if y < 30:
#             raise ValueError('y below 30 not possible')
#         self.__y = float(y)
# 생성자에서 받을 때부터 여러조건을 걸수 있다.
# 하지만, ... 이렇게 거는 경우이 문제점이 있다.
# 
# 첨 생성자에서 받을 때는 (10, 40)으로 에러가 안났지만,
# 이미 생성된 <객체 직접 접근>후 수정 v.__y = 10으로 생성자에 걸었던 조건이 무효화 되버린다.
# - itnit에서 <생성시 값 체크> + <타입변형> 까지 해줬자만 무용지물이 되었다.
# - init만 피해왔다면... string을 넣어도 잘 들어가기 때문
# >> 생성자에서 조건 거는 것은 별로 좋지 않다.

# python 버전 업그레이드마다 @데코를 제공해주는데,
# getter/setter 기능을 제공해준다.
# - private __x  + @getter/setter
# 1-4)로 class를 수정해보자.

# 1-5) @property -> x를 만들고 난 뒤 v.__x가 아닌 v.x로 접근해보자.
# print(v.__x)
# - 변수명의 method가 속성처럼 작동한다.
print(v.x) 

# 1-7) setter사용하기
# setter를 정의해주면, v.x(getter)에 할당이 가능해진다.
v.x = 10
print(v.x) 


# 1-9)
# - setter에 걸어둔 조건에 걸려 원하는 error가 났다.
# v.y = 20 # ValueError: 30 below is not possible

print('Ex1-2 - ', dir(v), v.__dict__) # .__dict__ ; 자체의 namespace
# - class의  namespace: 프로퍼티(getter)명대로 변수명이 들어가 있다. 
# - dir하면.. __x의 private 변수명이  property명으로 들어가있다.
#  [..., 'x', 'y']
# 
# - 객체의 namespace : 알아서 getter/setter의 변수를 지어놨따. : 
#   '_VectorP__x': 10.0, '_VectorP__y': 40.0
#   접근은 v.(def)x인데... _class명 +__프로퍼티명
print('EX1-3 - ', v.x, v.y)

# AAA private변수는 property로 안전하게 보호 + 유효성 검사까지하자.!



# 2) slot
# - python interpreter에게 통보하는 역할을 함.
# - 해당 클래스가 가지는 속성을 제한한다.
# - 모든 속성들을 __dict__ 형태로 관리되는데
# - dict는 key 중복 검사 등을 위해 hash table을 이용하기 때문에, 메모리를 많이 사용한다.
# - class 100개 -> __dict__ 100개 생성-> 다 메모리에? 
# -> 최적화가 필요한 자료구조 -> slot을 사용해서 dict속성을 최적화한다.
# -> 엄밀히 말하면, dict를 set으로 바꿔서 사용한다고 함.
# AAA dict속성최적화로 다수 객체 생성시 메모리 사용공간 대폭 감소 ! (최대 20%까지)
# AAA 해당 class에 만들어진 인스턴스 속성(__dict__)관리에 dictionary대신 set형태를 사용한다. 지정된 속성만 사용할 수 있음. 메모리 감소 시킴

# 2-1) 딱 사용할 속성을 튜플형태로 지정해줌 -> 밑에서는 그것만 사용
class TestA(object):
    __slots__ = ('a', )

# 2-2) slots을 사용하지 않으면, attr들을 dict로 관리하게 된다.
class TestB(object):
    pass 

use_slot = TestA()
no_slot = TestB()

print('EX2-1 - ', use_slot) # <__main__.TestA object at 0x03530870>
# - slots를 사용하면 __dict__는 존재하지 않는다. set이 사용됨.
# print('EX2-2 - ', use_slot.__dict__) # AttributeError: 'TestA' object has no attribute '__dict__'
print('EX2-3 - ', no_slot.__dict__) # {}

# AAA ML처럼 class자체가 많아지는 경우 -> slots을 사용하고 있다.
# - 좋은 패키지는 다 90%이상 slot을.. 사용함
# - 혼자쓸 프로그램은 그냥 slot없이 사용



# 2-3) 메모리 사용량 비교 ( timeit + closure )
# - 20% 성능은.. 엄청난 차이다.
# - timeit 모듈 + closure로 만든다.

from time import time
import timeit
# 외부함수 인자 -> func면 @deco / 그외 or 아무것도 없으면 closure
def repeat_outer(obj):
    # 내부함수 인자X -> 외부에서 호출()시 안받는다는 말
    def repeat_inner():
        # 내부함수 내용 : 외부인자들(외부함수or객체, 내부변수)처리 (및 외부함수 실제 결과 return)
        # - 문자열을 넣었다가 지움.
        obj.a = "TEST"
        del obj.a 
    return repeat_inner

# timeit.repeat() 함수+횟수를 넘겨주면, 그 횟수만큼 실행시켜서 시간 반환
# - slot사용 class의 객체 vs noslot class 객체의
# - 데이터입력 후 삭제되는 시간을 비교
# print(timeit.repeat(repeat_outer( use_slot ),number=1000))
# [0.0007304999999995232, 0.0007033999999999097, 0.0007327000000003636, 0.0006251999999999924, 0.00053760000000036]
# - 1/1000초도 안걸린다.
# - 여러 시간 중 제일 적게 걸린시간만 뽑아내자.
print(min(timeit.repeat(repeat_outer( use_slot ),number=10000))) 
# slot    만번 : 0.002679100000023027
print(min(timeit.repeat(repeat_outer( no_slot ),number=10000))) 
# no slot 만번 : 0.0035783999999239313
# -> 시간 많이 걸린다 = 내부프로세스 복잡 + 메모리도 많이 쓴다.















