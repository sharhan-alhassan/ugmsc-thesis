import hashlib
import concurrent.futures

# Function to compute SHA-256 hash of a data block
def sha256(data):
    return hashlib.sha256(data).digest()

# Function to process a block of data and hash it using SHA-256
def process_block(block):
    return sha256(block)

# Function to split data into blocks and hash them in parallel
def parallel_hash(data, block_size, num_workers):
    blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        hashes = list(executor.map(process_block, blocks))
    
    # Combine the hashes of blocks
    while len(hashes) > 1:
        new_hashes = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i+1]
            new_hashes.append(sha256(combined))
        hashes = new_hashes
    
    return hashes[0]

# Example input data
input_data = b"Hello, world! This is a test input for parallel hashing."

# Adjust these parameters based on your system's characteristics
block_size = 4096  # Size of data blocks to hash in parallel
num_workers = 4    # Number of parallel threads to use

# Perform parallel hashing
result = parallel_hash(input_data, block_size, num_workers)

# Print the final hash result
print("Parallel Hash:", result.hex())
