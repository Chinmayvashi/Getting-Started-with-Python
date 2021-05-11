print("Chinmay's Calculator")
print("--------------------------------------------------------------------------------")
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))
print(" ")
op = (input("Enter Operations[+,-,*,/,%,FOR ALL OPERATIIONS PRESS a ]: "))
if op =="+":
    result=num1+num2
elif op =="-":
    result=num1-num2
elif op =="*":
    result=num1*num2
elif op =="/":
    result=num1/num2
elif op =="%":
    result=num1%num2
else:
    print("invalid operator")
print(" ")
print('Num1  op Num2  result')
print("---------------------------------------------------------------------------------")
print(num1,  op,  num2, "=",  result)
