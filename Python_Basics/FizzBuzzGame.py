n = input("Enter a number : ")
while n != 0:
    for i in range(1, n + 1):
        if (i / 3) * 3 == i and (i / 5) * 5 == i:
            print("FizzBuzz")
        elif (i / 3) * 3 == i:
            print("Fizz")
        elif (i / 5) * 5 == i:
            print("Buzz")
        else:
            print(i)
    n = input("Enter a number : ")

