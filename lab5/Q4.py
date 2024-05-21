row1=int(input("Number of rows in matrix 1:"))
col1=int(input("Number of columns in matrix 1:"))
mat1=[]
for i in range (row1):
    a1=[]
    for j in range (col1):
        inp1=int(input("Enter element: "))
        a1.append(inp1)
    mat1.append(a1)

print("The entered matrix is: \n");
for i in range (row1):
    for j in range (col1):
        print(mat1[i][j], end=" ")
    print("\n")


row2=int(input("Number of rows:"))
col2=int(input("Number of columns:"))
    
mat2=[]
for i in range (row2):
    a2=[]
    for j in range (col2):
        inp2=int(input("Enter element: "))
        a2.append(inp2)
    mat2.append(a2)

print("The entered matrix is: \n");
for i in range (row2):
    for j in range (col2):
        print(mat2[i][j], end=" ")
    print("\n")

if row1!=row2 or col1!=col2:
    print("These matrices cannot be added")
else:
    res=[]
    for i in range(row1):
        ares=[]
        for j in range(col1):
            ares.append(0)
        res.append(ares)
    for i in range (row1):
        for j in range(col1):
            res[i][j]=mat1[i][j]+mat2[i][j]

    for i in range (row1):
        for j in range(row2):
            print(res[i][j], end=" ")
        print()

