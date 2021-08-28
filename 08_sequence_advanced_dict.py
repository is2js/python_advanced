# 08 시퀀스 - dictionary 심화
# AAA 중요한 이유 : python엔진의 데이터뼈대를 dict로 구성함.
# AAA 언어를 불문하고 다른 형태(json)로 사용되기 때문에
# AAA 파이썬의 핵심구현부로서 class, instance, 속성, 키워드, doc 전부 dict로 저장됨.
# AAA python은 hash table을 잘 만들어놔서 dict를 고성능으로 사용할 수 있다.
# AAA 예를 들어, 내장함수를 의미하는 __builtins__의 namespace를 .__dict__를 봤었다.
# print(__builtins__.__dict__) # 일반 shell에서 는 나옴
# 우리가 사용한 내장 함수들이 여기 다 있다. ex divmod, abs, id, hex ..
# {'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>
# -> 딕셔너리 형태로 목록을 저장해놓고 있다.

# 1) Dict의 내부 구성 : 해쉬테이블(hash)
# Dict -> key만 중복 허용x
# Set -> 중복 허용 X
# QQQ Dict가 key 중복을 허용하지 않는다? 
# -> 내부적으로 중복을 검사하고 있다는 말이다. -> 내부적으로 hash table을 사용해서 검사한다.
# -> 중복검사원리 : hash table에서 값->숫자로 치환 -> 숫자가 중복되면 중복
# AAA 충돌 가능성이 있지만, 적은 리소스로 많은 데이터를 효율적으로 관리할 수 있다.
# AAA hash -> 색인 -> 빠르게 찾아갈 수 있음.
# ex> 이진탐색트리에서 중요함.
# AAA python에서는 내부적으로 hash table로 구성되어 있으며,
#     dictionary가 class 객체 속성 메서드 등 모든 것을 표현하는데 대표 자료형으로 사용되고 있다.


# 1-1) Dict 일반적인 구조 (key, value)
# print('EX1-1 - ', __builtins__)

# 1-2) hash 값 확인
# - 중복이 되는지 안되는지를 어떻게 하는지 확인
t1 = (10, 20, (30, 40, 50)) # 튜플속 튜플
# AAA -> 튜플로만 구성 -> 불변형 -> hash값이 생성 가능하다
t2 = (10, 20, [30, 40, 50]) # 튜플속 리스트( container - list, tuple, deque)
# AAA -> 튜플 + list로 구성 -> 가변형 -> hash값 생성 불가능(언제든지 변화가능한 것은 hash를 안만든다.)
# AAA 가변형이 끼어있다면, 중복을 체크할 필요x -> hash값 생성할 필요x
print('EX1-2 - ', hash(t1)) # 불변형은 hash값이 출력된다. # 1238611460
# print('EX1-3 - ', hash(t2)) # 가변형은 hash()출력시 에러가 난다.
# TypeError: unhashable type: 'list' # 중복허용하는 list는 딱히 hash가 필요가 없다. 데이터만 차곡차곡 잘 채우면 된다.





# 2) dict comp로 dict만들기
# - cf) list comp는 데이터 generator받아풀기/생성/변형/필터링 다됨. but tuple comp()는 generator임
# - dict comp도 데이터 생성/변형/필터링 가능하다.
# [csv실습] resources > test1.csv [국가명, 국가코드]
import csv 
# 2-1) 외부파일 -> list of tuple로 만들어보자.
#  AAA  1줄씩 내려오는 csv 정보를 list comp를 이용해 데이터를 받아올 수 있다.
#  AAA  reader정보는 tuple(x)로 안만들어주면, list안에 각 line이 list로 내려온다.
# - my) 2중 리스트나 튜플리스트나 둘다 dict comp로 변환된다.
# - my) 짝을 가진 칼럼/데이터가 오면 dict comp로 변형해주자.
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # header 스킵
    next(temp) # reader로 읽으면 next()를 쓸 수 있는 generator라서 쉽게 넘긴다.
    # 변환
    NA_CODES = [x for x in temp ]

print('EX2-1 - ')
# print(NA_CODES)

# 2-2) tuple list -> dict 변형은 여러가지 방법이 있다.
n_code1 = { country: code for country, code in NA_CODES}
n_code2 = { country.upper(): code for country, code in NA_CODES}
# print(n_code1)
# print(n_code2)
# my) 짝을 가진 데이터가 오면  튜플 list comp(2중list or 튜플 list) -> dict comp로 받아서 만들자.


# 3) **Dict setdefault 예제**
# - 이것만 잘 사용해도, 성능 좋은 dict를 만들 수 있다.
# 3-1) 튜플속 튜플을 먼저 만들어보자. 짝을 이루지만, key자리에 중복이 있다.
# - 짝을 이룬 튜플안에 튜플 -> dict comp로 dict로 만들기. but hash가 가능해야하는 key는 중복 불가능.
# AAA key자리가 동일한 데이터의 값을 묶어서 가지고 싶다.
# - pandas문제에서 groupby([]).apply(list)로 줬던 것 같다.
# - key자리별 그룹별로 묶어서 중복없는 dict를 만들기 
# - setdefault 메소드 사용X/사용O 나눠서 해보자.
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
)

