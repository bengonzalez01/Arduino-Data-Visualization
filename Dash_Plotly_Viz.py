import serial
import time
import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go

import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# starting app
app = dash.Dash(__name__)

# reading data into csv
df = pd.read_csv('arduino_test_data.csv')

# creating the app layout
app.layout = html.Div([

    html.H1("Arduino Data Visualization", style= {'text-align': 'center'}),

    dcc.Dropdown(id = 'Select Data Type',
                options= [
                    {"label" : "Pressure", "value" : "Pressure"},
                    {"label" : "Altitude", "value" : "Altitude"},
                    {"label" : "Light", "value" : "Light"},
                    {"label" : "Sound", "value" : "Sound"},
                    {"label" : "Temperature", "value" : "Temperature"},
                    {"label" : "Humidity", "value" : "Humidity"}],
                    multi= False,
                    value= "Pressure",
                    style={'width' : "40%"}
                    ),

    
    html.Div(id= 'output_container', children=[]),
    html.Br(),

    dcc.Graph(id = "environmental_values", figure = {})

])

if __name__ == '__main__':
    app.run_server(debug=True)