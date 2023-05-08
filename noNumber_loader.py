import yaml

pokedex_NoNumbers = "./pokedex_nonNumbers.yaml"

def pokedex_noNumbers_load():
    with open(pokedex_NoNumbers, 'r') as f:
        pokedexDict = yaml.load(f, Loader=yaml.Loader)
    #pprint.pprint(pokedexDict)
    return pokedex_NoNumbers
