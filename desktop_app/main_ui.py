import sys
import pickle
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox

class MedicalPredictorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("醫療預測系統")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        # 主要佈局
        layout = QVBoxLayout()

        # 輸入框與標籤
        self.inputs = {}
        features = ['年齡 (age)', '平均血糖濃度 (avg_glucose_level)', '身體質量指數 (BMI)']
        for feature in features:
            layout.addWidget(QLabel(feature))
            input_box = QLineEdit(self)
            input_box.setPlaceholderText(f"請輸入 {feature}")
            self.inputs[feature] = input_box
            layout.addWidget(input_box)

        # 預測按鈕
        self.predict_button = QPushButton("進行預測", self)
        self.predict_button.clicked.connect(self.predict)
        layout.addWidget(self.predict_button)

        # 預測結果
        self.result_label = QLabel("預測結果將顯示在這裡", self)
        layout.addWidget(self.result_label)

        # 設置主視窗佈局
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def predict(self):
        try:
            # 收集輸入數據
            input_data = []
            for feature, input_box in self.inputs.items():
                value = float(input_box.text())  # 驗證輸入是否為浮點數
                input_data.append(value)

            # 載入模型
            with open('../models/random_forest_model.pkl', 'rb') as f:
                model = pickle.load(f)

            # 預測
            input_data = np.array([input_data])  # 轉換為 2D 數組
            prediction = model.predict(input_data)

            # 顯示結果
            result = "有中風風險" if prediction[0] == 1 else "無中風風險"
            self.result_label.setText(f"預測結果: {result}")

        except ValueError:
            QMessageBox.warning(self, "輸入錯誤", "請確保所有輸入為有效的數字！")
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"發生未知錯誤: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MedicalPredictorApp()
    mainApp.show()
    sys.exit(app.exec_())
    
    
    
