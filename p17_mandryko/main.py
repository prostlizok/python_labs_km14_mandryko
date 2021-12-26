from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithn import log, ln, lg


def num_input(n):
    while True:
        try:
            num = float(input(n))
            return num
        except ValueError:
            print("You must enter a number!")


def positive_check(n):
    if n < 0:
        return False
    else:
        return True


def main():
    """
    menu output
    """
    print("----Menu----")
    menu1 = ["1 - Exponentiation", "\n2 - Factorial", "\n3 - Root", "\n4 - Logarithm", "\n5 - Exit", "\n-------------"]
    menu_exp = ["1 - Second power", "\n2 - Third power", "\n-------------"]
    menu_log = ["1 - Logarithm", "\n2 - Natural logarithm", "\n3 - Logarithm to the base 10", "\n-------------"]
    menu_root = ["1 - Square root", "\n2 - Cube root", "\n-------------"]

    print(*menu1)
    n = num_input("Choose your option: ")
    if n == 1:
        print(*menu_exp)
        n = num_input("Choose your option: ")
        if n == 1:
            num = num_input("Enter your number: ")
            print(f"{num} to the second power is:", exp2(num))
        elif n == 2:
            num = num_input("Enter your number: ")
            print(f"{num} to the third power is:", exp3(num))
        else:
            print("Error! Function not found.")

    elif n == 2:
        num = num_input("Enter your number: ")
        print(f"Factorial of {num} is:", fact(num))

    elif n == 3:
        print(*menu_root)
        n = num_input("Choose your option: ")
        if n == 1:
            while True:
                num = num_input("Enter your number: ")
                if positive_check(num):
                    break
                else:
                    print("Number must be greater than 0!")

            print(f"Square root of {num} is:", round(root2(num),3))
        elif n == 2:
            while True:
                num = num_input("Enter your number: ")
                if positive_check(num):
                    break
                else:
                    print("Number must be greater than 0!")
            print(f"Cube root of {num} is:", round(root3(num),3))
        else:
            print("Error! Function not found.")

    elif n == 4:
        print(*menu_log)
        n = num_input("Choose your option: ")
        if n == 1:
            while True:
                num2 = num_input("Enter the base of logarithm: ")
                if positive_check(num2) and num2 != 1:
                    break
                else:
                    print("Error! Enter different number.")

            while True:
                num = num_input("Enter your number: ")
                if positive_check(num):
                    break
                else:
                    print("Error! Enter different number.")

            print(f"Log to the base {num2} of {num} is:", round(log(num2, num), 3))
        elif n == 2:
            num = num_input("Enter your number: ")
            print(f"Ln of {num} is:", round(ln(num), 3))
        elif n == 3:
            num = num_input("Enter your number: ")
            print(f"Lg of {num} is:", round(lg(num), 3))
        else:
            print("Error! Function not found.")

    elif n == 5:
        exit()


if __name__ == '__main__':
    while True:
        main()
