def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print("Enter the required Arthemetic Operaion \n 1.Additon \n 2.Subtraction \n 3.Multiplication \n 4.Division")
choice=int(input("Chose an option"))
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if choice==1:
    print(a,"+",b,"=",add(a,b))
if choice==2:
    print(a,"-",b,"=",sub(a,b))
if choice==3:
    print(a,"x",b,"=",mul(a,b))
if choice==4:
    print(a,"/",b,"=",div(a,b))
else:
    print("Please enter valid input.")