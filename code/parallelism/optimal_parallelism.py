import random
import hashlib
import multiprocessing

def hash_numbers(numbers, hash_function):
    return [hash_function(str(num).encode()).digest() for num in numbers]

def combine_hashes(hash_list, hash_function):
    new_level = []
    for i in range(0, len(hash_list), 2):
        combined = hash_list[i] + hash_list[i+1]
        new_hash = hash_function(combined).digest()
        new_level.append(new_hash)
    return new_level

def calculate_merkle_root_parallel(data, hash_functions):
    if len(data) == 1:
        return data[0]

    if len(data) % 2 != 0:
        data.append(data[-1])

    num_cores = multiprocessing.cpu_count()
    chunk_size = len(data) // num_cores
    pool = multiprocessing.Pool(processes=num_cores)

    hash_results = pool.starmap(hash_numbers, [(data[i:i+chunk_size], hash_functions[0]) for i in range(0, len(data), chunk_size)])

    pool.close()
    pool.join()

    hash_list = [hash for sublist in hash_results for hash in sublist]

    return calculate_merkle_root_parallel(combine_hashes(hash_list, hash_functions[1]), hash_functions[1:])

# Provide the desired value for generating random numbers
desired_value = 2

# Generate a list of random numbers
numbers = random.sample(range(1, 100000000000), desired_value)

# Convert the numbers to bytes
byte_numbers = [str(num).encode() for num in numbers]

# Define the hash functions for each group
hash_functions = [
    hashlib.sha3_384,
    hashlib.sha3_224,
    hashlib.sha384,
    hashlib.sha224
]

# Calculate the Merkle root using parallelism and the specified hash functions for each group
final_merkle_root = calculate_merkle_root_parallel(byte_numbers, hash_functions)
print("Final Merkle Root:", final_merkle_root.hex())
