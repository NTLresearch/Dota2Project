
import Tools.exportdata as tla
import dota2api
import os
import pandas as pd

api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")
data = tla.final_data_io(107940251, 200 )

data2 = tla.pull_match_id(107940251, 1000)
data2.head(2)



data3 = api.get_match_history(107940251, matches_requested=200)

type(data3)


data =





import pandas as pd
a = pd.read_html(r.text)

import json
import requests

response = requests.get("https://api.opendota.com/api/players/107940251/matches?limit=1000")
json_data = json.loads(response.text)
json_data
json_data[1]
data = pd.DataFrame()

for i in range(0, len(json_data)):
    temp = json_data[i]
    data = data.append(temp, ignore_index=True)

data.to_csv("107940251.csv")
