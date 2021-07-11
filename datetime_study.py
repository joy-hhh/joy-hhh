from datetime import datetime

now1 = datetime.now()
print(now1)

now2 = datetime.today()
print(now2)

t1 = datetime.now()
t2 = datetime(1970, 1, 1)
t3 = datetime(1970, 12, 12, 13, 24, 34)

print(t1)
print(t2)
print(t3)

print()
print()
print()

# 시간 형식 지정자
# %a 요일 출력 - Sun, Mon ...
# %A 요일 출력 긴 이름 Sunday ...
# %w 요일 출력(숫자, 0부터 일요일)
# %d 날짜 출력(2자리로 표시)
# %b 월 출력 - Jan, Feb ...
# %B 월 출력 긴 이름 January ...
# %m 월 출력(숫자) 01,02,03...
# %y 년 출력(2자리로 표시)
# %Y 년 출력(4자리로 표시)
# %H 시간 출력(24시간)
# %I 시간 출력(12시간)
# %p AM 또는 PM 출력 AM, PM

import pandas as pd
test_df1 = pd.DataFrame({'order_day':['01/01/15', '02/01/15', '03/01/15']})

test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
test_df1['date_dt2'] = pd.to_datetime(test_df1['order_day'], format='%m/%d/%y')
test_df1['date_dt3'] = pd.to_datetime(test_df1['order_day'], format='%y/%m/%d')

print(test_df1)

