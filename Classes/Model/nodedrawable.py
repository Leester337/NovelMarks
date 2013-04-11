__author__ = 'john'
import sys

sys.path.append('../../Lib/')

class NodeDrawable():
    def __init__(self, enclosed_node, position, radius, color, level):
        self.enclosed_node = enclosed_node
        self.color = color
        self.radius = radius
        self.position = position
        self.level = level
        self.children = []
        self.parent = None
