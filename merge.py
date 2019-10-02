# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:43:29 2019

@author: dyrakesh
"""

import pandas as pd

job = pd.read_excel("job.xlsx")

ret = pd.read_excel("ret.xlsx")

sch = pd.read_excel("sch.xlsx")

Groupsch = pd.merge(job,sch, on='Group')  #did merge on Group to get sch and group details.

Groupsch.to_csv('Groupsch.csv')

newret = pd.read_excel('newret.xlsx') #Copied retention from the grid to get the values of group and sch and retention

Groupschret = pd.merge(Groupsch,newret,on='Group')

df = Groupschret.Retention


df1 = Groupschret.Retention
j = 0
for i in df : 
    df1.iloc[j] = i[1:]
    j = j+1
    
#print(df1)
Groupschret.Retention = df1
Groupschret.to_csv('Groupschret.csv')

Groupschret = pd.read_csv('Groupschret.csv')

final = pd.merge(Groupschret,ret, on='Retention')

final.to_csv('final.csv')

final.columns

final1 = final.drop(['Server_y', 'Sub Name', 'Domain Name_y','Schedule_y',
                     'Calendar Hours','Enabled_x','Schedule Start Time',
                     'Time Zone','Type', 'Domain', 'Disabled','clinets',
                     'Server', 'Domain Name', 'Enabled_y', 'Read Only',
       'Expiration Date',  'Override',
       'Num Days Daily Kept', 'Num Weeks Weekly Kept',
       'Num Months Monthly Kept', 'Num Years Yearly Kept'],axis=1)
    
final1.to_csv('awsome.csv')


