from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

__all__ = [
    'rsa_key_gen',
    'rsa_encrypt',
    'rsa_decrypt',
]


def rsa_key_gen() -> tuple:
    'Generate RSA key, return (private_key, public_key)'
    key_obj = RSA.generate(1024)
    private_key = key_obj.export_key('PEM')
    public_key = key_obj.public_key().export_key('PEM')
    return (private_key, public_key)

def rsa_encrypt(data:bytes, key:bytes) -> bytes:
    'RSA encryption, output bytes'
    key_obj = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(key_obj)
    return cipher.encrypt(data)

def rsa_decrypt(data:bytes, key:bytes) -> bytes:
    'RSA decryption, output bytes'
    key_obj = RSA.import_key(key)
    cipher = PKCS1_OAEP.new(key_obj)
    return cipher.decrypt(data)
