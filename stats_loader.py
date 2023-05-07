import yaml

stats = "./stats.yaml"

def stats_load():
    with open(stats, 'r') as f:
        statsDict = yaml.load(f, Loader=yaml.Loader)
    print(statsDict)
    return statsDict
