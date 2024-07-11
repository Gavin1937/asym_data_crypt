# Asymmetric Data Encryption/Decryption

A python3 library that, similar to TLS/SSL algorithm, uses RSA & AES to encrypt/decrypt input data.

## Requirements:

### Python >= 3.8

### Install all the required packages

```sh
pip install -r requirements.txt
```

## Install

install after cloning source code

```sh
pip install .
```

or, install from github

```sh
pip install -U git+https://github.com/Gavin1937/asym_data_crypt.git
```

## Example

[Checkout demo.py](./demo/demo.py)

## Encrypted file data structure

```
  Addr |                  Operation                       |
       |                                                  |
0x0000 |    RSA.encrypt(RSA.key, AES.key) [128-bytes]     |
       |                                                  |
0x0080 |    RSA.encrypt(RSA.key, AES.iv)  [128-bytes]     |
       |                                                  |
0x0100 | AES.encrypt(AES.key, AES.MODE_CBC, AES.iv, data) |
       |                    ...                           |
```
