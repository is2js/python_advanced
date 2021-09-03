
# 파이썬 참조 심화
# - 참조의 다양한 특징
# - copy
# - deepcopy
# - 매개변수 주의점

# 객체 참조의 중요한 특징들(Python Object Referrence)
# print('EX 1-1 -', )
print('EX 1-1 -', )
print(dir()) # dir()에 인자를 안넣으면, py파일을 실행시키는 주체에 대한 attr들의 name space가 나온다.
# - 현재 scope(__main__, 파일1개)에 대한 attr를 모두 볼 수 있다.
# print(__name__) # py실행주체의 name은 __main__이다. (스크립트 실행시)
# - 스크립트로 실행시 python 13.py의 주체는 파일1개에 진입하고, 위에서부터 아래로 실행된다.


# 1) id vs __eq__(==)의 증명
x = {'name' : 'kim', 'age' : 13, 'city' : 'Seoul'}
y = x # 같은 값을 넣으면, 같은id
# AAA 효율성때문에, 다른변수지만, 같은값 할당시 같은 주소를 보고 있다.
# - 같이 수정된다.
print('EX 1-2 -', id(x), id(y)) # 같은 아이디. 
print('EX 1-3 -', x==y) # 같은 값. 
print('EX 1-4 -',  x is y) # 같은 아이디. for 효율성
print('EX 1-5 -',  x, y) # 같은 아이디. for 효율성

x['class'] = 10
print(y['class']) # x를 수정하면 y도 같이 수정된다. 여러변수가 1개 주소를 보고 있기 때문
# - 별개의 객체가 아니다. 개발시 주의해야함.
# - dict() 생성자나 똑같은 값(변수x)로 새로 할당받아서 원본을 유지해야한다.


# AAA 처음 할당을 같은 값으로 했다면? -> 다른 것
z = {'name' : 'kim', 'age' : 13, 'city' : 'Seoul', 'class':10}
print('EX 1-6 -', x==z) # 같은 값으로 생성했지만, 각각 생성했다면
print('EX 1-7 -',  x is z) # 다른 아이디 x, z
print('EX 1-7 -',  x is not z) # 다른 아이디 x, z


# 객체 생성후 id는 객체주소(=ideneity)를 비교 vs ==(__eq__)는 값을 비교
# AAA 값을 비교하기보단 is로 판단하는게 훨씬빠르다!!
# - dict의 100만건 데이터를 값을 다 비교하면 너무 느려짐.
# AAA 값이 같은 것 같은데 비교할 경우,  값 비교전에 id를 확인해주는 sense도 가지자.


# 2) 튜플-가변형 vs 튜플-불변형의 비교
# 튜플은 가변형(2차원 container)와 불변형(only tuple구성, 2차원도)이 따로 있다.
# - 불변형은 hash를 생성하고, 가변형은 언제든 변하니 hash생성이 없다.
# 2-1) 가변형은 같은값이라도 각각 값할당 -> 서로 다른id가 된다.
tuple1 = (1, 15, [100, 1000])
tuple2 = (1, 15, [100, 1000]) # 각각 값을 할당 -> id는 다르다.
# tuple3 = tuple1 # my) 튜플 불변형 hash를 생성하더라도, 똑같은 변수할당 -> 같은 id(주소)를 바라본다.
# print(tuple1 is tuple3) #true
print('EX3-1 - ', id(tuple1), id(tuple2))
print('EX3-2 - ', tuple1 is tuple2 ) # 튜플 가변형은 일반적인 copy가 된다.
print('EX3-3 - ', tuple1 == tuple2 ) # 값은 같다. 하지만 id는 값 각각할당시 다르다.
print('EX3-4 - ', tuple1.__eq__(tuple2) )

# 2-2) my) 튜플-불변형
# - 불변형은 only tuple로만 구성된 tuple이며, 불변형특징으로서 hash가 생성되어 매우 빠르다.
# - 불변형은 각각 값할당해도 -> 불변값=hash지정(고정, 값자체에id가 할당됨) -> 모든 변수가 같은 id를 보고 있는다.
tuple3 = (1, 15, (100, 1000))
tuple4 = (1, 15, (100, 1000)) 
print('EX3-5 -my) ', id(tuple3), id(tuple4))
print('EX3-6 -my) ', tuple3 is tuple4 ) 
print('EX3-7 -my) ',id((1, 15, (100, 1000)))) # 심지어.. 값자체에도 id가 있다.

# my) dict는 불변형key이외에 value 도 같이 움직이므로.. {} 값 자체에 대한 hash는 생성안하나보다.




# 3) Copy와 deepcopy
# - 위에서 한 것은 copy위주, 
# my) copy: 똑같은 (값의) 변수 할당 -> 같은 id를 보며 연결됨.
# my) 불변형 예외 : 똑같은 값을 할당 -> 같은 id를 봄 by hash, 고정된 값

tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1 # 똑같은 (값의) 변수할당 -> copy
tl3 = list(tl1) # **AAA list()생성자는 itertable을 받아 한꺼풀 벗겨내고 사용한다.
# - tl1 list나   list(tl1)이나 완전히 값은 같다!! 
# - but 값이 들어가는 것이므로 -> 같은 값을 할당 -> 불변형아닌 이상에는 다른 id
# AAA 같은 값의 변수를 이용해서, deepcopy하고 싶다면 생성자(list(), dict())등을 활용하자.
# - 생성자들은 iter변수를 받아도, 알아서 *언패킹 -> 패킹처리하여 값만 빼온다.

print('EX4-1 - ', tl1 == tl2 ) 
print('EX4-2 - ', tl1 is tl2 ) 
print('EX4-3 - ', tl1 == tl3 )
print('EX4-4 - ', tl1 is tl3 )

# 증명)
# - 증명은 값 변형후 출력해서 같이 변햇는지 따로 노는지 보면 됨.
tl1.append(1000)
tl1[1].remove(105)
# -> tl1, 2는 바뀌고 tl3는 새로운 객체라서 안바뀔 것
print('EX4-5 - ',tl1)
print('EX4-6 - ',tl2)
print('EX4-7 - ',tl3)


# 참고) list외에 tuple도 +연산으로 요소를 괄호떼고 이어붙일 수 있다.
# AAA 주의점 : list속이라도 only tuple은 불변형 -> id값일정
# AAA -> +=로 이어붙혀서 달라지면? -> 안변한 것 같지만 id는 변했다.
# [10, [100], (5, 10, 15), 1000]
print(id(tl1[2])) # (5, 10, 15)의 id값 17701384

tl1[1] += [110, 120]
tl1[2] += (20, 25)
print('EX4-8 - ',tl1)
print('EX4-9 - ',tl2)
print('EX4-10 - ',tl3)

print(id(tl1[2])) # (5, 10, 15, 20, 25)의 id값 17760880 -> 달라짐.
# - my) list의 각 요소들도 id를 가진다. (바깥 list 전체의 id값과도 다른 값이다.)
#   그리고 불변형 요소를 변경했다면, 새로운  id가 할당된 것.
#   만약, 튜플을 += 이어붙이기 안했다면? 해당 요소의 id값이 똑같이 찍힌다.

# AAA list안에 튜플을 넣으면 안전하지 않다!!
# - 새로운 객체를 넣는 것이므로 데이터가 소실 될 수 도.
# - 성능상 새로운 객체를 만드는 것도 코스트가 큰 것이다.


# 4) Deepcopy
# - class로 장바구니를 만들 때, copy와 deepcopy의 차이를 알아보자.
# AAA 생성자에서 데이터를 받는데, 
# AAA 그것을 인스턴스변수에 똑같은 값을 넣는 것 vs 데이터 값 활용 새로운 객체 생성 by list()생성자 - 알아서 iterable 언패킹후 list로 통합
class Basket:
    # AAA 이분이 핵심이다. 데이터가 넘어오면, 생성자로 초기화해서 연결된 copy가 안되게 or 원본이 수정안되게 하자.
    # 4-1) 장바구니에 데이터가 없을 때 -> 빈 리스트 / 기존 담긴 데이터가 오면 -> 새로운 객체 받아서 list에 저장
    # - default=None -> if is None -> 빈리스트 / else  = 생성자(기존 데이ㅓㅌ
    # my) if 비었으면?을 처리할 때는 default=None, if is None을 활용한다.
    def __init__(self, products):
        if products is None:
            self._products = []
        else:
            # **list(데이터iterable)을 활용해, 객체를 새로생성한다. 그대로 넣어주면, 연결된 copy가 되어버릴 수 있다.**
            self._products = list(products) # list()생성자는 알아서 언패킹하여 iterable내부값을 활용해준다.
            
    # 4-2) 생성자에서 데이터를 처리했으면, 그 데이터로 어떤 기능을 하는지
    #  장바구니에서 하는 action들을 메소드로 구현한다.

    # 4-2-1) 상품 추가하기
    # - action을 할 때, 필요한 목적어들을 인수로 받는 것도 생각하자.
    def put_prod(self, prod_name):
        self._products.append(prod_name)

    # - list.remove(데이터값)은 차장서 빼준다.
    def del_prod(self, prod_name):
        self._products.remove(prod_name)

# 4-3) copy패키지
# AAA list()등의 생성자로 새로운 객체생성을 못하는 상황일 때 or 코드를 모를 때
import copy

# 첫번재 장바구니는, 기존 장바구니리스트가 있다.
basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
# AAA 객체 자체를 복사하고 싶다.(장바구니1의 리스트를 복사하는 기능)
# - copy와 deepcopy로 복사
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket2)

print('EX5-1 - ',id(basket1), id(basket2), id(basket3))
# AAA 똑같은값의 변수 그대로 할당(basket2 = basket1, 연결된 copy) 와 copy.copy()는 다르다.
# EX5-1 -  62160304 / 2 -  62160624 / 3 -  17249136


