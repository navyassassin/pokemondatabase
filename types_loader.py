import yaml

types = "./type_table.yaml"

def types_load():
    with open(types, 'r') as f:
        typesDict = yaml.load(f, Loader=yaml.Loader)
    print(typesDict)
    return typesDict
