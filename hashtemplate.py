
import hashlib

# hashlib documentation site https://docs.python.org/3/library/hashlib.html

class Hasher:
    def __init__(self, algorithm: str = "sha256"):
        #Initialize the hasher with a chosen algorithm.
        #Supported examples: sha256, sha1, md5, sha512

        self.algorithm = algorithm.lower()

        #Check if the inputted algorithm is supported. The hashlib library has an attribute that 
        # is a collection of all supported algorithms
        # hashlib.algorithms_available

    def hash_message(self, message: str) -> str:
        #Hash a message and return the hexadecimal digest.
