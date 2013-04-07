from datetime import datetime

class Node:
    
    def __init__(self, name, date, clickCount):
        self.name = name
        self.date = date
        self.clickCount = clickCount

class Folder(Node):

    def __init__(self, name = '', date = datetime.now(), clickCount = 0, children = None):
        Node.__init__(self, name, date, clickCount)
        if children is None:
            self.children = []
        else:
            self.children = children

class Bookmark(Node):

    def __init__(self, name = '', date = datetime.now(), clickCount = 0, url = ''):
        Node.__init__(self, name, date, clickCount)
        self.url = url
