
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)

tina = turtle.Turtle()

for i in range(5):
    tina.left(360/5)
    tina.forward(100)
