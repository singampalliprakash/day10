x=int(input("enter the number:"))
y=int(input("enter the number:"))
oper=input("enter the operator(+,-,*,%,/)")
if oper=="+":
    result=x+y
elif oper=="-":
    result=x-y
elif oper=="*":
    result=x*y
elif oper=="%":
    result=x%y
elif oper=="/":
    result=x/y
else:
    print("invalid input")
print("the answer is",result)
