import matplotlib.pyplot as plt
import serial

# This program will take input from the serial monitor. In order to make sure that this works
# correctly, you must also be running the Light_Sensor_Test.ino code on the arduino.

print("This program plots infinitely:\nTo stop, you must manually stop the code")
print("At any point, you may press the 'Save' button on \
the bottom bar of the graph to save the image")

# Change this to the correct port of the specific arduino device on your computer
port = '/dev/cu.usbmodem14101'
arduino = serial.Serial(port, 9600)
plt.close('all')

# Allows for real-time plotting
plt.ion()
plt.figure()
plt.show()

# Creating the lists that will be plotted
x = list()
y = list()
x_val = 0

# The infinite loop that will plot data until user stops the code from running
while True:
    data = int(arduino.readline().decode().strip())
    y.append(data)
    x.append(x_val)
    plt.plot(x, y, 'tab:blue')
    plt.ylabel("Light Level")
    plt.title("Real Time Light Level")
    x_val += 1
    plt.pause(.001)
