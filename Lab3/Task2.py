import numpy as np

arr=np.random.randint(1,100,35)
a1 = arr.reshape(5, 7)
print("5X7:")
print(a1)

arr2=np.random.randint(1,100,9)
a2=arr2.reshape(3, 3)
print("3X3:")

print( a2)

arr3=np.random.randint(1,100,28)
a3=arr3.reshape(4, 7)
print("4X7:")
print( a3)