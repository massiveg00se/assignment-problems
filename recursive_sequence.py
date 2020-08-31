def first_n_terms(n):
    if n == 1:
        return 5
    for i in range(n):
        [].append(3 * first_n_terms(i - 1) - 4)
    return 

print(first_n_terms(3))

'''
def first_n_terms(n):
    if n == 1:
        return 5
    return 3 * first_n_terms(i - 1) - 4

arr = []
for i in range(n):
    arr.append(first_n_terms(i))
'''

'''
return [3 * first_n_terms(i - 1) - 4 for i in n]
'''
'''
first_n_terms(3)
return [5, 11, 29]
    return [5, 11]
        return [5]

n[len(n)-1]
'''