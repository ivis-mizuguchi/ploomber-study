# 面積のヒストグラムを作成する
import seaborn as sns
%matplotlib inline
sns.histplot(df["面積（㎡）"] , bins=10)

# + tags=["parameters"]
upstream = ['get']
product = None
# -
