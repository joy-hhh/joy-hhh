# 데이터를 시각화하지 않고 수치만 확인할 때 발생할 수 있는 함정을 보여주기 위해 만든 그래프 앤스콤 4분할 그래프
# 앤스콤 4분할 그래프를 구성하는 데이터 집합은 4개의 그룹으로 구성되어 있으며 모든 데이터 그룹은 x, y 열을 가지고 있다. 그런데 이 4개의 그룹은 각각 평균, 분산, 상관관계, 회귀선이 같다는 특징이 있다.
# 시각화 하면 서로 다른 데이터 패턴을 가지고 있다는 것을 금방 알 수 있다.

# seaborn 라이브러이에서 앤스콤 데이터 집합 가져오기
import pandas as pd
import seaborn as sns
anscombe = sns.load_dataset("anscombe")
# print(anscombe)
# print(type(anscombe))
# print(anscombe.shape)

import matplotlib.pyplot as plt

dataset_1 = anscombe[anscombe['dataset'] =='I']
# plt.plot(dataset_1['x'], dataset_1['y'], 'o')
# plt.show()

dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()   # 기본틀 격자 구성
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

axes1.set_title('dataset_1')
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')

fig.suptitle("Anscombe Data")  # 기본틀에 제목 추가
fig.tight_layout()   # 겹치는 이름과 숫자 조절

plt.show()



