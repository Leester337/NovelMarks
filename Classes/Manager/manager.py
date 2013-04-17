import sys

sys.path.append('../../Lib/')
sys.path.append('../Model')

from node import *
from renderer import *

class Manager:
    def __init__(self, scenario, save_filename="scenario_save.json"):
        """Creates a new manager object based off the given scenario representation

        Keyword Args:
        scenario -- dict representing all information necessary for the scenario
        save_filename -- name to save the scenario's current state to
        """

        # TODO Remove
        bkmk1 = Bookmark('Google', 'www.google.com')
        bkmk2 = Bookmark('Yahoo', 'www.yahoo.com')
        root = Folder('root', children=[bkmk1, bkmk2])
        self.renderer = Renderer()
        self.root = root

    def process_user_action():
        """Blocks until the user performs an action

        Return:
        System state (which may be indication to exit)
        """
        mousePt = getMouse()
        if (mousePt.getY() >= 10 and mousePt.getY() <= 30):
            if (mousePt.getX() >= 402 and mousePt.getX() <= 445):
                pass
                #Search box was clicked
                #TODO: retrieve text by calling getText() on the entry box
            elif (mousePt.getX() >= 540 and mousePt.getX() <= 580):
                pass
                #Sort by Folders was clicked
            elif (mousePt.getX() >= 604 and mousePt.getX() <= 636):
                pass
                #Sort by Name was clicked
            elif (mousePt.getX() >= 655 and mousePt.getX() <= 685):
                pass
                #Sort by Date was clicked
        elif (mousePt.getY() >= 40):
            pass
            #the bookmark space was clicked, proceed to check to see if a circle was clicked

    def flatten(self, node):
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

    def sort_hierarchy_into_list(self, node, sort_function):
        self.node_list = self.flatten(node)
        self.node_list = sorted(self.node_list, key=sort_function)

