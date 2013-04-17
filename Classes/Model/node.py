from datetime import datetime

class Node:
    def __init__(self, name, date, clickCount):
        """Represents a generic object in the bookmark manager
        
        Keyword Args:
        name -- name of the node
        date -- date the node was added
        clickCount -- frequency of node clicks
        """
        self.parent = None
        self.depth = 0
        self.name = name
        self.date = date
        self.clickCount = clickCount

    def update_depth(self):
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1


class Folder(Node):
    def __init__(self, name, children = None, date = datetime.now(), clickCount = 0):
        """Represents a folder in the manager
        
        Keyword Args:
        name -- name of folder
        children -- list of children (None by default)
        date -- date folder was added (current time by default)
        clickCount -- number of times folder has been clicked (0 by default)
        """
        Node.__init__(self, name, date, clickCount)
        if children is None:
            self.children = []
        else:
            for child in children:
                self.add_child(child)

    def add_child(self, obj):
        """Adds the object to the folder

        Keyword Args:
        obj -- object to add
        """
        if obj is None or not isinstance(obj, Node):
            raise ValueError("Cannot add invalid child")
        if obj in self.children:
            return
        self.children.append(obj)
        obj.parent = self
        obj.update_depth()

    def update_depth(self):
        """Recursively updates the depth of the node and its children relative to its parent"""
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
        for child in self.children:
            child.update_depth()

class Bookmark(Node):
    def __init__(self, name, url, date = datetime.now(), clickCount = 0):
        """Represents a bookmark in the manager
        
        Keyword Args:
        name -- user-defined name of bookmark
        url -- url the bookmark points to
        date --  date bookmark was added (current time by default)
        clickCount -- number of times bookmark has been clicked (0 by default)
        """
        Node.__init__(self, name, date, clickCount)
        self.url = url
