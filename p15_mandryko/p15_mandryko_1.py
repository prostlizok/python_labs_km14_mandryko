from math import factorial

while True:
    try:
        n = int(input("Enter n: "))
        break
    except ValueError:
        print("You must enter a number!")

def c(k, n):
    res = (factorial(n))/(factorial(k)*factorial(n-k))
    return int(res)

triangle = ([c(i, l) for i in range(l+1)] for l in range(n+1))

for i in range(n):
    print(*next(triangle))