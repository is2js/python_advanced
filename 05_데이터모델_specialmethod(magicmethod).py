# 04 데이터 모델 - special method = magic method
# 미리 python이 만들어놓은 연산자들을 overloading한 뒤 사용할 수 있는 집합들
# - cf) 파이썬 중요 프레임워크 : 시퀀스, 반복, 함수, 클래스

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






