import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# # 데이터 가져오기
# iris_df = pd.read_csv('iris.csv')
#
# y = iris_df['species']
# X = iris_df.drop('species', axis = 1)
#
# # 데이터 집어넣어서 모델 만들기 (학습)
# kn = KNeighborsClassifier()
# model_kn = kn.fit(X, y)
#
# joblib.dump(model_kn, 'model_kn.pkl')

# 미리 학습된 모델 저장하기
model_kn = joblib.load('model_kn.pkl')

# 예측
X_new = np.array([[2, 1, 2, 1]])
prediction = model_kn.predict(X_new)
print(f'KN prediction = {prediction}')
probability = model_kn.predict_proba(X_new)
print(f'KN prob={probability}')


# # 모델 하나 더 만들기
# rfc = RandomForestClassifier()
# model_rfc = rfc.fit(X, y)
#
# # 예측
# prediction = model_rfc.predict(X_new)
# print(f'RFC prediction = {prediction}')
# probability = model_rfc.predict_proba(X_new)
# print(f'RFC prob={probability}')