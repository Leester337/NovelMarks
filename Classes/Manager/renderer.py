import sys

sys.path.append('../../Lib/')

from graphics import *
from Classes.Model.node import *
from Classes.Model.nodedrawable import *

__author__ = 'john'
# Coordinates for first group of four points
_f_g = .45
# Coordinates for the second group of four points
_s_g = .54


class Renderer:
    def __init__(self):
        self.root = None
        self.width = 850
        self.height = 850
        self.half = self.width / 2
        self.center_diffs = [(0, -_f_g), (_f_g, 0), (0, _f_g), (-_f_g, 0),
            (_s_g, -_s_g), (_s_g, _s_g), (-_s_g, _s_g), (-_s_g, -_s_g)]
        self.win = GraphWin('My GUI Program', self.width, self.height)

    def convert_node(self, node, position, radius, color):
        return NodeDrawable(node, position, radius, color)

    def convert_nodes_to_drawables(self, nodes, parent_pos, parent_rad):
        if not nodes:
            return []

        node_drawables = []
        nodes = sorted(nodes, key=lambda x: x.clickCount, reverse=True)
        color = 'green'
        radius = parent_rad * 0.3
        for i, node in enumerate(nodes):
            center_diff = self.center_diffs[i]
            x = parent_pos.getX() + center_diff[0] * parent_rad
            y = parent_pos.getY() + center_diff[1] * parent_rad
            position = Point(x, y)
            node_drawable = self.convert_node(node, position, radius, color)
            node_drawables.append(node_drawable)
            radius = radius * 0.9

        for node_drawable in node_drawables:
            if isinstance(node_drawable.enclosed_node, Folder):
                node_drawable.children = self.convert_nodes_to_drawables(
                    node_drawable.enclosed_node.children,
                    node_drawable.position,
                    node_drawable.radius)

        return node_drawables

    def draw_helper(self, node_drawable):
        point = node_drawable.position
        circle = Circle(point, node_drawable.radius)
        circle.setFill(node_drawable.color)
        text_position = Point(point.getX(), point.getY() + 1.3 * node_drawable.radius)
        text = Text(text_position, node_drawable.enclosed_node.name)
        text.setSize(5 + 31 * int(node_drawable.radius / (450)))

        circle.draw(self.win)
        text.draw(self.win)

        if isinstance(node_drawable.enclosed_node, Folder):
            for child in node_drawable.children:
                self.draw_helper(child)

    def draw(self, node):
        self.root = node
        root_loc = Point(self.half, self.half)
        root_rad = self.half - 10
        self.root_drawable = self.convert_node(node, root_loc, root_rad, "blue")
        self.root_drawable.children = self.convert_nodes_to_drawables(
            self.root_drawable.enclosed_node.children, root_loc, root_rad)

        self.draw_helper(self.root_drawable)


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
            click_center_dist = math.sqrt(math.pow((click_point.x - child.position.x), 2) +\
                                          math.pow((click_point.y - child.position.y), 2))
            #if the click was within the child object of the current folder
            if (click_center_dist <= child.radius):
                return child
                #if no children were clicked, user clicked open space and return the parent object
        return parent




