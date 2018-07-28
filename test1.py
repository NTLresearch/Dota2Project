
import Tools.exportdata as tla
import dota2api
import os
import pandas as pd

data5 = pull_match_opendota(107940251, 100)
data6 = get_match_final(data5)
data6.loc[:,'start_time'][1]
data7 = add_result_data(data5, data6)
data7 = add_extra_data(data7)
data7.head()


dota_url = "https://api.opendota.com/api/players/{0}/matches?limit={1}".format(107940251, 10)
response = requests.get(dota_url)
json_data = json.loads(response.text)
match_info = pd.DataFrame()
json_data[1]['player_slot']
