from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label, DropdownList, VerticalDivider
from asciimatics.event import Event, KeyboardEvent
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from typing import TypeVar, Generic, Optional, Union

from abilities_loader import abilities_load
from alphabetical_loader import alphabetical_load
from moves_loader import moves_load
from pokedex_loader import pokedex_load
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
        name = None
        type1 = None
        type2 = None
        ability = None
        move1 = None
        move2 = None
        move3 = None
        move4 = None

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

    def __init__(self):
        self.name = ""
        bookmarks = []
        teams = []

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


"""Helper functions"""

T = TypeVar('T')

A = TypeVar('A')
B = TypeVar('B')

def indexify_dict_keys(objects: dict[Generic[T]]) -> list[(Generic[T], int)]:
    just_keys = objects.keys()
    just_indices = index_list(just_keys)

    return list(zip(just_keys, just_indices))

def indexify_dict_keys_add_None(objects: dict[Generic[T]]) -> list[(Generic[T], int)]:
    just_keys = list(objects.keys())
    just_keys.insert(0, "None")
    just_indices = index_list(just_keys)

    return list(zip(just_keys, just_indices))

def indexify_dict_values(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Values are most likely returned as a list of lists
    just_values = sum(objects.values(), [])
    just_indices = index_list(just_values)

    return list(zip(just_values, just_indices))

def indexify_dict_values_add_None(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Values are most likely returned as a list of lists
    just_values = list(sum(objects.values(), []))
    just_values.insert(0, "None")

    just_indices = index_list(just_values)

    return list(zip(just_values, just_indices))


def indexify_dict_values_unique(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Concatenate all values together, then turn it into a set which only contains unique members, and then turn it back into a list
    just_values = list(set(sum(objects.values(), [])))
    just_indices = index_list(just_values)

    return list(zip(sorted(just_values), just_indices))

def indexify_dict_values_unique_add_None(objects: dict[(Generic[A], Generic[B])]) -> list[(Generic[B], int)]:
    # Concatenate all values together, then turn it into a set which only contains unique members, and then turn it back into a list
    just_values = list(set(sum(objects.values(), [])))
    just_values.insert(0, "None")
    just_indices = index_list(just_values)

    return list(zip(sorted(just_values), just_indices))

def index_list(objects: list[Generic[T]]) -> list[int]:
    return range(len(objects))

"""
    index_list: list[int] = []
    for i in range(len(objects)):
        index_list.append(i)

    return index_list
"""

"""End of Helper Functions"""

class SearchView(Frame):
    search: SearchModel

    def __init__(self, screen, model):
        super(SearchView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Search View",
                                          reduce_cpu=True)

        #Save the passed in model for later
        self.search = model

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        types: list[str] = types_load()
        alphabetical: list[list[str]] = alphabetical_load()
        abilities: list[str] = abilities_load()
        moves: list[str] = moves_load()

        layout.add_widget(DropdownList(indexify_dict_values_add_None(alphabetical), "Name", "name", self.name_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_keys_add_None(types), "Type", "type1", self.type1_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_keys_add_None(types), "Type", "type2", self.type2_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_keys_add_None(abilities), "Ability", "ability", self.ability_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_values_unique_add_None(moves), "Move", "move1", self.move1_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_values_unique_add_None(moves), "Move", "move2", self.move2_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_values_unique_add_None(moves), "Move", "move3", self.move3_on_change, fit = True))
        layout.add_widget(DropdownList(indexify_dict_values_unique_add_None(moves), "Move", "move4", self.move4_on_change, fit = True))

        layout.add_widget(Button("Button to actual do the search and return a different screen that prints all of the matching Pokemon", self.placeholder))

        self.fix()

    def placeholder():
        pass

    def name_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("name").value

        if val is None:
            self.search.remove_query_name()
        else:
            self.search.query_name(lay.find_widget("name").value)

    def type1_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("type1").value

        if val is None:
            self.search.remove_query_type1()
        else:
            self.search.query_type1(lay.find_widget("type1").value)

    def type2_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("type2").value

        if val is None:
            self.search.remove_query_type2()
        else:
            self.search.query_type2(lay.find_widget("type2").value)

    def ability_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("ability").value

        if val is None:
            self.search.remove_query_ability()
        else:
            self.search.query_ability(lay.find_widget("ability").value)

    def move1_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move1").value

        if val is None:
            self.search.remove_query_move1()
        else:
            self.search.query_move1(lay.find_widget("move1").value)

    def move2_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move2").value

        if val is None:
            self.search.remove_query_move2()
        else:
            self.search.query_move2(lay.find_widget("move2").value)

    def move3_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move3").value

        if val is None:
            self.search.remove_query_move3()
        else:
            self.search.query_move3(lay.find_widget("move3").value)

    def move4_on_change(self):
        lay = self._layouts[0]
        val = lay.find_widget("move4").value

        if val is None:
            self.search.remove_query_move4()
        else:
            self.search.query_move4(lay.find_widget("move4").value)

    def raise_main_exit_view(idk):
        raise NextScene("Exit View")


class ConstructView(Frame):
    def __init__(self, screen):
        super(ConstructView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Construct View",
                                          reduce_cpu=True)

        # Create the form for displaying the list of contacts.
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
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
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
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
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
    def __init__(self, screen):
        super(ExitView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Exit View",
                                          reduce_cpu=True)

        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        layout.add_widget(Label("You are now exiting the program", align = "^"))
        layout.add_widget(Label("Would you like to save your changes to the following profile:", align = "^"))
        #layout.add_widget(Label(model.get_profile_name()))
        layout.add_widget(Label("PLACEHOLDER", align = "^"))

        layout.add_widget(Label("Press Y to save changes", align = "^"))
        layout.add_widget(Label("Press N to discard changes", align = "^"))
        self.fix()

"""
    def process_event(event: Event):
        key = self.get_event()

        if isinstance(event, KeyboardEvent):
            if (key.key_code is ord('y')) or (key.key_code is ord('Y')):
                #TODO do actual saving
                sys.exit(0)
            elif (key.key_code is ord('n')) or (key.key_code is ord('N')):
                sys.exit(0)
"""

class MainView(Frame):
    def __init__(self, screen):
        super(MainView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Main view",
                                          reduce_cpu=True)
        # Save off the model that accesses the contacts database.
        #self._model = model

        # Create the form for displaying the list of contacts.
        layout = Layout([20, 60, 20], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("Browse Bookmarks", self.raise_main_bookmark_view, add_box = False), 1)
        layout.add_widget(Button("Search Database", self.raise_main_search_view, add_box = False), 1)
        layout.add_widget(Button("Construct Team", self.raise_main_construct_view, add_box = False), 1)
        layout.add_widget(Button("Switch Profiles", self.raise_main_profile_view, add_box = False), 1)
        layout.add_widget(Button("Exit", self.raise_main_exit_view, add_box = False), 1)
        self.fix()

    def raise_main_bookmark_view(idk):
        raise NextScene("Bookmark View")

    def raise_main_search_view(idk):
        raise NextScene("Search View")

    def raise_main_construct_view(idk):
        raise NextScene("Construct View")

    def raise_main_profile_view(idk):
        raise NextScene("Profile View")

    def raise_main_exit_view(idk):
        raise NextScene("Exit View")

    def reset(self):
        # Do standard reset to clear out form, then populate with new data.
        super(MainView, self).reset()
        #self.data = self._model.get_current_contact()

    def _ok(self):
        self.save()
        #self._model.update_current_contact(self.data)
        raise NextScene("Main View")

    @staticmethod
    def _cancel():
        raise NextScene("Main View")

"""
def demo(screen, scene):
    scenes = [
        Scene([MainView(screen, contacts)], -1, name="Main View"),
        Scene([ExitView(screen, contacts)], -1, name="Exit View")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)
"""

def handle_search_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_search_view: bool = scene.name == "Search View"

    if not_None and is_search_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    return scenes[find_scene_index("Search View", scenes)]


def handle_bookmark_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_bookmark_view: bool = scene.name == "Bookmark View"

    if not_None and is_bookmark_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    return scenes[find_scene_index("Bookmark View", scenes)]

def handle_construct_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_construct_view: bool = scene.name == "Construct View"

    if not_None and is_construct_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    return scenes[find_scene_index("Construct View", scenes)]

def handle_profile_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_profile_view: bool = scene.name == "Profile View"

    if not_None and is_profile_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    return scenes[find_scene_index("Profile View", scenes)]


def handle_main_screen(screen: Screen, scenes: list[Scene], scene: Scene):
    not_None: bool = scene is not None
    is_main_view: bool = scene.name == "Main View"

    if not_None and is_main_view:
        screen.play(scenes, stop_on_resize = True, start_scene = scene)

    return scenes[find_scene_index("Main View", scenes)]

def exit_on_y_n(event: Event):
    if isinstance(event, KeyboardEvent):
        if event.key_code in (ord("Y"), ord("y"), ord("N"), ord("n")):
            sys.exit(0)

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


def controller(screen: Screen, scenes: list[Scene], scene: Scene) -> Scene:
    if scene is None:
        sys.exit(0)

    scene_name = scene.name
    if scene_name == "Main View":
        controller(screen, scenes, handle_main_screen(screen, scenes, scene))
    elif scene_name == "Search View":
        controller(screen, scenes, handle_exit_screen(screen, scenes, scene))
    elif scene_name == "Exit View":
        controller(screen, scenes, handle_exit_screen(screen, scenes, scene))
    elif scene_name == "Construct View":
        controller(screen, scenes, handle_construct_screen(screen, scenes, scene))
    elif scene_name == "Profile View":
        controller(screen, scenes, handle_profile_screen(screen, scenes, scene))
    elif scene_name == "Bookmark View":
        controller(screen, scenes, handle_bookmark_screen(screen, scenes, scene))


def main(screen: Screen):
    search: SearchModel = SearchModel()

    scenes = [
        Scene([MainView(screen)], -1, name="Main View"),
        Scene([ExitView(screen)], -1, name="Exit View"),
        Scene([ProfileView(screen)], -1, name="Profile View"),
        Scene([ConstructView(screen)], -1, name="Construct View"),
        Scene([BookmarkView(screen)], -1, name="Bookmark View"),
        Scene([SearchView(screen, search)], -1, name="Search View")
    ]
    scene = scenes[0]

    controller(screen, scenes, scene)


#contacts = ContactModel()
Screen.wrapper(func = main, catch_interrupt = False)

"""
contacts = ContactModel()
last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=True, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
"""
