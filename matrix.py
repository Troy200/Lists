num=[[1,2,3],[4,5,6],[7,8,9]]
print(num)
#number of rows
l=len(num)
print(l)
#number of coloms
print(len(num[0]))

print(num[0][2])

for i in range (3):
    for j in range(3): 
        print(num[i][j], end= " ")
    print("\n")

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

C=[[0,0],[0,0]]
D=[[0,0],[0,0]]

for x in range (2):
    for y in range(2): 
       C[x][y]= A[x][y]+B[x][y]
       D[x][y]= B[x][y]-A[x][y]



for x in range (2):
    for y in range(2): 
        print(C[x][y], end= " ")
    print("\n")


for x in range (2):
    for y in range(2): 
        print(D[x][y], end= " ")
    print("\n")