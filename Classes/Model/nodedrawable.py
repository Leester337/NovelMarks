__author__ = 'john'
import sys
sys.path.append('../../Lib/')

from datetime import datetime
from graphics import *

class NodeDrawable():

    def __init__(self, name, date, clickCount, color, radius, position):
        self.name = name
        self.date = date
        self.clickCount = clickCount
        self.color = color
        self.radius = radius
        self.position = position

class FolderDrawable(NodeDrawable):

    def __init__(self,
                 name = '',
                 date = datetime.now(),
                 clickCount = 0,
                 color = 0,
                 radius = 0,
                 position = Point(0,0),
                 children = None):
        Node.__init__(self, name, date, clickCount, color, radius, position)
        if children is None:
            self.children = []
        else:
            self.children = children

class BookmarkDrawable(NodeDrawable):

    def __init__(self,
                 name = '',
                 date = datetime.now(),
                 clickCount = 0,
                 color = 0,
                 radius = 0,
                 position = Point(0,0),
                 url = ''):
        Node.__init__(self, name, date, clickCount, color, radius, position)
        self.url = url