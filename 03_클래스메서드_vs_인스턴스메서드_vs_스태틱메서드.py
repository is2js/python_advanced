# 03 
# 메서드는 3가지가 있다. 클래스 vs 인스턴스 vs 스태틱
# - 변수에는 신통 공용의 클래스변수 vs 객체들만의 은닉화하고픈 인스턴스 변수 가 있다.

# 1) 기본 인스턴스 메소드
class Student(object):
    """
    Student Class
    Author : Cho
    Date : 2021.08.25
    Description : Class, Static, Instacne Method
    """

    # 1-1) 클래스변수 : 모든 데이터(학생)들이 같은 정보를 가질 때 선언해놓음. 바뀔 수 있으니 변수로. 
    tuition_per = 1.0

    # 1-2) 생성자 : 데이터 생성시 실행됨.
    def __init__(self, id, first_name, last_name, email, grade, tuition_per, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition_per
        self._gpa = gpa

        
    # 1-3) 인스턴스 메서드
    # - 인스턴스 변수를 활용해서 <개개의 데이터마다> 변형된 데이터를 처리or반환해줌
    # - 이때까지 했던 인자로 self가 들어가 데이터 변형후 결과를 반환해주는 객체용 메서드 
    # - 첫번째 인자로 접근자self가 들어가, 각 데이터 고유한 정보를 처리한다. return이 없어도 정보처리 등만 해도 된다.
    def full_name(self):
        return '{}, {}'.format(self._first_name, self._last_name)

    # - 개개의 정보를 return한다면? -> 인스턴스 메서드
    def detail_info(self):
        # AAA 각 인스턴스 메서드에서, 위에 정의한 인스턴스 메서드를  self.으로 사용할 수 잇음.
        # - 인스턴스메서드로 1개의 id값만 주면 -> 전체 정보를 출력해주는 함수도 작성할 수 있다.(여긴 아님)
        # - print(객체)의 기본정보 이외에, 따로 detail하게 보고 싶을 때 정의하면 된다.
        return 'Student Detail Info : {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email,  self._grade, self._gpa)

    # -개개인(-> 인스턴스메서드) 이 내고 있는 등록금 출력
    def get_fee(self):
        return 'Before Tuition -> id : {}, fee : {}'.format(self._id, self._tuition)

    # - 개개의 인상률 적용 등록금
    # AAA 클래스변수에 사용할 땐, 클래스명.클래스변수를 까먹지 말자. ex> Student.tuition
    def get_fee_calc(self):
        return 'After Tuition -> id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # 1-4) 매직메서드 & self가 들어간 인스턴스 메서드인 str메서드 정의해주기
    # - print(객체)에 보일 것으로.. 객체 기본정보를 반환하면 된다.
    def __str__(self):
        return 'Student Info -> name : {} grade : {} email :{} '.format(self.full_name(), self._grade, self._email)

    # 8) 클래스메서드로 클래스변수 조작
    # - 외부에서 접근가능(클래스명.클래스변수)한 변수라서 보호하면서 데이터처리하도록 작성
    # - @ 데코레이터는 python엔진에게 알려주는 것.
    # - 클래스변수는 객체가 아니지만, Student를 의미하는 cls로 첫번째 인자를 주어야한다.
    # - 인스턴스 -> 메서드에서는 (self, ) -> self._인스턴스변수 생성
    # - 클래스 -> 메서드에서는 (cls, ) -> cls.클래스변수로 사용
    @classmethod
    def raise_fee(cls, per):
        # class메서드의 목적에 부합하지 않는 경우는 알려주고 종료시킨다.
        if per < 1:
            print("Please Enter 1 or More")
            return
        cls.tuition_per = per 
        print("Succeed! tuition increased!")

    # 11) classmethod로 생성자, init, 데이터생성 정의해서 사용하기
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition_per, gpa):
        # - cls자체가 Student이므로, Student( , , , )형태로 바로 만들어버릴 수 있다.
        # return cls(id, first_name, last_name, email, grade, tuition_per , gpa)
        # - 만약, 등록금이 오를 상태로 데이터를 만들어주고 싶다면, 아래와 같이 클래스변수를 활용한다.
        return cls(id, first_name, last_name, email, grade, tuition_per * cls.tuition_per, gpa)

        






# 2) 객체(데이터 생성) 후 정보 확인해보기
student_1 = Student(1, 'Kim', 'Seokyoung', 'daisykim88@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Cho', 'Jaeseong', 'tingstyle1@gmail.com', '2', 500, 4.3)


# 2-1) 객체 자체(기본정보) 확인 by 인스턴스메서드
# - 직접print이므로 str메서드가 출력됨.
# - my) print(객체)는 __str__ 확인 or __repr__ 확인
print(student_1)
print(student_2)
# 2-2) 객체 내부(dictionay namespace는 __dict__로 확인)
# print(student_1.__dict__)
# print(student_2.__dict__)


# 3) 전체 정보 확인 by 인스턴스 메서드
print(student_1.detail_info())
print(student_2.detail_info())

