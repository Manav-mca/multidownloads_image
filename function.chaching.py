from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(4)
    return n *4


print(fx(20))
print("done for 20")

print(fx(15))
print("done for 15")

print(fx(10))
print("done for 10")

print(fx(5))
print("done for 5")

print(fx(4))
print("done for 4")

print(fx(10))
print("done for 10")

print(fx(20))
print("done for 20")

print(fx(15))
print("done for 15")

print(fx(10))
print("done for 10")

