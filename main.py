import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df=pd.read_csv("studentLevel.csv")

mean_of_levels=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
#print(mean_of_levels)

fig=px.scatter(mean_of_levels,x="student_id",y="level",size="attempt",color="attempt")

fig.show()