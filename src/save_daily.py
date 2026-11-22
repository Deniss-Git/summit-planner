import datetime
import os
import urllib.request
import sys

today = datetime.date.today()
folder = f"data/raw/{today}"
fail_count = 0
regions = ["IT-23", "SE", "FR"]

os.makedirs(folder, exist_ok= True)

for r in regions:
    URL = f"https://static.avalanche.report/eaws_bulletins/{today}/{today}-{r}.json"
    where_to_save = f"{folder}/{r}.json"

    if os.path.exists(where_to_save):
        print(f"{r} skipped")

    else:
        try:
            urllib.request.urlretrieve(url = URL, filename=where_to_save)
            print(f"{r} Saved")

        except Exception as e:
            print(f"{r} failed: {e}")
            fail_count += 1

if fail_count == len(regions):
    sys.exit(1)