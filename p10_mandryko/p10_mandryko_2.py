import numpy as np
years = np.arange(0, 2020+3, 1)

#part 1
def sort_help(n):
    if n%400 ==0:
        return n
    if n%100 != 0 and n%400 != 0 and n%4 == 0:
        return n

leap_year = list(filter(sort_help, years)) 

#part 2
def date_input(s):
    """
    ввод дати користувачем
    """
    while True:
        try:
            if s == "year":
                year = int(input("Введіть рік, в якому рахувати кількість днів у місяці(0, 2023): "))
                if year > 2023 or year < 0:
                    raise Exception("Немає данних по введенного року!")
                return year
            month = int(input("Введіть номер місяця, щоб дізнатися кількість днів в ньому(1-12):  "))
            if s == "month":
                if month > 12 or month < 0:
                    raise Exception("Введенного місяця не існує!")
                return month
        except ValueError:
            print("Треба ввести число!")
        except Exception as exp:
            print(exp)

year = date_input("year")
month = date_input("month")

#function for months and years calc
def day_num(y, m, leap):
    big_months = [1, 3, 5, 7, 8, 10, 12]
    small_months = [4, 6, 9, 11]
    if m in big_months:
        print(f"31 днів у {m}-ому місяці {y}-го року")
    elif m in small_months:
        print(f"30 днів у {m}-ому місяці {y}-го року")
    if y in leap and m == 2:
        print(f"29 днів у {m}-ому місяці {y}-го року")
    elif y not in leap and m == 2:
        print(f"28 днів у {m}-ому місяці {y}-го року")

day_num(year, month, leap_year)
