import random
import math


def is_prime(n: int):
    """Test if the given number is prime

    This test works in O(sqrt(n)), which is fast for small n (until around 2^64).
    For larger numbers, other algorithms like the Miller-Rabin test are a better alternative.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min_val: int, max_val: int):
    """Generate a random prime number within range."""
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num


def mod_inverse_simp(e: int, phi: int):
    """
    Calculate the modular multiplicative inverse of e modulo phi.

    Simple approach"""
    for d in range(1, phi):
        mult = d * e
        if (mult % phi) == 1:
            return d
    
def mod_inverse(e: int, phi: int):
    # better approach
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    _, x, _ = extended_gcd(e, phi)
    return x % phi


class RSAEncoder:
    def __init__(self, public_key: tuple[int, int]):
        """Initialize encoder with a public key (n, e)."""
        self.n, self.e = public_key

    def encode(self, message: str) -> str:
        """Encrypt a message using RSA public key."""
        if not self.n or not self.e:
            raise ValueError("Public key not set.")

        # Convert message to numbers and merge them in a string
        #pow(base, exponent, modulo)
        encoded_parts = [pow(ord(char), self.e, self.n) for char in message]
        return " ".join([str(p) for p in encoded_parts])


class RSADecoder:
    def __init__(self, key_size=8):
        """Initialize decoder and generate key pair"""
        self.public_key = self.generate_keys(key_size)

    def generate_primes(self, key_size: int) -> tuple[int, int]:
        lower_bound, upper_bound = 2 ** (key_size - 1), 2**key_size
        p = generate_prime(lower_bound, upper_bound)
        q = generate_prime(lower_bound, upper_bound)
        while p == q:
            q = generate_prime(lower_bound, upper_bound)
        return p, q

    def generate_keys(self, key_size: int):
        """Generate RSA key pair."""
        p, q = self.generate_primes(key_size)
        n = p * q
        phi = (p - 1) * (q - 1)

        # Choose e (public exponent)
        e = 0
        while math.gcd(e, phi) != 1:
            e = random.randrange(3, phi, 2)

        d = mod_inverse(e, phi)  # private exponent

        # Store keys
        self.n = n
        self.d = d
        self.public_key = (n, e)

        return self.public_key

    # Assumes the message was encrypted with this instances public key
    def decrypt(self, message: str) -> str:
        """Decrypt a message using RSA private key."""
        if not self.n or not self.d:
            raise ValueError("Private key not set.")

        # Split the message into parts
        parts = message.split(" ")

        # Decrypt each part and merge them into one string
        #pow(base, exponent, modulo)
        decrypted_parts = [pow(int(part), self.d, self.n) for part in parts]
        decrypted_message = "".join(chr(p) for p in decrypted_parts)
        return decrypted_message
    
    def get_public_key(self):
        return self.public_key
