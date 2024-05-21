def sumofn(x):
    if (x==1):
        return x
    else:
        return x+sumofn(x-1)
n=int(input("Enter a natural number: "))
print(sumofn(n))
