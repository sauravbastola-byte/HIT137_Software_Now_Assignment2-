import pandas as pd
import os

folder_name = "temperatures"
all_data = []

for file_name in os.listdir(folder_name):
    if file_name.endswith(".csv"):
        file_path = os.path.join(folder_name, file_name)
        df = pd.read_csv(file_path)
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

month_map = {
    "January": 1, "February": 2, "March": 3, "April": 4,"May": 5, "June": 6, 
    "July": 7, "August": 8,"September": 9, "October": 10, "November": 11, "December": 12
}

long_df = pd.melt(
    combined_df,
    id_vars= ["STATION_NAME"],
    value_vars= combined_df.columns.intersection(month_map).tolist(),
    var_name= "Month",
    value_name="Temperature"
)

long_df = long_df.dropna(subset=["Temperature"])
long_df["Month_Num"] = long_df["Month"].map(month_map)

def get_season(month):
    if month in (12, 1, 2):
        return "Summer"
    elif month in (3, 4, 5):
        return "Autumn"
    elif month in (6, 7, 8):
        return "Winter"
    else:
        return "Spring" # 9, 10, 11

long_df["Season"] = long_df["Month_Num"].apply(get_season)
seasonal_avgerage = long_df.groupby("Season")["Temperature"].mean()

with open("average_temp.txt", "w") as f:
    for season, temp in seasonal_avgerage.items():
        f.write(f"{season}: {temp:.1f}°C\n")

station_stats = long_df.groupby("STATION_NAME")["Temperature"].agg(["max", "min"])
station_stats["Range"] = station_stats["max"] - station_stats["min"]

maximum_range = station_stats["Range"].max()
largest_range_stations = station_stats[station_stats["Range"] == maximum_range]

with open("largest_temp_range_station.txt", "w") as f:
    for station, row in largest_range_stations.iterrows():
        f.write(
            f"Station {station}: Range {row['Range']:.1f}°C "
            f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
        )

std_dev = long_df.groupby("STATION_NAME")["Temperature"].std()
min_std = std_dev.min()
max_std = std_dev.max()

most_stable = std_dev[std_dev == min_std]
most_variable = std_dev[std_dev == max_std]

with open("temperature_stability_stations.txt", "w") as f:
    for station, value in most_stable.items():
        f.write("\nMost Stable:\n")
        f.write(f"Station {station}: StdDev {value:.1f}°C\n")
        
    for station, value in most_variable.items():
        f.write("\nMost Variable:\n")
        f.write(f"Station {station}: StdDev {value:.1f}°C\n")
       

print("Check output files created. Analysis complete.")
