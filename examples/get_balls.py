import pandas as pd

def ab_to_num(s):
    res = 0
    for c in s:
        n = ord(c) - ord('A') + 1
        res = res * 26 + n
    res -= 1
    return res


def getT(group, s):
    gr = {
        #'ПС': '10esCNHA3RDsWZVqORhgjG202woGanvZcMphIWNISwac',
        #'СППО': '1knJ8varCvxIMvcY6pyZDDaadbru_7-Im_-BE-QvzhZM',
        #'ПОАФ': '1XU5jvJIUQFLYeNER0iOpkqAw5kvPvcxYnhvgom4FM2g',
        #'ПОНОИ': '1bs_OizpEH4Gi95J_jdGYz5OdMNN0VrQQye1sEku4yXQ',
        #'МКН(б)-91':'1F9sR_gnvXFeGdPSqnZNqt_7TxQT4CIpYaOlAmKPfJQQ',
        #'МКН(б)-81':'1rymIqWX5_5MGCiNbjQXUxS-m9drLR9jz37AvHjvRgsc'
        #'МКН(б)-81':'1woy3XVL3blNckUL21ie0B_VuFNgDF5p-OFKtc-1cT7g'
        #'МКН(б)-81':'1rymIqWX5_5MGCiNbjQXUxS-m9drLR9jz37AvHjvRgsc'
        'ПОИФ(б)-91':'13qJs_ECI94vYySc5yd_KL4QUEAObsvlrPuc8rGx6JHo',
        'ПОМИ(б)-91':'16pM390Gu1eezMJ76IWjHPSbNka8GzUUgvXrx0TdSMmM',
        'ПОРМ(б)-12':'11PRiMaRNg4JcXMCsrHaTen-lqX9Lj4480g0iqk2f3qo',
        'ПОМИ(б)-81':'1BHupU3jGA5wz0KMTp8VQs1v5eZib5CTjDf2g3L1mx-c',
        'ПОАК(б)-11':'17mb2jLYv2IWs431PfiyYqZw0u6qfJj3xDZBLNamJ2mY'
    }

    prefix = 'https://docs.google.com/spreadsheets/d/'
    suffix = '/gviz/tq?tqx=out:csv'

    url = prefix + gr[group] + suffix
    cols = [0, ab_to_num(s)]
    data = pd.read_csv(url, skiprows=[0], usecols=cols)
    data = data[data[data.columns[0]].isnull()==False]
    #data = data.dropna()
    return data[data.columns[1]].astype('str')

#a = getT('МКН(б)-81','J')
#print(a)