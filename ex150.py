#!/usr/bin/env python
# coding: utf-8

# In[135]:


list = ["가", "나", "다", "라"]
# list[::-1]을 하게 되면 list 값을 거꾸로 읽고, 읽은 값을 result라는 변수에 넣음
result = list[::-1]
# for문을 사용하여 result의 값을 반복함
for i in result:
    print(i)

