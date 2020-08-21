def is_prime(n): return all(map(lambda a: n / a % 1 != 0, range(2, n)))

print("testing is_prime on input p59...")
assert is_prime(59)
print("PASSED")

print("testing is_prime on input 51...")
assert not is_prime(51)
print("PASSED")
