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

# data collection
def collect_data():
    """Collects Data from Arduino and separates it into previously defined lists"""
    # This is the port path that connects to the arduino (can be changed)
    port = '/dev/cu.usbmodem14101'

    # opening arduino data using Serial
    arduino = serial.Serial(port, 9600)
    arduino_data = arduino.readline()

    # decoding data and finding individual data values
    decoded = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    vals = decoded.split("x")

    # Creating a new list of values without the extra letters.
    new_vals = []
    for val in vals:
        new_val = val.strip()
        new_vals.append(new_val)

    # Creating the final list of data
    outlist = []
    for i in new_vals:
        outlist.append(float(i))
    # creating time stamp and returning data points
    stamp = time.time()
    return outlist[0], outlist[1], outlist[2], outlist[3], outlist[4], outlist[5], stamp


def run(num, secs):
    """Runs the collect_data function a certain number with a pause time given by user

    Arguments:
    num -- Number of times you want to collect a data value for each data category
    secs -- Number of seconds that are paused between each data collection
    """
    # Initializing the lists for data collection
    print("Starting Data Collection: ")
    pressures = []
    altitudes = []
    lights = []
    sounds = []
    temps = []
    hums = []
    times = []

    # Creating an interval to update the user about the data collection
    update_num = int(num / 10)

    # Looping the given amount of times and appending data to lists. Uses time.sleep() at user interval
    for i in range(num):
        pressure, altitude, light, sound, temp, hum, time_val = collect_data()
        pressures.append(pressure); altitudes.append(altitude); lights.append(light); sounds.append(sound)
        temps.append(temp); hums.append(hum); times.append(time_val)
        if (i + 1) % update_num == 0:
            print(f'{i+1} / {num} Complete')
        time.sleep(secs)

    # Returning the collected data
    print("Data Collection Complete")
    print(f"Collected {len(times)} Data Points")
    data = [pressures, altitudes, lights, sounds, temps, hums, times]
    return data