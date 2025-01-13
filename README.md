# Medical Predictor - Stroke Risk Detection

## 專案簡介
Medical Predictor 是一個基於機器學習的醫療風險預測系統，利用 Random Forest 模型預測使用者是否有中風風險。此專案結合了後端 API（FastAPI）和桌面應用程式（PyQt5），展示了完整的 AI 應用開發流程。

## 功能特色
疾病風險預測：
輸入年齡、血糖濃度、BMI 等數據，系統返回是否有中風風險。
桌面應用程式：
直觀的 GUI 界面，方便使用者操作。
後端整合：
使用 FastAPI 部署模型服務，支持 RESTful API。
機器學習模型：
使用 Random Forest 訓練的高效分類模型。
數據處理與清理：
對原始數據進行特徵處理，並處理缺失值。


## 專案結構
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


## 使用技術
後端：
Python, FastAPI
前端：
PyQt5
機器學習：
Scikit-learn, Random Forest
資料處理：
Pandas, NumPy

## 安裝與使用說明
1.git clone https://github.com/your-username/medical-predictor.git
cd medical-predictor
2. 安裝依賴套件
pip install -r requirements.txt
