for i in range(1, 1000):
    year = input("Enter a year: ")
    if (year / 400) * 400 == year:
        print(f"{year} is a leap year")
    elif (year / 100) * 100 == year:
        print(f"{year} is not a leap year")
    elif (year / 4) * 4 == year:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
