import random
from PokeAPI import *
from Pokemon import *
#POKEMON 1 à 386


class Team:
    def __init__(self, numbers):
        self.team = []
        self.api = WebClient()
        self.original_gen(numbers)

    def original_gen(self,numbers):
        for i in range(0,6):
            self.team.append(self.api.client.get_pokemon(numbers[i]))


def gen_numbers():
    numbers = []
    for i in range(0,6):
        numbers.append(random.randint(1,387))
    return numbers

tm = Team(gen_numbers())

print(tm.team)
