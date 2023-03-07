import numpy as np 
# Create Array
np.array([[[1,2,3],[4,5,6]]]) #สร้าง array
np.array([1,2,3,4] ,dtype='float') #สร้าง array โดยกำหนดให้เป็น float

#Create Zero Array
np.zeros(5, dtype = 'int') #สร้าง array ที่มีค่าเป็น 0 ทั้งหมด 3 ตัว type int 
np.zeros((3,3) , dtype = 'float') #สร้าง array เลข 0 จตุรัส 3*3

#Create One Array
np.ones(5,dtype = 'int') #สร้าง array เลข 1 5 ตัว

#Create Identity matrix 
np.identity(4,dtype="int") #สร้าง array แบบ identity matrix ตำแหน่งของเลข 1 (การเฉียง) หรือ k=0
np.eye(4, k=1,dtype="int") #สร้าง array แบบ identity matrix k=1
np.eye(4,k=-1) #สร้าง array แบบ identity matrix k=-1
np.eye(3,4) #สร้าง array ที่มี 1 เรียง ในขนาด 3*4

#Create All num in array
np.full(6,10) #สร้าง array ที่มี 10 จำนวน 6 ตัว 

#Linspace
np.linspace(1,5,20,dtype="float") #สร้าง array ที่มีจำนวน 20 ตัว ตั้งเเต่ 1-5 แบบ random 
np.linspace(1,5,endpoint=False) #สร้าง array ที่มีจำนวนเเบบ random ตั้งเเต่ 1-5 แต่ไม่เอา 5 

#Arange 
np.arange(1,5) #สร้าง Array 1-4 แบบเรียง 
np.arange(-5,4) #สร้าง Array (-5) - 3 แบบเรียง 
np.arange(4,10,dtype="complex") #สร้าง Array 4-9 แบบจำนวนเชิงซ้อน
np.arange(1,20,2)

#Random
np.random.rand(10,10) 

#Attribute
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a.dtype #Type ของ Data และจำนวน bit
a.ndim #จำนวนDimension 
a.shape #ขนาด row และ column
a.size # row*column

#Slice Array 1 Dimension
b = np.arange(1,11)
b # ปริ้นอาร์เรย์ b
b[2] #ปริ้น b ตำแหน่งที่ 2
b[:] #ปริ้น b ทั้งหมด
b[2:] #ปริ้น b ตั้งเเต่ตำแหน่งที่ 2 
b[:5] #ปริ้น b ตั้งแต่แรกจนถึงตัวก่อน index=5
b[2:9:2] #ปริ้น b ตั้งเเต่indexที่ 2 ถึง 9 โดยข้ามทีละ 2 step -> (2,4,6,7,8)

#Slica 2 Array Dimension 
a[:,:] #ปริ้นทั้งหมด
a[1:,1:] #ปริ้นตั้งแต่ row ที่ 1 และ column ที่ 1 
a[:,1:] #ปริ้นrowทั้งหมดแต่ column ตั้งแต่ 1 เป็นต้นไป 
a[:2,:] #ปริ้นrowไปจนถึงก่อน index=2 และcolumn ทั้งหมด
a[::2,:] #ปริ้นทั้งหมดโดยที่ row ขยับทีละ 2

#Index Operator
a[[0,1]] #ปริ้น x ตั้งเเต่ row ที่ 0-1 
b[a[0][1]] #ปริ้น อาร์เรย์ b ที่ตำแหน่งในของ a row=0 , col=1 
b[b>5] #ปริ้นอาร์เรย์ b ที่ b>5

#Mathematics Operator 
x1=np.arange(1,5) #1 2 3 4
x1 += 2 #3 4 5 6
x1 -= 5 #-2 -1 0 1 
x1 *= 3 #-6 -3 0 3
y1=np.arange(1,5) #1 2 3 4 
x1 += y1 #-5 -1 3 7
x2=np.array([[1,2,3],[4,5,6]])
y2=np.array([[5,6,7],[7,8,9]])
x2.shape #(2,3)
y2.shape #(2,3)
x2+y2 #[[6,8,10],[11,13,15]]
y2-x2 #[[4,4,4],[3,3,3]]
x2+[2] #[[3,4,5],[6,7,8]]
# x3=np.array([[1,2]]) --> x3 ไม่สามารถ operator กับ x2 ได้เพราะว่ามี col แค่ 2 ตัว
x3=np.array([[1,2,3]])
x2+x3 #บวกกันได้เพราะมีจำนวน column เหมือนกัน x3 จะทำการ clone ตัวเองขึ้นมาอีก row เพื่อบวกกับ x2 ได้ 
#การที่ Array ที่ขนาด rowหรือcolumn ไม่เท่ากัน แต่ยังบวกกันได้ เราเรียกว่า Board Casting 

