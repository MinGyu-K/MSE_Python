#!/usr/bin/env python
# coding: utf-8

# In[158]:


apart = [ [101, 102], [201, 202], [301, 302] ]
# 1. for문을 두 번 사용하면 apart의 리스트 값이 하니씩 출력
# 2. j값을 출력할 때 end를 사용하여 각각의 리스트 값에 " 호"가 출력
# 3. \n을 사용하여 " 호" 다음에 리스트 값이 바로 나오지 않고 한 줄 띄어 나오도록 함
for i in apart:
    for j in i:
        print(j, end = " 호 \n")

