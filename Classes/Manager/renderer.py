import sys
sys.path.append('../../Lib/')

from graphics import *

__author__ = 'john'

class Renderer:

    def __init__(self):
        self.win = GraphWin("My GUI Program", 600, 480)
        self.win.getMouse()

