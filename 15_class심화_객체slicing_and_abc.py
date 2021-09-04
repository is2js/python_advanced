# 파이썬 클래스 관련 메소드 심화2
# 1) 객체 slicing

class Objects:
    def __init__(self):
        # 외부에서 접근( 슬라이싱 )하려면, 언더바 2개하면 안된다.
        self._numbers = [ n for n in range(1, 10000, 3) ]

    # 1-1) 보이진 않지만, 부모에 있떤 것을 overring 한 것.
    # - len(객체)를 하면, 내부의 1~9997의 list를 len() 해서 반환하도록 수정함.
    def __len__(self):
        return len(self._numbers)

    # 1-2) __getitem__(self, idx) 매직메소드를 오버라이딩하면, 슬라이싱이 가능해진다.
    def __getitem__(self, idx):
        return self._numbers[idx]
        

s = Objects()
# print('EX1-1 - ', s.__dict__)
# -  __len__을 class에서 오버라이딩 하면, 객체도 내부 원하는 변수에 len()을 매길 수 있다.
print('EX1-2 - ', len(s)) 
print('EX1-3 - ', len(s._numbers)) 
# ** __getitem__(self, idx) 오버라이딩하면 -> idx로 하나씩뽑아낼 수 있으니 slicing도 가능!!**
print('EX1-4 - ', s[:100]) 
print('EX1-5 - ', s[-1]) 
print('EX1-6 - ', s[::10]) 

# AAA 사용자입장에서는 객체를 list처럼 활용한다.
# - list가 제공하는 len, slicing을 오버라이딩으로 구현해놔서.



# 2) 추상클래스 설명
# 공식 문서 https://docs.python.org/3/library/collections.abc.html
# Abstract Base Classes for Containers

# - 개발과 관련된 공통된 내용(필드-변수, 메서드)을 
# -- 추출 및 통합해서 공통된 내용으로 작성한 것.
# -- 규격화.
# ex> 자동차 class -> 수백 종류의 차 class 상속시
# - 추상클래스인 자동차class에서 잡아둔 메소드 변수 naming을 사용해함.

# - 언어에 따라 다르지만, python에서는 자체적으로 자신의 객체는 생성불가다.
# AAA 상속 -> 자식classs에서 인스턴스를 생성해야함!!
# ex> 동물 - 먹고/자고/활동하다의 method 정의 -> 자식들은 반드시 구현해야한다. 

# ex2> 간부들이, 추상클래스만 작성해서 내리면 -> 
# - 각 개발자들은 자식class에 상속받아 규격에 맞춰서 구현 + 개발자마다 추가 method 개발한다.

# ex3> 폰 class라는 추상클래스를 만드고 -> method들을 규격해서 정의함
# - 걸다, 끊다, 배터리충전(반드시 해야하는 것)
# -- 자식 갤럭시class, iphone class  부모method(반드시 구현) + 자기만의 독특한 method

# 오버라이딩은 보이지않는 부모 + 강제없이 우리가 필요해서 덮어씀.
# but 추상클래스는 강제성이 생기며, 반드시 자식들은 구현해야함.




