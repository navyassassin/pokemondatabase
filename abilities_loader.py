import yaml
abilities = "./abilities.yaml"

def abilities_load():
    with open(abilities, 'r') as f:
        abilitiesDict = yaml.load(f, Loader=yaml.Loader)
    #print(abilitiesDict)
    return abilitiesDict
