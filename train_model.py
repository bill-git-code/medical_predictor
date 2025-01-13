import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import pickle
import matplotlib.pyplot as plt
import numpy as np


# 讀取資料 
# Stroke Prediction Dataset  https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
data_path = r'C:\Users\billn\Desktop\personal\114_sideproject\medical_predictor\data'
data = pd.read_csv(data_path+'\\stroke-prediction-dataset.csv')

# 移除不必要的欄位（如 `id`）
data = data.drop(columns=['id'])

# 處理缺失值
data['bmi'] = data['bmi'].fillna(data['bmi'].median())

# Label Encoding 轉換類別型資料
categorical_columns = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])

# 特徵與標籤分離
X = data.drop(columns=['stroke'])
y = data['stroke']

# 分割訓練與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 訓練 Random Forest 模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 模型測試
y_pred = model.predict(X_test)

# 評估模型表現
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


# 儲存模型
with open('models/stroke_rf_model.pkl', 'wb') as f:
    pickle.dump(model, f)


# 繪製特徵重要性
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
features = X.columns

plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), features[indices], rotation=45)
plt.tight_layout()
plt.show()





