import pandas as pd
import numpy as np
import datetime

import matplotlib.pyplot as plt
import seaborn


import dota2api
api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")


hist = api.get_match_history(account_id=107940251, matches_requested=10)






hist2 = api.get_match_history(account_id=185077673)

len(hist['matches'])
hist['matches'][1]['match_id']

hist['matches'][1]
# Final DataFrame
data_summary = {"match_id":[np.nan], "account_id":[np.nan], "hero_id":[np.nan], "player_slot":[np.nan]}


hist['matches'][1]['players']
match_id = hist['matches'][1]['match_id']

for i in range(0,len(hist['matches'])):
    temp_acc = hist['matches'][1]['players'][i]
    acc_id = temp_acc['account_id']
    if acc_id == 107940251:
        hero_id = temp_acc['hero_id']
        print(hero_id)
        player_slot = temp_acc['player_slot']
        print(player_slot)
        if player_slot < 5:
            side = "Radiant"
        else:
            side = "Dire"
        match_info = {"account_id":acc_id, "hero_id":hero_id, "player_slot":player_slot, "side":side}



### Get match ID
match_info


data = api.get_match_details(match_id=match_id)
data
data['cluster_name']
data

radiant_win = data['radiant_win']
duration = data['duration']
match_seq_num = data['match_seq_num']
cluster_name = data['cluster_name']
first_blood_time = data['first_blood_time']
tower_status_radiant = data['tower_status_radiant']
tower_status_dire = data['tower_status_dire']


dict_game = {"cluster_name", "barracks_status_dire", "barracks_status_radiant". d}

invalid2 = {"players", "picks_bans"}

result3 = {x:data[x] for x in data if x not in invalid2}
result3



data_test = data['players'][1]
data_test['ability_upgrades']


invalid = {"ability_upgrades"}
new_data = {x: data_test[x] for x in data_test if x not in invalid}
new_data.update(match_info)
best = pd.DataFrame(new_data, index=[1])
best.append(new_data, ignore_index=True)

final_data =


ability
ability = x['ability_upgrades']

y = pd.DataFrame(x)
y
for i in range(0, len(data['players'])):
    if data['players'][i]['account_id'] == 10794251:
        temp_data = data['players'][i]
        ability = data['players'][i]['ability_upgrades']
        kills = temp_data['kills']
        denies = temp_data['denies']
        hero_id = temp_data['hero']
        gold = temp_data['gold']
        gold_per_min = temp_data['gold_per_min']
        gold_spent = temp_data['gold_spent']
        hero_damage = temp_data['hero_damage']
        hero_healing = temp_data['hero_healing']



my_dict = {"keyA":1, "keyB":2, "keyC":3}
invalid = {"keyA", "keyB"}

{x:my_dict[x] for x in my_dict if x not in invalid}

for x in my_dict:
    print(x)




len(hist2['matches'])

hist['matches'][1]['players']

test = hist['matches'][1]['match_id']
test

len(hist['matches'])

data = api.get_match_details(match_id=test)

for i in range(0,10):
    x = data['players'][i]
    if x['account_id'] == 107940251:
        print("ok")
        print(x)
        a = x


dict_info = {'Team_id':[np.nan], 'Team_name':[np.nan]}
match_info = pd.DataFrame(dict_info)

for i in range(0, len(match_data))








data['players'][2]['account_id']

data['players'][2]
data['radiant_win']
data['duration']
data['match_seq_num']
data['cluster_name']
data['first_blood_time']
data['tower_status_radiant']
data['tower_status_dire']
