import yaml
alphabetical = "./Alphabetical.yaml"

def abilities_load():
    with open(alphabetical, 'r') as f:
        alphabeticalDict = yaml.load(f, Loader=yaml.Loader)
    print(alphabeticalDict)
    return alphabeticalDict