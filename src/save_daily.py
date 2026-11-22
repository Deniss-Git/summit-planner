import datetime
import os
import urllib.request
import sys

today = datetime.date.today()
folder = f"data/raw/{today}"
fail_count = 0
regions = ["IT-23", "SE", "FR"]

latitude = [68.4258, 68.4180, 68.4065, 45.9231, 45.9016, 45.8328, 45.4480, 45.4452, 45.4051, 45.7966, 45.8291, 45.8458]
longitude = [18.1273, 18.1046, 18.0893, 6.8697, 6.8849, 6.8650, 6.9802, 6.9511, 6.8276, 6.9689, 6.9509, 6.9317]
elevation = [521, 909, 1051, 1035, 2317, 4800, 1850, 2827, 3855, 1200, 2173, 3462]
what_to_search = ["temperature_2m","wind_speed_10m","wind_direction_10m","wind_gusts_10m","precipitation","snowfall","snow_depth","freezing_level_height","cloud_cover","visibility","relative_humidity_2m"]
open_meteo_url = f"https://api.open-meteo.com/v1/forecast?latitude={",".join(map(str, latitude))}&longitude={",".join(map(str, longitude))}&elevation={",".join(map(str, elevation))}&forecast_days=1&hourly={",".join(what_to_search)}"
print(open_meteo_url)

os.makedirs(folder, exist_ok = True)

for r in regions:
    url = f"https://static.avalanche.report/eaws_bulletins/{today}/{today}-{r}.json"
    where_to_save = f"{folder}/{r}.json"

    if os.path.exists(where_to_save):
        print(f"{r} skipped")

    else:
        try:
            urllib.request.urlretrieve(url = url, filename=where_to_save)
            print(f"{r} Saved")

        except Exception as e:
            print(f"{r} failed: {e}")
            fail_count += 1

if os.path.exists(f"{folder}/Open_Meteo.json"):
        print("OM skipped")
else:
    try:
        urllib.request.urlretrieve(url = open_meteo_url, filename= f"{folder}/Open_Meteo.json")
        print("Open meteo Saved")

    except Exception as e:
        print(f"OM failed: {e}")
        fail_count += 1

if fail_count == len(regions) +1:
    sys.exit(1)