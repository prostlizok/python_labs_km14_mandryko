import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def inversion(tuple_i):
    inv_num = 0
    for i in range(len(tuple_i) - 1):
        for j in range(i + 1, len(tuple_i)):
            if tuple_i[i] > tuple_i[j]:
                inv_num += 1
    return inv_num

def matrix_list(matrix):
    """
    The function generates a list of indexs and numbers
    """
    print("Your matrix is:")
    print(matrix)

    len_matrix = len(matrix)
    main_list = []
    perm_list = []
#creating a list of indexs
    indexs = list(itertools.permutations(range(0, len_matrix), len_matrix))
#creating a list of nums
    for i in indexs:
        for a in range(0, len_matrix):
            perm_list.append(matrix[a][i[a]])
        main_list.append(perm_list.copy())
        perm_list.clear()  
    return indexs, main_list
        
def mat_multiply(indexs, list11):
    """
    The function multiplies numbers depending on calculated num of inversions
    """
    res_i = 1
    results = []
    for tuple_i, tuple_a in zip(indexs, list11):
        inv = inversion(tuple_i)
        #multiply
        if inv%2 == 0 or inv == 0:
            for i in tuple_a:
                res_i = res_i * i
            results.append(res_i)
            res_i = 1
        elif inv%2 != 0:
            for i in tuple_a:
                res_i = res_i * i
            results.append(res_i*(-1))
            res_i = 1
    return results

def sum(results):
    """
    The function calculate the sum of multiplied numbers
    """
    sum1 = 0
    for i in results:
        sum1 += i
    return sum1

#input check
def check():
    while True:
        try:
            n = int(input("Enter the dimension of matrix: "))
            if n < 0:
                print("Enter the number higher than 0!")
                continue
            break
        except ValueError:
            print("You must enter a number!")
    return n

x, y = matrix_list(random_matrix(check()))
print("Determinant of your matrix is:",sum(mat_multiply(x,y)))

