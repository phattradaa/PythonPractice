import matplotlib.pyplot as plt

#Create Graph 
product1 = [10,20,30,40,50]
product2 = [15,30,10,20,60]
month = [1,2,3,4,5]
plt.plot(month,product1)
plt.plot(month,product2)
plt.show()

#XLabel and YLabel 
plt.xlabel("Month")
plt.ylabel("Sale")