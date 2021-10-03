age = float(input("Enter dog's age!"))
if age <= 2 and age > 0:
    print("Humans age is:", age*10.5)
elif age > 2:
    print("Humans age is:", 21 + (age-2)*4)
else:
    print("Error")