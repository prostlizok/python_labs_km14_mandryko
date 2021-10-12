def check(l):
    for i in range(len(l)):
        l[i] = l[i].lower()
        if l[i].isalpha() == False or len(l[i]) > 1:         
            return 1

while True:
    list1 = input("Введіть першу множину літер: ").split(" ")
    if check(list1) == 1:
        print("Треба вводити тільки літери і тільки по одній")
    else:
        break
while True:
    list2 = input("Введіть другу множину літер: ").split(" ")
    if check(list2) == 1:
        print("Треба вводити тільки літери і тільки по одній")
    else:
        break

set1 = set(list1)
set2 = set(list2)

print("Літери першої фрази:", end = " ")
print(*list1, end = ", ")
print("літери другої фрази:", end = " ")
print(*list2, end = ". ")
if set2 == set1 & set2:
    print("З першого речення можна скласти друге речення")
else:
    print("З першого речення не можна скласти друге речення")




