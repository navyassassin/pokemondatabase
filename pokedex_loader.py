import yaml
import pprint

pokedex = "./pokedex.yaml"

def main():
        
    with open(pokedex, 'r') as f:
        pokedexDict = yaml.load(f, Loader=yaml.Loader)
    pprint.pprint(pokedexDict)
    return pokedexDict

if __name__ == "__main__":
    main()
    