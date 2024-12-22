import os
import pandas as pd
from test import combined_keyword_extraction

# 动态文件路径
input_file = r"D:\python\代码\weibo-search-master\weibo-search-master\结果文件\美国大选\美国大选.csv"
output_file = r"D:\python\代码\weibo-search-master\weibo-search-master\结果文件\美国大选\美国大选_with_keywords.csv"

# 读取 CSV 文件
def load_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件未找到: {file_path}")
    
    df = pd.read_csv(file_path, encoding='utf-8-sig')
    if '微博正文' not in df.columns:
        raise ValueError("CSV 文件中需要包含 '微博正文' 列。")
    
    return df, df['微博正文'].tolist()

# 保存关键词到 CSV
def save_keywords_to_csv(file_path, df, keywords):
    # 添加关键词列
    df['关键词'] = ['; '.join(kw) for kw in keywords]
    # 保存新文件
    df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print(f"关键词已保存到 {file_path} 文件中。")

# 主程序入口
if __name__ == "__main__":
    print("开始处理关键词提取...")

    # 读取数据
    df, texts = load_csv(input_file)
    
    # 提取关键词
    keywords = combined_keyword_extraction(texts)
    
    # 保存结果
    save_keywords_to_csv(output_file, df, keywords)
    
    print("关键词提取完成！")
