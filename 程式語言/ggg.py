import pandas as pd

# 讀取 CSV 文件
file_path = 'courses(1).csv'  # 替換為你的文件路徑
courses_df = pd.read_csv(file_path, encoding='utf-8')

# 檢查 DataFrame 結構
print(courses_df.head())

# 將 DataFrame 轉換為 CSV 格式的字符串
csv_content = courses_df.to_csv(index=False, header=True)
print(csv_content)
