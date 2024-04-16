import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from pydantic import BaseModel


class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 클래스 만들기
class IrisMachineLearning:
    def __init__(self):
        self.iris_df = pd.read_csv('iris.csv')
        self.rfc_name = 'iris_rfc.pkl'
        try:
            self.model_rfc = joblib.load(self.rfc_name)
        except (Exception, ) as _:
            self.model_rfc = self.rfc_train()
            joblib.dump(self.model_rfc, self.rfc_name)
        return

    def rfc_train(self):
        X = self.iris_df.drop('species', axis=1)
        y = self.iris_df['species']
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model

    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        x_new = np.array([[sepal_length, sepal_width,
                           petal_length, petal_width]])
        prediction = self.model_rfc.predict(x_new)
        # .max()가 없으면 오류가 생김
        probability = self.model_rfc.predict_proba(x_new)

        print(f'prediction = {prediction}')
        print(f'probability = {probability}')

        # prediction[0]를 주지 않으면 에러가 생김, probability 뒤에 .max()를 붙여도 됨
        # .tolist로 json 포맷을 맞추어서 모든 예측값이 전송 될 수 있도록 변경
        return prediction[0], probability.tolist()