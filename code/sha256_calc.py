import random
import hashlib

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
        new_hash = sha256(combined)
        new_level.append(new_hash)
        # print(f"Iteration {i//2 + 1}: {new_level[-1].hex()}")

    return calculate_merkle_root(new_level)

# Provide the desired value for generating random numbers
desired_value = 10000000

# Generate a list of 60 different random numbers
numbers = random.sample(range(1, 100000000000), desired_value)

# Convert the numbers to bytes
byte_numbers = [str(num).encode() for num in numbers]

# Calculate and print the Merkle root
merkle_root = calculate_merkle_root(byte_numbers)

# print("\nGenerated Numbers:", numbers)
# print("Generated Numbers:", numbers)
print("Merkle Root:", merkle_root.hex())
