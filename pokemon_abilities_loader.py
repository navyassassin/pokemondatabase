import yaml
abilities = "./pokemon_abilities.yaml"

def pokemon_abilities_load():
    with open(abilities, 'r') as f:
        abilitiesDict = yaml.load(f, Loader=yaml.Loader)
    #print(abilitiesDict)
    return abilitiesDict
