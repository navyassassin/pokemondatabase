import yaml

def main():
    with open("./pokemondatabase/type_table.yaml", 'r') as testFile:
        pokedexYaml = yaml.load(testFile, Loader=yaml.Loader)
    print(type(pokedexYaml))
    print(pokedexYaml)

if __name__ == "__main__":
    main()