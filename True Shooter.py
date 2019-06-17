import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression




LTPA = float(input('Enter 2PA: '))
TPA = float(input('Enter 3PA: '))
FT = float(input('Enter FTM: '))
FTA = float(input('Enter FTA: '))

FTP = FT / FTA
TPAr = TPA / (LTPA + TPA)
        
        
TPP = float(input('Enter 3P%: '))
if TPP > 1:
    while TPP > 1:
        print('Please enter 3P% as decimal')
        TPP = float(input('Enter 3P%: '))
        

FGP = float(input('Enter FG%: '))
if FGP > 1:
    while FGP > 1:
        print('Please enter FG% as decimal')
        FGP = float(input('Enter FG%: '))


eFGP = float(input('Enter eFG%: '))
if eFGP > 1:
    while eFGP > 1:
        print('Please enter eFG% as decimal')
        eFGP = float(input('Enter eFG%: '))
        
        
TS = float(input('Enter TS%: '))
if TS > 1:
    while TS > 1:
        print('Please enter TS% as decimal')
        TS = float(input('Enter TS%: '))
        



for i in range(1, 30):
    v = (TPP + TPA * math.sqrt(FGP) * (eFGP**2) * (TPAr**2) +
              (eFGP) * 1.67 * (math.sqrt(TPP) * (TS**2) * LTPA) +
                  (1.67 * TPA * math.sqrt(TPP) / ((i) * TPAr)) -
                  ((i) - (TS**2)) +
                  (math.sqrt(FT) * math.sqrt(TS) * 1.67 * math.sqrt(FTP + math.sqrt(FTA))) -
                  ((i) + (TPP**2)))
    if v > v:
        v = v
   


Ws = 0.6362561763846726 + (v * 0.0037882819270565235)

print(Ws)
        


        

        
    























