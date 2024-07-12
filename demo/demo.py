#! /bin/python3

#########################################################
#                                                       #
#  Demo application for asym_data_crypt                 #
#                                                       #
#  Make sure you run this file from "demo" directory,   #
#  so it can load the asym_data_crypt package properly  #
#                                                       #
#  Author: Gavin1937                                    #
#  GitHub: https://github.com/Gavin1937/asym_data_crypt #
#                                                       #
#########################################################


# set path to parent in order to import asym_data_crypt
import sys
sys.path.append('..')


# start here
import asym_data_crypt
from pathlib import Path
from base64 import b64encode


# folder structure setup
data = Path('data')
output = Path('output')
if not output.exists():
    output.mkdir(parents=True, exist_ok=True)



# create key
prv_key,pub_key = asym_data_crypt.key_gen()

# save key to file
with open(output/'private_key.pem', 'wb') as f1, open(output/'public_key.pem', 'wb') as f2:
    f1.write(prv_key)
    f2.write(pub_key)

# # load key
# prv_key,pub_key = None,None
# with open(output/'private_key.pem', 'rb') as f1, open(output/'public_key.pem', 'rb') as f2:
#     prv_key = f1.read()
#     pub_key = f2.read()



# In all the asym_data_crypt.*_encrypt() & asym_data_crypt.*_decrypt() functions,
# parameter "key" can be either public_key or private_key, since we are using RSA.
# You can use public_key to encrypt and decrypt with private_key. Or, you can use
# private_key to encrypt and decrypt with public_key.

chunk_size = asym_data_crypt.DEFAULT_CHUNK_SIZE


for file in data.iterdir():
    # init iteration
    if file.is_dir():
        continue
    original_name = file.name
    encrypted_name = original_name + '.enc'
    print(original_name)
    
    
    # encrypt file in chunks
    with open(data/original_name, 'rb') as fio_in, open(output/encrypted_name, 'wb') as fio_out:
        for chunk in asym_data_crypt.bio_encrypt(pub_key, fio_in, chunk_size):
            fio_out.write(chunk)
    # decrypt file in chunks
    with open(output/encrypted_name, 'rb') as fio_in, open(output/original_name, 'wb') as fio_out:
        for chunk in asym_data_crypt.bio_decrypt(prv_key, fio_in, chunk_size):
            fio_out.write(chunk)
    
    
    # # encrypt/decrypt bytes
    # with open(data/original_name, 'rb') as f:
    #     data_in = f.read()
    # with open(output/encrypted_name, 'wb') as encrypted_file, open(output/original_name, 'wb') as decrypted_file:
    #     encrypted_data = asym_data_crypt.bytes_encrypt(pub_key, data_in)
    #     encrypted_file.write(encrypted_data)
    #     decrypted_data = asym_data_crypt.bytes_decrypt(prv_key, encrypted_data)
    #     decrypted_file.write(decrypted_data)
    
    
    # # encrypt/decrypt base64
    # with open(data/original_name, 'rb') as file:
    #     b64_in = b64encode(file.read()).decode('utf-8')
    # with open(output/encrypted_name, 'w') as encrypted_file, open(output/original_name, 'w') as decrypted_file:
    #     encrypted_data = asym_data_crypt.base64_encrypt(pub_key, b64_in)
    #     encrypted_file.write(encrypted_data)
    #     decrypted_data = asym_data_crypt.base64_decrypt(prv_key, encrypted_data)
    #     decrypted_file.write(decrypted_data)
    
    
    # # encrypt file by path
    # with open(output/encrypted_name, 'wb') as fio_out:
    #     for chunk in asym_data_crypt.path_encrypt(pub_key, data/original_name, chunk_size):
    #         fio_out.write(chunk)
    # # decrypt file by path
    # with open(output/original_name, 'wb') as fio_out:
    #     for chunk in asym_data_crypt.path_decrypt(prv_key, output/encrypted_name, chunk_size):
    #         fio_out.write(chunk)
