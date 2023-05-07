from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, Label, DropdownList, VerticalDivider
from asciimatics.event import Event, KeyboardEvent
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import sys
from typing import TypeVar, Generic

from abilities_loader import abilities_load
from moves_loader import moves_load
from pokedex_loader import pokedex_load
from stats_loader import stats_load
from types_loader import types_load
from searchDictionary import searchForValue, searchForKey

"""
class BookmarkModel(object):
    isSearch: bool
    isTeam: bool

    def __init__(self)
"""

"""Helper functions"""

T = TypeVar('T')

A = TypeVar('A')
B = TypeVar('B')

def indexify_dict_keys(objects: dict[Generic[T]]) -> list[(Generic[T], int)]:
#def indexify_dict_keys(objects):
    just_keys = objects.keys()
    just_indices = index_list(just_keys)

    return list(zip(just_keys, just_indices))

#def indexify_dict_values(objects: dict[Generic[T]]) -> list[(Generic[T], int)]:
def indexify_dict_values(objects):
    just_values = objects.values()
    just_indices = index_list(just_values)

    return list(zip(iter(just_values), just_indices))

def index_list(objects: list[Generic[T]]) -> list[int]:
#def index_list(objects):
    index_list: list[int] = []
    for i in range(len(objects)):
        index_list.append(i)

    return index_list


class SearchView(Frame):
    def __init__(self, screen):
        super(SearchView, self).__init__(screen,
                                          screen.height * 2 // 3,
                                          screen.width * 2 // 3,
                                          hover_focus=True,
                                          can_scroll=False,
                                          title="Search View",
                                          reduce_cpu=True)

        # Create the form for displaying the list of contacts.
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        types: list[str] = types_load()
        pokedex: list[str] = pokedex_load()
        abilities: list[str] = abilities_load()
        moves: list[str] = moves_load()

        layout.add_widget(DropdownList(indexify_dict_keys(types), "Type", fit = False))
        layout.add_widget(DropdownList(indexify_dict_values(pokedex), "Name", fit = False))
        layout.add_widget(DropdownList(indexify_dict_keys(abilities), "Ability", fit = False))
        layout.add_widget(DropdownList(indexify_dict_keys(moves), "Move", fit = False))

        #layout.add_widget(Label("Use arrow keys to navigate profiles", align = "^"))
        #layout.add_widget(Label("Press Enter to select highlighted option", align = "^"))
        self.fix()

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
    scenes = [
        Scene([MainView(screen)], -1, name="Main View"),
        Scene([ExitView(screen)], -1, name="Exit View"),
        Scene([ProfileView(screen)], -1, name="Profile View"),
        Scene([ConstructView(screen)], -1, name="Construct View"),
        Scene([BookmarkView(screen)], -1, name="Bookmark View"),
        Scene([SearchView(screen)], -1, name="Search View")
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
