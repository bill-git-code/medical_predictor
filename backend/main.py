from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# 載入模型
with open('models/random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 定義輸入數據格式
class PatientData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    # 根據資料集定義特徵

@app.post("/predict")
def predict(patient: PatientData):
    # 將輸入轉換為 DataFrame
    input_data = pd.DataFrame([patient.dict()])
    # 預測
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}
