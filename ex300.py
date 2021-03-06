#!/usr/bin/env python
# coding: utf-8

# In[32]:


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(None)
    else:
        print("예외가 발생하지 않음")
    finally:
        print("끝")
        
# 1. try를 통해 실행코드 float(i)를 작성해줬고, 이때 float는 per값에 실수가 존재하기 때문에 실수 그대로 출력하기 위해서 사용
# 2. except를 통해 per값에 예외가 발생하였을 때 None을 실행
# 3. else를 통해 per값에 예외가 발생하지 않으면 per값을 출력한 다음 "예외가 발생하지 않음"이란 문구를 출력
# 4. finally를 통해 per값에 대한 출력이 한 번 반복될 때마다 마지막에 "끝"이라는 문구를 출력
# 5. per = ["10.31", "", "8.00"]에서 첫번째와 세번째 값은 예외가 없기 때문에 출력값이 나온 다음 차례대로 "예외가 발생하지 않음"과 "끝"이 출력됨
# 6. 두번째 값은 빈 칸으로, 예외가 발생하였기 때문에 None이 출력된 다음 else에 대한 출력값이 나오지 않고 바로 "끝"이 출력됨
# 따라서 10.31 예외가 발생하지 않음 끝 None 끝 8.0 예외가 발생하지 않음 끝이 차례대로 세로로 출력

