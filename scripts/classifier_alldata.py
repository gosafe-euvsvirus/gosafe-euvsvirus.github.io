# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:21:06 2020

@author: miquel.sarrias.ext
"""

import pandas

df = pandas.read_excel(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/nets/alldata.xlsx')

act = list(set(list(df['element'].values)))

dfs_selec = []
for i in act:
    dfs_selec.append(df[df['element']==i])

for i in range(len(dfs_selec)):
    dfs_selec[i].to_csv(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/'+act[i]+'.csv')