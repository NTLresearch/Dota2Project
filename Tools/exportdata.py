import pandas as pd
import numpy as np
import datetime
import dota2api
import os
import datetime
import json
import requests

api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")


def pull_match_opendota(acc_id, n):
    dota_url = "https://api.opendota.com/api/players/{0}/matches?limit={1}".format(acc_id, n)
    response = requests.get(dota_url)
    json_data = json.loads(response.text)
    match_info = pd.DataFrame()
    player_id = []
    side = []
    for i in range(0, len(json_data)):
        temp = json_data[i]

        player_id.append(acc_id)

        if temp['player_slot'] < 5:
            temp_side = "Radiant"
        else:
            temp_side = "Dire"
        side.append(temp_side)

        match_info = match_info.append(temp, ignore_index=True)

    match_info.insert(1, "account_id", player_id)
    match_info.insert(2, "side", side)
    return(match_info)


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

### internal function

def get_data_match(match_json):
    """ get match_data from match_json object from dota2api get_match_details function
    Args:
        match_json: object of dota2api get_match_details function
    Returns:
        pandas DataFrame
    """
    invalid1 = {"players", "picks_bans", 'start_time', "match_id", "radiant_win", "player_slot"}
    match_data = {x:match_json[x] for x in match_json if x not in invalid1}
    df1 = pd.DataFrame(match_data, index=[0])
    return(df1)


### internal function
def get_data_player(player_id, match_json):
    """ get player_data from match_json object from dota2api get_match_details function
        with specific player_id

    Args:
        player_id: id of player, for example 10790251
        match_json: object of dota2api get_match_details function
    Returns:
        pandas DataFrame
    """
    invalid2 = {"ability_upgrades", "account_id", "player_slot"}
    player = match_json['players']

    for j in range(0, len(player)):
        if player[j]['account_id'] == player_id:
            player_data = {x: player[j][x] for x in player[j] if x not in invalid2}
            df2 = pd.DataFrame(player_data, index=[0])
    return(df2)



def get_match_final(data):
    """ Wrapper for get_data_match and get_data_player, concatenate 2 dataframe into single DataFrame
        with hero stats data
    Args:
        data: object from pull_match_id function
    Returns:
        pandas DataFrame
    """
    final_data = pd.DataFrame()

    # Load hero_stats_2.csv data
    root_path = os.getcwd()
    data_path = "Data/dota_hero_stats_2.csv"
    hero_path = os.path.join(root_path, data_path)
    hero_stats = pd.read_csv(hero_path)

    for i in range(0, len(data)):
        id = int(data.loc[:,'match_id'][i])
        player_id = data.loc[:,'account_id'][i]

        match_json = api.get_match_details(id)

        temp1 = get_data_match(match_json)
        temp2 = get_data_player(player_id, match_json)

        hero_id = temp2.hero_id.values[0]
        hero_data = hero_stats[hero_stats.id == hero_id].reset_index()

        df = pd.concat([temp1, temp2, hero_data], axis=1)
        # df = pd.concat([df, data.iloc[i,:]], axis=1)
        final_data = final_data.append(df, ignore_index=True)
        print("Row loaded: ", i)
        # print('data row number:', i)
        # Exctract hero stats and concatenate to pandas DataFrame
    return final_data


def add_result_data(match_data, match_final_data):
    clean = pd.concat([match_data.reset_index(), match_final_data], axis=1)
    results = []
    # Path for hero file
    for i in range(0, len(clean)):
        if clean.loc[:,"player_slot"][i] < 5 and clean.loc[:,"radiant_win"][i]==True:
            results.append(1)
        elif clean.loc[:,"player_slot"][i] > 5 and clean.loc[:,"radiant_win"][i]==False:
            results.append(1)
        else:
            results.append(0)
        hero_id = clean.iloc[i, 2]

    clean['Results'] = results
    return clean

def add_extra_data(final_df):
    year, month, day, hour = ([] for i in range(4))
    for j in final_df['start_time'].index:
        ts = datetime.datetime.fromtimestamp(final_df['start_time'][j])
        year.append(ts.year)
        month.append(ts.month)
        day.append(ts.day)
        hour.append(ts.hour)
    final_df.insert(3, 'year', year)
    final_df.insert(4, 'month', month)
    final_df.insert(5, 'day', day)
    final_df.insert(6, 'hour', hour)
    return final_df

### Final Function
def final_data(acc_id, n, opendota):
    api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")

    if opendota=="dota2api":
        match_data = pull_match_id(acc_id, n)
    else:
        match_data = pull_match_opendota(acc_id, n)

    match_final_data = get_match_final(match_data)
    final_df = add_result_data(match_data, match_final_data)
    full_extra =  add_extra_data(final_df)
    return(full_extra)

### Data in order
def final_data_io(acc_id, n, opendota):
    # dota2api Initilise, change it later to pass argument instead of fixed value
    data = final_data(acc_id, n, opendota)

    # data in order
    col_export = ['match_id', 'year', 'month', 'day', 'hour', 'side', 'start_time','radiant_win',
                    'Results', "player_slot", 'duration','hero_id', 'localized_name', 'primary_attr', 'attack_type',
                    'primary_attr', 'carry', 'jungler', 'pusher', 'nuker', 'disabler', 'initiator', 'durable', 'support',
                    'legs','kills', 'deaths', 'assists',]

    data_io = data[col_export]
    return(data_io)


print("done")


if __name__ == '__main__':
    print("done")
