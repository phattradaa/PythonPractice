import pandas as pd 
import numpy as np 

#Create Series from pandas
data_ls = [10,20,'spy',15.05,'papaya']
data_tp = (10,20,'spy',15.05,'papaya')
ps=pd.Series(data_ls)
pl=pd.Series(data_tp)
# print(ps)
# print(pl)

#Create Series from numpy 
ndata = np.array(data_ls)
# print(ndata)

#Create Series and determine index 
items = ['grapes','banana','papaya']
idx = [50,20,30]
ps=pd.Series(items,index=idx)
# print(ps)

#Create Sereis from Dictionary 
data = {'grapes':50,'banana':20,'papaya':30} 
ps = pd.Series(data)
# print(ps)

#การเข้าถึงข้อมูลใน series 
print(ps['grapes'])
print(ps['banana'])
print(ps[2])
