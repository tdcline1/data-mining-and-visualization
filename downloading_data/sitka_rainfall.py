from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures
dates, precips = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        print(row[5])
        precip = float(row[5])
        print(precip)
    except ValueError:
        print(f"Missing data found for {current_date}")
    else:
        dates.append(current_date)
        precips.append(precip)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precips, color='blue')

# Format Plot
title = 'Daily Precip 2021\nSitka, AL'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precip (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()