import sys

sys.path.append('../../Lib/')
sys.path.append('../Model/')

from graphics import *
from node import *
from nodedrawable import *
from windowobj import *
import math

__author__ = 'john'
# Coordinates for first group of four points
_f_g = .45
# Coordinates for the second group of four points
_s_g = .54

center_diffs = [(0, -_f_g), (_f_g, 0), (0, _f_g), (-_f_g, 0),
    (_s_g, -_s_g), (_s_g, _s_g), (-_s_g, _s_g), (-_s_g, -_s_g)]
colors = ['blue', 'cyan', 'forest green', 'medium orchid',
          'dark orange', 'gold', 'light cyan', 'medium slate blue']
map_level_to_font_size = {0: 30, 1: 18, 2: 10, 3: 9, 4: 14, 5: 10}
radius_factor = [1, 1, 1, 1, .5, .5, .5, .5]
sorted_radius = 30

_title_bar_height = 40
_novelmarks_logo_center = Point(50, 20)
_search_box_center = Point(260, 20)
_search_text_center = Point(423, 20)
_search_button_top_left = Point(402, 10)
_search_button_bottom_right = Point(445, 30)
_sort_by_text_center = Point(500, 20)
_sort_by_folders_center = Point(560, 20)
_sort_by_name_center = Point(620, 20)
_sort_by_date_center = Point(670, 20)

