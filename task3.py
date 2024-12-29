import string
import random

# Function to generate a password
def generate_password(length, complexity):
    char_pools = {
        '1': string.ascii_letters,
        '2': string.ascii_letters + string.digits,
        '3': string.ascii_letters + string.digits + string.punctuation
    }
    if complexity not in char_pools:
        return "Invalid complexity level."
    char_pool = char_pools[complexity]
    return ''.join(random.choices(char_pool, k=length))

# Simulated inputs for 6 password generations
simulated_inputs = [
    ('1', 6),
    ('2', 8),
    ('3', 10),
    ('2', 5),
    ('3', 12),
    ('1', 7)
]

# Loop through simulated inputs
for i, (complexity, length) in enumerate(simulated_inputs, start=1):
    print(f"\nPassword Generation {i}:")
    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")
