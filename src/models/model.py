from sklearn.ensemble import RandomForestRegressor
import numpy as np

class StockModel:
    def __init__(self):
        self.model = None

    def build_model(self):
        # 使用RandomForest作为预测模型
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        return self.model

    def train(self, X_train, y_train):
        # 训练模型
        self.model.fit(X_train, y_train)
        
    def predict(self, X_test):
        # 使用模型进行预测
        return self.model.predict(X_test)
        
    def evaluate_model(self, X_test, y_test):
        # 评估模型性能
        predictions = self.model.predict(X_test)
        mse = np.mean((predictions - y_test) ** 2)
        rmse = np.sqrt(mse)
        return {
            'mse': mse,
            'rmse': rmse
        }