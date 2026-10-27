x = 3
y = 2

x += 3
y *= 2

result = x/y 
print (result)


a = 10
b = 4
c = 5

cond1 =  a > b

cond2 = (b % 2 == 0)

cond3 = c <= a
final_condition = cond1 or (cond2 and cond3)

print(final_condition)


score = int(input("Enter your test score(0-100)"))

if score >= 90:
     grade = "A"
elif score >= 80:
     grade = "B"
elif score >= 70:
     grade = "C"
elif score >= 60:
    grade = "D"
else:
     grade = "F"



num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

operation = input("Enter an operation (+, -, *, /): ").strip()

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation selected."

print("Result:", result)






