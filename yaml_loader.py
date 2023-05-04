import yaml

abilities = "./abilities.yaml"
moves = "./moves.yaml"
pokedex = "./pokedex.yaml"
stats = "./stats.yaml"
types = "./type_table.yaml"


def main():
    with open(abilities, 'r') as f:
        abilitiesDict = yaml.load(f, Loader=yaml.Loader)
    print(abilitiesDict)
    
    with open(moves, 'r') as f:
        movesDict = yaml.load(f, Loader=yaml.Loader)
    print(movesDict)
    
    with open(pokedex, 'r') as f:
        pokedexDict = yaml.load(f, Loader=yaml.Loader)
    print(pokedexDict)
    
    with open(stats, 'r') as f:
        statsDict = yaml.load(f, Loader=yaml.Loader)
    print(statsDict)

    with open(types, 'r') as f:
        typesDict = yaml.load(f, Loader=yaml.Loader)
    print(typesDict)

if __name__ == "__main__":
    main()