import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("107940251.csv")

data.columns.values


primary_attr = pd.get_dummies(data['primary_attr'])
attack_type = pd.get_dummies(data['attack_type'])
data = pd.concat([data, primary_attr,attack_type], axis=1)

kda = (data['kills'] + data['assists'])/data['deaths']
kdr = data['kills']/data['deaths']

x = len(data.columns.values)
x

data.insert(39, 'kda', kda)
data.insert(40, 'kdr', kdr)
data.kdr[data.deaths==0] = data.kills[data.deaths==0]/1
data.kda[data.deaths==0] = (data.kills[data.deaths==0] + data.assists[data.deaths==0])/1

total = len(data)
win = len(data[data['Results']==1])
win_pct = round(win/total,3)

radiant_wins = data['radiant_win'].value_counts()
radiant_wins

plt.figure()
plt.subplot(2,3,1)
sns.boxplot(y=data['duration']/60.0)
sns.boxplot(y=data['kills'])
sns.boxplot(y=data['assists'])

data[['kills', 'kdr', 'kda', 'assists']].describe()

played_hero = data['localized_name'].unique()
len(played_hero)

hero = data.groupby('localized_name')
hero_winloss = hero['Results'].mean().sort_values(ascending=False)
hero_winloss[:5]

hero_mostplayed = data['localized_name'].value_counts().sort_values(ascending=False)
most_played20 = hero_mostplayed[:21]
most_played20.index

wl20 = hero_winloss[most_played20.index]
plt.figure(figsize=(18,8))
ax = sns.barplot(y=most_played20.index, x=wl20, orient="h")

sns.barplot(y=most_played20.index, x=most_played20)

most_played20_kdr = data.groupby('localized_name')['kdr'].mean()[most_played20.index]
sns.barplot(y=most_played20.index, x=most_played20_kdr)

most_played20_kda = data.groupby('localized_name')['kda'].mean()[most_played20.index]
sns.barplot(y=most_played20.index, x=most_played20_kda)

primary_attr = data['primary_attr'].value_counts().reindex(['agi', 'str', 'int'])
primary_attr
attr_pal = ['green', 'blue', 'red']
sns.barplot(x=primary_attr.index, y=primary_attr, palette=attr_pal)

prm_wl = data.groupby('primary_attr')['Results'].mean().reindex(['agi', 'str', 'int'])
prm_wl

sns.barplot(x=prm_wl.index, y=prm_wl, palette=attr_pal)

prm_kda = data.groupby('primary_attr')['kda'].mean()
sns.barplot(x=prm_kda.index, y=prm_kda, palette=attr_pal)

attack_type = data['attack_type'].value_counts()
attack_type
sns.barplot(x=attack_type.index, y=attack_type)

at_wl = data.groupby('attack_type')['Results'].mean()
at_wl
sns.barplot(x=at_wl.index, y=at_wl)

at_kda = data.groupby('attack_type')['kda'].mean()
sns.barplot(x=at_kda.index, y=at_kda)

### duration

win_duration = data['duration'][data['Results']==1]/60.0
win_duration
sns.distplot(win_duration, bins=20)


loss_duration = data['duration'][data['Results']==0]/60.0
sns.distplot(loss_duration, bins=20)


duration_wl = data.groupby('duration')['Results'].mean()
duration_wl

duration_lin = np.linspace(data['duration'].min(), data['duration'].max(), num=len(duration_wl))
plt.plot(duration_lin, duration_wl)

hourly_wl = data.groupby('hour')['Results'].mean()
sns.barplot(x=hourly_wl.index, y=hourly_wl)


sns.distplot(data['hour'][data['Results']==1], bins=24, kde=False)

sns.distplot(data['hour'][data['Results']==0], bins=24, kde=False)

### year
govt = data['year'].value_counts()
govt
sns.barplot(x=govt.index, y=govt)

govm = data['month'].value_counts()
sns.barplot(govm.index, govm)
