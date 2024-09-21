# %%
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CO2 Emissions Data (downloaded from 'Our World in Data')
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
df = pd.read_csv(url)

# Step 2: Filter for global CO2 emissions
# Assuming the data has a 'year' column and a 'co2' column that contains CO2 emissions (in million tonnes)
df_global = df[df["country"] == "World"][["year", "co2"]]

# Calculate CO2 emissions per day for each year
df_global["co2_per_day"] = df_global["co2"] * 1e6 / 365  # Converting to tonnes/day

# Step 3: Plot the CO2 emissions per day over the years
plt.figure(figsize=(10, 6))
plt.plot(
    df_global["year"],
    df_global["co2_per_day"],
    label="CO2 Emissions per Day",
    color="green",
)

plt.title("Global CO2 Emissions Per Day (Million Tonnes)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("CO2 Emissions (Tonnes/Day)", fontsize=14)
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

# %%
