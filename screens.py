from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label, DropdownList, VerticalDivider
from asciimatics.event import Event, KeyboardEvent
from asciimatics.scene import Scene
from asciimatics.effects import Stars
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from typing import TypeVar, Generic, Optional, Union, Tuple

from abilities_loader import abilities_load
from alphabetical_loader import alphabetical_load
from moves_loader import moves_load
from pokemon_abilities_loader import pokemon_abilities_load
from pokedex_loader import pokedex_load
from pokedex_nonNumbers_loader import pokedex_nonNumbers_load
from stats_loader import stats_load
from types_loader import types_load
from searchDictionary import searchForValue, searchForKey
from pokemon_class_def import Pokemon

#A model for a search or query.
#A search can have as many or as little details as it wants, so every possible query option should be Optional.
class SearchModel(object):
    name: Optional[str]
    type1: Optional[str]
    type2: Optional[str]
    ability: Optional[str]
    move1: Optional[str]
    move2: Optional[str]
    move3: Optional[str]
    move4: Optional[str]

    def __init__(self):
        self.name = None
        self.type1 = None
        self.type2 = None
        self.ability = None
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None

    def __eq__(self, other):
        return self.name == other.name \
           and self.type1 == other.type1 \
           and self.type2 == other.type2 \
           and self.ability == other.ability \
           and self.move1 == other.move1 \
           and self.move2 == other.move2 \
           and self.move3 == other.move3 \
           and self.move4 == other.move4

    def query_name(self, input_name: str):
        self.name = input_name

    def remove_query_name(self):
        self.name = None

    def query_type1(self, input_type: str):
        self.type1 = input_type

    def remove_query_type1(self):
        self.type1 = None

    def query_type2(self, input_type: str):
        self.type2 = input_type

    def remove_query_type2(self):
        self.type2 = None

    def query_ability(self, input_ability: str):
        self.ability = input_ability

    def remove_query_ability(self):
        self.ability = None

    def query_move1(self, input_move: str):
        self.move1 = input_move

    def remove_query_move1(self):
        self.move1 = None

    def query_move2(self, input_move: str):
        self.move2 = input_move

    def remove_query_move2(self):
        self.move2 = None

    def query_move3(self, input_move: str):
        self.move3 = input_move

    def remove_query_move3(self):
        self.move3 = None

    def query_move4(self, input_move: str):
        self.move4 = input_move

    def remove_query_move4(self):
        self.move4 = None

#A team can be 6 Pokemon
class TeamModel(object):
    pokemon1: Optional[Pokemon]
    pokemon2: Optional[Pokemon]
    pokemon3: Optional[Pokemon]
    pokemon4: Optional[Pokemon]
    pokemon5: Optional[Pokemon]
    pokemon6: Optional[Pokemon]

    def __init__(self):
        self.pokemon1 = None
        self.pokemon2 = None
        self.pokemon3 = None
        self.pokemon4 = None
        self.pokemon5 = None
        self.pokemon6 = None

    def __eq__(self, other):
        return self.pokemon1 == other.pokemon1 \
           and self.pokemon2 == other.pokemon2 \
           and self.pokemon3 == other.pokemon3 \
           and self.pokemon4 == other.pokemon4 \
           and self.pokemon5 == other.pokemon5 \
           and self.pokemon6 == other.pokemon6

    def swap_pokemon_positions(self, index1: int, index2: int):
        if (index1 < 1 or index1 > 6) or (index2 < 1 or index2 > 6) or (index1 == index2):
            pass
        else:
            #TODO: I think they should actualy be Optionals
            first: Pokemon = get_pokemon_partial(index1)
            second: Pokemon = get_pokemon_partial(index2)

            #TODO: Trying to swap them, but not sure if this is correct
            first, second = second, first

    def remove_pokemon(self, index: int):
        if index == 1:
            pokemon1 = None
        elif index == 2:
            pokemon2 = None
        elif index == 3:
            pokemon3 = None
        elif index == 4:
            pokemon4 = None
        elif index == 5:
            pokemon5 = None
        elif index == 6:
            pokemon6 = None

    def get_team(self) -> list[Pokemon]:
        return_list: list[Pokemon] = []
        for maybe in [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6]:
            if maybe is not None:
                return_list.append(maybe)

        return return_list

    """Private functions"""

    #Partial function as it only works when index is 1-6
    def get_pokemon_partial(self, index: int):
        if index == 1:
            return self.pokemon1
        elif index == 2:
            return self.pokemon2
        elif index == 3:
            return self.pokemon3
        elif index == 4:
            return self.pokemon4
        elif index == 5:
            return self.pokemon5
        elif index == 6:
            return self.pokemon6

