import time
import string
import random
import itertools
from HA4096 import HA4096

def test_encryption():
    hasher = HA4096()
    length = 4

    while length <= 256:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        start_time = time.perf_counter()
        hashed = hasher.encrypt(random_string)
        end_time = time.perf_counter()
        print(f"Length: {length}, Time: {end_time - start_time:.9f}s, Hash: {hashed[:8]}...")
        length *= 2

def brute_force_test(target_hash, length=4):
    hasher = HA4096()
    characters = string.ascii_letters + string.digits
    attempts = 0
    start_time = time.perf_counter()

    for combo in itertools.product(characters, repeat=length):
        candidate = ''.join(combo)
        hashed = hasher.encrypt(candidate)
        attempts += 1
        if hashed == target_hash:
            end_time = time.perf_counter()
            print(f"Brute Force Successful! Password: {candidate}, Attempts: {attempts}, Time: {end_time - start_time:.9f}s")
            return candidate, end_time - start_time

    end_time = time.perf_counter()
    print(f"Brute Force Failed. Total Attempts: {attempts}, Time: {end_time - start_time:.9f}s")
    return None, end_time - start_time


def main():
    print("Testing encryption for strings of increasing lengths:")
    test_encryption()

    print("\nBrute forcing a 4-character hash:")
    test_string = ''.join(random.choices(string.ascii_letters + string.digits, k=2))
    print(f"Original string for brute force: {test_string}")
    target_hash = HA4096().encrypt(test_string)
    print(f"Target Hash: {target_hash[:8]}...")
    brute_force_test(target_hash, length=2)

if __name__ == "__main__":
    main()
