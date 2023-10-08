import hashlib
import json

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

# Read data from the "transactions.json" file
with open("./data/50000.json", "r") as json_file:
    transactions = json.load(json_file)

# Convert each transaction dictionary to bytes and hash them
byte_numbers = [json.dumps(transaction, sort_keys=True).encode() for transaction in transactions]

# Define the hash functions for each group
hash_functions = [
    hashlib.sha3_384,
    hashlib.sha3_224,
    # hashlib.sha384,
    # hashlib.sha224
]

# Initial hash of individual members of the list
hash_list = [hash_function(number).digest() for number, hash_function in zip(byte_numbers, hash_functions)]

# Grouping in pairs and hashing
while len(hash_list) > 1:
    new_level = []
    for i in range(0, len(hash_list), 2):
        combined = hash_list[i] + hash_list[i+1]
        new_hash = hash_functions[1](combined).digest()
        new_level.append(new_hash)
    hash_list = new_level

# Final Merkle root
final_merkle_root = hash_list[0]
print("Final Merkle Root:", final_merkle_root.hex())
