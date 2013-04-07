import sys
sys.path.append('../../Lib/')

from graphics import *

__author__ = 'john'

class Renderer:

    def __init__(self):
        self.width = 600
        self.height = 480
        self.win = GraphWin("My GUI Program", self.width, self.width)
        self.win.getMouse()

    def convert_node_hierarchy(self, Node):
        pass

    def draw(self, Node):
        pass
        # draw the entire hierarchy

    def get_object_clicked(self):
        click_point = getMouse()
        # return the node at the click position



