# pandasで13105_20211_20211.csvをロードして最初の10行を表示する
import pandas as pd
pd.set_option('display.max_columns', 100)
df = pd.read_csv('13105_20211_20211.csv', encoding='CP932')
df.head(10)

# + tags=["parameters"]
upstream = None
product = None
# -