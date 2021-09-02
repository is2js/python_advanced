# first-class functions = 일급함수
# - closure->파생되는 decorator

# 데코레이터
# 1. 중복 제거
# 2. 클로져보다 문법 간결
# 3. 조합해서 사용 용이. 협업가능.
# 예를 들어, 
# 클릭마다 로그 전송
# 로그인마다 회원정보 체크 전송
# 함수 실행시, 먼저 체크하기 ex> 결제시 마일리지 있는지

# 단점 : 디버깅이 어렵다. 가독성이 안좋다. 에러 발생지점 추적 어려움.(pycharm은 다 찾아준다.)

# AAA my) cloure의 메인함수 Freevariable에 보존데이터를 물고 다닌 것 과 달리
# AAA my) decorator는 메인함수 인자func을 물고 있으면서, 내부함수에서 func()호출 + 전후작업까지 정의해놓고 호출시 실행되게 한다.
# 1) 실행시간 - 함수실행 -  종료시간  걸린시간 + 매개변수 표기 데코
# - 함수실행전/후 항상 반복되는 것이라서 데코레이터로 만든다.


import time #  시간 측정
# print(time.perf_counter())  # 함수가 따로있다. 
# 1-1) 메인함수의 인자로는 <나중에 밖에서 실행할 함수>를 인자로 준다.
#     - closure에서는 메인함수 인자를 안받았었다.
#     - 메인함수는 Freevariable 할당(여기선 func인자 받기)+외부변수+처리하는 내부함수를 실행부없이 return하는 역할
def perf_clock(func):
    # 1-2) 하고싶은 처리는 항상 내부함수에서 외부변수를 받아서 한다.
    # - 외부에서 받을 인자를 *args를 통해 튜플형태로 내부에서 처리한다.
    # - 왜냐면 내부함수 실행부X반환후 -> 내부함수 실행부(외부인자)가 들어가는데, 콤마로 하나씩 받은 것을 편하게 처리하기 위해서는 *args로 매핑해서 넘겨서 처리한다.
    # - 외부인자는, 메인함수가 받은 func가 수행할 인자들이다.
    # - 내부함수는 시간이 이미 처리가 완료되서 반환되니 이름을 ed과거형으로
    def perf_clocked(*args):
        # 1-3) 시작시간
        st = time.perf_counter()
        # 1-4) return해줄 것은, 나중에 호출할 함수의 실행이다.
        # - 받은함수인자를 실행시, 당근 외부인자를 넘겨서 처리되어야한다.
        result = func(*args)
        # 1-5) 종료시간
        et = time.perf_counter() - st 
        # 1-6) 함수명, 매개변수를 추가로 출력해주자.
        # AAA 함수명은 함수.__name__에 string으로 입력되어있다.
        name = func.__name__
        # AAA 매개변수는 args를 tuple comp = generator로 돌면서 repr()를 찍어주면 된다.join해주면 된다.
        # - tuple comp는 없다. generator를 만드는 것일 뿐.
        arg_str = ','.join( repr(arg) for arg in args) # join은 list를 반환한다.
        # - %0.5f 실수를 잘라서 받기 위해 %를 썼으며, %로 했으면 -> %로 받아야한다. {} .format()
        print('[%0.5fs] %s(%s) -> %r' % ( et, name, arg_str, result))
        return result
    return perf_clocked

# cf) time.time is not accurate on windows we should be using perf_counter. 
# cf) 함수의 인자()에다가 튜플 변형해서 넘길 때는, tuple comp -> generator로 괄호없이 넘겨도된다.
# cf) 내부함수(*args)로 받은 것을 출력해보면
#   -> *args인자 -> 함수내부에서는 args로 쓸 경우(이때가 패킹), 튜플로 받아쓴다. args:  (0.01,)  (0.01, 3)
#   -> 함수내부에서 다시 *args를 그대로 쓸 경우, 알아서 나눠쓰는개별 인자가 된다.  *args:  0.01  0.01 3
#      - *argf를 그대로 쓸 경우, 알아서쓰다보니.. iterater자리에 못들어간다. for in 자리 등.


# 1-2) 데코레이터를 적용할 함수들 작성

# n초 쉬기
def time_func(seconds):
    time.sleep(seconds)

# 각 인자들을 콤마로 받 -> 패킹 (*args) -> args 튜플 로 사용 -> sum( 튜플 )로 누적합.
def sum_func(*numbers):
    return sum(numbers) 

# 재귀함수
def fact_func(n):
    return 1 if n<2 else n * fact_func(n-1)


# 2) 데코 사용 안했을 때 == 클로져처럼 사용해보기
# 2-1) 클로저에서 데이터를 물고 계속 사용했던 FreeVariable 영역의 변수와 달리
#  AAA  deco는 메인함수 인자로받은 (func)을 튜플 형태로 해당영역에서 가지고 있게 된다.
#  AAA 가지고 있어야, 내부함수에서 처리가능하다. 내부함수가 인식할 수 있는 영역이다.
non_deco1 = perf_clock( time_func ) # (func)의 자리에 -> time_func이 들와서 스냅샷상태. 실행은 아직 안된 상태
print('EX1-1 - ', non_deco1, non_deco1.__code__.co_freevars) # 실행전,  프리변수 영역 확인 
# 실행전 : 내부함수가 아직 실행전인 function상태 : function perf_clock.<locals>.perf_clocked at 0x039EF780>
# non_deco1.__code__.co_freevars : ('func',) 클로져의 list 등의 보존데이터 대신 함수로 받는 func가 물려있다.

non_deco2 = perf_clock( sum_func ) # (func)의 자리에 -> time_func이 들와서 스냅샷상태. 실행은 아직 안된 상태
non_deco3 = perf_clock( fact_func ) # (func)의 자리에 -> time_func이 들와서 스냅샷상태. 실행은 아직 안된 상태
print('EX1-2 - ', non_deco2, non_deco2.__code__.co_freevars) # 실행전,  프리변수 영역 확인 
print('EX1-3 - ', non_deco3, non_deco3.__code__.co_freevars) # 실행전,  프리변수 영역 확인 

# 2-2) 함수 실행
# - time_func을 실행시키면서, 선후에 작업이 추가됨을 확인.
# print('EX1-4 - ', non_deco1(1))
# print('EX1-5 - ', non_deco2( *range(1,100)))
# print('EX1-6 - ', non_deco3(100))



# 3) 데코레이터 사용
# - 함수 정의부분에 @클로져펑션이름을 달아주면, 
# - 해당함수만 실행시키면 알아서 데코부분이 작동한다.
@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers) 

@perf_clock
def fact_func(n):
    return 1 if n<2 else n * fact_func(n-1)

print('EX1-7 - ', time_func(1))
print('EX1-8 - ', sum_func(1,10,100))
print('EX1-9 - ', fact_func(5)) # 재귀함수에서는 deco를 생략하자.. 자기함수(n-1)이 실행되니까.. 계속 데코 실행됨ㅋㅋ