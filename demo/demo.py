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


# # create key
# prv_key,pub_key = asym_data_crypt.key_gen()

# # save key to file
# with open('private_key.pem', 'wb') as f1, open('public_key.pem', 'wb') as f2:
#     f1.write(prv_key)
#     f2.write(pub_key)

# load key
prv_key,pub_key = None,None
with open('private_key.pem', 'rb') as f1, open('public_key.pem', 'rb') as f2:
    prv_key = f1.read()
    pub_key = f2.read()



# In all the asym_data_crypt.*_encrypt() & asym_data_crypt.*_decrypt() functions,
# parameter "key" can be either public_key or private_key, since we are using RSA.
# You can use public_key to encrypt and decrypt with private_key. Or, you can use
# private_key to encrypt and decrypt with public_key.

chunk_size = asym_data_crypt.DEFAULT_CHUNK_SIZE

# encrypt/decrypt file in chunks
with open('file.in', 'rb') as fio_in, open('output.png', 'wb') as fio_out:
    # # encrypt
    # for chunk in asym_data_crypt.bio_encrypt(pub_key, fio_in, chunk_size):
    #     fio_out.write(chunk)
    
    # decrypt
    for chunk in asym_data_crypt.bio_decrypt(prv_key, fio_in, chunk_size):
        fio_out.write(chunk)


# # encrypt/decrypt bytes
# with open('file.in', 'rb') as file:
#     data_in = file.read()
# data_out = asym_data_crypt.bytes_encrypt(pub_key, data_in)
# data_out = asym_data_crypt.bytes_decrypt(prv_key, data_in)


# # encrypt/decrypt base64
# from base64 import b64decode
# with open('file.in', 'rb') as file:
#     b64_in = b64decode(file.read())
# b64_out = asym_data_crypt.base64_encrypt(pub_key, b64_in)
# b64_out = asym_data_crypt.base64_decrypt(prv_key, b64_in)


# # encrypt/decrypt file by path
# with open('output.png', 'wb') as fio_out:
#     # encrypt
#     for chunk in asym_data_crypt.path_encrypt(pub_key, 'file.in', chunk_size):
#         fio_out.write(chunk)
#     
#     # decrypt
#     for chunk in asym_data_crypt.path_decrypt(prv_key, 'file.in', chunk_size):
#         fio_out.write(chunk)
