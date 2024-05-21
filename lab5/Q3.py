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

res=[]
resrow=row1
rescol=col2
for i in range(resrow):
    ares=[]
    for j in range(rescol):
        ares.append(0)
    res.append(ares)

for i in range (resrow):
    for j in range(rescol):
        for k in range(row2):
            res[i][j]+=mat1[i][k]*mat2[k][j]

print("Resultant matrix is: ")
for i in range (resrow):
    for j in range (rescol):
        print(res[i][j], end=" ")
    print("\n")

