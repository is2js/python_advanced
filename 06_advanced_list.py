# 06 데이터 모델 - advanced_list

# - list comprehension
# - generator : 확장시 머리아프게 만듬. -> 나중에  coroutine, 병행처리, thread와 관련됨 

# - 시퀀스 정리
# - containter vs flat
# -- AAA 컨테이너 : 서로 다른 자료형(int str float 등)을 저장할 수 있는 것 
# -- AAA list tuple collections.deque 3개가 존재
# -- ex> [1, 3.0, 'str']
# -- AAA 플랫 : 1개의 자료형만 저장 -> 속도처리 좋음 -> numpy에서 list 대신 array 쓰는 이유도 array.array의 1개 자료형
# -- AAA str, bytes, bytearray, array.array, memoryview 5개 

# - mutable(list) vs immutable(tuple 등 불변형. 한번 값 삽입시  불변)
# -- AAA 가변 : 값 저징이후 변경해도 됨.
# -- AAA list, bytearray, array.array, memoryview, deque 5개 -> 언제든지 값을 변경할 수 있다.
# -- AAA 불변 : 한번 값 지정이후 변경안됨.
# -- AAA tuple, str, bytes 3개 -> 한번 값을 저장해놓고  갖다 씀. 값이 늘어날 수 있지만 수정은 없다.

# - list vs array 
# - sort vs sorted


# 1) 지능형 리스트(Comprehending Lists) = list comprehension 

# 1-1) 변수 + for 값 append or index 할당으로 데이터변환
# - 특수문자(기호,문자) to unicode(번호) by ord(기호문자)
# -- QQQ 변수1개 + for 값을돌며 QQQ<<변환값append>> or  for index를 돌며 QQQ<<할당  [i] = 변환값([i])>>s
chars='!@#$%^&*()_+'

codes1 = []
for s in chars:
    codes1.append( ord(s))

print('EX1-1 - ', codes1)


# 1-2) list comp로 데이터 변환
codes2 = [ ord(s) for s in chars]
print('EX1-2 - ', codes2)

#- AAA 성능은 데이터가 아주 많아질 경우에만, list comp가 우세하다고 한다. 2~3배도 아니라.. 일반 코딩에서는 거의 차이를 못느낀다.


# 1-2-1) if문 필터링도 빠른 list comp
# - python 공식 레퍼런스에서 추천함. 속도가 약간 우세하다고 많은 사람들의 의견.
# - 일반 변수+for(append or 할당)문으로 데이터변형시에는 if문도 따로 작성되어야함.
codes3 = [ ord(s) for s in chars if ord(s) > 40]
print('EX1-3 - ', codes3)

# 1-3) list map으로 데이터 변형
# - 데이터변형을 변수+for(값append or index할당)이 아닌 list( map( ))
# - AAA map은 안보이니 마지막에 list()처리도 묶어서 해줘야하는 것을 생각
# - AAA map은 함수를 실행()하지 않은 상태의 객체 상태로 넣어야 map이 알아서 하나하나 넣어준다.
# codes4 = list(map)
codes4 = list(map(ord, chars))
print('EX1-4 - ', codes4)

# 1-3-1) list filter map으로 데이터 필터링
# - AAA filter는 첫번째 인자로 함수를 받는다 like map -> lambda로 필터링 식을 만든다.
# - AAA 즉, filter함수의 첫번째 식에는 lambda로 필터링 식을 준다. (if문 처럼)
# - filter의 2번째 인자에 데이터를 줘야하는데 map으로변형한 데이터를 준다.
# filter(lambda x: x>40, )
codes5 = list(filter(lambda x:x>40, map(ord, chars)))
print('EX1-5 - ', codes5)
# - AAA list map or list filter map 보다 listcomp가 더 우세하다고 한다.

# 1-4) 반대로 unicode(숫자) -> 문자or기호로 바꿔보자. by chr() + list comp
print('EX1-5 - ', [chr(s) for s in codes1])

# AAA 짧으면 list comp를 사용하고, 너무 길어진다 싶으면 정석으로 변수+for 값append, index할당으로 해결하자!!!



# 2) generator 
# - AAA iterator : 반복문에 쓸 수 있는 것들
# - AAA generrator : 반복을 하는데 값을 하나씩 생성해내는 / 일괄생성=메모리유지의 과정X / 한번에 한개의 항목만 생성
# - 단일 자료형만 저장할거면 (containter vs flat) 
# - lsit보다 array가 더 낫다고 했다. 
import array

# AAA 한번에 한개 요소만 생성 -> 메모리유지X -> 성능상 압도적으로 좋다.
# 2-1) tuple comp를 이용한 데이터 변형 -> 데이터변형 + generator
tuple_g = ( ord(s) for s in chars) 
print('EX2-1', tuple_g) # <generator object <genexpr> at 0x04061BF0>
# AAA 대박) 튜플 comp는 list가 tuple형이 아니라 generator로 출력된다.
# - tuple comp는 사실 없고, generator가 생성된다.
# - 아직 메모리에 생성 + 전체를 생성하지 않고 + 줄만 세워서 첫번재 생성 대기 중
# - 일반적인 for x in list의 상태는 --> list 100만개를 이미 메모리에 올린 상태다.
# - 많은 데이터 -> generator를 이용해 대기 상태로 생성하는 것이 훨씬 우세하다. 

