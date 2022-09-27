import random
import requests
import time

N = 3
print("Welcome to my Minecraft IGN generator and checker! Made with <3 by WilliamAfton-codes")
tries = int(input("How many IGNs would you like to generate: "))
while True:
    time.sleep(0.5)
    ran_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890_', k=N))
    url = f'https://api.mojang.com/users/profiles/minecraft/{ran_str}?'
    response = requests.get(url)
    uuid = response.json()['id']
    if uuid is not None:
        print(ran_str, 'is invalid.')
        tries = tries - 1
        if tries == 0:
            if uuid is not None:
                print('Sorry, no valid IGN found :(')
                input("[Press Enter to exit]")
                break
        elif tries != 0:
            tries = tries
    elif uuid is None:
        print("Valid IGN found!", ran_str)
        input("[Press Enter to exit.]")
        break
