# 09 시퀀스 - set 심화
# Frozenset
# - 한번 할당하면 수정/추가 불가한 set을 만들어주는 클래스가 따로 있다.
# - 집합이라서 응용과학분야에 많이 사용 된다.

# 1) 선언
# 1-1) 딕셔너리 처럼 열지만 단일 자료형으로 입력
s1 = {'Apple', 'Orange', 'Apple', 'Orange','Kiwi'}
# 1-2) 생성자 메소드 set()안에다가 list 형태로 넣어줘도된다.
# cf) dictionary도 dict()생성자 메소드 안에, keyword방식으로 넣어줘도 됬었음.
s2= set(['Apple', 'Orange', 'Apple', 'Orange','Kiwi'])
s3 = {3} # 데이터가 1개라도 있으면 set이다
s4 = {} # 아무것도 안 줄때만, 딕셔너리다. 공집합x
#  빈 set은 set() 생성자 메서드로 선언해줘야한다.
s4 = set()
# AAA 프로즌셋은 생성자메소드 frozen()안에 set데이터를 넣어준다.
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange','Kiwi'})

# 2) 추가 
# 2-1) set에 추가(add)
# - 원소를 추가해주고, type()으로 set이 맞는지 확인해주기
# - set 메소드는 add가 있음.
s1.add('Melon')
print('EX1-1 - ',s1, type(s1)) # AAA set은 중복x -> hash가 더 중요함 -> 순서보장안된다.!!
# AAA 중복X가 중요한 set은 hash값이 중요해서 순서 보장안한다!
# AAA set과 dict key는 내부적으로 중복검사를 위해 hash값을 생성할 것임.
# -> 속도가 느려질 것이다. -> set은 이미 정재된 데이터로 사용해주는 게 좋다.
print('EX1-2 - ',s2, type(s2)) # AAA set은 중복x -> hash가 더 중요함 -> 순서보장안된다.!!
print('EX1-3 - ',s3, type(s3)) # AAA set은 중복x -> hash가 더 중요함 -> 순서보장안된다.!!
print('EX1-4 - ',s4, type(s4)) # AAA set은 중복x -> hash가 더 중요함 -> 순서보장안된다.!!
print('EX1-5 - ',s5, type(s5)) # AAA set은 중복x -> hash가 더 중요함 -> 순서보장안된다.!!


# 2-2) frozenset에 추가
# s5.add('Melon') # 'frozenset' object has no attribute 'add'
# - frozenset은 add메소드를 아예 가지고 있지도 않는다.
# AAA 중요한 데이터 + 캡슐화되서 보호 + 수정/추가 금지 일때 사용한다.



# 3) set선언 2가지 방법 ( {a } set([ a])  )
# - 생성자메소드쓰는 것보다, 딕셔너리처럼 단일로 쓰는 것이 더 빠르다.
# AAA 속도가 빠른지를 dis.dis를 활용해서 판단한다.
from dis import dis
# - dis는 python interpreter가 코드를 어떻게 실행하는지 보여준다.
print('EX2-1',dis( '{10}')) # load_const 10 변수선언 -> build set -> return
print('EX2-2',dis('set([])')) # name을 먼저 선언함 -> list build -> call function -> return  : 더 많은 line으로 구성



# 4) 지능형 집합
# - dict comp는 { key:value }형태 / set comp는 { 값 for }형태로 내부내용만 다르다.
from unicodedata import name

# print('EX3-1', { x for x in range(256)}) # set comp를 통한 중복제거
# print('EX3-1', { chr(x) for x in range(256)}) # 숫자(유니코드)->유니코드 문자(키보드key)
print('EX3-1', { name(chr(x),'') for x in range(256)}) # 유니코드 문자(키보드key)-> 설명 by name( 유니문자, '')
