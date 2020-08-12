# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests

req = requests.get('http://localhost:8000/api/trades');
trades = pd.json_normalize(req.json()['trades'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame(trades)
df['epc_cum'] = df.loc[::-1, 'epc'].cumsum()[::-1]
equity = px.line(df, x="entry_date", y="epc_cum")

wins = df[df['epc']>0]['direction'].value_counts()
losses = df[df['epc']<0]['direction'].value_counts()

directions = go.Figure(data=[
    go.Bar(name='loss', x=["long", "short"], y=losses),
    go.Bar(name='win', x=["long", "short"], y=wins)
])
directions.update_layout(barmode='stack')

app.layout = html.Div(children=[
    html.H1(children='Trading Stats'),

    dcc.Graph(
    		id='equity',
    		figure=equity
    ),

    dcc.Graph(
    	id='direction',
    	figure=directions
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)