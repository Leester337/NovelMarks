import sys

sys.path.append('../../Lib/')
sys.path.append('../Model')

from node import *
from renderer import *
from windowobj import *
import webbrowser

class ManagerState:
    RUNNING = 1
    EXITED = 2

class Manager:
    def __init__(self, scenario, save_filename="scenario_save.json"):
        """Creates a new manager object based off the given scenario representation

        Keyword Args:
        scenario -- dict representing all information necessary for the scenario
        save_filename -- name to save the scenario's current state to
        """


        # TODO Remove, for testing purposes only
        bkmk1 = Bookmark('Google', 'http://www.google.com')
        bkmk2 = Bookmark('Yahoo', 'http://www.yahoo.com')
        fldr1 = Folder('TestFolder', children=[bkmk1, bkmk2])
        root = Folder('root', children=[fldr1])

        # TODO Parse scenario file into manager, set root appropriately from that
        self.renderer = Renderer()
        self.root = root
        self.current_dir = root
        self.state = ManagerState.RUNNING

    def manage(self):
        """Main execution loop of the program"""
        self.renderer.draw(self.current_dir)
        while self.state != ManagerState.EXITED:
            # see what user's clicked
            try:
                clicked_obj = self.renderer.get_object_clicked()
            except GraphicsError:
                self.state = ManagerState.EXITED
                continue
            if clicked_obj is None:
                continue

            # change current directory to a new folder
            if clicked_obj.obj_type == WindowObjectType.BOOKMARK_OBJ:
                bookmark_obj = clicked_obj.value
                if isinstance(bookmark_obj, Bookmark):
                    webbrowser.open(bookmark_obj.url)
                elif isinstance(bookmark_obj, Folder):
                    self.current_dir = clicked_obj.value
                self.renderer.draw(self.current_dir)
            # read text and display list of search matches
            elif clicked_obj.obj_type == WindowObjectType.SEARCH:
                search_text = clicked_obj.value
                matched_objs = _find_matched_objs(self.root, search_text)
                self.renderer.draw_sorted_list(matched_objs)
            # go up a directory if it's possible
            elif clicked_obj.obj_type == WindowObjectType.GO_UP:
                if self.current_dir.parent is not None:
                    self.current_dir = self.current_dir.parent
                    self.renderer.draw(self.current_dir) 
            elif clicked_obj.obj_type == WindowObjectType.ADD:
                # TODO Add a bookmark using passed-in information
                pass
            elif clicked_obj.obj_type == WindowObjectType.EXIT:
                self.state = ManagerState.EXITED

def _find_matched_objs(tree_root, search_text):
    """Recursively searches the bookmark obj tree rooted at the given node for any reference to the search term

    Keyword Args:
    tree_root -- root of tree to search
    search_text -- term to search bookmark obj. names/urls for

    Returns:
    List of matched objects
    """
    matched_objects = list()
    if search_text in tree_root.name or (isinstance(tree_root, Bookmark) and search_text in tree_root.url):
        matched_objects.append(tree_root)
    if isinstance(tree_root, Folder):
        for child in tree_root.children:
            matched_objects = matched_objects + _find_matched_objs(child, search_text)
    return matched_objects

    def _flatten(self, node):
        """Recursive function to flattens a node hierarchy into a list
        
        Keyword Args;
        node -- root node to flatten descendants into list

        Returns:
        Nodes flattened into linear form
        """
        node_list = [node]
        if isinstance(node, Folder):
            for child in node.children:
                node_list = node_list + self.flatten(child)
        return node_list

    def _sort_hierarchy_into_list(self, node, sort_function):
        self.node_list = self._flatten(node)
        self.node_list = sorted(self.node_list, key=sort_function)

