import pokepy


class Pokemon:
    def __init__(self, request):
        self.name = request[0].name
        self.id = request[0].id
        self.moves = []
        self.hp = request[0].stats[0].base_stat
        self.attack =  request[0].stats[1].base_stat
        self.spAttack =request[0].stats[3].base_stat
        self.defense =request[0].stats[2].base_stat
        self.spDefense = request[0].stats[4].base_stat
        self.speed = request[0].stats[5].base_stat
        self.rounds = 0
        self.deaths = 0
        self.kills = 0

    def printName(self):
        return self.name

    def printStats(self):
        print(self.hp)
        print(self.attack)
        print(self.spAttack)
        print(self.defense)
        print(self.spDefense)
        print(self.speed)
