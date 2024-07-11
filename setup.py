from setuptools import setup


# get descriptions
description = 'A python3 library that, similar to TLS/SSL algorithm, uses RSA & AES to encrypt/decrypt input data.'
long_description = ''
with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

# load __version__.py
version = {}
with open('./asym_data_crypt/__version__.py', 'r', encoding='utf-8') as file:
    exec(file.read(), version)

# load requirements.txt
requirements = []
with open('requirements.txt', 'r', encoding='utf-8') as file:
    requirements = [line.strip() for line in file.readlines() if len(line.strip()) > 0]


# package settings
setup(
    name='asym_data_crypt',
    author='Gavin1937',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Gavin1937/asym_data_crypt',
    version=version['__version__'],
    packages=[
        'asym_data_crypt',
    ],
    python_requires='>=3.8.0',
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)