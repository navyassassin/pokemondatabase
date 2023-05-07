import yaml

stats = "./stats.yaml"

def main():
    with open(stats, 'r') as f:
        statsDict = yaml.load(f, Loader=yaml.Loader)
    print(statsDict)
    return statsDict

if __name__ == "__main__":
    main()