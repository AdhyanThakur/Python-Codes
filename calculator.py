num1=int(input("enter the number 1:"))
operator=input("enter the operator(+,-,*/):")
num2=int(input("enter the number 2:"))

if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    if num2!=0:
        result=num1/num2
    else:
        result="invalid input"                
else:
    print("invalid operator")
print("result:",result)            