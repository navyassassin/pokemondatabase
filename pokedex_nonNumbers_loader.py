import yaml
import pprint

pokedex = "./pokedex_nonNumbers.yaml"

def pokedex_nonNumbers_load():
    with open(pokedex, 'r') as f:
        pokedexDict = yaml.load(f, Loader=yaml.Loader)
    #pprint.pprint(pokedexDict)
    return pokedexDict
