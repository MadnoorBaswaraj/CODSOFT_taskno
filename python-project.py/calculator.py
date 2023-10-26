print("CHOOSE ANY OPTION FROM THE CALCULATOR LIST\n 1.ADD 2.SUB 3.MUL 4.DIV")
cal=int(input("ENTER ANY CHOOSED OPTION"))
a=float(input("Enter a Value"))
b=float(input("Enter b Value"))
if cal==1:
    ADD=lambda a,b:a+b
    print("Addition is:",ADD(a,b))
elif cal==2:
    SUB=lambda a,b:a-b
    print("Substraction is:",SUB(a,b))
            
elif cal==3:
    MUL=lambda a,b:a*b
    print("Multiplication is:",MUL(a,b))
elif cal==4:
    DIV=lambda a,b:a/b
    print("Division is:",DIV(a,b))
else:
    print("Enter valid option")