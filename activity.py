try:
    number= int(input("Please enter the divisor."))
    number2 = int(input("Please enter the dividend."))
except ValueError:
    print("Invalid number. Try adding actual numbers.")
except ZeroDivisionError:
    print("You can't divide a number by 0. The value is undefined")
except:
    print("I don't know what happened. But, it was something wrong.")
else:
    print("The result is:", int(number2/number))
finally:
    print("this will be printed whatever happens in the code")