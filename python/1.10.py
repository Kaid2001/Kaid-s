def add(num1,num2):
    return num1 + num2

def subtrart(num1,num2):
    return num1 -num2
    
def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0 :
        return"Error"
    else:
        return num1 / num2

def calculator():
    print("select an opration")
    print("1,add")
    print("2,subtrart")
    print("3,multiply")
    print("4,divide")

    choice = input()

    if choice == "1":
        num1=int(input("enter num1 "))
        num2=int(input("enter num2 "))
        
        print(add(num1,num2))
    
    if choice == "2":
        num1=int(input("enter num1 "))
        num2=int(input("enter num2 "))
        print(subtrart(num1,num2))
    
    if choice =="3":
        num1=int(input("enter num1 "))
        num2=int(input("enter num2 "))
        print(multiply(num1,num2))
    
    if choice == "4":
        num1=int(input("enter num1 "))
        num2=int(input("enter num2 "))
        print(divide (num1,num2))      


calculator ()