#!/usr/bin/env python
# coding: utf-8

# In[30]:


# 주어진 코드
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
# super().__init__() 라는 수식으로 class 자식(부모) 안의 함수에 대해 먼저 출력되도록 하고 나중에 class 부모 안의 함수가 출력됨
# 아는 대로 적어보았습니다

