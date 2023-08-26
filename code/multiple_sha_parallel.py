import random
import hashlib
import concurrent.futures

def calculate_merkle_level(data, hash_function):
    new_level = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(0, len(data), 2):
            combined = data[i] + data[i + 1]
            new_hash = hash_function(combined).digest()
            new_level.append(new_hash)
    return new_level

# Provide the desired value for generating random numbers
desired_value = 4

# Generate a list of 60 different random numbers
numbers = random.sample(range(1, 1000), desired_value)

# Convert the numbers to bytes
byte_numbers = [str(num).encode() for num in numbers]

# Define the hash functions for each group
hash_functions = [
    hashlib.sha3_384,
    hashlib.sha3_224,
    hashlib.sha384,
    hashlib.sha224
]

# Initial hash of individual members of the list
initial_hash_function = hash_functions[0]  # Choose the appropriate hash function
hash_list = [initial_hash_function(number).digest() for number in byte_numbers]

# Calculate the Merkle tree levels in parallel
while len(hash_list) > 1:
    next_level = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_index = {executor.submit(calculate_merkle_level, hash_list, hash_function): i for i, hash_function in enumerate(hash_functions)}
        for future in concurrent.futures.as_completed(future_to_index):
            i = future_to_index[future]
            result = future.result()
            next_level.extend(result)
        hash_list = next_level

# Final Merkle root
final_merkle_root = hash_list[0]
print("Final Merkle Root:", final_merkle_root.hex())
