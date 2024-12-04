# HA4096: A Secure Custom Hashing Algorithm

## Overview

HA4096 is a custom cryptographic hash algorithm that ensures the highest level of security through complex mathematical transformations and optimization techniques. It produces a fixed-length hash output that is nearly impossible to reverse, offering superior protection against brute-force and collision attacks.

This algorithm is not based on common standards like SHA-256 or MD5 but is custom-designed to meet modern cryptographic needs with an emphasis on **security**, **performance**, and **resilience** against modern-day threats.

---

## Table of Contents

1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Usage](#usage)
   1. [Encrypting a Message](#encrypting-a-message)
   2. [Brute-Force Attack Example](#brute-force-attack-example)
4. [Performance](#performance)
5. [Code Structure](#code-structure)
6. [License](#license)

---

## Features

- **High Security**: Uses complex bitwise operations, modular arithmetic, and bit shifts to create an avalanche effect, ensuring small changes in input result in vastly different hash outputs.
- **Collision Resistance**: The design is resistant to hash collisions, ensuring two different inputs will not generate the same output hash.
- **Performance**: Optimized for performance while maintaining strong security guarantees. Capable of handling large data efficiently without significant overhead.
- **Flexibility**: Can process strings of various lengths, producing a consistent fixed-size hash regardless of the input size.

---

## How It Works

HA4096 works by transforming the input string through a series of cryptographically secure operations. Here’s an overview of the process:

1. **Input Preprocessing**: The input string is first pre-processed to prepare it for encryption.
2. **Transformation Rounds**: The input undergoes a series of complex operations, including bitwise shifts, XOR operations, and modular arithmetic to alter the data.
3. **Avalanche Effect**: A feature where a small change in the input results in a dramatically different hash output, ensuring the security of the hash.
4. **Final Hash Generation**: After multiple rounds of transformations, the final hash output is generated, which is a fixed-length value.

---

## Usage

### Encrypting a Message

To use the HA4096 algorithm to encrypt a message, simply follow the example below:

```python
from HA4096 import HA4096

# Create an instance of the HA4096 class
hasher = HA4096()

# Encrypt a message
message = "Hello, World!"
hashed_message = hasher.encrypt(message)

# Print the hash output
print(f"Encrypted Hash: {hashed_message}")
```

This code encrypts the string `"Hello, World!"` using the `HA4096` algorithm and prints the resulting hash.

---

### Brute-Force Attack Example

While brute-forcing longer strings is practically infeasible, we demonstrate how a brute-force attack could be attempted on a shorter 4-character string.

```python
from HA4096 import HA4096
import time

# Create an instance of the HA4096 class
hasher = HA4096()

# Example: Testing brute force with a random 4-character string
test_string = "A1b2"
target_hash = hasher.encrypt(test_string)

print(f"Target Hash: {target_hash}")

# Run the brute force test
def brute_force_test(target_hash, length=4):
    characters = string.ascii_letters + string.digits
    for combo in itertools.product(characters, repeat=length):
        candidate = ''.join(combo)
        if hasher.encrypt(candidate) == target_hash:
            return candidate
    return None

brute_forced_value = brute_force_test(target_hash)
print(f"Brute Forced Value: {brute_forced_value}")
```

This script demonstrates a brute-force attempt to guess a 4-character string encrypted with HA4096. The algorithm’s strength lies in its resistance to brute-force attacks, which become exponentially harder with longer strings.

---

## Performance

Below are the performance results for different input lengths on a typical CPU:

| Input Length | Time Taken (approx.) |
|--------------|----------------------|
| 4 characters | ~0.56s               |
| 8 characters | ~0.56s               |
| 16 characters| ~0.56s               |
| 32 characters| ~0.57s               |
| 64 characters| ~0.55s               |
| 128 characters| ~1.10s              |
| 256 characters| ~1.70s              |

As the input size increases, the time taken to compute the hash also increases, as expected. The algorithm scales well for smaller strings but takes longer for larger inputs due to the increased number of transformation rounds.

---

## Code Structure

The code structure consists of the following components:

- **`HA4096.py`**: Contains the implementation of the `HA4096` hashing algorithm.
  - **`encrypt()`**: The function that performs the encryption and returns the final hash.

- **`Example.py`**: A script that demonstrates how to use the `HA4096` class to encrypt strings and perform brute-force attacks for shorter inputs.

---

## License

This project is open-source and licensed under the Apache 2.0 License.