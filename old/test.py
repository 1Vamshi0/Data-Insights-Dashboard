import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

akv16 = pd.read_csv('Laptop Sales dataset.csv')
akv16.drop(['TypeName','ScreenW','ScreenH','Touchscreen','IPSpanel','RetinaDisplay','SecondaryStorage','Unnamed: 22'], axis=1, inplace=True)
akv16.rename(columns={'Price_euros':'Price'}, inplace=True)

# Group by company to get average price
avg_price_data = akv16.groupby('Company').agg({'Price': 'mean'}).reset_index()

# Create bar chart using Plotly Express
fig = px.bar(avg_price_data, x='Company', y='Price', 
             labels={'Price':'Average Price', 'Company':'Company'},
             title="Average Price of Products by Company",
             color='Company',
             template="plotly")

# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Company Product Pricing Dashboard'),

    dcc.Graph(
        id='price-bar-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
