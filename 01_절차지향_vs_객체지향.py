# 01-01

# 절차 지향 -> top-down 방식으로 쭉 실행되는 것
# - 컴퓨터의 실행과정과 같아서 실행속도가 빠르다
# - 길어지므로 유지보수, 개선시 힘듬

# 객체 지향(OOP)
# - 코드재사용 + 코드중복방지 + 메소드 활용

# 일반적인 코딩(절차지향)
# 학생1명을 담을 때? -> list ? dict ? 어디에 담을까?
# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = {'gender' : 'Male',   'score1' : 95, 'score2' : 88}
    
# 실행하는 순간, 내려오면서 주석들~변수들 할당~
# QQQ 학생1 -> 1명 표현하는데도 **너무 많은 변수 필요**
# - XR, CT 프로그램들은 넣으면 바로 나와야하므로 절자치향으로 코드를 짜서 속도를 높인다.
# - 절차용 : 기계에서 목적이 분명하기 때문에, XR -> 결과로 바로 나올 경우, 단순한 프로그램일 경우 
# - 객체용 : 범용적 데이터를 많이 담아야 하는 경우는, 객체지향으로 짜야한다.

# 학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = {'gender' : 'Female', 'score1' : 77, 'score2' : 92}

# 학생3
# QQQ 변수가 많아지면서, 각각의 변수가 다 달라야한다.
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = {'gender' : 'Male',   'score1' : 99, 'score2' : 100} 



# QQQ 학생들을 list나 dict에 담아보고, class기반과 차이점을 확인해보자.
## list 구조
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1,2,3]
student_grades_list = [1,2,4]
student_details_list = [
    {'gender' : 'Male',   'score1' : 95, 'score2' : 88},
    {'gender' : 'Female', 'score1' : 77, 'score2' : 92},
    {'gender' : 'Male',   'score1' : 99, 'score2' : 100},
] 
# QQQ dict에 k:value를 직접입력하도록 코드를 짜진 않는다.
#     형태를 만들어거 가져오지.. generator를 이용해서 직접 타이핑 하진 않는다.
# list 구조의 데이터를 사용해보기
## 학생2 한명을 삭제
## - del로 정학하게 QQQ짝을 맞춰주면서 삭제해야한다.
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]
# 출력해보기
# print(student_names_list)
# print(student_numbers_list)
# print(student_grades_list)
# print(student_details_list)
# QQQ 관리하기 불편: 데이터의 정확한 위치(index)를 매핑해서 사용
# - 즉, 순서를 알고 있어야하며, 1개의 속성을 삭제하려면, 그 index에 맞게 다른 속성들도 다 같이 삭제해줘야함.


# print()
# print()

# dict구조로 만들어보기(=dict_list)
# - 딕트1개당 학생1명정보를 다 넣음.
# - dict리스트의 dict마다, key값은 동일하게 다써줘야한다.
# - 사람마다 변수를 여러개 썼던 것과 달리, dict의 key로 가서 변수가 줄었다.
# - dict의 value에도 dict를 넣을 수 있음
student_dicts =[
    {'student_nmae' :'Kim', 'student_number' : 1, 'student_grade' : 1, 'student_detail' : {'gender' : 'Male', 'score1':95, 'score2':88}},
    {'student_nmae' :'Lee', 'student_number' : 2, 'student_grade' : 2, 'student_detail' : {'gender' : 'Female', 'score1':77, 'score2':92}},
    {'student_nmae' :'Park', 'student_number' : 3, 'student_grade' : 4, 'student_detail' : {'gender' : 'Male', 'score1':99, 'score2':100}},
]
# 학생2 지우기
# - 어차피 parent 자료구조는 list다.
# - QQQ list구조에서는 해당index를 모두 매핑해서 수동으로 모든 속성 삭제해줘야하는데, 
# -     dict구조에서는 맨 바깥 부모list의 index1개만 삭제해주면되니 편해졌다.
del student_dicts[1]
# print(student_dicts)
# QQQ 그러나, dict를 매번 작성해서 매번 반복 작성 및 key중첩 되고 있다.
# QQQ 여전히 바깥은 list라 index를 기억해서 삭제해야한다
# - stack이든 heap이든 자료를 넣고 / 빽고할 때는 index를 사용할 수 밖에 없다.
# - 사실 json형태의 자료구조(dict들의 list) 라서 자연스러운 것이기도 하다.
# - ORM -> dict -> json으로 뽑아올 떄 사용된다.
# - list(  dict()  )를 담는 형태는 매우 많이 활용된다. 
# - DB나 기타 3rd party(외부에서 제공하는 것들, 구글닥스, 노션 등?)에서 많이 쓰이는 형태다.
# QQQ 그러나, <<직접 데이터를 생성할 때 or 데이터가 많을 때>> 는 적합하지 않는 구조다.
# print()
# print()


# 클래스 구조
# - 객체 지향. 유/무형 다 가능.
# - 구조 설계후 재사용성(기능추가/삭제 쉬어짐) + 코드반복 최소화 + 메소드활용
# 1) 모든 클래스는 object를 상속하도록 작성되어있어서, 3가지 형태 중 아무거나 써도 된다.
# class Student(object):
# class Student:
class Student():
    # 2) 클래스는 정적인 속성들 + 동적인 메소드로 이루어져있다.
    #  모든 클래스는 init메소드(생성자, constrtuctor)가 1번 호출된다. 초기화시 할당받을 속성값도 같이 지정해준다.
    def __init__(self, name, number, grade, phone, details):
        # 3) 할당받을 속성값과 실제 객체의 속성을 구분 짖기 위해, 언더바를 붙혀서 _속성을 넣어준다.
        self._name = name
        self._number = number
        self._grade = grade
        # 6)
        # AAA 각 객체들의 속성 추가/제거가 쉬워진다.
        # - 대신 받을 때의 순서를 기억해야함.
        self._phone = phone
        self._details = details
        

    # 4) 객체의 정보를 출력해줄 str메소드를  init작성후 일단 작성해주자.
    #   return 'string'을 반환해주면, 객체1개 print시 나온다.
    # - 없어도 되나, 작성시 이용할 수 있다 = override
    def __str__(self):
        return 'str: {} - {}'.format(self._name, self._grade)

    # 10) str과 유사한 메소드가 repr이다.
    #  return 'string'을 반환해주면, ????시 나온다.
    def __repr__(self):
        return 'repr: {} - {}'.format(self._name, self._grade)

# 5) 
#객체 생성은 생성자가 받는 순서대로 기입한다.
# - 속성에 dict를 넣어줄 수 잇는 것을 까먹지 말자.
student1 = Student('Kim', 1, 1, '01046001111', {'gender': 'Male', 'score1' : 95, 'score2':88})
# AAA 객체(데이터) 생성시, 반복되는 key값중첩은 없어진다. vs dict
# AAA 각 속성마다 index(순서)로 기억되던 값들이 class의 속성으로 들어가버렸다. vs list, dict
student2 = Student('Lee', 2, 2, '01046001111', {'gender': 'Female', 'score1' : 77, 'score2':98})
student3 = Student('Park', 3, 4, '01046001111', {'gender': 'Male', 'score1' : 99, 'score2':100})


# 7) 모든 객체는 init, str, 뿐만 아니라, dict메서드를 가지고 있다.
# dict를 통해, dictionary로 이루어진 namespace에서 속성값들을 확인한다.
# 파이썬은 모두 객체로 이루어져있다.. 그리고 그 객체는 __dict__라는 메서드를 통해 dictionary형태의 namespace를 가지며 속성값들이 들어가 있다.
print(student1.__dict__)
# {'_name': 'Kim', '_number': 1, '_grade': 1, '_phone': '01046001111', '_details': {'gender': 'Male', 'score1': 95, 'score2': 88}}
# print(student2.__dict__)
# print(student3.__dict__)
# AAA 즉, 객체들은 __dict__메서드로 내부 속성들을 확인한다.

# 8) 
# 객체들도 list에 담아야, 함수의 인자 등으로 보내기가 쉽다.
# AAA 클래스기반=객체지향으로 작성하면, 편한 것이 아니다.
# - 재사용성을 포함한, 상속시켜 확장 필수적으로 들어간다.
students_list = []
students_list.append(student1)
students_list.append(student2)
students_list.append(student3)
print()
print()
# 9)
# 객체 list를 출력해보면, 객체(인스턴스)들이 모여있는 것 처럼 찍힌다.
# - print( 객체list )가 아니라, 개별 print( 객체 )시에만 str메소드에 정의해준 string이 반환된다.
# - 객체list 출력시 나오게 하려면. str메소드가 아니라 repr로 작성해야한다.
print(students_list)

# 9.5)
for x in students_list:
    # 11) 객체1개 print시, str 우선 -> 없으면 repr이 호출되어 출력
    #     객체 list에서 호출시, repr만 호출되어 출력
    #    my) str메서드에 작성한 것은 각 객체 1개 print만 담당
    #    my) repr메서드에 작성한 것은 print 및 범용적으로 적용. but 1개 print시에는 str에 밀린다.
    # print(x)
    # 12) str이 있더라도 repr로 찍고 싶다면? 
    #    print( repr() ) 로서 repr()메소드를 사용하면 된다.
    print(repr(x))