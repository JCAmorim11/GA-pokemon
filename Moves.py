import pokepy

class Moves:
    def __init__(self, request):
        self.id = request[0].id
        self.name = request[0].name
        self.type = request[0].type.name
        self.accuracy = request[0].accuracy
        self.PP = request[0].pp
        self.gen = request[0].generation.name
        self.dmgClass = request[0].damage_class.name
        self.power = request[0].power
        self.used = 0
        self.killMove = 0
        self.maxDmg = 0
        self.minDmg = 0
        self.timesEmpty = 0


