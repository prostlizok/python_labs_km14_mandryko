res = []

def cons(head, tail=[]):
    res.append(head)
    return res



l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')
