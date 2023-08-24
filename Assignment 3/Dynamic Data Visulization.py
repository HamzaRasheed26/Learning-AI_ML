import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import pandas as pd

# Create the figure and axis for the plot
fig, ax = plt.subplots()

data_path = "FINAL_USO.csv"
gold_data = pd.read_csv(data_path, index_col='Date', parse_dates=True)

# Initialize arrays to store time and price data
time_intervals = []
open_prices = []
close_prices = []

# Maximum number of data points to display on the screen
max_data_points = 40


def update_data(frame):
    time_intervals.append(gold_data.index[frame])
    open_prices.append(gold_data['Open'][frame])
    close_prices.append(gold_data['Close'][frame])

    # Trim data arrays to maintain the maximum number of data points
    if len(time_intervals) > max_data_points:
        time_intervals.pop(0)
        open_prices.pop(0)
        close_prices.pop(0)

    ax.clear()
    ax.plot(time_intervals, open_prices, marker='o', label='Open Price')
    ax.plot(time_intervals, close_prices, marker='x', label='Close Price')
    ax.set_title("Live Gold Price Visualization")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.legend()


# Create the animation
ani = FuncAnimation(fig, update_data, frames=range(100),
                    repeat=False, interval=100)

plt.show()
