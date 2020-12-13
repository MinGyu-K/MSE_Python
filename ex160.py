#!/usr/bin/env python
# coding: utf-8

# In[56]:


list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# 1. for문을 사용하여 list를 돌림
# 2. split으로 list의 문자를 '.'을 기준으로 쪼개고 a라는 변수에 넣음
# 3. 쪼개진 리스트 중 a[1]번째에 확장자에 대한 내용이 담겨 있기 때문에 a[1]에 대한 조건문을 작성
# 4. 확장자가 h나 c일때 출력하도록 작성
# 5. 따라서 'run.py'이외의 3개의 값이 차례대로 출력됨
for i in list:
    a = i.split('.')
    if (a[1] == 'h') or (a[1] == 'c'):
        print(i)

