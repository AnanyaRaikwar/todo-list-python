print(" Simple Calculator ")
a = float(input("Enter first number: "))
opr = input("Choose an operator (+, -, *, /, %): ")
b = float(input("Enter second number: "))
if opr == "+":
    result = a + b

elif opr == "-":
    result = a - b

elif opr == "*":
    result = a * b

elif opr == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error! Division by zero."
        
elif opr == "%":   
    result = a % b 
else:
    result = "Invalid operator"
print("Result:", result)