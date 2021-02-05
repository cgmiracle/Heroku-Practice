#Documentation for library
#https://github.com/vishaalagartha/basketball_reference_scraper

#dependencies
import pandas as pd
import numpy as np
import os
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot
import scipy.stats as st
import matplotlib.pyplot as plt

# GEt stats
player_input = input("Please Enter an NBA Player: ")

player_stats = get_stats(player_input)


#Graphing 
x = (player_stats["MP"])
xx = x.dropna()
y = player_stats["FGA"]
yy = y.dropna()
plt.scatter(x, y)
plt.xlabel("Minutes")
plt.ylabel("Points")


#Linear Regression
#import scipy.stats as st
cor=round(st.pearsonr(x,y)[0],2)
print(f"The correlation between minutes and game score is {cor}")
model = st.linregress(xx,yy)

y_values = x*model[0]+model[1]
plt.scatter(x, y)
plt.plot(x,y_values,color="red")
plt.xlabel("minutes")
plt.ylabel('game score')
plt.show()