class BookmarkModel(object):
    #A bookmark has access to: a bookmark name, and a bookmarked object
    #A bookmarked object can either be a team TeamModel or a query with the resulting matching Pokemon

    name: str
    bookmark: TeamModel | SearchModel

    def __init__(self, name: str, input_bookmark: TeamModel | SearchModel):
        self.name = name
        self.bookmark = input_bookmark

    def __eq__(self, other):
        return self.name == other.name \
           and self.bookmark == other.bookmark

    def get_bookmark(self) -> TeamModel | SearchModel:
        return self.bookmark

#This will be the class to represent a single Profile
class ProfileModel(object):
    #A profile has access to: profile name, bookmarks, and teams

    name: str
    bookmarks: list[BookmarkModel]
    teams: list[TeamModel]
    current_search: Optional[Tuple[SearchModel, list[str]]]

    def __init__(self):
        self.name = ""
        self.bookmarks = []
        self.teams = []
        self.current_search = None

    def modify_name(self, new_name: str):
        self.name = new_name

    def addBookmark(self, bookmark: BookmarkModel):
        self.bookmarks.append(bookmark)

    def removeBookmark(self, bookmark: BookmarkModel):
        try:
            self.bookmarks.remove(bookmark_name)
        except ValueError:
            pass

    def replaceBookmarks(self, bookmarks_list: list[BookmarkModel]):
        self.bookmarks = bookmarks_list

    def addTeam(self, team: TeamModel):
        self.teams.append(team)

    def removeTeam(self, team_name: TeamModel):
        try:
            self.teams.remove(team_name)
        except ValueError:
            pass

    def replaceTeams(self, teams_list: list[TeamModel]):
        self.teams = teams_list

    def add_current_search(self, search: SearchModel, matches: list[str]):
        self.current_search = (search, matches)

class PrimaryModel(object):
    #list_profiles: list[ProfileModel]
    #current_profile: Optional[ProfileModel]

    def __init__(self):
        self.list_profiles: list[ProfileModel] = []
        self.current_profile: Optional[ProfileModel] = None

    def set_current_profile(self, curr: Optional[ProfileModel]):
        self.current_profile = curr

    def add_current_profile_to_list(self):
        if self.current_profile is not None:
            self.list_profiles.append(self.current_profile)

    def remove_profile_from_list(self, name: str):
        for i in len(self.list_profiles):
            if self.list_profiles[i].name == name:
                self.list_profiles.pop(i)
                break


    #TODO: need to read from a file that should be a yaml file that contains bookmarks and teams
    #If it exists, then improt
    #Otherwise, assume empty and give the user a temporary one

    #def read_profiles_from_file():

"""Helper functions"""

class HomeView(Frame):
    primaryModel: PrimaryModel

    def __init__(self, screen, model: PrimaryModel):
        super(HomeView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Home View",
                                          reduce_cpu=True)

        self.primaryModel = model

        self.add_effect(Stars(screen, 200))

        layout1 = Layout([100])
        self.add_layout(layout1)

        layout1.add_widget(Label("Welcome to Project Celery", align = "^"))

        layout2 = Layout([20, 60, 20])
        self.add_layout(layout2)
        #The DropdownList should be populated with the options from the PrimaryModel, otherwise they should be able to enter a string to create a new ProfileModel. For now, let's only let them choose from the DropdownList. We can prepopulate this with empty ProfileModels and use them during class.
        profile_names: list[str] = []
        for profile in model.list_profiles:
            profile_names.append(profile.name)

        layout2.add_widget(DropdownList(list(zip(profile_names, model.list_profiles)), "Profile Name", "profile", self.profile_on_change, fit = True), 1)

        layout3 = Layout([30, 40, 30], fill_frame = True)
        self.add_layout(layout3)
        layout3.add_widget(Button("Enter", self.go_to_main_screen), 1)

        self.fix()

    def profile_on_change(self):
        self.primaryModel.set_current_profile(self._layouts[1].find_widget("profile").value)

    def go_to_main_screen(self):
        raise NextScene("Main View")


