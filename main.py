import random
import requests
import json

with open('iso_list.txt', 'rt') as file:
    iso_list = [iso.strip() for iso in file if len(iso) > 0]

iso = random.choice(iso_list)

###########

# depending on the ammount of players in each country there may be less players...
# it might be smart to check all the ISO codes with the API and see if there is enough players.
players = json.loads(requests.get(f'https://api.chess.com/pub/country/{iso}/players').text)
if not 'players' in players:
    print(players)
    exit(1)
players = players['players']
    
player = random.choice(players)

############

# not all players might have played games, so it might be a good idea to check if this is empty
days = json.loads(requests.get(f'https://api.chess.com/pub/player/{player}/games/archives').text)
if not 'archives' in days:
    print(days)
    exit(1)
days = days['archives']

day = random.choice(days)

############

games = json.loads(requests.get(day).text)['games']

game = random.choice(games)

############

print(game)
