print("Hello! This is a unit converter (kms to miles)")


while True:
    km = input("Kilometers: ")
    km = float(km.replace(",", "."))
    miles = km * 0.621371

    print("{} kilometers is {} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")
    if choice.lower() != "y" and choice.lower() != "yes":
       break



