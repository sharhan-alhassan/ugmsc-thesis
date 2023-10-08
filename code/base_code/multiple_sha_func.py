import random
import hashlib
import hashlib

def calculate_merkle_root(data, hash_function):
    if len(data) == 1:
        return data[0]

    if len(data) % 2 != 0:
        data.append(data[-1])

    new_level = []
    for i in range(0, len(data), 2):
        combined = data[i] + data[i+1]
        new_hash = hash_function(combined).digest()
        new_level.append(new_hash)
    
    return calculate_merkle_root(new_level, hash_function)

# Provide the desired value for generating random numbers
desired_value = 1000000

# Generate a list of 60 different random numbers
numbers = random.sample(range(1, 100000000000), desired_value)

# Convert the numbers to bytes
byte_numbers = [str(num).encode() for num in numbers]

# Define the hash functions for each group
hash_functions = [
    hashlib.sha256,
    hashlib.sha512,
    hashlib.sha3_256,
    hashlib.sha3_512
]

# Iterate through hash functions and calculate Merkle root for each group
for group_idx, hash_function in enumerate(hash_functions):
    # print(f"\nGroup {group_idx + 1} (Using {hash_function.__name__}):")
    merkle_root = calculate_merkle_root(byte_numbers, hash_function)
    # print("Merkle Root:", merkle_root.hex())
