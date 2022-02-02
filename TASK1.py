import pandas as pd
import math

activity_data=pd.read_csv(r"activity_data.csv")
movie_data=pd.read_csv(r"data.csv")
df=activity_data
d={}

for i in range(0,len(df.index)):
    value=df.loc[i]
    id=value['id'].split("_")[0].split(":")[1].strip()[1:]
    rating=eval(value['rating'])['M']['value']
    rating=[v if k!='NULL' else math.nan for k,v in rating.items()][0]
    watchlist=eval(value['watchlist'])['M']['value']
    watchlist=[v if k!='NULL' else math.nan for k,v in watchlist.items()][0]
    d[id]={
        'rating':rating,
        'hide':math.nan,
        'watchlist':watchlist,
        'watched':math.nan,   
    }

_source=movie_data['_source'].tolist()
lst=[]

for i in range(0,len(_source)):
    val=eval(_source[i])
    if val['id'] in list(d.keys()):
        val.update(d[val['id']])
    else:
        val['rating']=math.nan
        val['hide']=math.nan
        val['watchlist']=math.nan
        val['watched']=math.nan
    lst.append(val)

df2= pd.Series((i for i in lst),name="_source")
df2.to_csv("final_output.csv",index=False)

print("Completed The Execution")





