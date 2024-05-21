n1=eval(input("Enter first number\n"))
n2=eval(input("Enter second number\n"))
op=input("Choose operator: \n 1. Addition (+) \n 2. Subtraction (-) \n 3. Multiply (*) \n 4. Divide (/)")
if op=="1":
    res=n1+n2
elif op=="2":
    res=n1-n2
elif op=="3":
    res=n1*n2
elif op=="4":
    res=n1/n2
else:
    print("Invalid Operator")
print("Result: "+str(res));


