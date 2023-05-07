import yaml
abilities = "./abilities.yaml"

def main():
    with open(abilities, 'r') as f:
        abilitiesDict = yaml.load(f, Loader=yaml.Loader)
    print(abilitiesDict)
    return abilitiesDict

if __name__ == "__main__":
    main()
    