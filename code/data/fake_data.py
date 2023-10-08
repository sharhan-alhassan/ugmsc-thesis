import json
import random
from faker import Faker

# Set the number of dictionaries you want to generate
num_transactions = 100000  # You can change this to 10,000 or any desired number

fake = Faker()

# Initialize an empty list to store the dictionaries
transactions = []

# Generate random data and create dictionaries
for _ in range(num_transactions):
    transaction = {
        "timestamp": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
        "transactionID": fake.sha256(),
        "lockTime": str(random.randint(40000, 50000)),
        "amount": str(random.randint(10, 100)),
        "senderAddress": fake.uuid4(),
        "recipientAddress": fake.uuid4(),
    }
    transactions.append(transaction)

# Write the list of dictionaries to a JSON file
with open("./data/100000.json", "w") as json_file:
    json.dump(transactions, json_file, indent=4)

print(f"{num_transactions} random transactions have been generated and saved to transactions.json.")
