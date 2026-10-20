valid= False
while valid== False:
    try:
        number= int(input("What is the number?"))
    except:
        print("Invalid number. Try again.")
    else:
        print("Thank you")
        valid= True