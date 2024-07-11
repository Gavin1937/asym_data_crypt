from Crypto.Cipher.AES import block_size

__all__ = [
    'AES_IV_SIZE',
    'AES_KEY_SIZE',
    'DEFAULT_CHUNK_SIZE',
    'DEFAULT_IV',
    'RSA_ENCRYPTED_SIZE',
]

RSA_ENCRYPTED_SIZE = 128
AES_IV_SIZE = 16
AES_KEY_SIZE = 32
DEFAULT_CHUNK_SIZE = block_size * 1024
DEFAULT_IV = b'\x00' * 16
