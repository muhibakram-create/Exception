try:
    n = int(input("Enter a number."))
except ValueError:
    print("Invalid number. Try again")
else:
    print("Valid number. Good job.")