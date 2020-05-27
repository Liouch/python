def say_hello(name):
    return "Hello {0}!".format(name)

def main():
    hello_nina = say_hello(name="Nina")
    print(hello_nina)

if __name__ == "__main__":
    main()