# AAA 하지만, 함정은 다른 곳에 있다.
# copy.copy()는 제일 바깥 객체껍데기만... 다른id로 복사하고
# 객체내부의 인스턴스변수 들은 똑같다.
# 62742776 / 62742776 /  62608528
print('EX5-2 - ',id(basket1._products), id(basket2._products), id(basket3._products))
# 이게 바로 얕은복사 shallow copy다

# 하지만, 편리를 위해 객체를 복사했는데 안에 변수들이 같이 움직이면 안된다.


# 4-4) 증명
basket1.put_prod('Orange')
basket2.del_prod('Snack')
print('EX5-3 - ',basket1._products) # baseket2와 같이 움직임.
print('EX5-4 - ',basket2._products) # baseket1과 같이 움직임.
print('EX5-5 - ',basket3._products)

# AAA class의 인스턴스들은.. 불안하면 그냥 copy패키지로 copy.deepcopy를 하자





# 5) 함수 매개변수 전달 사용법

# 5-1) 일반 정수타입은 매개변수로 넘겨도 원본이 변하지 않는다.
def mul(x, y):
    x+=y
    return x # 값을 return하지 않고, 한 변수에 옮겨서 return하는 경우
x,y=10,5 
print('EX6-1 - ', mul(x,y), x, y)

# 5-2) 불변형과 가변형
# - 가변형인 list를 인자로 받고, 함수내에서 수정을 한다면?
a=[10, 100]
b=[5,10]
print('EX6-1 - ', mul(a,b), a, b)
# EX6-1 -  [10, 100, 5, 10] [10, 100, 5, 10] [5, 10]
# AAA 뭐야.. 함수내부에서 연산했는데, 전역변수 list가 바뀌었다.
# - 원본이 변경되었다.
# - 그 뜻은 함수매개변수에 주소(id)를 넘긴다고 생각해야한다.
# -> 일단 가변형데이터(list)는 함수내에서도 데이터가 변경된다.
# -> 엄청 큰 데이터를 새롭게 넘기면 코스트가 크니까.. id를 넘겨서 같은놈으로 처리한다.
# AAA 가변형은 함수내부연산시 원본으로 처리하니 조심해야한다.

# - 튜플의 불변형을 인자로 받고, 함수내에서 수정한다면?
c = (10, 100)
d = (5, 100)
print('EX6-2 - ', mul(c,d), c, d)
# EX6-2 -  (10, 100, 5, 100) (10, 100) (5, 100)
# - 불변형은 원본 c, d를 함수내에서 연산후 할당해줘도.. 안변한다.
# -> 그 뜻은 불변형은 함수내에서 새롭게 복사해서 사용됨. 코스트 큼.
# -> immutalbe은 함수내에서 새로운객체로 복사해서 사용한다.

# AAA 원본이 함수내에서 수정되어도 괜찮으면 list 등의 가변형으로 넘긴다.
# AAA 원본이 보존되어야한다면, tuple로 보내며 코스트가 크다고 생각해야한다.



# 5-2) python 불변형(hash, id고정)으로서, 값으로 할당 or 생성자이용 할당했는데도 변수가 연결된 copy의 원본인 경우
# - tuple, str, bytes, frozenset -> 불변형이라도 복제되지 않고 원본을 반환함
# AAA 어떻게 생성을 하든 t,s,b,f은 같은 값-> 같은 객체를 바라본다.
# - frozenset은 아예 변경이 안되니... 함수내부에서도 원본을 봐라보고 수정해도 안된다.
# - str과 tuple 등은 사본생성을 하지 않는다. 같은 값이면 다 원본이다.

tt1 = (1,2,3,4,5)
tt2 = tuple(tt1) # list(원본)이라면, 새로운 id의 객체가 만들어져야한다.
# - 하지만, only tuple은 값 : id = 1:1 고정이다.
tt3 = tt1[:] # 슬라이싱으로 같은 값을 가져왔다 -> 같은 값이면? -> 같은 id를 바라본다.

print('EX7-1 - ', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 - ', tt1 is tt3, id(tt1), id(tt3))
# EX7-1 -  True 62789264 62789264
# EX7-2 -  True 62789264 62789264

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
print('EX7-3 - ', tt4 is tt5, tt4==tt5, id(tt4), id(tt5))
# EX7-1 -  True True 63154960 63154960
# ㅋㅋ tuple, string, bytes, frozenset은 값 같으면, id도 같다. 같은 곳을 바라봄.
ss1 = 'Apple'
ss2 = 'Apple'
print('EX7-4 - ', ss1 is ss2, id(ss1), id(ss2))
# EX7-4 -  True 62540384 62540384
# string도 '조재성'으로 값이 갔다면 ㅋㅋ 모든 변수가 id가 같다.

# 효율성을 위해서 python이 예외를 만든 것이다.
st1 = '조재성'
st2 = '조재성'
print(id(st1), id(st2))