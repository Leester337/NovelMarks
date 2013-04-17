#!/usr/bin/python

import sys
from datetime import date

sys.path.append('../Manager')
from manager import *

if __name__ == "__main__":
    #renderer = Renderer()
    manager = Manager("blah", "blah")

    # Testing drawing of absolute nodes
    #root_drawable_children = [
    #    NodeDrawable('classes', 'date', 10, 'green', 20, Point(290, 260), []),
    #    NodeDrawable('google', 'date', 15, 'blue', 40, Point(230, 240), 'www.google.com')
    #]
    #root_drawable = NodeDrawable('computer science', 'date', 0, 'red', 70, Point(250, 250), root_drawable_children)

    # Testing conversion using algorithm to drawable hierarchy
    cs465 = Bookmark('cs465', 'https://wiki.engr.illinois.edu/display/cs465sp13/Home', date(2013, 2, 15))

    root_children = [
        Folder('classes', [cs465], date(2013, 1, 5), 40),
        Bookmark('1', 'www.google.com', date(2013, 1, 15), 1),
        Bookmark('2', 'www.google.com', date(2013, 2, 17), 2),
        Bookmark('3', 'www.google.com', date(2013, 1, 16), 3),
        Bookmark('4', 'www.google.com', date(2013, 2, 14), 4),
        Bookmark('5', 'www.google.com', date(2013, 2, 18), 5),
        Bookmark('6', 'www.google.com', date(2013, 4, 1), 6),
        Bookmark('7', 'www.google.com', date(2013, 3, 9), 7),
        ]

    cs = Folder('CS', root_children, date(2012, 1, 29), 100)
    work = Folder('work', [], date(2013, 1, 15), 20)
    root = Folder('root', [cs, work], date(2012, 1, 2), 0)

    # sort by date
    # renderer.draw_sorted(root, lambda x: x.date)

    # sort by frequency
    manager.sort_hierarchy_into_list(root, lambda x: x.name)
    manager.renderer.draw_sorted_list(manager.node_list)
    pt = manager.renderer.win.getMouse()
    print "X: " + str(pt.getX())
    print "Y: " + str(pt.getY())


