#!/usr/bin/env python
# coding: utf-8

# In[171]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# 1. money라는 변수에 0의 초기값 설정, money = 수익
# 2. ohlc 리스트의 2번째 배열부터 반복하는 for문을 만듦
# 3. money에 수익금(종가 - 시가)를 더해주면 수익이 되고 다시 money라는 변수로 지정
# 4. for문을 통해 3일간의 수익을 계산해 주기 때문에 money를 출력하면 총 수익이 나옴, 이때 money는 초기값 0과 다름
money = 0
for i in ohlc[1:]:
    money += (i[3] - i[0])
print(money)