T = TypeVar('T')

A = TypeVar('A')
B = TypeVar('B')

def self_indexify_dict_keys(objects: dict[Generic[T]]) -> list[(Generic[T], Generic[T])]:
    just_keys = objects.keys()
    return list(zip(just_keys, just_keys))


def indexify_dict_keys(objects: dict[Generic[T]]) -> list[(Generic[T], int)]:
    just_keys = objects.keys()
    just_indices = index_list(just_keys)

    return list(zip(just_keys, just_indices))

def self_indexify_dict_keys_add_None(objects: dict[Generic[T]]) -> list[(Generic[T], Generic[T])]:
    just_keys = list(objects.keys())
    just_keys.insert(0, "None")

    return list(zip(just_keys, just_keys))

def indexify_dict_keys_add_None(objects: dict[Generic[T]]) -> list[(Generic[T], int)]:
    just_keys = list(objects.keys())
    just_keys.insert(0, "None")
    just_indices = index_list(just_keys)

    return list(zip(just_keys, just_indices))

def self_indexify_dict_values(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], Generic[B])]:
    # Values are most likely returned as a list of lists
    just_values = sum(objects.values(), [])

    return list(zip(just_values, just_values))

def indexify_dict_values(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Values are most likely returned as a list of lists
    just_values = sum(objects.values(), [])
    just_indices = index_list(just_values)

    return list(zip(just_values, just_indices))

def self_indexify_dict_values_add_None(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], Generic[B])]:
    # Values are most likely returned as a list of lists
    just_values = list(sum(objects.values(), []))
    just_values.insert(0, "None")

    return list(zip(just_values, just_values))

def indexify_dict_values_add_None(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Values are most likely returned as a list of lists
    just_values = list(sum(objects.values(), []))
    just_values.insert(0, "None")

    just_indices = index_list(just_values)

    return list(zip(just_values, just_indices))

def self_indexify_dict_values_unique(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], Generic[B])]:
    # Concatenate all values together, then turn it into a set which only contains unique members, and then turn it back into a list
    just_values = list(set(sum(objects.values(), [])))

    return list(zip(sorted(just_values), just_values))

def indexify_dict_values_unique(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Concatenate all values together, then turn it into a set which only contains unique members, and then turn it back into a list
    just_values = list(set(sum(objects.values(), [])))
    just_indices = index_list(just_values)

    return list(zip(sorted(just_values), just_indices))

def self_indexify_dict_values_unique_add_None(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], Generic[B])]:
    # Concatenate all values together, then turn it into a set which only contains unique members, and then turn it back into a list
    just_values = list(set(sum(objects.values(), [])))
    just_values = sorted(just_values)
    just_values.insert(0, "None")

    return list(zip(just_values, just_values))

