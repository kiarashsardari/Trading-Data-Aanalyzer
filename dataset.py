import pandas as pd
df = (pd.read_excel(r'D:\Python\data.xlsx'))
df.to_csv('my_dataset.csv', index=False, encoding='utf-8-sig')