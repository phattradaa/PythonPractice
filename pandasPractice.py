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
# print(ps['grapes']) # 50
# print(ps['banana']) #20 
# print(ps[2]) #30

#Slice Series Data 
a = pd.Series([10,20,30,40,50,60,70,80,90,100])
# print(a[1:8]) #20,30,40,50,60,70,80
# print(a[:3]) #10,20,30

#Dataframe
df_ls = pd.DataFrame(data_ls)
df_tp = pd.DataFrame(data_tp)
# print(df_ls)
# print(df_tp)
data_1 = [15,20,23,30]
cols_1 =['Age']
# print(pd.DataFrame(data_1,columns=cols_1))


#Create DataFrame from a lot of dimension List 
data_2 = [
    ['Keyboard','Computer Widget',1200]
    ,['Dolls','Toys',900],
    ['Iphone12','Telephone','300000']]
cols_2 = ['Product Name','Category','Price']
# print(pd.DataFrame(data_2,columns=cols_2))


#Create DataFrame from zip 
name = ['Keyboard','Dolls','Iphone12']
category = ['Computer Widget','Toys','Telephone']
price = [1200,900,30000]
data_2_1 = list(zip(name,category,price))
# print(pd.DataFrame(data_2_1,columns=cols_2))


#Create DataFrame from Dictionnary 
data_3 = [{'name':'Keyboard','category':'IT','price':1200},
          {'name':'Dools','category':'Toys','price':900},
          {'name':'Iphone12','category':'IT','price':30000}]
# print(pd.DataFrame(data_3))

#Create DataFrame from Series
name=pd.Series(name)
category=pd.Series(category)
price=pd.Series(price)
frame={'Name':name,'Category':category,'Price':price}
a = pd.DataFrame(frame)

#Sent CSV (DataFrame.to_csv(ตำแหน่งไฟล์,attribute))
a.to_csv("product.csv",header=True,index=False) 
a.to_csv("product2.csv",header=False,index=True)

#Read CSV (pd.read_('ตำแหน่งไฟล์',encoding='utf-8'))
c = pd.read_csv('product.csv')
#print(c)
c = pd.read_csv('product.csv',usecols = ['Name','Category'],index_col='Name')
#print(c)
cols=['Name','Price','Category']
c2 = pd.read_csv('product2.csv',names=cols)
#print(c2)

#DataFrame From Excel (pd.read_excel('ตำแหน่งไฟล์','ชื่อ sheet'))
dataupdate = pd.re