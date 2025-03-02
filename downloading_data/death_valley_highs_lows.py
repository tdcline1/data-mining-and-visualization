from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
for index, entry in enumerate(header_row):
    if entry == "TMAX":
        tmax_index = index
    elif entry == "TMIN":
        tmin_index = index
    elif entry == "DATE":
        date_index = index
    elif entry == "NAME":
        name_index = index

# Extract dates and high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    station_name = row[name_index]
    try:
        high = int(row[tmax_index])
        low = int(row[tmin_index])
    except ValueError:
        print(f"Missing data found for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format Plot
title = f'Daily High and Low Temperatures 2021\n{station_name}'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()