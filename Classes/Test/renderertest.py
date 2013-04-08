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
        Folder('classes', 'date', 10, None),
        Bookmark('google', 'date', 15, 'www.google.com'),
        Folder('classes', 'date', 10, None),
        Bookmark('google', 'date', 15, 'www.google.com'),
        Folder('classes', 'date', 10, None),
        Bookmark('google', 'date', 15, 'www.google.com'),
        Folder('classes', 'date', 10, None),
        Bookmark('google', 'date', 15, 'www.google.com'),
        ]

    cs = Folder('computer science', 'date', 0, root_children)
    work = Folder('computer science', 'date', 0, [])
    root = Folder('root', 'date', 0, [cs, work])

    renderer.convert_node_hierarchy(root);
    renderer.draw(renderer.root_drawable);
    #renderer.draw(root_drawable)
    renderer.win.getMouse()


