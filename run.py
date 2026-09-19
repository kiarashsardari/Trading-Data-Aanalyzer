import analyzer
import pandas as pd


log_file = open('your_analyzed_data.txt', 'w', encoding='utf-8')


def out(text):
    log_file.write(text + '\n')
    print(text)


try:
    df = pd.read_csv(r'my_dataset.csv', index_col=0)

    #Total trades per strategy
    cs = (analyzer.count_strategies(df)).to_string(header=None)
    out(f'--- Total trades per strategy ---\n{cs}\n\n')

    #Analyze win rate
    input('press enter to show << Win rates >>...')
    out('--- Win rates --- \n')
    for dic in (analyzer.analyze_win_rate(df)):
        wr = dic['Win Rate']
        tpc = dic['TP count']
        slc = dic['SL count']
        s = dic['Strategy']
        out(f"Strategy: {s} | Stop Loss: {slc} | Take Profit: {tpc} | Win Rate: {wr} % |\n\n")

    #Analyze exit rate
    input('press enter to show << Exit rates >>...')
    out('--- Exit rates --- \n')
    grp = analyzer.tp_exit_rate(df)
    out('position : (count × andis) ÷ number of trades = exit rate % \n')
    for pos, rate in grp.items():
        out(f'{pos} : {rate:.1f} %\n')

    # Analyze best tps
    input('press enter to show << Best TPs >>...')
    out('--- Best TPs --- \n')
    lst = analyzer.best_tp(df)
    for i in lst:
        out(i + '\n')

except Exception as e:
    out(f'!!! ERROR: {e}')
finally:
    log_file.close()
    input('press enter to Exit...')
