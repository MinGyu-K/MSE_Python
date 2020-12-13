#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 주어진 코드
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 1. 첫번째 조건문에서 if True라고 나와있기 때문에 True의 값이 출력될 것이고 else의 "4"는 출력이 안될 것이다
# 2. if True 안의 또다른 조건문에 if False와 else가 나와있는데, True의 값이 나와야 하기 때문에 else의 "3"이 출력될 것이다
# 3. 마지막의 "5"는 조건문 밖에 있기 때문에 당연히 출력될 것이다
# 4. 따라서 "3"과 "5"가 출력된다

