list1 = []

def rrange(begin, end, step = 1):
    list2 = []
    if begin == end:
        list2 = list1.copy()
        list1.clear()
        return list2   
    elif begin != end:
        if (begin < end and step > 0) or (begin > end and step < 0):
            list1.append(begin)
            return rrange(begin+step, end, step)
        else:
            return [] 

# ПЕРЕВІРКА

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
#print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')
