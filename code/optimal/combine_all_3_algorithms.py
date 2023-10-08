import json
import hashlib

def calculate_merkle_root(data, hash_functions):
    if len(data) == 1:
        return data[0]

    if len(data) % 2 != 0:
        data.append(data[-1])

    new_level = []
    num_steps = len(hash_functions)
    hash_function_index = 0
    
    for i in range(0, len(data), 2):
        combined = data[i] + data[i + 1]
        new_hash = hash_functions[hash_function_index](combined).digest()
        new_level.append(new_hash)
        
        num_steps -= 1
        if num_steps == 0:
            num_steps = len(hash_functions)
            hash_function_index = (hash_function_index + 1) % len(hash_functions)
    
    return calculate_merkle_root(new_level, hash_functions)

# Read data from the "transactions.json" file
with open("./data/50000.json", "r") as json_file:
    transactions = json.load(json_file)

# Convert each transaction dictionary to bytes and hash them
byte_numbers = [json.dumps(transaction, sort_keys=True).encode() for transaction in transactions]

# Define the hash functions for each group
hash_functions = [
    hashlib.sha3_384,
    hashlib.sha3_224,
    hashlib.sha384,
    # hashlib.sha224, 0596538336
]

# Calculate the Merkle root using the available hash functions
final_merkle_root = calculate_merkle_root(byte_numbers, hash_functions)
print("Final Merkle Root:", final_merkle_root.hex())


"""
Here's how the code works:

Generate a list of random numbers (byte_numbers) and define the hash functions for each group (hash_functions).

calculate_merkle_root is the main recursive function responsible for constructing the Merkle tree. It takes the dataset (data) and the list of hash functions (hash_functions) as input.

If the length of the data is 1, it means we have reached a leaf node, and that single hash value becomes the root of this subtree. It is returned.

If the length of data is odd, duplicate the last item to make it even, ensuring that we have an even number of items.

Initialize an empty list new_level to hold the hash values of the next level of the Merkle tree.

Determine the number of steps (num_steps) based on the number of available hash functions. In this case, it's the length of the hash_functions list.

Initialize hash_function_index to 0, which will keep track of the current hash function being used.

Iterate through the data in pairs. For each pair, concatenate the hash values (combined) and apply the current hash function to get a new hash value (new_hash). Append the new hash value to the new_level list.

Decrement num_steps by 1. If num_steps reaches 0, it means we have used all available hash functions, so we reset it to the original value and increment the hash_function_index to switch to the next hash function in the list (cycling back to the first if necessary).

Recursively call calculate_merkle_root with the new_level and the same list of hash functions. This continues the construction of the Merkle tree for the next level.

The process continues until the Merkle root is obtained, which is the final hash value.

In this explanation, I've described how the algorithm automatically determines the number of steps based on the available hash functions. The code ensures that all available hash functions are utilized evenly in the construction of the Merkle tree, adapting to the depth of the tree.
"""
