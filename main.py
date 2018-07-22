import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import dota2api

api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")
hist = api.get_match_history(account_id=107940251, matches_requested=10)


def pull_match_id(acc_id, n):
    hist = api.get_match_history(account_id=acc_id, matches_requested=n)
    match_info = {"match_id":[np.nan], "account_id":[np.nan], "hero_id":[np.nan], "player_slot":[np.nan]}
    match_info = pd.DataFrame(match_info)
    for i in range(0, len(hist['matches'])):
        for j in range(0, len(hist['matches'][i]['players'])):
            temp_acc = hist['matches'][i]['players'][j]
            account_id = temp_acc['account_id']
            if account_id == acc_id:
                match_id = hist['matches'][i]['match_id']
                account_id = int(acc_id)
                hero_id = temp_acc["hero_id"]
                player_slot = temp_acc["player_slot"]
                if player_slot < 5:
                    side = "Radiant"
                else:
                    side = "Dire"
                final_data = {"match_id":match_id, "account_id":acc_id, "hero_id":hero_id, "player_slot":player_slot, "side":side}

                match_info = match_info.append(final_data, ignore_index=True)

    return match_info.dropna()


def get_data_overall(i, temp_match):
    invalid1 = {"players", "picks_bans"}
    match_data = {x:temp_match[x] for x in temp_match if x not in invalid1}
    df1 = pd.DataFrame(match_data, index=[0])
    return(df1)

def get_data_player(i, player_id, temp_match):
    invalid2 = {"ability_upgrades", "account_id"}
    player = temp_match['players']
    for j in range(0, len(player)):
        if player[j]['account_id'] == player_id:
            player_data = {x: player[j][x] for x in player[j] if x not in invalid2}
            df2 = pd.DataFrame(player_data, index=[0])
    return(df2)


def get_match_final(data):

    final_data = pd.DataFrame()

    for i in range(0, len(data)):
        id = int(data.iloc[i,2])
        player_id = data.iloc[i,0]
        temp_match = api.get_match_details(id)

        temp1 = get_data_overall(i, temp_match)
        temp2 = get_data_player(i, player_id, temp_match)

        df = pd.concat([temp1, temp2], axis=1)
        # df = pd.concat([df, data.iloc[i,:]], axis=1)
        final_data = final_data.append(df, ignore_index=True)
        # final_data = pd.concat([final_data, data], axis=1)

    return final_data

match_data = pull_match_id(acc_id=181798082, n=10)
player_data = get_match_final(match_data)

def clean_data(match_data, player_data):
    clean = pd.concat([match_data.reset_index(), player_data], axis=1)
    results = []
    for i in range(0, len(clean)):
        if clean.iloc[i, 59]==1 and clean.iloc[i,5]=='Radiant':
            results.append(1)
        elif clean.iloc[i,59]!=1 and clean.iloc[i,5]=='Dire':
            results.append(1)
        else:
            results.append(0)
    clean['Results'] = results
    return clean




def final_data(acc_id, n):
    match_data = pull_match_id(acc_id, n)
    player_data = get_match_final(match_data)
    final_df = clean_data(match_data, player_data)
    return(final_df)


final1 = final_data(181798082, n=10)
x = final1.columns.values
x

final1.columns.values[59]

col_type1 = ['match_id', 'side', 'start_time', 'duration','hero_id', 'radiant_win','kills', 'deaths', 'assists']



test0 = pull_match_id(181798082, 100)
test1 = get_match_final(test0)
test2 = clean_data(test0, test1)
test3 = test2[col_type1]


final2 = final1[col_type1]
final2.head(2)


### Analysis
wins = len(test2[test2['Results']==1])
wins_pct = round(wins/len(test2),3)
wins_pct

losses = len(test2[test2['Results']==0])
losses_pct = 1 - wins_pct

radiant_wins = test2['radiant_win'].value_counts()
test3.head(2)


### Converting to year month date
test3['duration'] = round(test3['duration']/60, 3)
print(test3.index)



year = []
month = []
day = []
hour = []

a = datetime.datetime.fromtimestamp(test3['start_time'][1])
a


for ix in test3['start_time'].index:
    ts = datetime.datetime.fromtimestamp(test3['start_time'][ix])
    year.append(ts.year)
    month.append(ts.month)
    day.append(ts.day)
    hour.append(ts.hour)

test3.insert(3, 'year', year)
test3.insert(3, 'month', month)
test3.insert(3, 'day', day)
test3.insert(3, 'hour', hour)







print("done")
