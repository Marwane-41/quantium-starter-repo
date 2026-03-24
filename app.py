# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_sales.csv')

app = Dash()

fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    labels={
        "date": "Date",
        "sales": "Sales ($)",
        "region": "Region"
    },
    title="Pink Morsel Sales Over Time"
)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales ( 2018-2020 )'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)