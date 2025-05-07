one = "addition"
two = "subtraction"
three = "multiplication"

print("Hello and welcome to Patrick's calculator")

calc = input("which function would you want to perform (addition, subtraction or multiplication): \n")

if calc == one:
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    result = num_1 + num_2
    print("The answer is " + result)
elif calc == two:
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    result = num_1 - num_2
    print("The answer is " + result)
elif calc == three:
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    result = num_1 * num_2
    print("The answer is " + result)
else:
    print("Not programmed for this")