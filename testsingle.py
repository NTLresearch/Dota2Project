import dota2api
import pprint
import pandas as pd
import numpy as np
import os

os.getcwd()
api = dota2api.Initialise("8AC9317F6C4C6AA98EECEC8638314A11")

pd.set_option('display.expand_frame_repr', False)

match = api.get_match_details(match_id=3979702213)

p1 = match['players'][1]
type(p1)
#
# data need to collect:
# 1. assists
# 2. denies
# 3. gold_per_min
# 4. hero_healing
# 5. hero_damage
# 6. tower_damage
# 7. xp_per_min




pp = pprint.PrettyPrinter(depth=6)
pp.pprint(match)
pprint(match)


pp.pprint(match['players'][1])

match['radiant_name']
match['tower_status_radiant']
