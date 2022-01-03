import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.express as px

df = pd.read_csv(r"D:\Coding\python codes\bell-curve-normal-distribution\brands.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], [
                         "Mobile Brand"], show_hist=False)


fig.show()
