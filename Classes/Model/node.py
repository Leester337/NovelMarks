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
        self.name = name
        self.date = date
        self.clickCount = clickCount

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
            self.children = list(children)
            for child in children:
                child.parent = self

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
