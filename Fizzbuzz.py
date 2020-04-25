number = (input("Select a number between 1 and 100: "))
number = int(number)
x = range(1, number+1)
for number in x:
    if (number % 3) == 0 and (number % 5) == 0:
        print("fizzbuzz")
    elif (number % 3) == 0:
        print("fizz")
    elif (number % 5) == 0:
        print("buzz")
    else:
        print(number)

