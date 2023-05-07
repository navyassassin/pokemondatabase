import yaml
moves = "./moves.yaml"

def moves_load():
    with open(moves, 'r') as f:
        movesDict = yaml.load(f, Loader=yaml.Loader)
    print(movesDict)
    return movesDict
