
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression


data = pd.read_csv("Seasons_Stats.csv")



shooter = data[(data['3P%'] > 0.35) &
               (data['eFG%'] > 0.55) &
               (data['3PA'] > 4.5) &
               (data['3PAr'] > 0.5) &
               (data['G'] > 30) &
               (data['OWS'] < 98) ]


               

        
x = (shooter['3P%']  + np.sqrt(shooter['FG%']) + np.square(shooter['eFG%']) + np.square(shooter['3PAr']) +
                  (1.67 * shooter['3PA'] * np.sqrt(shooter['3P%']) / (shooter['USG%'] * shooter['3PAr'])) *
                  (shooter['USG%'] / np.square(shooter['TS%'])) *
                   shooter['2P%'] * shooter['eFG%'] * np.square(shooter['3P%']) * shooter['TS%'] -
                  (shooter['FT%'] + shooter['TS%'] + shooter['USG%']))
                  


y = shooter['WS']


x2 = pd.DataFrame((shooter['USG%'] / np.square(shooter['TS%'])) *
                   (shooter['2P%'] * shooter['eFG%'] * np.square(shooter['3P%']) * shooter['TS%']) -
                  (shooter['TS%'] / np.sqrt(shooter['USG%']) + shooter['3P%']))
                  
                    
                  
                  
                  
                  


y2 = pd.DataFrame(shooter['WS'])



model = LinearRegression().fit(x2, y2)

r_sq = model.score(x2, y2)


print(r_sq)

stats = linregress(x, y)

m = stats.slope
b = stats.intercept

#print(m)
#print(b)

#plt.scatter(x,y)
#plt.plot(x, (m*x) + b, color = 'red')
#plt.xlabel('True Shooter Value')
#plt.ylabel('Win Shares')

#plt.show()