#Reshape & Resize 
c = np.arange(0,10) #[0,1,2,3,4,5,6,7,8,9]
c.reshape((2,5)) #reshape ชั่วคราวเป็น 2 row 5 col 
d = c.reshape((2,5)) #[[0,1,2,3,4],[5,6,7,8,9]]
c.resize((2,5)) #resize ถาวรเป็น 2 row 5 col #[[0,1,2,3,4],[5,6,7,8,9]]


#Flatten : แปลงarrayให้เหลือมิติเดียว แบบไม่เชื่อมต่อกันเมื่อข้อมูลเปลี่ยนแปลง
a # [[1,2,3],[4,5,6],[7,8,9]]
f = a.flatten() #[1,2,3,4,5,6,7,8,9]
f[0] = 5 #[5,2,3,4,5,6,7,8,9] #a จะไม่เปลี่ยนเมื่อ f เปลี่ยน

#Ravel : แปลงarrayให้เหลือมิติเดียวเเบบเชื่อมต่อกัน 
a # [[1,2,3],[4,5,6],[7,8,9]]
e = a.ravel() #[1,2,3,4,5,6,7,8,9]
e[0] = 5 #[5,2,3,4,5,6,7,8,9] # a จะเปลี่ยนตาม
a #[5,2,3,4,5,6,7,8,9]

#Transpose 
a = np.array([[1,2,3],[4,5,6]]) #row2 * col3 
a.transpose() #row3 * col2 แบบไม่ถาวร 

#Statistic Operator 
#1 Dimension
b # [1,2,3,4,5,6,7,8,9,10]
b.sum() # ผลบวกของทั้งarray 
b.prod() # ผลคูณของทั้งarray
b.mean() # ค่าเฉลี่ย
b.min() #ค่า min
b.max() #ค่า max 
b.argmin() #return ตำแหน่งของค่าmin
b.argmax() #return ตำแหน่งของค่าmax 
#2 Dimension
a # [[1,2,3],[4,5,6]]
np.min(a,axis=1) #หาค่า min ใน array แนวนอน
np.max(a,axis=0) #หาค่า max ใน array แนวตั้ง 

#Dot product 
a1 = np.array([[1,2],[3,4]])
a2 = np.array([[11,12],[13,14]])
a3 = a1.dot(a2)

#Concatenate & Append
a.flatten() #[1,2,3,4,5,6]
a4 = np.arange(11,15) #[11,12,13,14]
a5 = np.concatenate((a.flatten(),a4)) #[1,2,3,4,5,6,11,12,13,14]
a6 = np.append(a.flatten(),100)  #[1,2,3,4,5,6,100]
a # [[1,2,3],[4,5,6]]
np.append(a,[[10],[20]],axis=1) #[[1,2,3,10],[4,5,6,20]]

#Insert 1 Dimension Array 
arr = np.arange(1,11) #[1,2,3,4,5,6,7,8,9,10]
np.insert(arr,1,100) #[1,100,2,3,4,5,6,7,8,9,10]
np.insert(arr,(1,3),100) #[1,100,2,3,100,4,5,6,7,8,9,10]

#Insert 2 Dimension Array 
arr2 = np.array([[1,2],[3,4]])
np.insert(arr2,1,100,axis=0) #[[1,2],[100,100],[3,4]]
np.insert(arr2,1,100,axis=1) #[[1,2,100],[3,4,100]]
np.insert(arr2,1,[10,20],axis=0) #[[1,2],[10,20],[3,4]]

#Delete
arr #[1,2,3,4,5,6,7,8,9,10]
np.delete(arr,3) #ลบ index ที่ 3 [1,2,3,5,6,7,8,9,10]
arr = np.arange(1,13) #[1,2,3,4,5,6,7,8,9,10,11,12]
arr = arr.reshape(4,3) #[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
np.delete(arr,2,axis=1) #[[1,2,3],[4,5,6],[10,11,12]]

#Split 
arr3 = np.arange(1,21) #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(np.split(arr3,4))
arr3=arr3.reshape(5,4)
print(arr3)
print(np.hsplit(arr3,4)) #horizontol split ออกเป็น 4 ชุด 
print(np.vsplit(arr3,5))#verticol split ออกเป็น 5 ชุด