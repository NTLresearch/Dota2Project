import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
def getMatchIds(team_a, team_b, match_ids):
    try:
        datdota = 'https://www.datdota.com/teams/head-to-head?team-a=' + team_a + '&team-b=' + team_b + '&tier=1&tier=2&valve-event=does-not-matter&patch=7.06&patch=7.05&patch=7.04&patch=7.03&patch=7.02&patch=7.01&patch=7.00&patch=6.88&patch=6.87&patch=6.86&patch=6.85&patch=6.84&patch=6.83&patch=6.82&patch=6.81&patch=6.80&patch=6.79&patch=6.78&winner=either&after=01%2F01%2F2015&before=25%2F07%2F2017&duration=0%3B200'
        r = requests.get(datdota)
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.find(class_ ='table table-striped table-bordered table-hover data-table')
        for row in table.find_all('tr')[2:]:
            col = row.find_all('td')    
            temp_id = col[1].text.strip()
            print(temp_id)
            temp_df = {'match_id': temp_id}
            match_ids = match_ids.append(temp_df, ignore_index=True)
            return match_ids
    except:
        return match_ids




dict1 = {'match_id': [np.nan]}
match_ids = pd.DataFrame(dict1)
# match_ids = getMatchIds(team_a, team_b, match_ids)
team_ids = pd.read_csv("data\\match_info_data.csv", encoding = "ISO-8859-1")
# print(team_ids)
for i in range(0, len(team_ids)):
    for x in range (i + 1, len(team_ids)):
        team_a = team_ids.loc[i, 'Team_ID']
        team_b = team_ids.loc[x, 'Team_ID']
        match_ids = getMatchIds(str(team_a), str(team_b), match_ids)

match_ids = match_ids.dropna(how ='all')
print(match_ids)
match_ids.to_csv("data\\match_ids.csv", index = False)
