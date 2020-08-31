def count_characters(a):
    a = a.lower()
    result = {}
    for i in a:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print("testing count_characters('A cat!!!')...")
assert count_characters('A cat!!!') == {'a': 2, 'c': 1, 't': 1, ' ': 1,
                                        '!': 3}, "There is something wrong."
print("PASSED")
