__author__ = 'john'
import sys

sys.path.append('../../Lib/')

class NodeDrawable():
    def __init__(self, enclosed_node, position, radius, color):
        self.enclosed_node = enclosed_node
        self.color = color
        self.radius = radius
        self.position = position
        self.children = []
