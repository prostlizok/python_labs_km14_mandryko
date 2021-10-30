from math import sqrt

print("Введіть індекси квадратного рівняння(типу ax^2 + bx + c = 0)")
x1 = "-"
x2 = "-" #because of output

#letter check
def check(a):
    while True:
        try:
            format_string = "Введіть {}: "
            num = float(input(format_string.format(a)))
            return num
        except ValueError as ve:
            print("Помилка:", ve)
            print("Треба вводити числа!")

a = check("a")
b = check("b")
c = check("c")

#0 check
if a != 0 and b != 0 and c != 0:
    D = b**2 - 4*a*c 
    try:
        if D>=0:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
        elif D<0:
            raise Exception("Дискримінант менше нуля!")
    except Exception as exc:
        print("Рівняння не має коренів.", exc)
        exit()
elif a == 0 and b == 0:
    try:
        if c == 0:
            x1 = "R"
        else:
            raise Exception(f"Рівняння не має коренів, бо {c} не може дорівнювати нулю.")
    except Exception as exc:
        print(exc)
        exit()
elif a == 0:
    x1 = (-c)/b
elif b == 0:
    try:
        x1 = sqrt((-c)/a)
        x2 = -(sqrt((-c)/a))
    except Exception as exc:
        print("Помилка:", exc)
        exit()
elif c == 0:
    x1 = 0 
    x2 = (-b)/a
else:
    x1 = 0

try:
    print(f"Ваше рівняння набуває вигляд: {a}x^2 + {b}x + {c} = 0 \nДискримінант дорівнює: {D}")
except Exception:
    print(f"Ваше рівняння набуває вигляд: {a}x^2 + {b}x + {c} = 0")

if x1 == "R":
    print("Рівняння має безліч коренів.")  
elif x1 == 0:
    print("Корінь заданного рівняння: 0.")  
elif x1 == x2 or x2 == "-":
    print(f"Корінь заданного рівняння: {round(x1, 3)}.")
else:
    print(f"Корені заданного рівняння: {round(x1, 3)}, {round(x2, 3)}.")
