arr1=set()
arr2=set()
num1=int(input("Enter length of array 1: "))
num2=int(input("Enter length of array 2: "))
print("Input arr1: ")
for i in range(num1):
    arr1.add(input("Enter value: "))
print("Input arr2: ")
for i in range(num2):
    arr2.add(input("Enter value: "))
union=arr1 | arr2
inter=arr1 & arr2
diff=arr1 - arr2
print("Union set: ")
print(union)
print("Intersection set: ")
print(inter)
print("Difference: ")
print(diff)
