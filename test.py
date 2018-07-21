import dota2api
import pprint
import pandas as pd
import numpy as np
import os

os.getcwd()
api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")

pd.set_option('display.expand_frame_repr', False)

matches_data = pd.read_csv("/Users/thanhuwe8/Google Drive/Dota2Project/matches.csv", encoding="ISO-8859-1")

matches_data.tail(2)

dict_info = {"Team_id": [np.nan], "Team_name":[np.nan]}
match_info = pd.DataFrame(dict_info)


for i in range(0, len(matches_data)):
    try:
        current_match = matches_data['Match ID'][i]
        # print(current_match)
        match = api.get_match_details(match_id=current_match)

        try:
            radiant_current = match['radiant_team_id']
        except:
            radiant_current = ""

        try:
            radiant_name = match['radiant']
        except:
            radiant_name = ""

        temp_info1 = {"Team_id": radiant_current, 'Team_name': radiant_name}
        match_info = match_info.append(temp_info1, ignore_index=True)

        try:
            dire_current = match['dire_team_id']
        except:
            dire_current = ""


        try:
            dire_name = match['dire_name']
        except:
            dire_name =  ""

        temp_info2 = {"Team_id":dire_current, "Team_name":dire_name}
        match_info = match_info.append(temp_info2, ignore_index=True)

    except:
        print("Something went wrong")

match_info = match_info.dropna()
match_info_nodups = match_info.drop_duplciates()
