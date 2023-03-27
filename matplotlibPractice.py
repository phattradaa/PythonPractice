import matplotlib.pyplot as plt

# Create Graph
product1 = [10, 20, 30, 40, 50]
product2 = [15, 30, 10, 20, 60]
month = [1, 2, 3, 4, 5]
plt.plot(month, product1, color="blue", marker="o", linestyle="--")
plt.plot(month, product2, color="red", marker="s", linestyle="-.")

# XLabel and YLabel
plt.xlabel("Month", size=10, color="red")  # size , color กำหนดคุณสมบัติให้หัวข้อ
plt.ylabel("Sale", size=10, color="purple")

# Save Graph to Photo
# plt.savefig("matplot.jpg")

# Configure Title
data = {"size": 20, "color": "green"}
plt.title("Data Of Sale", {"size": 20, "color": "green"}, loc="center")

#Legend Function 
plt.legend(["product1","product2"],loc="upper right")
plt.show()
