#!/usr/bin/env python
# coding: utf-8

# In[76]:


# 1. print_max 함수에 매개변수 a, b, c 입력
# 2. if 조건문을 이용하여 a, b, c중 가장 큰 수에 대한 비교 문장을 출력하게 하고 그 수를 리턴시킴
# 3. print_max 함수를 a, b, c에 각각 숫자를 입력하여 호출하면 결과값이 출력됨
def print_max(a, b, c):
    if (a > b) and (a > c):
        print("%d는 %d와 %d보다 크다"%(a,b,c))
        return a
    if (b > a) and (b > c):
        print("%d는 %d와 %d보다 크다"%(b,a,c))
        return b
    if (c > a) and (c > b):
        print("%d는 %d와 %d보다 크다"%(c,a,b))
        return c
    
print_max(5, 4, 1)

