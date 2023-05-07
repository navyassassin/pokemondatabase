import yaml
import pprint

pokedex = "./pokedex.yaml"

def pokedex_load():
    with open(pokedex, 'r') as f:
        pokedexDict = yaml.load(f, Loader=yaml.Loader)
    pprint.pprint(pokedexDict)
    return pokedexDict
