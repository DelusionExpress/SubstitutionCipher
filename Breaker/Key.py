from string import ascii_lowercase as  _DEFAULT_ALPHABET

alphabet = _DEFAULT_ALPHABET
_alphabet = alphabet.upper()+alphabet.lower()
def encode(plaintext,key):
    _key = key.upper()+key.lower()
    return plaintext.translate(str.maketrans(_alphabet,_key))

def decode(ciphertext,key):
    _key = key.upper() + key.lower()
    return ciphertext.translate(str.maketrans(_key,_alphabet))
# what happen

