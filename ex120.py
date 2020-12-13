#!/usr/bin/env python
# coding: utf-8

# In[11]:


fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
# type 라는 변수를 설정하고 그 안에 "좋아하는과일은?"이라는 문장에 대한 입력창이 나오게 함
type = input("좋아하는과일은?")
# 1. 조건문에 in을 이용하여 type이라는 입력값에 fruit의 value값에 포함되 있는지를 물음
# 2. 만약 포함되면 "정답입니다.", 포함되지 않으면 "오답입니다."를 출력하도록 설정
# 3. 한라봉을 입력하였고, 이것은 fruit의 value값에 포함되어 있지 않기 때문에 "오답입니다."가 출력됨
if type in fruit.values() :
    print("정답입니다.")
else:
    print("오답입니다.")

