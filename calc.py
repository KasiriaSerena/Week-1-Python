num1 = int(input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
operator = input("Enter an operator: ")

if(operator == "+"):  
        output = num1 + num2 
elif(operator == "-"):
        output = num1 - num2
elif(operator == "*"):
        output = num1 * num2
elif(operator == "/"):
        output = num1 / num2
else:
      print("Invalid input!")
    

print(f"{num1} {operator} {num2} = {output}")