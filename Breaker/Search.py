from heapq import nlargest
from itertools import combinations
from random import  shuffle,choice
from string import ascii_uppercase as _DEFAULT_ALPHABET
from Breaker.Score import *
from Breaker.Key import *

alphabet = _DEFAULT_ALPHABET
def find_key(ciphertext, score_func, key=None, choices=10):

    if key is None:
        key = list(alphabet)
        shuffle(key)
    best_key = key
    best_score = score_func(decode(ciphertext,''.join(key)))

    swaps = list(combinations(range(len(alphabet)), 2))

    def neighbours():
        for i, j in swaps:
            key = list(best_key)
            key[i], key[j] = key[j], key[i]
            score = score_func(decode(ciphertext, ''.join(key)))
            if score > best_score:
                yield score, key


    while True:
        try:
            best_score, best_key = choice(nlargest(choices, neighbours()))

        except IndexError:
            best_key = ''.join(best_key)
            return best_score,best_key, decode(ciphertext, best_key)
ciphertext=''
with open('test.txt') as file:
    for line in file:
        ciphertext+=line

print(max(find_key(ciphertext,score) for _ in range(5)))
