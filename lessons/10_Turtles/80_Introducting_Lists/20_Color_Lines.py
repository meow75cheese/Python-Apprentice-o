"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

def square_1():
    for color in colors:                            # loop through the colors
        tina.pencolor(color)
        tina.pendown()
        tina.left(90)
        tina.forward(100)

#square_1()


# 2) Make another square, but put the colors in reverse order, using a negative index. 

def square_2():
    for i in range(len(colors)):
        tina.pencolor(colors[-1-i])
        tina.pendown()
        tina.left(90)
        tina.forward(100)

square_1()

turtle.exitonclick()                     # Close the window when we click on it