import pyRAPL
import json
import hashlib
import sys

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


def main(json_filename):
    # Read data from the "transactions.json" file
    with open(json_filename, "r") as json_file:
        transactions = json.load(json_file)

    # Convert each transaction dictionary to bytes and hash them
    byte_numbers = [json.dumps(transaction, sort_keys=True).encode() for transaction in transactions]

    # Define the hash functions for each group
    hash_functions = [
        hashlib.sha3_384,
        hashlib.sha384,
        hashlib.sha3_224,
        # hashlib.sha224, 0596538336
    ]

    # Calculate the Merkle root using the available hash functions
    final_merkle_root = calculate_merkle_root(byte_numbers, hash_functions)
    print("Final Merkle Root:", final_merkle_root.hex())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <json_filename>")
        sys.exit(1)

    json_filename = sys.argv[1]
    
    pyRAPL.setup()
    measure = pyRAPL.Measurement('bar')
    with measure:
        measure.begin()

        main(json_filename)

        measure.end()
    

