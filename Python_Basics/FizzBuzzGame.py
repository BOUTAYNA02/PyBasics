n = int(input("Enter a number : "))
while n != 0:
    for i in range(1, n + 1):
        if int(i / 3) * 3 == i and int(i / 5) * 5 == i:
            print("FizzBuzz")
        elif int(i / 3) * 3 == i:
            print("Fizz")
        elif int(i / 5) * 5 == i:
            print("Buzz")
        else:
            print(i)
    n = int(input("Enter a number : "))

