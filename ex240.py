#!/usr/bin/env python
# coding: utf-8

# In[80]:


# 주어진 코드
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
# 1. 이 함수는 앞의 함수를 리턴시키기 때문에 함수2부터 함수0까지 역순으로 계산됨
# 2. 함수2에서 매개변수 num을 입력하고 num에 10을 더한 새로운 num값을 함수1로 리턴함
# 3. 함수1의 num은 num+10이 되고 다시 num+10에 2를 더한 새로운 num값을 함수0으로 리턴함
# 4. 함수0의 num은 num+10+2 = num+12가 되고 다시 num+12에 2를 곱한 새로운 num값이됨
# 5. 최종적으로 함수0의 num값은 (num+12)*2가 되고(여기서 (num+12)*2의 num은 함수2의 num), 함수2의 num에 2를 넣어 출력함
# 6. 따라서 (2+12)*2가 출력되어 28이 나옴

