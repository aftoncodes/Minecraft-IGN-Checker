import random
import string
import requests
import time

print("Hello to my Minecraft IGN generator and checker!\nMade with love by WilliamAfton-codes <3")
N = int(input("How long would you like each IGN to be?: "))
tries = int(input("How many IGNs would you like to generate: "))
for i in range(tries):
    ran_str = ''.join(random.choices(string.ascii_lowercase + string.digits + '_', k=N))
    url = f'https://api.mojang.com/users/profiles/minecraft/{ran_str}?'
    response = requests.get(url)
    uuid = response.json()['id']
    if uuid is not None:
        print(ran_str, 'is invalid.')
        tries = tries - 1
        if tries == 0:
            if uuid is not None:
                print('Sorry, no valid IGN found :(')
                time.sleep(10)
        elif tries != 0:
            tries = tries
    elif uuid is None:
        print("Valid IGN found!", ran_str)
        break
        time.sleep(10)
