from dash import Dash, html, dcc
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px

app = Dash(__name__)
server = app.server

app.layout = [html.H1('Hello, look at this graph')]
df = pd.read_csv("https://raw.githubusercontent.com/RisanNarmi/DeploymentTestMCM7183Ex3/main/gdp_1960_2020.csv")
subMY = df[df["country"].isin(["Malaysia"])]
fig = px.scatter(subMY, x="year", y="gdp")

if __name__ == '__main__':
    app.run(debug=True)
