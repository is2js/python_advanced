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
l = (10, 15, 20)
m = [10, 15, 20]