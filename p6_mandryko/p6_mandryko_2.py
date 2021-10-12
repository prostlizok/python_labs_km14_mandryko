dict = {"Newfoundland" : "A",
"Nova Scotia" : "B",
"Prince Edward Island" : "C",
"New Brunswick" : "E",
"Quebec" : ["G", "H", "J"],
"Ontario" : ["K", "L", "M", "N", "P"],
"Manitoba" : "R",
"Saskatchewan" : "S",
"Alberta" : "T",
"British Columbia" : "V",
"Nunavut" : "X",
"Northwest Territories" : "X",
"Yukon" : "Y"}

index1 = []   

while True:
    index1 = input("Введіть почтовий індекс(B2b): ")
    if len(index1) != 3:
        print("Length error")
    elif index1[0].isalpha() == False or index1[2].isalpha() == False:
        print("Digit error")
    elif index1[1].isdigit() == False:
        print("Num error", index1[1])
    else:     
        break 

if index1[1] == "0":
     a = "села"
else:
    a = "міста"

for k, v in dict.items():
    if isinstance(v, list) == True:
        for i in v:
            if i == index1[0].upper():
                print(f"{index1} - індекс {a} {k}")
    else:
        if v == index1[0].upper():
            print(f"{index1} - індекс {a} {k}")

