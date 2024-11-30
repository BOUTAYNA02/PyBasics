for i in range(1, 1000):
    year = int(input("Enter a year: "))

    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        print(f"{year} is not a leap year")
    elif year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
