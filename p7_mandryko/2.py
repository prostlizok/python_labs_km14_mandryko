def check(text):
    while True:
        num = input(text)
        if str(num).isdigit() == True and int(num) >= 0 and int(num) <= 255:
            return num
        else:
            print("Enter a number! And between 0 and 255")

def letters(num):
    if num == 10: 
        num = "A"
    elif num == 11:
        num = "B"
    elif num == 12:
        num = "C"
    elif num == 13:
        num = "D"
    elif num == 14:
        num = "E"
    elif num == 15:
        num = "F"
    else:
        pass
    return num

def transport(num, list):
    #first letter or num
    num = int(num)/16
    num2 = round((num%1), 5)
    num = int(num - num2)
    num = letters(num)
    list.append(num)
    #second letter or num
    num2 = int(num2 * 16)
    num2 = letters(num2)
    if num2 == 0:
        list.append(0)
    else:
        list.append(num2)
    return list

colour = []
red = check("Enter red value(between 0 and 255): ")    
green = check("Enter green value(between 0 and 255): ")
blue = check("Enter blue value(between 0 and 255): ")

colour = transport(red, colour)
colour = transport(green, colour)
colour = transport(blue, colour)

print("Your colour is:", end = " ")
for i in colour:
    print(i, end = (""))