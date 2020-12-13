#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# a = 시가, b = 변동폭(최고가 - 최저가), c = 최고가로 지정
# float는 각각의 value 값이 실수라는 것을 알려줌
a = float(btc['opening_price'])
b = float(btc['max_price']) - float(btc['min_price'])
c = float(btc['max_price'])
# 1. 조건문을 활용하여 시가와 변동폭의 합이 최고가보다 높으면 "상승장", 그렇지 않으면 "하락장"을 출력하도록 설정
# 2. 시가와 변동폭의 합이 최고가보다 높아서 "상승장"이 출력됨
if (a + b) > c:
    print("상승장")
else:
    print("하락장")

