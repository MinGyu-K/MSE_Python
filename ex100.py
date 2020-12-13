#!/usr/bin/env python
# coding: utf-8

# In[25]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# dict를 사용하여 두 리스트를 딕셔너리로 바꿔주고 그 중 키와 벨류를 zip을 이용하여 지정한다
close_table = dict(zip(date, close_price))
print(close_table)

