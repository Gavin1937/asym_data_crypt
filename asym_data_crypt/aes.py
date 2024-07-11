from io import BytesIO, IOBase
from typing import Generator, Any
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

__all__ = [
    'AES_IV_SIZE',
    'AES_KEY_SIZE',
    'DEFAULT_IV',
    'aes_iv_gen',
    'aes_key_gen',
    'aes_encrypt',
    'aes_decrypt',
]

AES_IV_SIZE = 16
AES_KEY_SIZE = 32
DEFAULT_IV = b'\x00' * 16

def aes_iv_gen() -> bytes:
    'AES key generation, returns a 16-bytes (128-bits) iv'
    return Random.get_random_bytes(AES_IV_SIZE)

def aes_key_gen() -> bytes:
    'AES key generation, returns a 32-bytes (256-bits) key'
    return Random.get_random_bytes(AES_KEY_SIZE)

def aes_encrypt(bio:BytesIO, key:bytes, iv:bytes=DEFAULT_IV) -> Generator[bytes, Any, None]:
    'AES encryption, taking BytesIO and encrypts input in chunks, yield chunks out'
    
    if not isinstance(bio, IOBase):
        raise ValueError("bio MUST be IOBase.")
    if not isinstance(key, bytes):
        raise ValueError("key MUST be bytes.")
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    last_chunk = None
    while True:
        chunk = bio.read(AES.block_size*1024)
        
        # no more chunk, pad last_chunk & encrypt
        if chunk == b'':
            encrypted = pad(last_chunk, AES.block_size, style='pkcs7')
            encrypted = cipher.encrypt(encrypted)
            yield encrypted
            break
        
        # encrypt last_chunk
        if last_chunk:
            yield cipher.encrypt(last_chunk)
        
        last_chunk = chunk

def aes_decrypt(bio:BytesIO, key:bytes, iv:bytes=DEFAULT_IV) -> Generator[bytes, Any, None]:
    'AES decryption, taking BytesIO and decrypts input in chunks, yield chunks out'
    
    if not isinstance(bio, IOBase):
        raise ValueError("bio MUST be IOBase.")
    if not isinstance(key, bytes):
        raise ValueError("key MUST be bytes.")
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    last_chunk = None
    while True:
        chunk = bio.read(AES.block_size*1024)
        
        # no more chunk, decrypt & unpad last_chunk
        if chunk == b'':
            decrypted = cipher.decrypt(last_chunk)
            decrypted = unpad(decrypted, AES.block_size, style='pkcs7')
            yield decrypted
            break
        
        # encrypt last_chunk
        if last_chunk:
            yield cipher.decrypt(last_chunk)
        
        last_chunk = chunk
