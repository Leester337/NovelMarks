from graphics import *
   
# creates new GraphWin object, 500x500 pixels in size
win = GraphWin("My GUI Program", 500, 500)
c1,r1 = (100,60),50
c2,r2 = (190,100),30
c3,r3 = (240,180),40
c4,r4 = (380,320),80

# creates a new Circle object centered at 50,50 with a radius of 20 pixels
circ = Circle(Point(*c1), r1)
circ.setFill("red")
circ.setWidth(3)
circ.draw(win) 

circ = Circle(Point(*c2), r2)
circ.setFill("blue")
circ.setWidth(3)
circ.draw(win) 

circ = Circle(Point(*c3), r3)
circ.setFill("green")
circ.setWidth(3)
circ.draw(win) 

circ = Circle(Point(*c4), r4)
circ.setFill("purple")
circ.setWidth(6)
circ.draw(win) 

text = Text(Point(*c1),"Lee")
text.draw(win)

text = Text(Point(*c2),"is")
text.draw(win)

text = Text(Point(*c3),"really")
text.draw(win)

text = Text(Point(*c4),"fat")
text.setSize(32)
text.draw(win)



while(1):
    pass
