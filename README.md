# **Medical Predictor - Stroke Risk Detection**
使用的數據集來自 Kaggle： Stroke Prediction Dataset (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?resource=download)
## **專案簡介**
Medical Predictor 是一個基於機器學習的醫療風險預測系統，利用 **Random Forest** 模型預測使用者是否有中風風險。此專案結合了後端 API（FastAPI）和桌面應用程式（PyQt5），展示了完整的 AI 應用開發流程。

---

## **功能特色**
- **疾病風險預測**：
  - 輸入年齡、血糖濃度、BMI 等數據，系統返回是否有中風風險。
![Figure_1](https://github.com/user-attachments/assets/7e2cb4ed-93fc-447f-b3b2-f274cd46d8fc)

- **桌面應用程式**：
  - 直觀的 GUI 界面，方便使用者操作。
![image](https://github.com/user-attachments/assets/06a17fca-3f48-4e2e-ba94-b97b12acbb01)

- **後端整合**：
  - 使用 FastAPI 部署模型服務，支持 RESTful API。
- **機器學習模型**：
  - 使用 Random Forest 訓練的高效分類模型。
- **數據處理與清理**：
  - 對原始數據進行特徵處理，並處理缺失值。

---

## **專案結構**

```bash
medical_predictor/
│
├── data/                     # 資料集
│   └── healthcare-dataset-stroke-data.csv
│
├── models/                   # 訓練好的模型
│   └── random_forest_model.pkl
│
├── backend/                  # 後端服務
│   ├── main.py               # FastAPI 主程式
│   ├── database.py           # 資料庫設定（未實作）
│   └── schemas.py            # 資料結構定義
│
├── desktop_app/              # 桌面應用程式
│   ├── main_ui.py            # PyQt5 主程式
│   └── utils.py              # 工具函式
│
├── train_model.py            # 模型訓練程式
├── requirements.txt          # 依賴套件清單
└── README.md                 # 專案說明文件
