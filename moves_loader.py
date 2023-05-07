import yaml
moves = "./moves.yaml"

def main():
    with open(moves, 'r') as f:
        movesDict = yaml.load(f, Loader=yaml.Loader)
    print(movesDict)
    return movesDict

if __name__ == "__main__":
    main()
    