# 4) 학비 정보 확인 by 인스턴스 메서드
# - self.get_fee_calc()에서는 클래스변수가 사용되었다.
print(student_1.get_fee())
print(student_2.get_fee())

# 5) AAA**클래스변수는 외부(어디서든)에서도 접근가능**하다.
# - 외부에서 클래스변수 변경후 -> 각 객체들에 적용되는지 확인
# 5-1) 인상률 1.0 그대로
print(student_1.get_fee_calc())
print(student_2.get_fee_calc())
# 5-2) 인상률 1.2로 외부에서 클래스변수 바꿔도 -> 이미 생성된 객체에 적용된다.
Student.tuition_per = 1.2
print(student_1.get_fee_calc())
print(student_2.get_fee_calc())

# 6) AAA 하지만, 클래스 밖(외부)에서 클래스변수에 직접 접근하는 것은 좋지 않다.
# - 만약, 프로그래머가 실수로 숫자를 바꿔버리면.. 
# - 10000개의 데이터(객체)가 이 변수(클래스변수)를 바라보고 있고, 외부에서 쉽게 변경된다면..
# - AAA 모든 인스턴스가 바라보는 공용변수(클래스변수)는 캡슐화(보호)가 되어야하고, 수정을 위한 코딩은 따로 해야한다.





# 7) 클래스 메소드
# - 모든 인스턴스가 바라보고 사용되는 공용 변수가 외부에서 막 사용되지 않기 위해 
# - 클래스 내부에서 클래스변수 수정하도록 코딩해주는 것

# 9) 8)에서 정의한 클래스메서드를 호출하여, 클래스변수 수정하기
# - 인스턴스가 공통적으로 바라보고 있는 클래스변수를, 클래스 메서드로 호출할 때는 2가지 방식이 있다.
# 9-1) 클래스.클래스메서드 호출 -> 클래스 변수 값 바꾸기
# Student.tuition_per = 1.2 # 클래스 변수를 직접 수정하지 않는다.
Student.raise_fee(1.5)
print(student_1.get_fee_calc())
print(student_2.get_fee_calc())
# AAA 외부에 클래스 변수에 직접 접근하는 것보다 클래스 메서드를 넣으면
# - 우리가 원하는 흐름도 같이 넣을 수 있다. if 1이하면 더 큰 값 입력
Student.raise_fee(0.9) # 적용안됨.
Student.raise_fee(1.0)


# 10) classmethod로 데이터(객체) 생성하기
# - Pythonic하며, 좋은 어플리케이션에서는 클래스(속성값, 나열, ...)형태가 아닌 
# - classmethod로 객체를 생성하도록 한다. (기능은 똑같다. 권장사항)

# 12) 클래스메서드로 인스턴스 생성 
# - Student()로 객체 생성하는 것보다 목적의식이 뚜렷해지며, 권장되고 있다.
student_3 = Student.student_const(3, 'Cho', 'Jaekyoung', 'zzamilove@hanmail.net', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Ara', 'Student@hanmail.net', '4', 600, 4.1)

# 객체 확인 by 인스턴스 메서드
print(student_3.detail_info())
print(student_4.detail_info())

# 등록금 확인
# - 학생 개개의 입력된 등록금을 확인한다. 
# - 왜냐면, 이미 데이터 생성시, 클래스 메서드에서 인상률이 적용되서 생성된 상태기 때문
print(student_3._tuition)
print(student_4._tuition)
# - AAA 기존 사람들은 일반 객체 생성방법으로 적용안된상태로 생성할 수도 있다.
# - 클래스메서드로 생성하는 것 = 인상률 적용시켜서 생성하는 것 + 권장하는 방식
# - 일반 객체 생성하는 것 = 인상률 적용안된상태의 데이터 생성 + 권장방식X
# -> AAA 2가지 방법을 혼용해서 쓸 수 있다.
# -> 객체 생성 + 인스턴스메소드로 처리
# -> 클래스메서드로 처리하면서 생성



# 13) 스태틱 메소드
# - 장학금 대상자와 아닌 사람을 걸러내는 로직 
# 13-1) 스태틱 메소드 없이 별모의 함수 작성
# - 일반적으로 객체를 받아서, 인스턴스변수(_속성)을 활용하여 처리함.
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient'.format(inst._last_name)
    # else문은 return으로 끝나는 상황에서는 쓸 필요가 없다.
    return 'Sorry. Not a scholarship recipient.'
print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

# 13-2) 사고 확장해보기
# - is_scholarship()은 전체 데이터(객체)를 대상으로 적용되는 함수다.
# - 외부(클래스 밖)에 있어도 상관없지만, 
# - Student클래스의 객체에만 적용 +  찾아서 유지보수 편리 
# - 를 위해 class내부에 선언해주는게 맞다.
# - class관계 + class정보를 사용하는 함수 
# - 객체를 사용하므로 인스턴스메서드로 작성해도 되지만, **self를 받을 필요없고, cls도 받을 필요 없는** 함수여
