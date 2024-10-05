import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

akv16 = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# Padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Sidebar layout
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("Number of students per education level", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Page content layout
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# App layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callback to render page content
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        # Create a layout with 5 graphs in a single row
        return html.Div(
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=px.bar(akv16, x='Years', y='Girls Kindergarten')), width=10),
                    
                ]
            )
        )
    
    
    elif pathname == "/page-1":
        return [
            html.H1('Grad School in Iran', style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph', figure=px.bar(akv16, barmode='group', x='Years', y=['Girls Grade School', 'Boys Grade School']))
        ]
    
    elif pathname == "/page-2":
        return [
            html.H1('High School in Iran', style={'textAlign': 'center'}),
            dcc.Graph(id='bargraph', figure=px.bar(akv16, barmode='group', x='Years', y=['Girls High School', 'Boys High School']))
        ]
    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
