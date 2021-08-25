# 01-02

# 클래스 상세 설명 
# - 클래스변수, 인스턴스변수
# AAA 클래스변수 : 메서드바깥 scope, 클래스에 그냥 선언후 -> 메서드안에서 클래스명.변수로 사용 ex> 데이터생성(init), 데이터 삭제(del)
#                 객체들 모두가 공유한다.
# AAA 인스턴스변수 : self가 붙는 객체들의 속성들 ex self._name, self._number
#                   객체 자신만의 값을 가진다. 방안에서만 논다.

# 클래스 재 선언
# 1) class 작성시 docstring 작성 버릇을 들이자.
    # 클래스 이름
    # 저자
    # 날짜
class Student():
    
    """
    Student Class
    Author : Cho
    Date : 2021.08.23
    """

    # 2) 클래스변수 - 있다가 사용할 것임.
    student_count = 0
    
    # 2-1) init메서드
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email
        
        # 2-2) **init**으로 초기화(객체=데이터 생성)가 될 때, init안에서 클래스명.클래스변수로 클래스변수에 접근이 가능하다.
        # - (메서드안이므로)초기화시 사용가능 -> 데이터 생성시 수정 가능 -> 데이터 생성시 +1가능
        # - 클래스 틀에 박힌 변수지만, 객체인 학생데이터 생성시마다 +1씩 시켜줄 수 있다.
        # AAA class코드내에서 데이터 생성갯수를 카운트할 수 있는 것은, 초기화시=데이터생성시 접근가능한 class변수가 가능하다.
        # - 클래스기반으로 변수를 생성하지 않으면, 숫자가 증가되지 않는다.
        Student.student_count += 1

    # 2-3) str 메서드
    def __str__(self):
        return "str {}".format(self._name)
    # 2-4) repr 메서드
    def __repr__(self):
        return "repr {}".format(self._name)


    # 3) 메서드+print문으로 디버깅용 객체id출력 메소드 만들기
    # - 디버깅, 객체 상태를 보기 위해 메서드+print조합을 많이 쓴다고 함.
    # - 객체의 id, 그리고 객체의 속성들을 출력해보자.
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details ))

    # 4) 잘 사용하진 않는 del 메서드 overriding
    # - 객체가 삭제될 때 호출되는 메서드?
    # - 객체 생성시에는 클래스변수에 +=1 해줫었는데, 삭제시는 여기가 호출되니 -=1 해줌
    def __del__(self):
        Student.student_count -= 1


        
# 5) id로 객체 확인(self = 찍어 낸 것 = 객체 )
#  - AAA파이썬에서는 찍어낸 것 =  객체 생성의 확인은 id()값으로 한다.
#  - id다르다 = 메모리에서 각자 다른 영역을 가지고 있다.
studt1 =  Student('Cho', 2, 3, {'gender' : 'Male', 'score1' : 80, 'score2' : 44})
studt2 =  Student('Cho', 4, 1, {'gender' : 'Female', 'score1' : 85, 'score2' : 74})
# - 객체1, 객체2의 id값이 다르다 
# - Q 서로 다른 객체면, 안의 속성도 다를까?
# - A No. 서로 다른 객체지만, 같은 속성값을 받아서 생성될 수 있다.
# - 즉, id값이 같다 = 서로 같은 객체 = 당연히 속성값들이 같다
# - but id값 다르다 = 서로 다른 객체 = 속성값은 같을 수 도 있다.
print(id(studt1))
print(id(studt2))

print(id(studt1) == id(studt2))
print(studt1._name == studt2._name)

# 5-1) id(객체) == 값비교가 아니라, is는 default로 id값 비교다
# - 즉, is는  instance(객체)비교 == 객체의 id값 비교
# cf) id값 = reference label(레이블) 비교
print(studt1 is studt2) 

# 5-2) 참고
a = 'ABC'
b = a
print(a == b) # 값은 같다.
print(a is b) # **a가 변경되면 b도 같이 변경되는 구조**일 때는, 각각 선언된 변수라도 id값이 같다.
# 즉, 같은 방을 가르킨다.  방은 1개인데, 가리키는 주소가 2개
# 객체(self)의 확인은 id값 확인으로 시작된다.



# 6) 객체.__dict__ -> dir(객체) 으로 속성확인(실무용)
# 6-1) dir(객체)
# - dir가 정보의 양이 많아지나 코드가 너무 많아진다.
# - 클래스의 속성값만 보고 싶다면, dict으로 보자.
print(dir(studt1))
print(dir(studt2))
# dir(객체) 
#  - 내가 만들어준 _속성&클래스변수 이외에 + 파이썬내부작성된 attribute들?(메서드들도)도 다 표기됨.
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_details', '_email', '_grade', '_name', '_number', 'detail_info', 'student_count']

# 6-2) 객체.__dict__
# - 내가 만든 _속성들 +  **속성값들까지** 들이 출력되며, 클래스변수는 안보인다.
# 객체.__dict__
# {'_name': 'Cho', '_number': 2, '_grade': 3, '_details': {'gender': 'Male', 'score1': 80, 'score2': 44}, '_email': None}
print()
print()
print(studt1.__dict__)
print(studt2.__dict__)
#  코딩시, 클래스나 객체의 __dict__, dir()은 굉장히 많이 찍어볼 것이다.
# print()
# my) 클래스.__dict__시, 속성값들이 아닌... 메서드 : 메서드 값, 클래스변수와 값 등이 보인다.
# print(Student.__dict__)

# 선택 매개변수인 email=None -> 없으면 None을 대입하도록 작성 -> 있으면 해당값이 할당됨.


