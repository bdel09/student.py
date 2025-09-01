#Name: Benjamin Del Barrio

#Email: benjamin.delbarrio31@myhunter.cuny.edu

import turtle              

wn = turtle.Screen()       

t = turtle.Turtle()

t.pensize(5)

t.shape("circle")

t.color("black")

t.color(“red”)

t.right(90)

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(300)

t.color("cyan")

for i in range(2):

   t.left(90)

   t.forward(100)

t.left(90)

t.forward(300)

t.color("blue")

for i in range(2):

   t.left(90)

   t.forward(100)

t.left(90)

t.forward(300)

t.color("green")

for i in range(2):

   t.left(90)

   t.forward(100)

t.left(90)

t.forward(300)

t.color("red")

wn.exitonclick()
