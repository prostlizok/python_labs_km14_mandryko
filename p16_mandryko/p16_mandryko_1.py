while True:
    try:
        page_num = int(input("Введіть кількість сторінок(не більше за 1280): "))
        if page_num > 1280 or page_num < 0:
            raise Exception("Було введено некоректне число. Спробуйте знову.")
        if page_num%16 != 0:
            raise Exception("Було введено некоректне число. Спробуйте знову.")
        break
    except ValueError:
        print("Треба вводити число.")
    except Exception as exp:
        print(exp)

def page_divide(active = True):
    def wrap(func):
        def wrapper(n):
            if active:
                b = func(n)
                for i in b:
                    for j in range(4):
                        a = i[:4]
                        i.append(tuple(a))
                        del i[:4]
                print(b)
            else:
                pass
        return wrapper
    return wrap

@page_divide()
def pages(n):
    book = []
    note = []
    note_num = int(n/16)
    def book_n(note_num):
        for i in range(note_num):
            for j in range(4):
                a = [16*(i+1)-2*j, 1+16*i+2*j, 2+16*i+2*j, 16*(i+1)-1-2*j]
                yield a
    
    
    b = book_n(note_num)

    for i in range(note_num):
        for j in range(4):
            a = next(b)
            for num in a:
                note.append(num)
        book.append(note)
        note = []

    return book 


a = pages(page_num)
print(a)

