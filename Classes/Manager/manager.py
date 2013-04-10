import sys
sys.path.append('../../Lib/')

import node
from graphics import *

class Manager:
    def __init__(self, scenario, save_filename="scenario_save.json"):
        """Creates a new manager object based off the given scenario representation

        Keyword Args:
        scenario -- dict representing all information necessary for the scenario
        save_filename -- name to save the scenario's current state to
        """

        # TODO Remove
        bkmk1 = Bookmark('Google', 'www.google.com') 
        bkmk2 = Bookmark('Yahoo', 'www.yahoo.com')
        root = Folder('root', children=[bkmk1, bkmk2])

        self.root = root

    def process_user_action():
        """Blocks until the user performs an action

        Return:
        System state (which may be indication to exit)
        """
        pass





   
# # creates new GraphWin object, 500x500 pixels in size
# win = GraphWin("My GUI Program", 500, 500)
# 
# titlebar = Rectangle(Point(0,0), Point(510,40))
# titlebar.setFill("gray")
# titlebar.draw(win)
# 
# #title for NovelMarks
# text = Text(Point(50,20),"NovelMarks")
# text.draw(win)
# 
# #search box
# entry = Entry(Point(220, 20), 20)
# entry.setText("search")
# entry.draw(win)
# 
# text = Text(Point(350, 20), "sort by:")
# text.setSize(8)
# text.draw(win)
# 
# c1,r1 = (100,150),50
# c2,r2 = (190,100),30
# c3,r3 = (240,180),40
# c4,r4 = (380,320),80
# 
# # creates a new Circle object centered at 50,50 with a radius of 20 pixels
# circ = Circle(Point(*c1), r1)
# circ.setFill("red")
# circ.setWidth(3)
# circ.draw(win) 
# 
# circ = Circle(Point(*c2), r2)
# circ.setFill("blue")
# circ.setWidth(3)
# circ.draw(win) 
# 
# circ = Circle(Point(*c3), r3)
# circ.setFill("green")
# circ.setWidth(3)
# circ.draw(win) 
# 
# circ = Circle(Point(*c4), r4)
# circ.setFill("purple")
# circ.setWidth(6)
# circ.draw(win) 
# 
# text = Text(Point(*c1),"Lee")
# text.draw(win)
# 
# text = Text(Point(*c2),"is")
# text.draw(win)
# 
# text = Text(Point(*c3),"really")
# text.draw(win)
# 
# text = Text(Point(*c4),"fat")
# text.setSize(32)
# text.draw(win)
# 
# win.getMouse()
# 
