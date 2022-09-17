import pokepy
client = pokepy.V2Client()
mew = pokepy.V2Client().get_pokemon(14)
print(mew)
