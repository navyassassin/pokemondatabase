from searchDictionary import searchForKey, searchForValue

from abilities_loader import abilities_load
from moves_loader import moves_load
from pokedex_loader import pokedex_load
from stats_loader import stats_load
from types_loader import types_load
from alphabetical_loader import alphabetical_load

def main():
    abilities = abilities_load()
    moves = moves_load()
    pokedex = pokedex_load()
    stats = stats_load()
    types = types_load()
    alphabetical = alphabetical_load()
    dictSelect = input("Enter a dictionary file to select (abilites, moves, pokedex, stats, types, alphabetical): ")
    if(dictSelect == "abilities"):
        dict = abilities
    elif(dictSelect == "moves"):
        dict = moves
    elif(dictSelect == "pokedex"):
        dict = pokedex
    elif(dictSelect == "stats"):
        dict = stats
    elif(dictSelect == "types"):
        dict = types
    elif(dictSelect == "alphabetical"):
        dict = alphabetical
    else:
        print("IDk how you got here")
        exit()
    item = input("Enter something to search for (can be a key or a value): ")
    try:
        searchForValue(item, dict)
    except:
        print("No value found, searching for a key...")
    
    try:
        searchForKey(item, dict)
    except:
        print("No value or key found please try again.")
        exit()

if __name__ == "__main__":
    main()