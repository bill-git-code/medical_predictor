import pickle

def load_model(model_path):
    """載入模型檔案"""
    with open(model_path, 'rb') as f:
        return pickle.load(f)
