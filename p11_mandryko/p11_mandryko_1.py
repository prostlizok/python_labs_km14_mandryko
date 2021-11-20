
def sum(l):
   if len(l) == 1:
        return l[0]
   else:
        return l[0] + sum(l[1:])

#print(sum([1, 2, 3]))
assert sum([1, 2 ,3]) == 6, 'Failed on sum'
print('All tests good!')