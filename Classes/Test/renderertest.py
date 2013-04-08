__author__ = 'john'
import sys

sys.path.append('../Manager')

from renderer import *

if __name__ == "__main__":
    renderer = Renderer()
    root_children = [
        FolderDrawable('classes', 'date', 10, 'green', 20, Point(290, 260), []),
        BookmarkDrawable('google', 'date', 15, 'blue', 40, Point(230, 240), 'www.google.com')
    ]
    root_drawable = FolderDrawable('computer science', 'date', 0, 'red', 70, Point(250, 250), root_children)
    renderer.draw(root_drawable)
    renderer.win.getMouse()


