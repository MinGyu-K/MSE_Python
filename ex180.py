#!/usr/bin/env python
# coding: utf-8

# In[111]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
# volatility 라는 리스트를 선언
volatility = []
# 1. append 멤버함수를 활용해서 비어있는 volatility 리스트 안에 5일간의 변동폭 값을 넣음
# 2. 여기서 for문을 활용하여 i를 5번 돌도록 설정하였기 때문에 고가와 저가의 차가 리스트 순서대로 나옴
# 3. 따라서 5일간의 변동폭이 리스트 형태로 출력됨
for i in range(0,5):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)

