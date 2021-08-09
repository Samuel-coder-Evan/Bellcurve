import pandas as pd
import plotly.figure_factory as ff
import plotly_express as px

df = pd.read_csv('project.csv')
height = df['Mobile Brand'].tolist()
weight = df['Avg Rating'].tolist()
fig = ff.create_distplot([df['Avg Rating'].tolist()],['result'],show_hist = False)
fig.show()
fig2 = px.bar(df,x = 'Mobile Brand' , y = 'Avg Rating')
fig2.show()
