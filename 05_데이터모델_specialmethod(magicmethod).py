# 04 데이터 모델 - special method = magic method
# 미리 python이 만들어놓은 연산자들을 overloading한 뒤 사용할 수 있는 집합들
# - cf) 파이썬 중요 프레임워크 : 시퀀스, 반복, 함수, 클래스
# - my) int데이터타입의 변수도 일종의 객체다
# - my) 파이썬은 객체(+)객체에서 (+)인식을 __add__ 등의 매직메소드를 통해 치환되어 처리되도록 설계했다.
# - my) 1+2가 1.__add__(2)로 치환되어 처리된다. 치환되는 미리 작성된 메소드가 magic method special method다.
# - my) 이 __add__를 객체를 정의한 클래스에서 오버라이딩 한다면
# - my) custom객체1 + custom 객체2 -> custom객체1.__add__(custom 객체2)도 가능해진다.
# - AAA python엔진에서 제공되는 연산자-> magicmethod는 객체로 제공된다.
# - AAA 클래스안에서 magic method를 오버라이딩한다면, 객체끼리 연산이 가능해지다.

# 1) 기본형
print(int) 
# <class 'int'> -> 클래스 형태를 띄고 있다. 
# - 파이썬의 모든 자료형(데이터타입) -> (데이터 구조)에서는 객체로 취급됨.

# 2) 모든 속성 및 메소드 출력후 살펴보기
# - 정수 데이터타입 -> 객체로서 가지는 속성+메서드 (전부 속성이라 부름)
# - 속성 중 언더바 2개가 들어간 method들을 special method라고 부름
# print(dir(int))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
n = 100 # n은 데이터타입은 int형 변수/ 데이터구조는 객체
print('EX1-1', n+200)  # 객체 + 200은 어떻게 더해질까?

# -> 내부적으로 magic method 객체.__add__()가 작동해서 +를 계산한다.
print('EX1-2', n.__add__(200))
# 즉 +  -> 내부적으로 .__add___()로 치환되고 ->  __add__ 는 메모리에서 진법을 이용하여 계산됨

# print('EX1-3', n.__doc__) # doc타입으로 python 개발자가 넣어놓음.

print('EX1-4', n.__bool__(), bool(n)) # 0이외의 값은 다 True 

print('EX1-5', n * 100 , n.__mul__(100)) # 곱하기도 매직메서드로 처리된다.



# 3) 클래스 작성으로 알아보는 magic method 활용법
class Student:
    # 1. doc 생략
    # 2. 생성자
    def __init__(self, name, height):
        self._name = name
        self._height = height
    
    # 3. str-> 우리는 매직메서드를 오버라이딩 해서 쓰고 있다.
    # - 생성자에서 받아주는 인스턴스 변수를 사용해서 작성한다.
    # - **str메서드는 항상 오버로딩 해서 사용하자! 그래야 데이터 분석등에서 편하다.
    def __str__(self):
        return "Student Class Info : {}, {}".format(self._name, self._height)

    # 4. 객체끼리 비교용 메서드 오버라이딩
    # AAA 이미 정의된 매직메소드를 클래스내부에서 오버로딩하여 활용할 수 있다.
    # - 코딩이  쉽고, 객체지향적이고, 불필요한 코드를 줄일 수 있으며
    # AAA **__ge__ __le__ 매직메서드는  주위의 [>=] [<=] 를 인식되어 치환되며 수행되는 연산자다**
    # - 만약 객체 2개가  >= 나 <=가 쓰였다면, __ge__ , __le__가 수행된다.
    # - AAA 객체끼리의 비교를 클래스 내부에서 작성해두자.
    # - 현재(개별) 객체는 self -> 비교할 나머지 객체x를 따로 받아야한다.
    def __ge__(self, x):
        print('확인용 Called >> __ge__ method')
        if self._height >= x._height:
            # True말고, string을 return, 값을 return시켜도 됨.
            # 웹에다가 전송하는 함수를 짜도 됨.
            return True
        else:
            return False

    def __le__(self, x):
        print('확인용 Called >> __le__ method')
        if self._height <= x._height:
            return True
        else:
            return False

    # 6) 객체 비교용으로 - 도 구현해보자.
    # - 는 python이 __sub__ 매직메소드로 치환해서 처리한다.
    # 이 매직메소드를 클래스에서 오버라이딩 해주면, 객체끼리 빼기도 가능하다.
    def __sub__(self, x):
        print('확인용 Called >> __sub__ method')
        # cf) 절대값으로 받고 싶다면 abs(  -  )
        return self._height - x._height


    

s1 = Student('조재성' , 162)
s2 = Student('김석영' , 167)

# 3-1) 클래스의 inst는 더할 수 없다.-> 연산지원X 에러
# print( s1+s2) # TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
# - but s1, s2의 키는 비교 및 연산 가능함.
# - AAA 키는 int형이며 대소관계 구분 가능하여 매직메소드에 이미 정의 되어있어서 -> 연산 가능
print(s1._height < s2._height)



