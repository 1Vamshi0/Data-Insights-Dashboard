from dash import Dash, dcc, html
import matplotlib.pyplot as plt
import pandas as pd

# Loading and cleaning dataset
akv16 = pd.read_csv('Laptop_Sales_dataset.csv')
akv16.drop(['TypeName', 'ScreenW', 'ScreenH', 'Touchscreen', 'IPSpanel', 'RetinaDisplay', 'SecondaryStorage', 'Unnamed: 22'], axis=1, inplace=True)
akv16.rename(columns={'Price_euros': 'Price'}, inplace=True)

# Initialize the app
app = Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1(children="Company Laptop Sales Dashboard"),
    html.P(children="This dashboard displays the company's laptop sales data."),

    # Container for graphs with CSS styles for layout
    html.Div(
        style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-between', 'flexWrap': 'wrap'},
        children=[
            # Second graph with border
            html.Div(
                style={'border': '2px solid #28a745', 'borderRadius': '10px', 'padding': '10px', 'width': '30%'},
                children=[
                    dcc.Graph(
                        figure={
                            "data": [
                                {
                                    "x": akv16["Company"],
                                    "y": akv16["Price"],
                                    "type": "scatter",  # Scatter plot for price distribution
                                    "mode": "markers",
                                    "name": "Price Distribution",
                                },
                            ],
                            "layout": {"title": "Scatter Plot of Laptop Prices","height":"500px"},
                        },
                    ),
                ],
            ),
            # Third graph with border
            html.Div(
                style={'border': '2px solid #dc3545', 'borderRadius': '10px', 'padding': '10px', 'width': '30%','height':'300px'},
                children=[
                    dcc.Graph(
                        figure={
                            "data": [
                                {
                                    "x": akv16["Company"],
                                    "y": akv16["Price"],
                                    "type": "line",  # Line graph for price trends
                                    "name": "Price Trend",
                                },
                            ],
                            "layout": {"title": "Line Graph of Laptop Prices"},
                        },
                    ),
                ],
            ),
        ],
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)
