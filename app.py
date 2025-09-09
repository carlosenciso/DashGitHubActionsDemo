import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "NYC", "NYC"]
})

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("My GitHub Actions Dashboard", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': city, 'value': city} for city in df['City'].unique()],
        value='SF'
    ),
    
    dcc.Graph(id='fruit-plot')
])

@app.callback(
    dash.dependencies.Output('fruit-plot', 'figure'),
    [dash.dependencies.Input('city-dropdown', 'value')]
)
def update_graph(selected_city):
    filtered_df = df[df['City'] == selected_city]
    fig = px.bar(filtered_df, x="Fruit", y="Amount", title=f"Fruit Amounts in {selected_city}")
    return fig

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)