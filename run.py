import analyzer
import pandas as pd
df = pd.read_csv(r'my_dataset.csv',index_col=0)

#Total trades per strategy
print(f'- Total trades per strategy -\n{(analyzer.count_strategies(df)).to_string(header=None)}\n\n')

#Analyze win rate
print('- Analyze win rate - \n')
for dic in (analyzer.analyze_win_rate(df)):
    print(f'Strategy: {dic['Strategy']} | Stop Loss: {dic['SL count']} | Take Profit: {dic['TP count']} | Win Rate: {dic['Win Rate']} |\n')