class Renderer:
    def __init__(self):
        self.hierarchy_mode = True
        self.root = None
        self.width = 850
        self.height = 850
        self.half = self.width / 2

        self.win = GraphWin('My GUI Program', self.width, self.height)

        self.setUpTitleBar()

    def convert_node(self, node, position, radius, color_index, level):
        return NodeDrawable(node, position, radius, colors[color_index], level)


    def setUpTitleBar(self):
        titlebar = Rectangle(Point(0, 0), Point(self.width, _title_bar_height))
        titlebar.setFill("gray")
        titlebar.draw(self.win)

        # title for NovelMarks
        text = Text(_novelmarks_logo_center, "NovelMarks")
        text.setSize(14)
        text.draw(self.win)

        # search box
        self.entry = Entry(_search_box_center, 30)
        self.entry.draw(self.win)

        text = Text(_search_text_center, "search")
        text.setSize(12)
        text.draw(self.win)

        button = Rectangle(_search_button_top_left, _search_button_bottom_right)
        button.draw(self.win)

        text = Text(_sort_by_text_center, "sort by:")
        text.setSize(14)
        text.draw(self.win)

        text = Text(_sort_by_folders_center, "folders")
        text.setSize(10)
        text.setStyle("bold")
        text.draw(self.win)

        text = Text(_sort_by_name_center, "name")
        text.setSize(10)
        text.setStyle("bold")
        text.draw(self.win)

        text = Text(_sort_by_date_center, "date")
        text.setSize(10)
        text.setStyle("bold")
        text.draw(self.win)

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
        text_position = Point(point.getX(), point.getY() + 1.2 * node_drawable.radius)
        text = Text(text_position, node_drawable.enclosed_node.name)
        text.setSize(map_level_to_font_size[node_drawable.level])

        circle.draw(self.win)
        text.draw(self.win)

        if isinstance(node_drawable.enclosed_node, Folder):
            for child in node_drawable.children:
                self.draw_helper(child)

    def draw(self, node):
        self.hierarchy_mode = True
        # Convert the hierarchy into node drawables
        self.root = node
        # added _title_bar_height to the y parameter to make room for the titlebar
        root_loc = Point(self.half, self.half + _title_bar_height)
        root_rad = self.half - 10
        root_level = 0
        color_index = 0
        self.root_drawable = self.convert_node(node, root_loc, root_rad, color_index, root_level)
        self.root_drawable.children = self.convert_nodes_to_drawables(
            self.root_drawable.enclosed_node.children, root_loc, root_rad, color_index + 1, root_level + 1)

        # Draw the hierarchy
        self.draw_helper(self.root_drawable)


    def draw_sorted_list(self, node_list):
        self.hierarchy_mode = False
        # Convert the hierarchy into a list of node drawables
        initial_x_pos = 40
        delta_x_pos = 100
        delta_y_pos = 100
        x_pos = initial_x_pos
        y_pos = 40 + _title_bar_height
        self.node_drawable_list = []
        # Draw nodes in a grid format
        for node in node_list:
            if x_pos > (self.width - 30):
                x_pos = initial_x_pos
                y_pos = y_pos + delta_y_pos
            node_drawable = self.convert_node(node, Point(x_pos, y_pos), sorted_radius, 5, 0)
            # set the root drawable
            if self.root == node:
                self.root_drawable = node_drawable
            self.node_drawable_list = self.node_drawable_list + [node_drawable]
            self.draw_sorted_node_drawable(node_drawable)
            x_pos = x_pos + delta_x_pos

    def draw_sorted_node_drawable(self, drawable_node):
        x_pos = drawable_node.position.getX()
        y_pos = drawable_node.position.getY()
        point = drawable_node.position
        circle = Circle(point, drawable_node.radius)
        circle.setFill(drawable_node.color)
        text_position = Point(x_pos, y_pos + 1.5 * sorted_radius)
        text = Text(text_position, drawable_node.enclosed_node.name)
        text.setSize(18)
        circle.draw(self.win)
        text.draw(self.win)


    """
    returns the object clicked within a folder currently opened. If whitespace was clicked,
    then it just returns the folder opened. It checked TWO levels deep. In other words it
    checks to see if any children were clicked of the opened folder and any children of a child
    of the opened folder.
    """

    def within_circle(self, point1, point2, radius):
        x_squared = math.pow(point1.getX() - point2.getX(), 2)
        y_squared = math.pow(point1.getY() - point2.getY(), 2)
        r_squared = math.pow(radius, 2)
        if(x_squared + y_squared <= r_squared):
            return True
        else:
            return False

    def get_object_clicked(self):
        click_point = self.win.getMouse()
        x, y = click_point.getX(), click_point.getY()
        if(x <= 20 and y <= 10):
            return WindowObject(WindowObjectType.EXIT, None)
        elif (y >= 10 and y <= _title_bar_height - 10):
            if (x >= 402 and x <= 445):
                return WindowObject(WindowObjectType.SEARCH, self.entry.getText())
            elif (x >= 540 and x <= 580):
                return WindowObject(WindowObjectType.SORT_HIER, None)
                #Sort by Folders was clicked
            elif (x >= 604 and x <= 636):
                return WindowObject(WindowObjectType.SORT_NAME)
                #Sort by Name was clicked
            elif (x >= 655 and x <= 685):
                return WindowObject(WindowObjectType.SORT_DATE)
                #Sort by Date was clicked
        elif (y >= _title_bar_height):
            if(self.hierarchy_mode):
                return self.get_object_clicked_hierarchy(click_point)
            else:
                return self.get_object_clicked_grid(click_point)

    def get_object_clicked_grid(self, click_point):
        for node_drawable in self.node_drawable_list:
            if(self.within_circle(node_drawable.position, click_point, node_drawable.radius)):
                return WindowObject(WindowObjectType.BOOKMARK_OBJ, node_drawable.enclosed_node)
        return None

    def get_object_clicked_hierarchy(self, click_point):
        if(not self.within_circle(click_point, self.root_drawable.position, self.root_drawable.radius)):
            return WindowObject(WindowObjectType.GO_UP)
            # click outside of the radius of the root circle
        child_clicked = self.find_subobject(self.root_drawable, click_point)
        subchild_clicked = self.find_subobject(child_clicked, click_point)
        return WindowObject(WindowObjectType.BOOKMARK_OBJ, subchild_clicked.enclosed_node)


    def find_subobject(self, parent, click_point):
        for child in parent.children:
            #if the click was within the child object of the current folder
            x, y = click_point.getX(), click_point.getY()
            if(self.within_circle(child.position, click_point, child.radius)):
                return child
                #if no children were clicked, user clicked open space and return the parent object
        return parent









