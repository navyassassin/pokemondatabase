import yaml

types = "./type_table.yaml"

def main():
    with open(types, 'r') as f:
        typesDict = yaml.load(f, Loader=yaml.Loader)
    print(typesDict)
    return typesDict

if __name__ == "__main__":
    main()