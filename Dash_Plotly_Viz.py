import serial
import time
import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go

import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
# reading data into csv
df = pd.read_csv('arduino_test_data.csv')