# 7) doc스트링 확인
# - 클래스도 되고 객체에서도 된다.  .__doc__ 해주면 된다.
# - 다른사람이 만든 클래스를 가져왔을 때, 한번은 찍어보자.
print(Student.__doc__)
print(studt1.__doc__)

print()
print()

# 8) 만든 메서드 확인해보기
# - id(self)로 객체의 id값을 출력하도록 하는 함수
print(studt1.detail_info())
# Current Id : 1959091572592
# Student Detail Info : Cho None {'gender': 'Male', 'score1': 80, 'score2': 44}
# None
print(studt2.detail_info())
# Current Id : 1959091588352
# Student Detail Info : Cho None {'gender': 'Female', 'score1': 85, 'score2': 74}
# None
# AAA 여기서, 클래스안에서 메소드를 설계하면 되게 편해진다.
# - 학생의 디테일한 정보를 출력해주므로, 굳이 class 밖에서 정의해줄 필요가 없다. 여기서만 쓰임.
# - 클래스 안에서 만들면, 객체들은 self마다 자기만의 정보를 사용한 함수를 생성된 뒤 계속 사용할 수 있다.



# 9) 에러
# 9-1) 클래스에서 객체의 메서드를 호출한다면?
#      메서드 자체가 self를 받으므로, 객체단위에서만 실행된다.
#      self에러가 난다면? 객체에서 호출하는 메서드다. 하지만.. 클래스.메서드(객체)형태로 객체를 직접 넣어줄 수 도 있는데...
# Student.detail_info()
# Traceback (most recent call last):
#   line 148, in <module>
# TypeError: detail_info() missing 1 required positional argument: 'self'
# 9-2) 클래스.메서드( 객체 ) 형태로 직접 self를 넣어줘도된다.
print(Student.detail_info( studt1))
# 9-3) 정리하자면, self와 함께 정의된 인스턴스(?) 메서드는
#      객체.메서드()로 보통 호출되며
#      클래스.메서드( 객체 ) 로 self자리에 직접 넣어줘도된다.


# 10) 객체의 클래스 확인
# -  객체.__class__로 클래스명을 확인하면 된다. 
# - 코딩하다가 많이 만낙게 될 수도 있다.
print(studt1.__class__)
print(studt2.__class__)
# <class '__main__.Student'>
# 10-2) 2 객체의 원형클래스 비교
# 객체.__class__ 한 원형클래스의 id값을 비교하면 된다.
print(id(studt1.__class__) == id(studt1.__class__))
print(studt1.__class__ is studt2.__class__ )



## 정리하면서 클래스변수 값 확인해보기
# 11) 인스턴스 변수와 캡슐화
# - AAA 좀 더 높은 수준의 개발자가 되면, PEP문법상 변수에 직접접근을 권장하지 않는다.
print(studt1._name)

# - 변수에 직접접근하면, 변수의 값을 바꿔버릴 수 있다.
studt1._name = 'HAHAHA'
# - 장난으로, 실수로 바꿔버릴 수 있음 -> 무결화, 캡슐화가 안된 상태다.
# - 캡슐화 = 안의 정보를 은닉해두고, 수정시에는 AAA내가 지정한 메서드로만 수정할 수 있게 함.
# - 자바의 접근제어자.. private등..
# - 인스턴스변수 : 각 클래스에서 생성된, 인스턴스에 종속된 변수 -> 직접 접근은 하지말자.
print(studt1._name, studt1._email)
print(studt2._name, studt2._email) # 출력은 여기서만 직접하더라도, 직접접근 하지말자...

# 12) 클래스 변수
# - 접근 : 클래스변수는 공용이라, 모두(주인인 class, 각 객체)가 확인할 수 있다.
# - 객체.클래스변수 / 클래스.클래스변수 / 
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)


# 13) 신통한 클래스변수의 (클래스든 객체들이든) 공유 진짜 확인
# 13-1) 클래스의 dict namespace에서 보면, 클래스변수가 들어가 있다.
print(Student.__dict__)
# {'__module__': '__main__', '__doc__': '\n    Student Class\n    Author : Cho\n    Date : 2021.08.23\n    ',
#  'student_count': 2, '__init__': <function Student.__init__ at 0x000001C822EF4940>, '__str__': <function Student.__str__ at 0x000001C822EF4EE0>, '__repr__': <function Student.__repr__ at 0x000001C822EF4820>, 'detail_info': <function Student.detail_info at 0x000001C822EF48B0>, '__del__': <function Student.__del__ at 0x000001C822EF49D0>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>}
# 13-2) 인스턴스의 dict namespace를 보면, 클래스변수가 없다.
# - AAA 규칙 : 인스턴스의 네임스페이스에 없으면, python이 알아서 상위(클래스 변수, 부모클래스 변수)에서 검색한다.
# - 포인트 : 인스턴스 냉장고에 없다 -> 공용 냉장고에서 검색후 출력 -> 없으면 에러
print(studt1.__dict__)
# {'_name': 'HAHAHA', '_number': 2, '_grade': 3, '_details': {'gender': 'Male', 'score1': 80, 'score2': 44}, '_email': None}

print()
# 14) 객체 제거해보기
del studt2
print(studt1.student_count)
print(Student.student_count)
# - AAA 중요포인트 : 파이썬을 잘하게 되면, del메서드를 직접 구현하지 않는다. 지우는 것은 python이 알아서 해주기 때문 
# - sequence나 값 내부에 접근해서 찍어볼때 출력을 해볼라고 구현한 것일 뿐.


# 클래스변수냐 vs 인스턴스변수냐.. 
# 목적에 따라 적절히 선언해서 써야함.