# 5) 클래스에서 오버라이딩해준 비교용 매직메서드 호출하기
# - 원래 정의된 클래스의 객체는 비교가 안된다.
# - 하지만, 객체비교를 위해 클래스 내부에 __ge__ __le__를 오버라이딩 해주면
# - 객체의 인스턴스변수(속성)을 활용해서 비교됨 + 비교로직을 짤 수 있다.
# - > < 와는 별개이므로 주의
# - python에서는 모든 것을 객체 취급하므로, 
# int가 연산되는 것도 -> 객체취급되어 매직메소드로 연산되듯이
# 내 클래스 객체도 -> 객체 취급되니 -> 매직메소드 오버라이딩만 잘해주면 연산이 되어버린다.
print('EX2-1', s1 >= s2) # s1(self) >=(__ge__)  s2(x)
print('EX2-2', s1 <= s2)

# 7) 객체 빼기 by __sub__ 오버라이딩 in class
print('EX2-3', s1, s2)
print('EX2-4', s1 - s2)
print('EX2-5', s2 - s1)




# 8) 클래스 작성으로 알아보는 magic method 활용법 2
# - Vector : 계산을 직접해주는 클래스 생성 
class Vector(object):
    # 8-1) AAA 생성자 인자 self이후에 오는 , , , , 는 
    # - AAA각각에 접근하여 배정할게 아니라면(순서대로만 쓴다면) *args로 tuple unpacking해주자.
    def __init__(self, *args):
        # 8-2) AAA 생성자(매직메소드)에서도 docstring도 나중에 클래스.메직메서드.__doc__으로 확인할 수 있다. 
        """Create a vector, example : V = Vector(1, 2)"""
        # - tuple을 *args unpacking으로 들어올 때, 
        # - 아무것도 안넣어온 검사는 len(args) == 0 으로 하고, 
        # - default값은 self._x, self._y에다가 넣어주자.
        if len(args) == 0:
            # 아무것도 안들어왔다면, 0, 0을 _x, _y로 주자.
            self._x , self._y = 0, 0
        else:
            # 8-3) *args로 언패킹시킨 뒤 -> 각각을 튜플 = args 할당 unpacking시켜야한다.
            # - AAA 인자는 *args지만, 내부에서는 args로 튜플이 온다고 생각하면 된다.
            self._x, self._y = args

    # 8-4) str대신 repr로 한번 해보자.
    def __repr__(self):
        """returns the vector informations"""
        # {} {} .format(,)
        # %r %r %( , ) 2가지 방법이 있음.
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    # 11) 기존add와는 다른 벡터add를 오버라이딩해서 객체끼리 가능하게 해보자.
    # - AAA 이 때, 연산(x1+x2, y1+y2)결과의 튜플을 반환하는게 아니라 
    # - AAA 연산결과로 만들어진 튜플 -> 그 튜플로 새로운 객체를 만들어서 반환하자.
    def __add__(self, other):
        """Returns the vector addition of self and other"""
        return Vector(self._x + other._x , self._y + other._y)

    # 12) 곱하기도 작성
    # - 벡터의 곱은 주로 벡터 x 숫자를 곱한다.
    # - 벡터 x 벡터는... 외적?
    def __mul__(self, y):
        """Returns the vector multipulation of self and y"""
        return Vector(self._x * y , self._y * y)

    # 14) bool은 0만 아니면 true다.
    # - bool()이 치환되는 메소드가 __bool__임
    # - 그냥 bool이 아니라 _x, _y 중에 큰 값이 0이 아니면 True, 0이면 False 
    def __bool__(self):
        return bool( max(self._x, self._y))


            
# 9) inst 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
# - 중요한 건, 생성자에 if검사를 해서 튜플이 안들어왔을 때 0,0을 대입해줬다.
v3 = Vector()

# 9-1) docstring 확인 매직메소드 출력
print('EX3-1',Vector.__init__.__doc__) # Create a vector, example : V = Vector(1, 2)
print('EX3-2',Vector.__repr__.__doc__) # returns the vector informations
print('EX3-3', v1, v2, v3) # print만 str우선순위 -> 없으면  repr가 출력된다.
# AAA 객체생성시 생성자 부분에 빈값이 올 경우도 대비해주자


# 10) vector에서는 + 계산이 __add__기본과는 좀 달려져야한다.
# - 보통  a+b 는 x끼리 더해져야한다.
# - AAA 특정 객체 끼리의 연산이 없을 때 뿐만 아니라  특정객체의 연산을 변형할 때도 
# - AAA 매직메소드(python정의)를 변환 오버라이딩 한다.
print('EX3-4',Vector.__add__.__doc__) # returns the vector informations
print('EX3-5',v1 + v2) # returns the vector informations

# 13) 
print('EX3-6',Vector.__mul__.__doc__) 
print('EX3-7',v1 * 4) # returns the vector informations
print('EX3-8',v2 * 10) # returns the vector informations
# 15)
print('EX3-9',bool(v2), bool(v3)) # returns the vector informations
# - v3는 인자없이 생성하여 기본값 0, 0이 들어갔다. -> 최대값 0 -> bool(0) -> False




