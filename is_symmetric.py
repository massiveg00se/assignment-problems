def is_symmetric(input_string):
    return input_string[::-1] == input_string

print("checking if 'racecar' is a palindrome...")
print(is_symmetric("racecar"))
print("testing is_symmetric on input 'racecar'...")
assert is_symmetric("racecar")
print("PASSED")

print("checking if 'batman' is a palindrome...")
print(is_symmetric("batman"))
print("testing is_symmetric on input 'batman'...")
assert not is_symmetric("batman")
print("PASSED")