# no setdefault
# - 변수 + for문으로 받으면서 처리한다.
# - key가 있으면, append만 해주면된다. list로 모을 예정인가보다.
# -> key별로 모으고 싶다? -> key가 있으면 append, 없으면 list에 초기값 넣어서 할당해주기.
new_dict1 = {}
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v] # 값을 모을 때는 list로 담자.
print('EX3-1 - ', new_dict1)

# AAA 고급 서적이나 공식 문서 등에서
# - key로 사용할 것들(짝 중에 key자리)이 중복되는 구조로 list나 tuple로 있다면
# - key중복방지용으로 분기를 나눠 있으면 append, 없으면 할당
# - value는 중복을 허용해서 상관없다.



# setdefault 메서드를 사용하면
# - 속도 + 성능까지 더 좋다고 한다. recommand됨.
# - 변수 for문 돌면서 처리하는 것은 똑같다.
# - 바로 변형이 아니므로 dict comp로 dict는 못만들다-> for문 돌면서 setdefault로 처리한다.
# - dict.setdefault(있으면사용/없으면생성할 key, 없으면 초기값) -> 초기값 상태에서 할 행동(ex .append())
new_dict2 = {}
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print('EX3-2 - ', new_dict2)



# 4) 사용자 정의 dict
# AAA class로 dict를 재정의해서 사용한다. (어려움)

class UserDict(dict):
    def __missing__(self, key):
        # 없는 key가 들어왔을 때 호출되는 것 같다.
        print('Called : __missing__')
        # key는 str이 들어올 예정인데, 
        # 없는키가 -> [문자열]면 그냥 에러, 다른자료형으로 잘못입력했으면 str(key)로 바꿔서 직접호출 dict[str(key)] 한번더
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__') # 엄밀히는 getitem이 호출 되는 것.
        try:
            return self[key]
        except KeyError:
            # key에러가 났을 때는, default에러메세지를 띄운다.
            return default


    def __contains__(self, key):
        print('Called : __contains__') 
        # 혹시 형변환해서라도, 있던 키인지 해당되면, True를 반환.
        return key in self.keys() or str(key) in self.keys()


# 4-1) 사용
# - AAA일반 딕셔너리도... 인스턴스처럼 keyword방식으로 생성할 수 있다.
# - key는 다 문자열로 자동변경되니, 문자열'' str()하면 에러난다.
# print(dict(one=1, two=2)) # {'one': 1, 'two': 2}
# - AAA 튜플 리스트도 dict로 변경가능하다.
# print(dict([('one',1), ('two',2)])) # {'one': 1, 'two': 2}
# - 사용자 정의 dict도 keyword방식으로 만들어보자.
user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one' : 1, 'two' : 2})
user_dict3 = UserDict([('one',1), ('two',2)])

print('EX4-1 - ', user_dict1, user_dict2, user_dict3)
# - 내부적으로 dict는 class로 구성되며, 값을 꺼낼 때는 .get()메서드가 호출된다.
# - dict.get( key ) -> __get__ 호출
# - key in dict -> __contains__ 호출
# - dict.get( 없는 key )  -> 내부적으로 __missing__ 호출
print('EX4-2 - ',  user_dict2.get('two')) # 있는 키 Called : __getitem__
# print('EX4-2 - ',  user_dict2.get('111')) # 없는 키 Called : __missing__
# AAA .get()으로 꺼내면, 없는 key가 __get__부터 탄 뒤-> default None 반환
print('EX4-3 - ',  'one' in user_dict3) # in검사 Called : __contains__
# print('EX4-4 - ',  user_dict3[111]) 
# AAA 직접호출하면 get으로 None return이 없이 missing타고 에러냄. -> 문자열 아니면 문자열로 바꾼 뒤 KeyError냄.

# AAA 상속후 직접 dictionary class를 만들어서 사용할 수 있다.
# - 사용용 개발자들 = 프레임워크 개발자들은 orm 등 개발해서 사용할 수 있다.
# - 예를 들어, **불필요한 것들을 if문으로 미리 제거해놓고 사용할 수 잇다. **
# - 환자 데이터를 dict에 저장하는데, 불필요한 부분을 못받도록 user_dict를 사용하도록 정의한다.
print('EX4-5 - ', 'three' in  user_dict3 ) 


# 5) Immutable dict
a = dict(name='kim')
a['name']='park' 
print(a)# dict는 기본적으로 mutable으로 재할당 가능하다.
# AAA dict를 한번 선언후 절대 수정안되도록 사용하고 싶다면
# 개별적으로 지원하는 class로 dict를 사용하면 된다.
# Read Only
from types import MappingProxyType

d = {'key1' : 'TEST1'}
d_frozen = MappingProxyType(d)
print('EX5-1 - ', d, id(d))
print('EX5-2 - ', d_frozen, id(d_frozen)) # 생긴 것은 같고, id는 다르다. 재할당은?
print('EX5-3 - ', d is d_frozen, d == d_frozen) # 값도 같다. id는 다르다.

d_frozen['key1'] = 'TEST2' # TypeError: 'mappingproxy' object does not support item assignment
# key, value가 같은 값으로 나오지만, 재할당은 불가능한 immutable dict가 되었다.
# AAA 원본은 잘 숨겨둬야함.







