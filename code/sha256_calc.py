import random
import hashlib
import json

def sha256(data):
    return hashlib.sha256(data).digest()

def calculate_merkle_root(data):
    if len(data) == 1:
        return data[0]
    
    # Ensure the number of elements is even
    if len(data) % 2 != 0:
        # Duplicate the last element to make it even
        data.append(data[-1])

    new_level = []
    for i in range(0, len(data), 2):
        combined = data[i] + data[i+1]
        new_hash = sha256(sha256(combined))
        new_level.append(new_hash)
        # print(f"Iteration {i//2 + 1}: {new_level[-1].hex()}")

    return calculate_merkle_root(new_level)


# Read data from the "transactions.json" file
with open("./data/transactions.json", "r") as json_file:
    transactions = json.load(json_file)

# Convert each transaction dictionary to bytes and hash them
byte_numbers = [json.dumps(transaction, sort_keys=True).encode() for transaction in transactions]

# Calculate and print the Merkle root
merkle_root = calculate_merkle_root(byte_numbers)

# print("\nGenerated Numbers:", numbers)
# print("Generated Numbers:", numbers)
print("Merkle Root:", merkle_root.hex())
