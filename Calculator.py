user_name = input("Welcome to our calculator, What\'s your name?: ")
user_number1 = input("Type the first number " + user_name + ": ")
user_number2 = input("Type the second number " + user_name + ": ")
operation = input("What would like to do? (+,-,*, /)?: ")

if operation == "+":
    print(float(user_number1)+float(user_number2))
elif operation == "-":
    print(float(user_number1)-float(user_number2))
elif operation == "*":
    print(float(user_number1)*float(user_number2))
elif operation == "/":
    print(float(user_number1)/float(user_number2))
else:
    print("We don\'t support that opperation yet " + user_name)

print("Thank you for using my mega perfect calculator " + user_name)