# 2-2) next()를 써야 첫번째 값 생성후 반환
print('EX2-2', next(tuple_g)) 
print('EX2-3', next(tuple_g)) # 수식만 물고 있다가 2번째 next가 호출 될 때, 데이터를 메모리에 올린다.
# - next()나 for()문 뒤에 올린 경우가 아니라면, generator상태로 메모리에 올리지 않는다.


# 2-3) array.array( 'typecode', generator)
# - 첫번째 인자는 자료형1개만 가능하므로 -> 데이터타입<코드>을 받는다 ex> int -> 'I' or 'i'
# - 2번재 인자에 tuple comp의 generator를 넣어주자.
array_g = array.array('I', (ord(s) for s in chars))
print('EX2-4', array_g) # array객체는 그대로 출력된다. 근데 list모양은 아니다. 
print('EX2-5', array_g.tolist()) # array객체를 마지막사용시만 tolist()로 변환해서 사용한다.

# 3) generator 예제1
# 3-1) c 그룹리스트 (ABCD): by comprehension for 첫번째 
#      n 그룹리스트 (1,2,..20) : by comprehension for 2번째
#      list(x)  tuple comp로 generator 생성
#      생성시 '%s' % 를 이용하여 2개의 그룹데이터 이용한 A1, A2 ... 의 generator
# AAA my) 그냥 list comp처럼 데이터를 작성하고, 마지막에 [ ] 대괄호를 () 소괄호로 바꾼 tuple comp같이 생긴 것은 generator다.
# AAA generator는 출력해도 generator object라고만 표시되고 데이터는 메모리에 안올라가있음.
# AAA next()나 for문 in에 들어가지 않은 이상 첫값을 뱉어내진 않는다.
# AAA generator는 실행시점에 값을 반환하는 구조이다.
print('EX3-1', ('%s'%c +str(n) for c in list('ABCD') for n in range(1,11)) )

# 3-2) for문의 in자리에 generator를 붙혀보자.
# AAA for문의 in자리에 오면, 내부적으로 next()를 게속 호출하는 것임.
for s in ('%s'%c +str(n) for c in list('ABCD') for n in range(1,11)):
    # print('EX3-2 - ',s)
    pass


# 4) list comp 사용시 주의점
# - AAA list안에서 list의 곱하기는  1개의 리스트안에 그만큼 list가 +(유일한 연산) 붙어서 요소들이 콤마로 붙는다.
# marks1 = [['~'] * 3] # ['~', '~', '~'] # 1개 리스트안에 요소드이 반복
# - AAA list안에서 list의 반복은 반복수만큼의 n개의 리스트가 복제 
# - AAA   for반복시 내부적으로 요소가 append된다고 한다.
marks1 = [['~'] * 3 for n in range(3)] # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks1)
# - AAA 엌... 
marks2 = [['~'] * 3 ] * 3 # [['~' '~' '~']<--이놈이 요소]  요소가 늘어나서 [ [], [], []]
# - but AAA list밖에서 곱하면.. 결국에는 똑같은 id의 놈을  append시켜 같이 변하는 것을 확인해보자.
print(marks2) 

# 4-1) 위의 선언이 왜 잘못되었는지 알아보기
# - AAA 객체의 증명은 값을 수정해서 파악한다.!
marks1[0][1] = 'x'
print(marks1) # [['~', 'x', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks2[0][1] = 'x'
print(marks2) # [['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~']]
# - marks1는 원하는 것만 바꼈으나..
# - marks2는 모든 요소의 2번재 데이터가 다 바꼈다...

# 4-2) 증명 by id값 출력
# - 느낌상.. 출력상... marks2의 3개의 요소가 다 똑같은 놈인 것 같다.
print('EX4-5 - ', [id(i) for i in marks1]) # EX4-5 -  [59311728, 68515760, 59333768]
# - list comp로 반복해서 복제한 [['~','~','~']->3개 ] 는 모두 다른 것이지만.
print('EX4-6 - ', [id(i) for i in marks2]) # EX4-6 -  [59330968, 59330968, 59330968]
# - list * 3으로 요소를 더하여 복제한 [['~','~','~']->3개 ] 는 모두 같은 id이다.
# - AAA 
# - AAA list comp로 데이터 생성시, list 밖에서 곱하면 동일id객체를 append시킨 결과다 주의하자.
# - AAA list comp로 시작했으면, 내부에서 데이터를 완전히 다 만들고 밖으로 나오지 말고 끝내자.
# - my) 난 list comp안에서 list를 반복시켜 복제하는 것을 거의 사용하지 않았음.
print('My test', [ list('ABCD') for n in range(2)])
print('My test2', [ '조재성 조재경'.split() for n in range(3)])