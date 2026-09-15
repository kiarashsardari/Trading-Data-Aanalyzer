import pandas as pd
df = pd.read_csv(r'D:\Python\my_dataset.csv',index_col=0)

def get_positions(df):
    return(list(df['position']))

def get_strategies(df):
    return(list(df['strategy']))

def get_date(df):
    return(list(df['date']))

# تعداد هر استراتژی
def count_strategies(df):
    try:
        c = df['strategy'].value_counts()
        return c 
    except KeyError:
        return('Error: Strategy column does not exist...')

def analyze_win_rate(df):

    '''for s,groupe in grouped_strategies:
        print(df[df['strategy'].isin([s]) & df['position'].isin(['SL'])])
        print(groupe[groupe['position'] == 'SL'])

    print(len(df['position']))

    c1 = df['strategy']
    c = df['strategy'].value_counts()
    strategies_name = c.index
    strategies_count = c.iloc[:]
    positions = list(j for j in df['position'] if j!='SL')
    #.startswith('TP')
    for p in positions:
        for o in strategies_name:
            print(df[df['strategy'].isin([o]) & df['position'].isin([p])])
    print(df[c1.isin(['s']) & df['position'].isin(['SL'])])'''
    # یک سری از هر استراتژی و تعداد اس ال های اون
    sl_size = (df[df['position'] == 'SL']).groupby('strategy').size().items()
    # یک دیکشنری از هر استراتژی و تعداد تی پی های اون
    tp_size = dict((df[df['position'].str.startswith('TP')]).groupby('strategy').size().items())
    #دیکشنری خالی برای تولید دیکشنری از تعداد اس ال های هر استراتژی
    sl_dic = {}
    # اسم هر استراتژی و تعداد اس ال های اون
    for strtgy,sl_count in sl_size:
    # تعداد تی پی ها . اگه اسم استراتژی توی دیکشنری تی پی ها نبود یعنی اون استراتژی تی پی نداشته و 0 میشه
        tp_count = tp_size[strtgy] if strtgy in tp_size else 0
    # محاسبه درصد برد
        win_precent = (tp_count/(sl_count + tp_count)*100)
    # چاپ مقادیر
        print(f'Strategy: {strtgy} | Stop Loss: {int(sl_count)} | Take Profit: {tp_count} --> Win precent: {win_precent:.3f}%\n')
    # تولید دیکشنری از تعداد اس ال های هر استراتژی
        sl_dic[strtgy] = sl_count
    ''' تعریف دوباره ی سری از تعداد تی پی های هر استراتژی
    چون با تبدیل اون به دیکشنری دیگه خالی میشه و برای همین مجبوریم دوباره تعریفش کنیم'''
    tp_size_items = (df[df['position'].str.startswith('TP')]).groupby('strategy').size().items()
    # اسم هر استراتژی و تعداد تی پی های اون
    for sgy,tp_count in tp_size_items:
    # بررسی کن اگر اسم استراتژی ما توی دیکشنری 
        if sgy not in sl_dic:
            print(f'Strategy: {sgy} | Stop Loss: {0} | Take Profit: {int(tp_count)} --> Win precent: 100% (n={int(tp_count)})\n')