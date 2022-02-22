#2 dimensional list in python

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
#using nested loops to iterate through matrix
for row in matrix:
    for item in row:
        print(item)