import datetime
import os
import urllib.request

today = datetime.date.today()
folder = f"data/raw/{today}"

if (os.path.exists(folder) == False):
    os.makedirs(folder)
    

regions = ["IT-23", "SE", "FR"]

for r in regions:
    URL = f"https://static.avalanche.report/eaws_bulletins/{today}/{today}-{r}.json"
    filePath = f"{folder}/{r}.json"

    if(os.path.exists(filePath)):
        print("skipped")

    else:
        try:
            urllib.request.urlretrieve(url = URL, filename=filePath)
            print(f"{r} Saved")

        except Exception as e:
            print(r)
            print(e)