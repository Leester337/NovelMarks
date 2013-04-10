__author__ = 'john'
import sys

sys.path.append('../Manager')

from renderer import *

if __name__ == "__main__":
    renderer = Renderer()

    # Testing drawing of absolute nodes
    root_drawable_children = [
        FolderDrawable('classes', 'date', 10, 'green', 20, Point(290, 260), []),
        BookmarkDrawable('google', 'date', 15, 'blue', 40, Point(230, 240), 'www.google.com')
    ]
    root_drawable = FolderDrawable('computer science', 'date', 0, 'red', 70, Point(250, 250), root_drawable_children)

    # Testing conversion using algorithm to drawable hierarchy
    root_children = [
        Folder('classes', None, 'date', 10),
        Bookmark('google', 'www.google.com', 'date', 15),
        Folder('classes', None, 'date', 10),
        Bookmark('google', 'www.google.com', 'date', 15),
        Folder('classes', None, 'date', 10),
        Bookmark('google', 'www.google.com', 'date', 15),
        Folder('classes', None, 'date', 10),
        Bookmark('google', 'www.google.com', 'date', 15)
    ]

    cs = Folder('computer science', root_children, 'date', 0)
    work = Folder('computer science', [], 'date', 0)
    root = Folder('root', [cs, work], 'date', 0)

    #renderer.convert_node_hierarchy(root)
    renderer.draw(root)
    renderer.win.getMouse()


