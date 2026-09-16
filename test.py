import analyzer
import pandas as pd
df = pd.read_csv(r'my_dataset.csv',index_col=0)
print(f'Number of each strategy:\n{(analyzer.count_strategies(df)).to_string(header=None)}\n')
analyzer.analyze_win_rate(df)