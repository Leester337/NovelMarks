import sys

sys.path.append('../../Lib/')
sys.path.append('../Model/')

from graphics import *
from node import *
from nodedrawable import *

__author__ = 'john'
# Coordinates for first group of four points
_f_g = .45
# Coordinates for the second group of four points
_s_g = .54

center_diffs = [(0, -_f_g), (_f_g, 0), (0, _f_g), (-_f_g, 0),
    (_s_g, -_s_g), (_s_g, _s_g), (-_s_g, _s_g), (-_s_g, -_s_g)]
colors = ['blue', 'cyan', 'forest green', 'medium orchid',
          'dark orange', 'gold', 'light cyan', 'medium slate blue']
map_level_to_font_size = {0: 30, 1: 18, 2: 10, 3: 18, 4: 14, 5: 10}
radius_factor = [1, 1, 1, 1, .5, .5, .5, .5]


class Renderer:
    def __init__(self):
        self.root = None
        self.width = 850
        self.height = 850
        self.half = self.width / 2

        self.win = GraphWin('My GUI Program', self.width, self.height)

    def convert_node(self, node, position, radius, color_index, level):
        return NodeDrawable(node, position, radius, colors[color_index], level)

    def convert_nodes_to_drawables(self, nodes, parent_pos, parent_rad, color_index, level):
        if not nodes:
            return []

        node_drawables = []
        nodes = sorted(nodes, key=lambda x: x.clickCount, reverse=True)
        radius = parent_rad * 0.3
        for i, node in enumerate(nodes):
            center_diff = center_diffs[i]
            this_radius = radius * radius_factor[i]
            x = parent_pos.getX() + center_diff[0] * parent_rad
            y = parent_pos.getY() + center_diff[1] * parent_rad
            position = Point(x, y)
            node_drawable = self.convert_node(node, position, this_radius, color_index, level)
            node_drawables.append(node_drawable)

        for node_drawable in node_drawables:
            if isinstance(node_drawable.enclosed_node, Folder):
                color_index = color_index + 1

                node_drawable.children = self.convert_nodes_to_drawables(
                    node_drawable.enclosed_node.children,
                    node_drawable.position,
                    node_drawable.radius,
                    color_index,
                    level + 1)
                for node_child in node_drawable.children:
                    node_child.parent = node_drawable

        return node_drawables

    def draw_helper(self, node_drawable):
        point = node_drawable.position
        circle = Circle(point, node_drawable.radius)
        circle.setFill(node_drawable.color)
        text_position = Point(point.getX(), point.getY() + 1.1 * node_drawable.radius)
        text = Text(text_position, node_drawable.enclosed_node.name)
        text.setSize(map_level_to_font_size[node_drawable.level])

        circle.draw(self.win)
        text.draw(self.win)

        if isinstance(node_drawable.enclosed_node, Folder):
            for child in node_drawable.children:
                self.draw_helper(child)

    def draw(self, node):
        # Convert the hierarchy into node drawables
        self.root = node
        root_loc = Point(self.half, self.half)
        root_rad = self.half - 10
        root_level = 0
        color_index = 0
        self.root_drawable = self.convert_node(node, root_loc, root_rad, color_index, root_level)
        self.root_drawable.children = self.convert_nodes_to_drawables(
            self.root_drawable.enclosed_node.children, root_loc, root_rad, color_index + 1, root_level + 1)

        # Draw the hierarchy
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




