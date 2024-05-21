row=int(input("Number of rows:"))
col=int(input("Number of columns:"))
mat=[]
for i in range (row):
    a=[]
    for j in range (col):
        inp=input("Enter element: ")
        a.append(inp)
    mat.append(a)

print("The entered matrix is: \n");
for i in range (row):
    for j in range (col):
        print(mat[i][j], end=" ")
    print("\n")

print ("Transpose: \n")
transpose=[]
row1=col
col1=row
for i in range (row1):
    a1=[]
    for j in range(col1):
        a1.append(0)
    transpose.append(a1)


for i in range(row):
    for j in range(col):
        transpose[j][i]=mat[i][j]

for i in range (row1):
    for j in range (col1):
        print(transpose[i][j], end=" ")
    print("\n")



        
