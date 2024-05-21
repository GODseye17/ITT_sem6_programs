def DecimaltoBinary(x):
    if x>=1:
        DecimaltoBinary(x//2)
    print(x%2, end='')
def DecimaltoOctal(n):
    octal = [0] * 100
    i = 0
    while (n != 0):
        octal[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octal[j], end="")
def DecimaltoHexa(x):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
                    13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = '' 
    while(x > 0): 
        remainder = x % 16
        hexadecimal = conversion_table[remainder] + hexadecimal 
        x = x // 16
    print(hexadecimal)
    
num=int(input("Enter decimal number: "))
ch=int(input("Enter your choice: \n 1. Binary \n 2. Octal \n 3. Hexadecimal \n"))
if ch==1:
       DecimaltoBinary(num)
elif ch==2:
    DecimaltoOctal(num)
elif ch==3:
    DecimaltoHexa(num)
else:
    print("Invalid Input")
