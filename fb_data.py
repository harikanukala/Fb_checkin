import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from ggplot import *

df=pd.read_csv("train.csv",sep=",")
df=df[(df['x']>1)]
df=df[df['x']<1.25]
df=df[df['y']>2.5]
df=df[df['y']<2.75]



df['hour']=(df['time']/60) % 24
df['weekday']=(df['time']/(60*24))%7
df['month']=(df['time']/(60*24*30))%12
df['year']=df['time']/(60*24*365)
df['day']=df['time']/(60*24) % 365

df.to_csv("new_train.csv",sep=',')

#small_train = df[df['time'] < 7.3e5]
#small_val = df[df['time'] >= 7.3e5] 
# 
#g1=ggplot(small_train, aes(x='x', y='y', color='place_id')) +\
#    geom_point(aes(color='place_id')) +\
#    scale_color_brewer(type='diverging', palette=4) +\
#    xlab("x") + ylab("y")
#
#g1.draw()
#
##trace = go.Scatter(
##x = df['x'],
##y = df['y'],
##z = df['hour'],
##mode = 'markers'
##)
##
##data = [trace]
##plot_url = py.plot(data,filename='basic-scatter')
#
#group_data = df.groupby('place_id').size()
#print type(group_data)
