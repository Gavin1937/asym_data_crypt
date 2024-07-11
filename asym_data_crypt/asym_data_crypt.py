from io import BytesIO, IOBase
from pathlib import Path
from typing import Union, Generator, Any
from base64 import b64encode, b64decode

from .rsa import *
from .aes import *

__all__ = [
    'key_gen',
    'bio_encrypt',
    'bio_decrypt',
    'bytes_encrypt',
    'bytes_decrypt',
    'base64_encrypt',
    'base64_decrypt',
    'path_encrypt',
    'path_decrypt',
]

def key_gen() -> tuple:
    'Generate RSA key, return (private_key, public_key)'
    return rsa_key_gen()

def bio_encrypt(key:bytes, bio_in:BytesIO) -> Generator[bytes, Any, None]:
    'Asymmetric data encryption, encrypt BytesIO object, yield chunks out'
    if not isinstance(key, bytes):
        raise ValueError("key MUST be bytes.")
    if not isinstance(bio_in, IOBase):
        raise ValueError("bio_in MUST be IOBase.")
    
    # key generation
    aes_iv = aes_iv_gen()
    aes_key = aes_key_gen()
    
    # aes key encryption
    encr_aes_key = rsa_encrypt(aes_key, key)
    encr_aes_iv = rsa_encrypt(aes_iv, key)
    
    # write aes key & iv
    yield encr_aes_key
    yield encr_aes_iv
    
    # data encryption
    for chunk in aes_encrypt(bio_in, aes_key, aes_iv):
        yield chunk

def bio_decrypt(key:bytes, bio_in:BytesIO) -> Generator[bytes, Any, None]:
    'Asymmetric data decryption, decrypt BytesIO object, yield chunks out'
    if not isinstance(key, bytes):
        raise ValueError("key MUST be bytes.")
    if not isinstance(bio_in, IOBase):
        raise ValueError("bio_in MUST be IOBase.")
    
    # aes key decryption
    decr_aes_key = bio_in.read(RSA_ENCRYPTED_SIZE)
    decr_aes_key = rsa_decrypt(decr_aes_key, key)
    decr_aes_iv = bio_in.read(RSA_ENCRYPTED_SIZE)
    decr_aes_iv = rsa_decrypt(decr_aes_iv, key)
    
    # data encryption
    for chunk in aes_decrypt(bio_in, decr_aes_key, decr_aes_iv):
        yield chunk


def bytes_encrypt(key:bytes, bytes_in:bytes) -> bytes:
    'Asymmetric data encryption, encrypt bytes object, output bytes'
    bytes_out = b''
    for chunk in bio_encrypt(key, BytesIO(bytes_in)):
        bytes_out += chunk
    return bytes_out
def bytes_decrypt(key:bytes, bytes_in:bytes) -> bytes:
    'Asymmetric data decryption, decrypt bytes object, output bytes'
    bytes_out = b''
    for chunk in bio_decrypt(key, BytesIO(bytes_in)):
        bytes_out += chunk
    return bytes_out

def base64_encrypt(key:bytes, base64_in:str) -> str:
    'Asymmetric data encryption, encrypt base64 data, output base64 str'
    bytes_in = b64decode(base64_in)
    bytes_out = bytes_encrypt(key, bytes_in)
    return b64encode(bytes_out)
def base64_decrypt(key:bytes, base64_in:str) -> str:
    'Asymmetric data decryption, decrypt base64 data, output base64 str'
    bytes_in = b64decode(base64_in)
    bytes_out = bytes_decrypt(key, bytes_in)
    return b64encode(bytes_out)

def path_encrypt(key:bytes, path:Union[str,Path]) -> Generator[bytes, Any, None]:
    'Asymmetric data encryption, encrypt file from path, yield chunks out'
    bytes_out = b''
    with open(path, 'rb') as file:
        for chunk in bio_encrypt(key, file):
            yield chunk
def path_decrypt(key:bytes, path:Union[str,Path]) -> Generator[bytes, Any, None]:
    'Asymmetric data decryption, decrypt file from path, yield chunks out'
    bytes_out = b''
    with open(path, 'rb') as file:
        for chunk in bio_decrypt(key, file):
            yield chunk
