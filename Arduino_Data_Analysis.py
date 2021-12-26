import serial
import time
import matplotlib.pyplot as plt


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
    num -- number of times you want to collect a data value for each data category
    secs -- number of seconds that are paused between each data collection
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


def plot(time_graph, data, data_type, plot_type):
    """Plots the collected Data into a Frequency Distribution Histogram, Line Plot, or Scatter Plot

    Arguments:
    time_graph -- Time Data collected during the collection phase
    data -- The specific data that the user decides to plot
    data_type -- Integer representing the type of data being plotted
    plot_type -- Integer representing the type of plot that will be used
    """
    # Creating Lists of data types and labels for plotting
    data_types = ["Pressure", "Altitude", "Light", "Sound", "Temperature", "Humidity"]
    labels = ["Pa", "Meters", "Light Value", "Sound Level", "Degrees Celsius", "%"]

    # Plotting the Histogram
    if plot_type == 0:
        plt.title(f"Distribution of {data_types[data_type]}")
        plt.hist(data, bins=15, color="red")
        plt.xlabel(labels[data_type])
        plt.show()

    # Plotting the Line Plot
    elif plot_type == 1:
        plt.title(f"Line Plot of {data_types[data_type]}")
        plt.plot(time_graph, data, 'tab:red')
        plt.ylabel(labels[data_type])
        plt.xlabel("Time")
        plt.show()

    # Plotting the Scatter Plot
    elif plot_type == 2:
        plt.title(f"Scatter Plot of {data_types[data_type]}")
        plt.scatter(time_graph, data, c='red')
        plt.ylabel(labels[data_type])
        plt.xlabel("Time")
        plt.show()


def main():
    print("This program takes in data from the Arduino and plots it according to the user.")
    points = eval(input("How many data points do you want to plot (50 - 200 Recommended)?\n"))
    delay = eval((input("What delay do you want between each data point (2 Recommended)?\n")))
    data = run(points, delay)
    d_type = eval(input("""What type of data would you like to plot?\nEnter '0' for Pressure
Enter '1' for Altitude\nEnter '2' for Light\nEnter '3' for Sound\nEnter '4' for Temperature
Enter '5' for Humidity\n"""))
    p_type = eval(input("""What type of plot would you like?\nEnter '0' for Histogram of Distribution:
Enter '1' for Line Plot\nEnter '2' for Scatter Plot\n"""))
    plot(data[6], data[d_type], d_type, p_type)


if __name__ == "__main__":
    main()
