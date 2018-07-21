import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn
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

thanh = get_match_final(test)
thanh

abc = pd.concat([thanh, test.reset_index()], axis=1)


for i in range(0, len(abc)):
    result = []
    if abc['radiant_win'][i] == True and abc['player_slot'][i] < 5:
        result.append(1)
    elif abc['radiant_win'][i] == False and abc['player_slot'][i] > 5:
        result.append(1)
    else:
        result.append(0)

abc['radiant_win'][2]

abc.shape
aaa = abc.columns.values
type(aaa)
aaa[53]
aaa[68]

aaa[1:5]
aaa[8]


def recolumn_data(data):
    col_name = [aaa[0], aaa[8], aaa[]]




thanh2 = thanh[['assists',]


tuan_anh = pull_match_id(acc_id=181798082,n=100)
data_tuan_anh = get_match_final(tuan_anh)









print("done")
