replace1=""
num1=int(input("Enter a number1:"))

num2=int(input("Enter a number2:"))

print("These are the operators you can use")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
result=0
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=="1":
    result=num1+num2
    print("The result of addition of",num1,"and",num2,"is",result)
if operator=="2":
    if num1<num2:
     print("cannot subtract because the First number is less than the Second number")
    else:
     result=num1-num2
    print("The result of subtraction of",num1,"and",num2,"is",result)
if operator=="3":
    if num2==0 or num1==0:
           print("cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of Multiplication of",num1,"and",num2,"is",result)
if operator=="4":
    if num2==0:
        print("Cannot divide by zero")
    else:
        result=num1//num2
        print("The result of Division of",num1,"and",num2,"is",result)
if operator=="5":
    replace1="Modulus"
    result=num1%num2
    print("The Result of",replace1,"of",num1,"and",num2,"is",result)
