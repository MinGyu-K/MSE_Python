#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 주어진 코드
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
# 1. message1과 message2의 함수 안에서는 호출된 함수가 없기 때문에 바로 출력되지 않음
# 2. message3의 함수에서 for문을 이용하여 출력값을 3번 돌도록 함
# 3. for문 안에서 message2의 함수가 호출되었고 바로 뒤에 C를 출력하도록 했기 때문에 message2 함수의 출력값 B와 message3 함수의 출력값 C가 3번 반복됨
# 4. 여기서 message3 함수는 정의된 이후에 호출되었기 때문에 출력이 가능함
# 5. 마지막으로 message1 함수가 호출되었고, 이때는 for문 밖에 있기 때문에 마지막에 한 번 출력됨
# 6. 따라서 B C B C B C A가 한글자씩 세로로 출력됨

