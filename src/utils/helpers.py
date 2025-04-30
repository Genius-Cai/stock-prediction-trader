import os
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def save_results(results, file_path):
    """
    保存预测结果到文件
    
    参数:
    results: 预测结果
    file_path: 保存路径
    """
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 保存为JSON格式
    with open(file_path, 'w') as f:
        json.dump(results, f, indent=4)

def log_activity(activity, log_file='logs/activity.log'):
    """
    记录应用活动信息
    
    参数:
    activity: 活动描述
    log_file: 日志文件路径
    """
    # 确保日志目录存在
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # 添加时间戳并记录活动
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f'{timestamp} - {activity}\n')

def visualize_predictions(actual, predicted, title='Stock Price Prediction', save_path=None):
    """
    可视化预测结果与实际价格
    
    参数:
    actual: 实际价格
    predicted: 预测价格
    title: 图表标题
    save_path: 图表保存路径(可选)
    """
    plt.figure(figsize=(12, 6))
    plt.plot(actual, label='Actual Prices')
    plt.plot(predicted, label='Predicted Prices')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    
    # 保存图表
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    
    plt.show()

def calculate_statistics(df):
    """
    计算数据的统计信息
    
    参数:
    df: pandas DataFrame
    
    返回:
    统计信息的字典
    """
    stats = {
        'mean': df.mean().to_dict(),
        'std': df.std().to_dict(),
        'min': df.min().to_dict(),
        'max': df.max().to_dict(),
        'median': df.median().to_dict()
    }
    return stats