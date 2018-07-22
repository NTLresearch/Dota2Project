import pandas as pd
import numpy as np
import dota2api
import os


os.chdir("/Users/thanhuwe8/Google Drive/Project/Dota2Project/Data/")

api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")

her = api.get_heroes()
heroes = []
id = []

for i in range(0, len(data)):
    temp_hero = data[i]['localized_name']
    temp_id = data[i]['id']
    heroes.append(temp_hero)
    id.append(temp_id)

hero_raw = pd.DataFrame({"localized_name":heroes, "id":id})
hero_raw = hero_raw.sort_values(by=['id'])

heroes_old = pd.read_csv("dota_hero_stats.csv")
result = pd.merge(heroes_old, hero, on='localized_name')

result.to_csv("dota_hero_stats_2.csv")
