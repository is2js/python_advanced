# 06 데이터 모델 - advanced_tuple
# - tuple에서 중요한 것은 불변성 -> 변경되면 id값이 변경됨.
# AAA **packing(1개를 알아서 쓰도록 인자에)과 unpacking(할당시)**

# 1) 패킹( 묶음이다 -> 알아서 풀어씀.) 예제
# - 튜플은  변수할당시 갯수에 맞춰서 나숴 삽입해준다.
print('EX5-1 - ',divmod(100, 9)) #(11, 1)
# AAA 만약, 튜플 괄호가 있다면 -> 1개의 인자가 된다.
# - divmod()함수 입장에서는 1개의 인자가 온 것이 됨.
# AAA 튜플앞에 *()를 붙이면, packing = 1개로 넘기지만, 알아서 풀어서 써라.
# - *는 1개로 묶어서 보내니 <<알아서 써라>>라는 말 -> 내부적으로 unpacking을 할 것이다.
# - 예를 들어 *(100, 9) -> 100, 9 
print('EX5-2 - ',divmod(*(100, 9)))
# - 극단적인 패킹의 예제 -> 튜플앞에 *()를 씌워주면, 튜플이 아닌 space로 띄워서 풀린 상태로 출력된다.
print('EX5-3 - ',*(divmod(100, 9)))


# 2) 언패킹(할당) 에제
#  - range(10)을 언패킹(할당)을 할 떄, 패킹이 있다면?
x, y, *rest = range(10)
print('EX5-4', x, y, rest) 
# - AAA 알아서 변수에 삽입하는데, 패킹이 붙어있으면 알아서 리스트로 삽입됨.
# - 즉, 패킹된 변수는 python이 일아서 list로 묶어놓는다.
x, y, *rest = range(2)
print('EX5-5',x, y, rest) 
# - 언패킹되는 값이 없을 때도, 에러 없이 알아서 list를 비워둔다.
x, y, *rest = 1,2,3,4,5
print('EX5-6',x, y, rest) 

# method에서는 
# - *1개 : 패킹된 묶음 ex> tuple, list 등
# - **2개 : dictionary
def test(*args, **kargs):
    pass



# 3) 가변 vs 불변형
# list나 tuple이나 서로 다른 자료형을 담을 수 있는 컨테이너라는 것은 동일하지만
# - 가변 대표 : list, 불변 대표: tuple
l = [10, 15, 20]
t = (10, 15, 20)

# - AAA 원소의 재할당으로 가변/불변을 판단한다.
# l[0]=1
# t[0]=1 # TypeError: 'tuple' object does not support item assignment


print('EX6-1 - ', l, t, id(l), id(t))  
# - AAA 각 list나 tuple에 2를 곱해보자. -> 곱하기 -> list안에서 요소들이 콤마로 여러개가 복제됨.
# print(l*2, t*2) # (10, 15, 20, 10, 15, 20) [10, 15, 20, 10, 15, 20]
# - AAA 같은 값을 다시 할당해도, id는 변하지 않는다.
l = l
t = t
print('EX6-2 - ', id(l), id(t)) 

# 4) list 재할당시 주의 
# 4-1) 일반 재할당 : 새로운id의 객체가 됨.
# - AAA **새로운 값을 변수에 할당하면 무조건 id는 달라진다.!!**
# - AAA 곱한 것을 다시 해당 변수에 대입해서 id를 보면, 둘다 똑같이 id가 변한다.
l = l*2
t = t*2
print('EX6-3 - ', id(l), id(t)) 

# 4-2) 연산자재할당 : shallow copy로 객체id는 동일한놈이 값만 바뀐다.
# - list만 연산자재할당을 이용시, 같은 객체를 재활용해서 바뀐다.
# - AAA 객체가 deepcopy되지 않도록(메모리 사용량..) 주의할 때는 연산자재할당..
l *= 2
t *= 2
print('EX6-3 - ', id(l), id(t)) 


# cf) DataFrame.copy()는 deepcopy()로 같은값을 할당해도 보존된다.
# - 원본df을 보존하면서 & 같은 값을 복제(할당)할 때 쓴다.



# 5) sort vs sorted 정렬 메소드 2개 4개의 인자.
# - reverse, key=len, key=str.lower, key=func 의 인자를 받음.

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
# 5-1) sorted는 원본은 변경안되고, 새로운정렬된 객체를 반환만 함.
# - AAA 정렬된 새로운객체로 copy해서 사용하고싶을 땐 sorted
# - AAA 원본이 귀중한 정보이면, sorted로 새로 받아서 사용하자.
test = sorted(f_list) # 문자열도 기본적으로 abc순으로 정렬됨.
# print(test)
# print(f_list) # 원본은 그대로 있음.
print('EX7-1 - ', sorted(f_list))
print('EX7-2 - ', sorted(f_list, reverse=True))
print('EX7-3 - ', sorted(f_list, key=len)) # 내장함수 len을 넣어주면, 길이 순으로 오름차순으로 정렬해준다.
print('EX7-4 - ', sorted(f_list, key=lambda x:x[-1])) # lambda는 각 원소를 받아서 정렬대상을 조작하여 정렬기준을 만든다.
print('EX7-5 - ', sorted(f_list, key=lambda x:x[-1], reverse=True)) 
print('EX7-6 - ', f_list) # sorted는 원본이 변경안되고 새로운 객체를 반환해줬었다.


# 5-2) sort : 정렬후 객체 직접 변경
# - sort 는  객체.sort()는 직접 객체 변환한다. 할당의 개념이 아니 replace=True개념으로 
# - AAA .sort()는 할당받아도, None이 출력된다.
a = f_list.sort()
print(a, f_list) # 원본이 바뀌니 .sort()는 조심해서 사용한다.

# AAA Python에서는 None값을 반환하는 메소드는 -> 반환값이 없다는 의미이다.
# - AAA 이미 구현된 함수가 None을 반환? -> 아~ 객체를 직접 바꾸는 함수구나!!
# - AAA 직접 함수를 작성해도 객체 직접변환이면 None반환하도록 작성
print('EX7-7', f_list.sort(), f_list)
print('EX7-8', f_list.sort(reverse=True), f_list) # sort() 찍은 문장은 다 None이다 .원본을 봐야함.
print('EX7-9', f_list.sort(key=len), f_list) 
print('EX7-10', f_list.sort(key=lambda x:x[-1]), f_list) 
print('EX7-11', f_list.sort(key=lambda x:x[-1], reverse=True), f_list) 
