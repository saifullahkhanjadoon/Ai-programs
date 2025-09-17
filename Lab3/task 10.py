import numpy as np
matrix=np.zeros((3, 3), dtype=int)
position=int(input("Enter a position between 1 and 9: "))
value=int(input("Enter a value : "))
row=(position-1)%3
col=(position-1)%3
matrix[row][col]=value
print("Updated Matrix:")
print(matrix)


5