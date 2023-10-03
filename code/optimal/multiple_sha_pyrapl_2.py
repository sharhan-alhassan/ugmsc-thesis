import random
import hashlib
import pyRAPL

def calculate_merkle_root(data, hash_function):
    if len(data) == 1:
        return data[0]

    if len(data) % 2 != 0:
        data.append(data[-1])

    new_level = []
    for i in range(0, len(data), 2):
        combined = data[i] + data[i + 1]
        new_hash = hash_function(combined).digest()
        new_level.append(new_hash)
    
    return calculate_merkle_root(new_level, hash_function)

# Provide the desired value for generating random numbers
desired_value = 10000000

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

# Start energy measurement using pyRAPL
pyRAPL.setup()

# Initial hash of individual members of the list
hash_list = [hash_function(number).digest() for number, hash_function in zip(byte_numbers, hash_functions)]

# Grouping in pairs and hashing
while len(hash_list) > 1:
    new_level = []
    for i in range(0, len(hash_list), 2):
        combined = hash_list[i] + hash_list[i + 1]
        new_hash = hash_functions[1](combined).digest()
        new_level.append(new_hash)
    hash_list = new_level

# Final Merkle root
final_merkle_root = hash_list[0]
print("Final Merkle Root:", final_merkle_root.hex())

# Stop energy measurement and output the results
energy_measurement = pyRAPL.Measurement('package')
energy_measurement.begin()
energy_measurement.end()
print("Energy Consumption:", energy_measurement.result.pkg)
