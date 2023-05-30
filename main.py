import matplotlib.pyplot as plt
import pygame as py
import numpy as np
import hashlib
import random
import string
import hmac

e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"

game_hash = '100af1b49f5e9f87efc81f838bf9b1f5e38293e5b4cf6d0b366c004e0a8d9987'

def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0

def get_prev_game(hash_code):
    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()


game_hash = '100af1b49f5e9f87efc81f838bf9b1f5e38293e5b4cf6d0b366c004e0a8d9987'  # Update to latest game's hash for more results
first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"

results = []
current = 0
temp_multiplier = 0.0
count = 0
Results_empty = False
game = True

while game_hash != first_game and Results_empty == False:
    results.append(get_result(game_hash))
    count += 1
    game_hash = get_prev_game(game_hash)

results = np.array(results)

while game == True:
    bet = float(input("Place your bet: "))
    cash_out = input("Cash out? (Y/N): ")
    if cash_out.lower() == "y":
        current_multiplier = results[current]
        print(current_multiplier)
        current += 1
    else:
        print("You lost")
        current_multiplier = results[current]
        print(current_multiplier)
        current += 1


