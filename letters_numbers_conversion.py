alph = list(" abcdefghijklmnopqrstuvwxyz")


def convert_to_numbers(input_string):
    return [alph.index(a) for a in input_string]


def convert_to_letters(input_string):
    return ''.join([alph[a] for a in input_string])

print(convert_to_numbers('a cat'))
print("testing convert_to_numbers on input 'a cat'...")
assert convert_to_numbers('a cat') == [1, 0, 3, 1, 20]
print("PASSED")

print(convert_to_letters([1, 0, 3, 1, 20]))
print("testing convert_to_letters on input [1, 0, 3, 1, 20]...")
assert convert_to_letters([1, 0, 3, 1, 20]) == "a cat"
print("PASSED")
