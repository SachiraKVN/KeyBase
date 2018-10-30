import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import binascii

class NuCrypt():
    """
    Simple hashing machanism  
    """
    
    def __init__(self, *args, **kwargs):
        
        self.salt_size = 16
        self.num_iteration = 20
        self.AES_multiple = 16
        self.password = b'1993Nov29'
    
    def generate_key(self, salt, iterations):
        assert iterations > 0

        key = self.password + salt

        for i in range(iterations):
            key = hashlib.sha256(key).digest()

        return key
    
    def pad_text(self, text, multiple):

        extra_bytes = len(text) % multiple
        pad_size = multiple - extra_bytes

        padding = chr(pad_size) * pad_size

        padded_text = text + padding

        return padded_text

    def unpad_text(self, padded_text):

        pad_size = padded_text[-1]

        text = padded_text[:-pad_size]

        return text
    def encrypt(self, plaintext):

        salt = Crypto.Random.get_random_bytes(self.salt_size)
        # print(salt)
        key = self.generate_key(salt, self.num_iteration)

        cipher = AES.new(key, AES.MODE_ECB)

        padded_plaintext = self.pad_text(plaintext, self.AES_multiple)

        ciphertext = cipher.encrypt(padded_plaintext)

        ciphertext_wih_salt = salt + ciphertext

        hex_data = binascii.hexlify(ciphertext_wih_salt)
        str = hex_data.decode('utf-8')

        return str
    
    def decrypt(self, ciphertext):  
        # print(ciphertext)
        binary_data = binascii.unhexlify(ciphertext.encode('utf-8'))
        salt = binary_data[0:self.salt_size]
        # print(salt)
        ciphertext_sans_salt = binary_data[self.salt_size:]

        key = self.generate_key(salt, self.num_iteration)

        cipher = AES.new(key, AES.MODE_ECB)

        padded_paintext = cipher.decrypt(ciphertext_sans_salt)

        plaintext = self.unpad_text(padded_paintext)

        return plaintext.decode('utf-8')

def export():
    return NuCrypt()

if __name__ == '__main__':
    # this Class 
    export()
