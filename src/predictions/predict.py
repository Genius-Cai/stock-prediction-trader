import joblib
import pandas as pd

def make_prediction(new_data, model_path='models/stock_model.pkl'):
    """
    使用训练好的模型对新数据进行预测
    
    参数:
    new_data: 需要预测的新数据
    model_path: 训练好的模型路径
    
    返回:
    预测结果
    """
    try:
        # 加载训练好的模型
        model = joblib.load(model_path)
        
        # 确保新数据是pandas DataFrame格式
        if not isinstance(new_data, pd.DataFrame):
            if isinstance(new_data, dict):
                new_data = pd.DataFrame([new_data])
            else:
                raise TypeError("新数据必须是pandas DataFrame或字典格式")
        
        # 提取预测所需的特征
        features = ['open', 'high', 'low', 'volume', 'year', 'month', 'day']
        
        # 检查新数据是否包含所有必要特征
        for feature in features:
            if feature not in new_data.columns:
                raise ValueError(f"新数据缺少必要的特征: {feature}")
        
        # 使用模型进行预测
        X_new = new_data[features]
        predictions = model.predict(X_new)
        
        return {
            'predicted_close_price': predictions.tolist(),
            'status': 'success'
        }
        
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }