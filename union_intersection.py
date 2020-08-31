def intersection(a, b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result


def union(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i])
        if i < len(b) and b[i] not in a:
            result.append(b[i])			
    return result

print("testing intersection([1, 2, 'a', 'b'], [2, 3, 'a'])...")
assert intersection([1, 2, 'a', 'b'],
                    [2, 3, 'a']) == [2, 'a'], "There is something wrong."
print("PASSED")

print("testing union([1, 2, 'a', 'b'], [2, 3, 'a'])...")
assert union([1, 2, 'a', 'b'],
             [2, 3, 'a']) == [1, 2, 3, 'a', 'b'], "There is something wrong."
print("PASSED")
