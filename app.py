# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_sales.csv')
df = df.sort_values(by="date")

app = Dash()

#defining the app layout
app.layout = html.Div([
    
    html.H1(children='Pink Morsel Sales ( 2018-2020 )'),
    
    html.Div([
        dcc.Graph(
            id='starter-graph',
            
        ),
        dcc.RadioItems(
            ['east', 'west', 'north', 'south', 'all'],
            id='xaxis-type', inline=True
        )
    ], style={'width': '100%', 'display': 'inline-block'})
])



@callback(
    Output('starter-graph', 'figure'),
    Input('xaxis-type', 'value'))


def update_figure(selected_region):
    
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
        
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        labels={
            "date": "Date",
            "sales": "Sales ($)",
            "region": "Region"
        },
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run(debug=True)