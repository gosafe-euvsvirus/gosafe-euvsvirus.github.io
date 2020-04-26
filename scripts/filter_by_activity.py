# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:49:22 2020

@author: miquel.sarrias.ext
"""

import pandas

df = pandas.read_csv(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/2019_censcomercialbcn_detall.csv')

df = df[['Nom_Principal_Activitat',
       'Nom_Sector_Activitat', 'Nom_Grup_Activitat',
       'Nom_Activitat', 'Nom_Local',
       'X_UTM_ETRS89', 'Y_UTM_ETRS89', 'Latitud',
       'Longitud']]

act = list(set(list(df['Nom_Activitat'].values)))

ens_quedem_amb = [
'Farmàcies PARAFARMÀCIA',
'Peix i marisc',
'Pa, pastisseria i làctics',
'Fruites i verdures',
'Carn i Porc',
'Herbolaris, dietètica i NUTRICIÓ',
'Tabac i articles fumadors',
'Autoservei / Supermercat',
'Ous i aus',
'Llibres, diaris i revistes',
'Grans magatzems i hipermercats']

dfs_selec = []
for sector in ens_quedem_amb:
    dfs_selec.append(df[df['Nom_Activitat']==sector])

df_2 = pandas.concat(dfs_selec)

df_2.to_csv(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/censcomercial_filtrat.csv')


