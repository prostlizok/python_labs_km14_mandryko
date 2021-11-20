def cons(head, tail=[]):
    res = []
    if tail == []:
        res.append(int(head))
        return res
    else:
        res.append(head)
        res.extend(tail)
        return res

def sum(l):
   if len(l) == 1:
        return l[0]
   else:
        return l[0] + sum(l[1:])

l = cons(3, cons(2, cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')
#print(sum([1, 2, 3]))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')