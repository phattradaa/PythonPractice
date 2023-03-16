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
dataupdate = pd.read_excel('dataupdate.xlsx','weather',index_col='Day')
#print(dataupdate)

#Examine DataFrame
#print(dataupdate.head()) # 5แถวแรก 
#print(dataupdate.head(n)) อ่าน n แถวแรก 
#print(dataupdate.tail(10)) #อ่าน 10 สุดท้าย 
#print(dataupdate.sample(7)) #สุ่มข้อมูล 7 แถว 
#print(dataupdate.describe()) #count,mean,std,min,25%,50%,75%,max
#print(dataupdate.shape) #row 30,col 3 
#print(dataupdate.columns) #column
#print(dataupdate.values) #values

#Choose column and range of data 
#print(dataupdate.WindSpeed[1:3]) #printข้อมูลdataupdate หัวข้อ windSpeed ตั้งเเต่ 1-2
#print(dataupdate[['Day','Event'][1:10]])#printข้อมูลหัวข้อ day,event ตั้งเเต่ 1-9 
#print(dataupdate[2:12]) #printตั้งเเต่ 2-11 
#print(dataupdate[0:3].Event) #print 0-2 just event
#print(dataupdate.loc['2020-12-03':'2020-12-15']['Event']) #print event ตั้งเเต่วันที่ 3 - 15 ธันวา

#Find Data
#print(dataupdate[dataupdate.Event.str.match('แดดร้อน')]) #เช้ควันที่มีแดดร้อน 
#print(dataupdate[dataupdate.Event.str.contains('น')]) #เช้ควันที่มี event ตัว น

#Loop For 
#for idx , row in dataupdate.iterrows():
    #print("{} Temperature : {} ส่งผลให้เกิด {}".format(idx,row.Temperature,row.Event))

#Condition Choose
#print(dataupdate[dataupdate.Temperature<=20]) print วันที่อุณหภูมิ <= 20
#print(dataupdate[dataupdate.Event=='แดดร้อน']) print วันที่แดดร้อน 
#print(dataupdate.loc[(dataupdate.Event=='ฝนตก') & (dataupdate.Temperature <=25)]) print วันที่ฝนตกและอุณหภูมิ <= 25 

#Isin Function 
#print(dataupdate.loc[(dataupdate.Temperature == 18) | (dataupdate.Temperature == 20) | (dataupdate.Temperature == 25)])
# กรองให้เลือก temp = 18,20,35
#print(dataupdate.loc[dataupdate.Temperature.isin([18,20,25])]) ลดรูปจากด้านบน

#Sort Index
stock = pd.read_excel('Stock.xlsx','แผ่น1',index_col='Name')
sort1 = stock.sort_index() #เรียงตามพยัญชนะ
sort2 = stock.sort_index(ascending=False) #False -> เรียงสระไปพยัญชนะ ไทยไปอังกฤษ True -> เรียงพยัญชนะไปสระ อังกฤษไปไทย 
#print(sort2)

#Sort by value 
stock.sort_values('Amount',ascending=True,inplace=True)
#ascending True -> less to more False -> more to less 
#inplace แทนค่าทับ 

#Add Column 
#stock["delivery"]=100
#stock["total"] = stock["Price"]+stock["delivery"]
#print(stock)

#Change Column Name 
cols={'WindSpeed':'แรงลม'}
dataupdate.rename(columns=cols,inplace=True)
#print(dataupdate)
cols={'แรงลม':'WindSpeed'}
dataupdate.rename(columns=cols,inplace=True)
#print(dataupdate)

#Delete Column 
#Delete and don't effect to DataFrame 
dataupdate.drop('Temperature',axis=1,inplace=True)
#Delete and effect to DataFrame 
#dataupdate.drop('WindSpeed',axis=1,inplace=True)    axis =1(by columns) axis =0(by rows)
#print(dataupdate)

#Add Rows 
products = [['หูฟัง',1500,'อุปกรณ์คอม'],['สายชาร์จ',500,'อุปกรณ์คอม']]
cols = ['Name','Price','Category']
newdata = pd.DataFrame(data=products,columns=cols)
newdata.set_index('Name',inplace=True)
#stock = stock.append(newdata)
#print(stock)

#Delete Row by Index (DataFrame )
#print(a)
#print(a.drop(0,axis=0))

#Delete Row by Keys 
#print(stock)
#row = "หูฟัง"
#stock.drop(row,axis=0,inplace=True)
#print(stock)

#Sum of column and row 
#print(stock.sum(axis=1))
stock["total"] = stock["Price"] * stock["Amount"]
#print(stock)
#print(stock.sum())

#Missing Value isnull and notnull
employee = pd.read_excel("Employee.xlsx",index_col="Name")
#print(employee.isnull())
#print(employee.isnull().any())
#print(employee.isnull().sum())
#print(employee.notnull())
#print(employee.notnull().any())
#print(employee.notnull().sum())


