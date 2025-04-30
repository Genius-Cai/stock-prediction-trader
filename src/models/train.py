import joblib
from sklearn.model_selection import train_test_split
from .model import StockModel

def train_model(preprocessed_data, model_save_path='models/stock_model.pkl'):
    """
    训练股票预测模型并保存
    
    参数:
    preprocessed_data: 预处理后的数据
    model_save_path: 模型保存路径
    """
    # 准备特征和目标变量
    features = ['open', 'high', 'low', 'volume', 'year', 'month', 'day']
    X = preprocessed_data[features]
    y = preprocessed_data['close']
    
    # 分割训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 初始化股票模型
    model = StockModel()
    
    # 构建模型
    model.build_model()
    
    # 训练模型
    model.train(X_train, y_train)
    
    # 评估模型
    metrics = model.evaluate_model(X_test, y_test)
    print(f"模型评估结果: MSE={metrics['mse']:.4f}, RMSE={metrics['rmse']:.4f}")
    
    # 保存训练好的模型
    joblib.dump(model, model_save_path)
    print(f"模型已保存到: {model_save_path}")
    
    return model