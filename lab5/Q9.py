arr1=[]
num=int(input("Enter number of elements: "))
for i in range(num):
    arr1.append(input("Enter element: "))
rev=[]
rev=arr1[::-1]
print(rev)
for i in range (num):
    if arr1[i]==rev[i]:
        flag=0
    else:
        flag=1
        break
if flag==0:
    print("Palindrome")
else:
    print("Not a palindrome")
