a=int(input("Enter number1:"))
b=int(input("Enter number2:"))

print("1:Add")
print("2:Sub")
print("3:Mul")
print("4:Div")
choice=int(input("Enter any choice for operations:"))

if choice==1:
    print("Sum:",a+b)
elif choice==2:
    print("Sub:",a-b)
elif choice==3:
    print("Mul:",a*b)
elif choice==4:
    print("Div:",a/b)
else:
    print("Error!")