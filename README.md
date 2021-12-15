# Arduino Data Visualization
This repository shows my experience collecting, analyzing, and visualizing data from an Arduino using Python. It is broken up into two parts, with two files per part.

Part 1 - Data Collection and Visualization:
Has two Files needed: Arduino_Data_Collection_and_Basic_Visualization.ipynb and Sensors_Data_Ouput.ino
This project takes 200 data inputs over time from an Arduino Uno (connected to a Sensor Base Kit) and provides Descriptive Statistics and Visualizations on the different types of environmental factors (Pressure, Altitude, Light, Sound, Temperature, and Humidity. It is a Jupyter Notebook (.ipynb) file and shows the steps that I went through to collect and analyze / visualize the data. The notebook is broken up into two parts: Part A - Data Collection and Part B - Data Analysis and Visualization.

Part 2 - Real Time Data Plotting:
Has two files needed: Arduino_Real_Time_Data_Plotting.py and Light_Sensor_Test.ino
For this projext, I worked with the Arduino UNO and the light sensor on the Arduino SensorKit. I decided to use the light sensor as the data can vary drastically in a controlled environment, as lights can be turned on and off. This program uses the matplotlib.pyplot.ino() function to plot data in real time until the user decides to stop the code from running.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info
This project is part of my extracurricular work as a Research Assistant at the Data Mining and Connectivity (DMC) Lab at the College of Charleston. I utilized the technologies that I have learned through my classes, such as libraries like matplotlib and numpy, and learned new technoligies, such as the arduino coding language and the python serial package, in order to collect, visualize, and analyze data about different types of environmental factors. All of the data collection was done indoors, in a controlled environment. 

There are currently two files in this repository:
1. The Arduino_Data_Collection_and_Basic_Visualization.ipynb file where I was doing the processing and visualizing of data. __(In order to see the visualizations you have to scroll down past the output of the run() function which shows all of data retrieval being completed)__
2. The Sensors_Data_Ouput.ino file which is the code that I was running on the Arduino during the time that I was doing the data collection. This file accompanies the Arduino_Data_Collection_and_Basic_Visualization.ipynb file.
3. The Arduino_Real_Time_Data_Plotting.py file is where I did the real-time plotting of the light sensor data. This will infinitely plot data until the code is manually stopped.
4. The Light_Sensor_Test.ino is the code that I was running on the Arduino at the time of real-time data plotting. This file accompanies the Arduino_Real_Time_Data_Plotting.py file.
	
## Technologies
Project is created with:
* Python 3.8.5
* Jupyter Notebook
* Arduino IDE
* Arduino UNO R3
* Arduino SensorKit - Base
	
## Setup
For Part 1:
To run this project locally you must have an Arudino UNO R3 (+ SensorKit) connected to your computer and change the variable 'port' on the Arduino_Data_Collection_and_Basic_Visualization.ipynb file to the local path of the arduino. You also need to have the Sensors_Data_Ouput.ino file uploaded and running on the Arduino UNO. 

For Part 2:
Similar to Part 1, to run this project locally you must have an Arudino UNO R3 (+ SensorKit) connected to your computer and change the variable 'port' on the Arduino_Real_Time_Data_Plotting.py file to the local path of the arduino. You need to also have the Light_Sensor_Test.ino file uploaded and running on the Arduino UNO.

For both, you must install the following Arduino and Python libraries:

On the Arduino sketches, you need to download:
Arduino_SensorKit.h library 

For python you need to install following libraries:
* time (built-in) 
* pip install numpy
* pip install matplotlib
* pip install serial

## Status
This project is still in progress. I plan to expand by creating and adding a .py file (instead of a .ipynb file) that takes in user input on the amount of data values that are collected from the arduino, and the time between each value. From this, the user can also input what type of visualization they want on a chosen type of collected data.