def indexify_dict_values_unique_add_None(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Concatenate all values together, then turn it into a set which only contains unique members, and then turn it back into a list
    just_values = list(set(sum(objects.values(), [])))
    just_values.insert(0, "None")
    just_indices = index_list(just_values)

    return list(zip(sorted(just_values), just_indices))

def index_list(objects: list[Generic[T]]) -> list[int]:
    return range(len(objects))

"""End of Helper Functions"""

class SearchView(Frame):
    search: SearchModel
    primary: PrimaryModel

    alphabetical_yaml: list[list[str]]
    types_yaml: list[str]
    abilities_yaml: list[str]
    pokemon_abilities_yaml: list[str]
    moves_yaml: list[str]

    def __init__(self, screen, model: PrimaryModel):
        super(SearchView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Search View",
                                          reduce_cpu=True)

        #Save the passed in model for later
        self.search = SearchModel()
        self.primary = model
        self.types_yaml = pokedex_nonNumbers_load()
        self.alphabetical_yaml = alphabetical_load()
        self.abilities_yaml = abilities_load()
        self.pokemon_abilities_yaml = pokemon_abilities_load()
        self.moves_yaml = moves_load()

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(DropdownList(self_indexify_dict_values_add_None(self.alphabetical_yaml), "Name", "name", self.name_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_keys_add_None(self.types_yaml), "Type", "type1", self.type1_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_keys_add_None(self.types_yaml), "Type", "type2", self.type2_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_keys_add_None(self.abilities_yaml), "Ability", "ability", self.ability_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_values_unique_add_None(self.moves_yaml), "Move", "move1", self.move1_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_values_unique_add_None(self.moves_yaml), "Move", "move2", self.move2_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_values_unique_add_None(self.moves_yaml), "Move", "move3", self.move3_on_change, fit = True))
        layout.add_widget(DropdownList(self_indexify_dict_values_unique_add_None(self.moves_yaml), "Move", "move4", self.move4_on_change, fit = True))

        layout2 = Layout([100])
        self.add_layout(layout2)
        layout2.add_widget(Divider())

        layout3 = Layout([1, 1, 1, 1])
        self.add_layout(layout3)

        layout3.add_widget(Button("Search", self.perform_query), 0)
        layout3.add_widget(Button("Cancel", self.back_to_main_screen), 3)

        self.fix()

    def back_to_main_screen(self):
        raise NextScene("Main View")

    def perform_query(self):
        #Start with the list of all Pokemon
        allPokemon: set[str] = set(sum(self.alphabetical_yaml.values(), []))

        #Then, for any non-empty

        if self.search.name is not None:
            allPokemon.intersection(self.alphabetical_yaml[self.search.name])

        if self.search.type1 is not None:
            allPokemon.intersection(self.types_yaml[self.search.type1])

        if self.search.type2 is not None:
            allPokemon.intersection(self.types_yaml[self.search.type2])

        if self.search.ability is not None:
            pokemon_with_ability: list[str] = []

            for poke in allPokemon:
                poke = poke.lower()
                if poke in self.abilities_yaml:
                    if self.search.move1 in self.pokemon_abilities_yaml[poke]:
                        pokemon_with_ability.append(poke.capitalize())

            allPokemon.intersection(pokemon_with_ability)

        if self.search.move1 is not None:
            pokemon_with_move: list[str] = []

            for poke in allPokemon:
                if poke in self.moves_yaml:
                    if self.search.move1 in self.moves_yaml[poke]:
                        pokemon_with_move.append(poke)

            allPokemon.intersection(pokemon_with_move)


        if self.search.move2 is not None:
            pokemon_with_move: list[str] = []

            for poke in allPokemon:
                if poke in self.moves_yaml:
                    if self.search.move2 in self.moves_yaml[poke]:
                        pokemon_with_move.append(poke)

            allPokemon.intersection(pokemon_with_move)

        if self.search.move3 is not None:
            pokemon_with_move: list[str] = []

            for poke in allPokemon:
                if poke in self.moves_yaml:
                    if self.search.move3 in self.moves_yaml[poke]:
                        pokemon_with_move.append(poke)

            allPokemon.intersection(pokemon_with_move)

        if self.search.move4 is not None:
            pokemon_with_move: list[str] = []

            for poke in allPokemon:
                if poke in self.moves_yaml:
                    if self.search.move4 in self.moves_yaml[poke]:
                        pokemon_with_move.append(poke)

            allPokemon.intersection(pokemon_with_move)

        #Now allPokemon should only have the Pokemon that have matched all of the queries
        #Need to pass this to the other related Screen somehow
        self.primary.current_profile.add_current_search(self.search, allPokemon)

        raise NextScene("Search Result View")

    def name_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("name").value

        if val == "None":
            self.search.remove_query_name()
        else:
            self.search.query_name(lay.find_widget("name").value)

    def type1_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("type1").value

        if val == "None":
            self.search.remove_query_type1()
        else:
            self.search.query_type1(lay.find_widget("type1").value)

    def type2_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("type2").value

        if val == "None":
            self.search.remove_query_type2()
        else:
            self.search.query_type2(lay.find_widget("type2").value)

    def ability_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("ability").value

        if val == "None":
            self.search.remove_query_ability()
        else:
            self.search.query_ability(lay.find_widget("ability").value)

    def move1_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move1").value

        if val == "None":
            self.search.remove_query_move1()
        else:
            self.search.query_move1(lay.find_widget("move1").value)

    def move2_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move2").value

        if val == "None":
            self.search.remove_query_move2()
        else:
            self.search.query_move2(lay.find_widget("move2").value)

    def move3_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move3").value

        if val == "None":
            self.search.remove_query_move3()
        else:
            self.search.query_move3(lay.find_widget("move3").value)

    def move4_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move4").value

        if val == "None":
            self.search.remove_query_move4()
        else:
            self.search.query_move4(lay.find_widget("move4").value)

    def raise_main_exit_view(idk):
        raise NextScene("Exit View")

#TODO: Move this helper function to be with other helper functions
def print_id_or_empty(obj: Optional[str]):
    if obj is None:
        return "None"
    else:
        return obj

#We pretty much want to return the result of the Search
class SearchResultView(Frame):
    primary: PrimaryModel

    def __init__(self, screen, model: PrimaryModel):
        super(SearchResultView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          on_load = self.reload,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Search Result View",
                                          reduce_cpu=True)

        self.primary = model

        current_search = model.current_profile.current_search

    def reload(self):
        current_search = self.primary.current_profile.current_search

        for lay in self._layouts:
            self.remove_effect(lay)

        curr_query, curr_results = current_search

        layout = Layout([100])
        self.add_layout(layout)

        layout.add_widget(Label("Name: " + print_id_or_empty(curr_query.name)))
        layout.add_widget(Label("Type: " + print_id_or_empty(curr_query.type1)))
        layout.add_widget(Label("Type: " + print_id_or_empty(curr_query.type2)))
        layout.add_widget(Label("Ability: " + print_id_or_empty(curr_query.ability)))
        layout.add_widget(Label("Move: " + print_id_or_empty(curr_query.move1)))
        layout.add_widget(Label("Move: " + print_id_or_empty(curr_query.move2)))
        layout.add_widget(Label("Move: " + print_id_or_empty(curr_query.move3)))
        layout.add_widget(Label("Move: " + print_id_or_empty(curr_query.move4)))

        layout2 = Layout([100])
        self.add_layout(layout2)
        layout2.add_widget(Divider())

        layout3 = Layout([100])
        self.add_layout(layout3)
        if curr_results == []:
            layout3.add_widget(Label("No matching Pokemon."))
        else:
            for i in curr_results:
                layout3.add_widget(Label(i))

        layout4 = Layout([1, 1, 1, 1])
        self.add_layout(layout4)
        layout4.add_widget(Button("IDK", self.go_to_main_screen), 3)

        self.fix()


    def go_to_main_screen(self):
        raise NextScene("Main View")


class ConstructView(Frame):
    def __init__(self, screen):
        super(ConstructView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Construct View",
                                          reduce_cpu=True)

        layout = Layout([30, 0, 70], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(Button("Team 1", self.raise_main_exit_view), 0)
        layout.add_widget(Button("Team 2", self.raise_main_exit_view), 0)

        layout.add_widget(VerticalDivider(), 1)

        counter: int = 1
        common_name: str = "NAME "
        profile_names: list[(str, int)] = []
        while counter <= 10:
            profile_names.append((common_name + str(counter), counter))
            counter = counter + 1

        layout.add_widget(DropdownList(profile_names, fit = False), 2)
        #layout.add_widget(Label("\n\n\n\n", align = "^"))

        #layout.add_widget(Label("Use arrow keys to navigate profiles", align = "^"))
        #layout.add_widget(Label("Press Enter to select highlighted option", align = "^"))
        self.fix()

    def raise_main_exit_view(idk):
        raise NextScene("Exit View")


class BookmarkView(Frame):
    def __init__(self, screen):
        super(BookmarkView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Bookmark View",
                                          reduce_cpu=True)

        # Create the form for displaying the list of contacts.
        layout = Layout([30, 0, 70], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(Button("Bookmark 1", self.raise_main_exit_view), 0)
        layout.add_widget(Button("Bookmark 2", self.raise_main_exit_view), 0)

        layout.add_widget(VerticalDivider(), 1)


        counter: int = 1
        common_name: str = "NAME "
        profile_names: list[(str, int)] = []
        while counter <= 10:
            profile_names.append((common_name + str(counter), counter))
            counter = counter + 1


        layout.add_widget(DropdownList(profile_names, fit = False), 2)
        #layout.add_widget(Label("\n\n\n\n", align = "^"))

        #layout.add_widget(Label("Use arrow keys to navigate profiles", align = "^"))
        #layout.add_widget(Label("Press Enter to select highlighted option", align = "^"))
        self.fix()

    def raise_main_exit_view(idk):
        raise NextScene("Exit View")



class ProfileView(Frame):
    def __init__(self, screen):
        super(ProfileView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Profile View",
                                          reduce_cpu=True)

        # Create the form for displaying the list of contacts.
        layout = Layout([20, 60, 20], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(Label("Select a profile\n", align = "^"))

        counter: int = 1
        common_name: str = "NAME "
        profile_names: list[(str, int)] = []
        while counter <= 10:
            profile_names.append((common_name + str(counter), counter))
            counter = counter + 1

        layout.add_widget(DropdownList(profile_names, fit = False))
        layout.add_widget(Label("\n\n\n\n", align = "^"))

        layout.add_widget(Label("Use arrow keys to navigate profiles", align = "^"))
        layout.add_widget(Label("Press Enter to select highlighted option", align = "^"))
        self.fix()


class ExitView(Frame):
    primary: PrimaryModel
    def __init__(self, screen, model: PrimaryModel):
        super(ExitView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Exit View",
                                          reduce_cpu=True)

        self.primary = model

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(Label("You are now exiting the program", align = "^"))
        layout.add_widget(Label("Would you like to save your changes to the following profile:", align = "^"))
        layout.add_widget(Label(model.current_profile.name, align = "^"))

        layout.add_widget(Divider())

        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)

        layout2.add_widget(Button("Save", self.save_profile), 0)
        layout2.add_widget(Button("Discard", self.exit), 3)

        self.fix()

    def save_profile(self):
        self.primary.list_profiles.append(self.primary.current_profile)
        sys.exit(0)

    def exit(self):
        sys.exit(0)

class MainView(Frame):
    def __init__(self, screen):
        super(MainView, self).__init__(screen,
                                          screen.height,
                                          screen.width,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Main view",
                                          reduce_cpu=True)
        # Save off the model that accesses the contacts database.
        #self._model = model

        # Create the form for displaying the list of contacts.
        layout1 = Layout([20, 60, 20])
        self.add_layout(layout1)
        layout1.add_widget(Button("Browse Bookmarks", self.raise_main_bookmark_view, add_box = False), 1)

        layout2 = Layout([20, 60, 20])
        self.add_layout(layout2)
        layout2.add_widget(Button("Search Database", self.raise_main_search_view, add_box = False), 1)

        layout3 = Layout([20, 60, 20])
        self.add_layout(layout3)
        layout3.add_widget(Button("Construct Team", self.raise_main_construct_view, add_box = False), 1)

        layout4 = Layout([20, 60, 20])
        self.add_layout(layout4)
        layout4.add_widget(Button("Switch Profiles", self.raise_main_profile_view, add_box = False), 1)

        layout5 = Layout([20, 60, 20])
        self.add_layout(layout5)
        layout5.add_widget(Button("Exit", self.raise_main_exit_view, add_box = False), 1)

        self.fix()

    def raise_main_bookmark_view(self):
        raise NextScene("Bookmark View")
        #return scenes[find_scene_index("Bookmark View", scenes)]

    def raise_main_search_view(self):
        raise NextScene("Search View")
        #return scenes[find_scene_index("Search View", scenes)]

    def raise_main_construct_view(idk):
        raise NextScene("Construct View")
        #return scenes[find_scene_index("Main View", scenes)]

    def raise_main_profile_view(idk):
        raise NextScene("Profile View")
        #return scenes[find_scene_index("Profile View", scenes)]

    def raise_main_exit_view(idk):
        raise NextScene("Exit View")
        #return scenes[find_scene_index("Exit View", scenes)]

    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(MainView, self).reset()
        #self.data = self._model.get_current_contact()

    def _ok(self):
        self.save()
        #self._model.update_current_contact(self.data)
        raise NextScene("Main View")
        #return scenes[find_scene_index("Main View", scenes)]

    @staticmethod
    def _cancel():
        raise NextScene("Main View")

def handle_search_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_search_view: bool = scene.name == "Search View"

    if not_None and is_search_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    #return scenes[find_scene_index("Search View", scenes)]

def handle_bookmark_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_bookmark_view: bool = scene.name == "Bookmark View"

    if not_None and is_bookmark_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    #return scenes[find_scene_index("Bookmark View", scenes)]

def handle_construct_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_construct_view: bool = scene.name == "Construct View"

    if not_None and is_construct_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    #return scenes[find_scene_index("Construct View", scenes)]

def handle_profile_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_profile_view: bool = scene.name == "Profile View"

    if not_None and is_profile_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    #return scenes[find_scene_index("Profile View", scenes)]

def handle_home_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    screen.play(scenes, stop_on_resize = True, start_scene = scene)

def handle_main_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_main_view: bool = scene.name == "Main View"

    if not_None and is_main_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    #return scenes[find_scene_index("Main View", scenes)]

def handle_exit_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    #is_exit_view: bool = scene.name == "Exit View"

    if not_None and scene.name == "Exit View":
        #scene.effects[0].update(0)
        while True:
            exit_on_y_n(screen.get_event())

    #return scenes[find_scene_index("Main View", scenes)]
    return None

def find_scene_index(name: str, scenes: list[Scene]) -> int:
    index: int = 0
    for scene in enumerate(scenes):
        if name == scene.name:
            return index
        else:
            index = index + 1

    #Scene was not found
    return -1


def controller(screen: Screen, scenes: list[Scene], scene: Optional[Scene]):

    while True:
        if scene is None:
            sys.exit(0)

        scene_name = scene.name
        if scene_name == "Home View":
            handle_home_screen(screen, scenes, scene)
        elif scene_name == "Main View":
                #raise NextScene("Main View")
            handle_main_screen(screen, scenes, scene)
        elif scene_name == "Search View":
                #raise NextScene("Search View")
            handle_exit_screen(screen, scenes, scene)
        elif scene_name == "Exit View":
                #raise NextScene("Exit View")
            handle_exit_screen(screen, scenes, scene)
        elif scene_name == "Construct View":
                #raise NextScene("Construct View")
            handle_construct_screen(screen, scenes, scene)
        elif scene_name == "Profile View":
                #raise NextScene("Profile View")
            handle_profile_screen(screen, scenes, scene)
        elif scene_name == "Bookmark View":
                #raise NextScene("Bookmark View")
            handle_bookmark_screen(screen, scenes, scene)
        else:
            sys.exit(0)


def main(screen: Screen, primary: PrimaryModel):

    search: SearchModel = SearchModel()

    scenes = [
        Scene([HomeView(screen, primary)], -1, name="Home View"),
        Scene([MainView(screen)], -1, name="Main View"),
        Scene([ExitView(screen, primary)], -1, name="Exit View"),
        Scene([ProfileView(screen)], -1, name="Profile View"),
        Scene([ConstructView(screen)], -1, name="Construct View"),
        Scene([BookmarkView(screen)], -1, name="Bookmark View"),
        Scene([SearchView(screen, primary)], -1, name="Search View"),
        Scene([SearchResultView(screen, primary)], -1, name="Search Result View")
    ]
    scene = scenes[0]

    controller(screen, scenes, scene)


primary: PrimaryModel = PrimaryModel()
for i in range(5):
    profile: ProfileModel = ProfileModel()
    profile.modify_name("temp" + str(i))
    primary.set_current_profile(profile)
    primary.add_current_profile_to_list()


while True:
    try:
        Screen.wrapper(func = main, catch_interrupt = False, arguments = [primary])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene

