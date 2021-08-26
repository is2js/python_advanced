# 04 데이터 모델 - namedtuple
# 참조 : https://docs.python.org/3/reference/datamodel.html
# [1]파이썬의 중요 프레임워크(데이터타입) 4가지 
# - sequence(시퀀스), iterator(반복), function(함수), class(클래스)
# @ 시퀀스
# - iterator의 부분집합으로 반복이 가능하면서 + indexing이 가능한 것
# - 규칙을 가진, 연속성(index)이 있는 데이터 구조 ex> [1,2,3,4], (tu,ple)
# @ 반복 iterator
# - generator로 파생되면서, 나중에 병행처리도 해준다.
# @ 함수 @ 클래스
# - 파이썬에서 제공하는 int, str, dict, tuple, set 등의 데이터타입을 활용하여 데이터 모델을 만든다.

# [2] [데이터 모델] : 직접입력, 크롤링, 웹 데이터들을 
# - <python에서 제공한> 데이터 타입  = <4가지 형태 객체 형태 > 데이터 타입 4가지를 활용하여
# - sequence or Iterator or function or class로 잘 설계 한 것


# 1) 파이썬에서 데이터모델은 객체로 표현함.
# - 객체 : 파이썬의 데이터를 추상화 해놓은 것.
# - AAA **모든 객체는 id, type으로 정의할 수 있고 -> 각각 value를 가진다.**
# -     id(객체) -> identity-> reference값=주소값으로 생각
# -     type(객체) -> 객체의 자료형을 반환
a = 7 # 여기서 a도 객체. 데이터이므로
# print(id(a), type(a), dir(a))
#  <class 'int'> : 클래스형태로 객체로 표현된 int (python은 데이터타입을 4가지형태로 제공함. int 데이터타입 = 4가지중 class 표현)
# ['__abs__', '__add__',  : 부모 or 파이썬interpreter로부터 내려반은 더블스코어언더바메소드 + 속성값들
# dir()자체도 데이터 타입(list)이기 때문에, for문이 돌려진다.

# - [데이터 모델] : 직접입력, 크롤링, 웹 데이터들을 
# - <python에서 제공한> 데이터 타입  = <4가지 형태 객체 형태 > 데이터 타입 4가지를 활용하여
# - sequence or Iterator or function or class로 잘 설계 한 것


# 2) 일반튜플 vs  namedtuple 
# - 비교를 두점사이 거리로 한다.
# - 각 점을 tuple로 선언한다.
# - AAA tuple : [데이터 추가]는 가능하나, [불변형] = 한번 선언한 값은 변경할 수 없다. (list는 가능)
# - AAA 집합(set)과 비슷하게 추가되는 것은 유연하게 받아들이나 변하지 않는 것을 모아두는 것
# - AAA 바뀔일이 없기 때문에, list보다 속도가 빠르다. 

# 2-1) 일반 tuple로 데이터모델로 설정
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
# - 여기서부터 잘못된 코딩이다. 그 이유는??
from math import sqrt
line_leng1 =  sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1] )**2)
print('EX1-1 - ', line_leng1)
# - 일반 tuple은 sequence라, 순서(index)를 기억해야한다.
# ex> 0: x좌표, 1: y좌표 -> 비효율적이다.
# - 한번 코딩해놓은 것은 100년이상 지속되어야할 수도 있는 데, 저걸 항상 기억해야하다니
# - tuple의 각 index마다 label(레이블)링 해놓으야만 하는 불편함.
# - 복잡한 것에는 tuple에 label을 붙이도록 한 것이 namedtuple이다.
# - if 클래스로 작성한다면 훨씬 편하다. init메서드에서 self의 _x와 self의 _y를 처리하는게 더 편할 수 있다.
# - 인덱스가 아니라 <각 객체의 속성들>로 직접 x, y라고 명시하기 때문, 일관성이 있다. but 너무 무거워진다??
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
# pt1 = Point(1.0, 5.0)
# print(pt1.__dict__)
# - 추가는 되지만, 불변형으로 빠른 tuple에 label을 쓰고 싶어서 나온 것이 namedtuple이다.

# 2-2) namedtuple
# - 콜렉션 패키지에서 가져온다.-> namedtuple은 외부에 있다.
from collections import namedtuple
# - namedtuple은 클래스형태로 받아들일 수 있다. 소문자는 가능하지만, 첫글자만 대문자로 지어서 클래스처럼 나타낼 수 있음
# - 인자로는 '가짜 객체 name', '띄워쓰기형태로 label을 나열한다.' 가 들어간다.
Point = namedtuple('Point','x y')
# 클래스같이 선언한 뒤, inst처럼 데이터를 생성한다.
# - 띄워쓰기로 만든 label순서대로 콤마(,)를 찍어 데이터를 밀어넣는다.
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# inst의 속성 사용하듯이 namedtuple.사용형태1, namedtuple.사용형태2로 사용한다.
line_leng2 =  sqrt((pt2.x-pt1.x)**2 + (pt2.y-pt1.y )**2)
print('EX1-2 - ', line_leng2)
# AAA 클래스의 냄새가 나면서, 메모리는 적게 잡아먹으면서, tuple의 불변형 성질을 가지고 있다.
# - tuple과 달리, index를 사용X 속성처럼 label을 사용하여 틀릴일이 없다.

# 값의 비교 == 는 당연히 같다.
print('EX1-3 - ', line_leng1 == line_leng2)

# 3) 본격 namedtuple 사용법 
# - label 형태는 'x y' or 'x, y' 공백or콤마로 나눈 문자열 or ['x', 'y'] 문자열 리스트로 줘도 된다.
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# - label 형태에 tuple이 싫어하는 중복 + python예약어 class를 넣어보자.
# - rename=False -> True로 바꿔보자.
Point4 = namedtuple('Point', 'x y x class', rename=True)

print('EX2-1 - ', Point1, Point2, Point3, Point4 )
# <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>
# namedtuple은 class형태로 선언되어있다.

# 4) 객체 생성 
p1 = Point1(x=10, y=35) # 정말 유연하게도, label을 keyword방식으로지정할 수 있다.
p2 = Point2(20, 40)
p3 = Point3(45, y=20) # 순서대로 입력하더라도 마지막 하나를 지정해줄 수 있다.
# keyword방식도 제공하는데 label이 동일한 x가 2개가 있으면 어캐 keyword로 넣을까?
# 예약어는 어떻게 될까? (일단 vscode 도우미에서는 4개가 다 뜨긴한다. x y x class)
p4 = Point4(10, 20, 30, 40)
# namedtuple을 출력하면, 그 안의 label이 찍히니까 확인해본다.
print('EX2-2 - ', p1, p2, p3, p4)
# p4 --- Point(x=10, y=20, _2=30, _3=40)
# -> 중복된 것 _2 / 예약어도 _3
# - 잘 만들어진 고급 패키지에서는 rename옵션을 많이 사용한다.
# - x가 중복되니 랜덤으로 알아서 _2로 label을 바꿔줬다. 예약어도 _3으로 바꿔줬다.
# - rename을 default =False로 두면?? 에러가 난다.
# Point5 = namedtuple('Point', 'x y x class')
# ValueError: Type names and field names cannot be a keyword: 'class'

# cf) python의 똑똑함 
# AAA dictionary unpacking으로 kwarg 인자 대입
# - key:value를 get으로 꺼내서 -> 함수의 인자에 key=value의 kwarg로 대입해준다.
temp_dict = {'x' : 75, 'y' : 55}
p5 = Point3(**temp_dict)

# 5) namedtuple 사용
# 5-1) tuple의 index 접근방식
#       label을 가졌지만 index로도 쓸 수 있다.
#      tuple의 성질을 가지고 있기 때문에 가능.
#      but AAA index를 사용할거면 IndexError를 주의하자
print('EX3-1 - ', p1[0] + p2[1])
# 5-2) 클래스 변수 접근방식 : 데이터모델링을 똑똑하게 하고 싶어서 namedtuple을 사용한다.
print('EX3-2 - ', p1.x + p2.y)

# 5-3) unpacking 방식으로 사용
# - dictionary unpacking으로 함수인자에 keyword방식으로 넣어주는 것 이외에도 여러 unpacking이 있다.
# - 튜플을 콤마로 unpacking하는 것 처럼
# - namedtuple도 label없이 순서대로 unpacking가능함.
x, y = p3
print('EX3-3 - ',x+y)

# 5-4) rename 테스트
# - label의 이름이 똑같거나, 예약어를 사용했다면 알아서 다른이름으로 rename시킨다. by rename=True
print('EX3-4 - ',p4)


# 6) namedtuple의 강력한 메서드
# - namedtuple을 stackoverflow에서 recommand하는 이유.
# - python문서에서도 performance가 좋아서 많이 권장한다.

temp = [52, 38] # list는 데이터를 담은 container + iterator > sequence 

# 6-1) _make() : 새로운 객체를 생성한다.
# - 정해진 클래스형태의 nametuple._make( list )
# - list를 namedtuple로 만들 때 사용한다. 갯수가 맞아야함. 안맞으면 알아서 언패킹으로 들어감.
p4 = Point1._make(temp)
print('EX4-1 - ', p4)

# 6-2) _fields : 필드 네임(label) 확인 
print('EX4-2 - ', p4._fields)

# 6-3) _asdict() : 정렬된 사전인 OrderdedDict으로 반환한다.
# -> 오름차순정렬시킨 dict를 반환
print('EX4-3 - ', p1._asdict(), p4._asdict())
# OrderedDict([('x', 10), ('y', 35)]) OrderedDict([('x', 52), ('y', 38)])
# -> OrderedDict을 보면, 튜플리스트로 이루어져있다.
# -> AAA dict( OrderedDict))를 통해 리얼 dictionary로 변환시킬 수 있음.
print( dict(p1._asdict())) # {'x': 10, 'y': 35}

# 6-4) _replace() : 불변성을 지닌 tuple을 일부수정시킨 뒤 -> '새로운(id값이다른)' naemdtuple을 반환시킨다.
print('EX4-4 - ', p2._replace(y=100)) 

# 7) 실사용 실습(예제) : 짝을 이룬 
# - 학생 전체 그룹을 생성
# -- 각 반 20명, 4개 반(A, B, C, D반) -> 각 반에 학생 A1~20, B1~20, C1~20, D1~20 생성해보기
# - 가장 빠르고, 효율적으로 생성하는 방법은?

# 7-1) 네임드 튜플 선언 
# - tuple은 불변성을 가져 list보다 빠르다.
# - 학급 -> Classes의 namedtuple (클래스) 생성
# - 반 -> fieldname (label) 첫번째임. rank
# - 번호 -> 2번째 fieldname number
# - my AAA) 전체를 namedtuple로 선언하고, ->  2개 상/하위 group을 반별(ABCD) 번호(1~20).. 를 field에 순서대로 나열해서 작성한다.
# - 즉 4 * 20의 각 그룹을 순서대로 fieldname(label)로 준 것이다.
Classes = namedtuple('Classes', ['rank','number'])


# 7-2) 각 그룹의 리스트 생성 by list comp
# - 각각의 그룹을 만들거 R그룹 * N그룹을 80개의 string을 붙혀서 조합을 만들어줘야한다.
# - 번호는 str()으로 문자열로 생성하자.
# rank = list('ABCD')
# - 공백 + split으로도 리스트를 만들 수 있다. -> 2글자 이상의 리스트 쉽게 만들 때 유용할 듯
ranks = 'A B C D E'.split()
# print(ranks)
# - 데이터 생성도 comp로 !
numbers = [ str(n) for n in range(1, 21)]
# print(numbers) 
# AAA 2중포문을 list comp에 넣어서 멋있게 2개 그룹 string붙이기


# 7-3) 그룹명을 field로 준 namedtuple + 그룹 데이터리스트 + list comp를 이용한 데이터 생성
# - namedtuple로 객체 생성에 들어갈 2개의 인자를 2중 list comp를 돌면서 그룹별로 주면 된다.
# - AAA 이미 데이터는 그룹별로 주어져있어야한다. -> list comp로 생성
# - AAA 각 그룹별 list데이터 + namedtuple구조체(class형태)를 이용해서
# - AAA 그룹갯수만큼의 for문을 listcomp에 중복하여 데이터 모델을 만든다.
# - AAA namedtuple의 fielname을 사용해서 각 그룹정보를 각각 뽑아낼 수 있다.
# - s.rank, s.number
# - 그러나.. 인덱싱을 해야한다.. 결국 제일 껍데기는 list라서
# - 접근만 .rank / .number를 마치 dictionary처럼 사용할 수 있다.
students = [ Classes(rank, number) for rank in ranks for number in numbers ]
# print(students)
print('EX5-1 - ', students[4].rank)
print('EX5-2 - ', students[4].number)
# cf) list comp는 for x for y 일 때 ,x먼저 돈다 
# - AAA list comprehension + namedtuple 조합을 많이 사용한다고 한다.


# 8) 각 field들의 데이터 생성 선언없이 한번에 해결할  수 있다.
# - 추천하지 않는다. -> list comp를 너무 길게 적으면 **가독성이 떨어져 추천하지 않는다.**
# - AAA  최종자리 + for 자리 -> 변경이 안되므로 in에서 list comp를 한번 더 돌려 미리 완성해주는 방법
# students2 = [  Classes(rank, number) for rank in 'A B C D'.split() for number in [str(n) for n in range(1, 21)]]
# - 외국사람들 중에 줄바꿈을 가독성을 살리는 사람들도 있다.
# students2 = [  Classes(rank, number) for rank in 'A B C D'.split() 
#     for number in [str(n) for n in range(1, 21)]    ]
students2 = [  Classes(rank, number) 
                        for rank in 'A B C D'.split() 
                            for number in [str(n) 
                                for n in range(1, 21)]]


print('EX6-1 - ', students[4].rank)
print('EX6-2 - ', students[4].number)

# 9) 출력
for s in students: 
    print('EX7-1', s)
# EX7-1 Classes(rank='A', number='1')
# EX7-1 Classes(rank='A', number='2')
# EX7-1 Classes(rank='A', number='3')
# EX7-1 Classes(rank='A', number='4')

