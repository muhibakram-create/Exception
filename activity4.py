try:
    number= int(input("Enter a number."))
    while number%2 == 0:
        print("Number is even")
        number= int(input("Enter a number."))
except:
    print("Invalid number")
