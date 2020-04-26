# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:15:00 2020

@author: miquel.sarrias.ext
"""

import xarray
import json
import os

files = os.listdir(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/')


with open(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/weights.json', encoding='UTF-8') as f:
    weight = json.load(f)

all_keys = list(weight)




all_datasets = []
dsx = xarray.open_dataset(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/out_blank.nc')

for key in all_keys:
    print(key)
    new_dsx = xarray.open_dataset(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/out_'+key+'.nc')
    dsx['Band1'] = dsx['Band1'] + new_dsx['Band1']*weight[key]
    all_datasets.append(new_dsx)
    
dsx.to_netcdf(r'd:/Users/miquel.sarrias.ext/Desktop/GoSafe/datasets/pertipus/merged.nc')
