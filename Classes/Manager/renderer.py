import sys
sys.path.append('../../Lib/')

from graphics import *
from Classes.Model.node import *
from Classes.Model.nodedrawable import *
from random import random

__author__ = 'john'

class Renderer:

    def __init__(self):
        self.root = None
        self.width = 640
        self.height = 640
        self.win = GraphWin('My GUI Program', self.width, self.height)
        self.win.getMouse()

    def convert_node(self, node, position, radius, color):
        if isinstance(node, Folder):
            node_drawable = FolderDrawable( node.name,
                node.date,
                node.clickCount,
                color,
                radius,
                position,
                node.children)
        else:
            node_drawable = BookmarkDrawable( node.name,
                node.date,
                node.clickCount,
                color,
                radius,
                position,
                node.url)
        return node_drawable


    def convert_nodes_to_drawables(self, nodes):
        if not nodes:
            return

        node_drawables = []
        nodes = sorted(nodes, key=lambda x: x.clickCount, reverse=True)
        color = 'green'
        radius = 100
        for node in nodes:
            position = Point(100*random(), 100*random())
            node_drawable = convert_node(node, position, radius, color)
            node_drawables.append(node_drawable)
            size = radius - 10

        for node_drawable in node_drawables:
            node_drawable.children = convert_nodes_to_drawables(node_drawable.children)

        return node_drawables


    def convert_node_hierarchy(self, node):
        self.root = node
        self.root_drawable = self.convert_nodes_to_drawables([node])
        if(len(root_drawable) != 1):
            print 'Something went wrong - convert_node_hierarchy\n'
            exit(1)
        else:
            self.root_drawable = self.root_drawable[0]

    def draw(self, node):
        pass
        # draw the entire hierarchy

    """
    returns the object clicked within a folder currently opened. If whitespace was clicked,
    then it just returns the folder opened. It checked TWO levels deep. In other words it
    checks to see if any children were clicked of the opened folder and any children of a child
    of the opened folder.
    """
    def get_object_clicked(self):
        
        click_point = getMouse()
        # return the node at the click position
        child_clicked = find_subobject(self, self.root_drawable, click_point)
        subchild_clicked = find_subobject(self, child_clicked, click_point)
        return subchild_clicked


    def find_subobject(self, parent, click_point):
        for child in parent.children:
            click_center_dist = math.sqrt(math.pow((click_point.x - child.position.x), 2) + \
                math.pow((click_point.y - child.position.y), 2))
            #if the click was within the child object of the current folder
            if (click_center_dist <= child.radius):
                return child
        #if no children were clicked, user clicked open space and return the parent object
        return parent




