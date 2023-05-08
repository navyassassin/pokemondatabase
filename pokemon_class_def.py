
class Pokemon:
    def __init__(self, ability, move_list, name, type, stats):
        self.ability = ability
        self.move_list = move_list
        self.name = name
        self.type = type
        self.stats = stats

    def __eq__(self, other):
        return self.ability == other.ability \
           and self.move_list == other.move_list \
           and self.name == other.name \
           and self.type == other.type \
           and self.stats == other.stats
