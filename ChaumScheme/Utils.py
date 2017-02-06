import random
import sys
from fractions import gcd
from Crypto.PublicKey import RSA


def relatively_prime_to(mvalue):
    number = generate_random_number()
    good_value = gcd(number, mvalue)
    while good_value != 1:
        number = generate_random_number()
        good_value = gcd(number, mvalue)

    return number


def import_key(plik_klucza):
    file_to_read = open(plik_klucza, 'r')
    key = RSA.importKey(file_to_read.read())
    return key


def generate_random_number():
    return random.randint(1, sys.maxint)


def fill_text(text):
    txt = str(text)
    while len(txt) < 4096:
        txt += "="
    return str(txt)


def delete_equalities(text):
    txt = text.rstrip('=')
    return txt
