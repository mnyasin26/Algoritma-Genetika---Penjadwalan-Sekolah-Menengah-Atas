# Fungsi mengambil satu buah elemen random dari sebuah list
import random

def randomizer(source: list):
    # random index list
    index = random.randrange(0, len(source))
    temp = source[index]
    return temp, index
