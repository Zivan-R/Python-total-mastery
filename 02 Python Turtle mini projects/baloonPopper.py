from turtle import *

diameter = 40
pop_diameter = 100

def draw_balloon ():
    color('red')
    dot(diameter)

def inflate_balloon ():
    global diameter

    if diameter == 40:
        clear()

    diameter += 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("BOUH! JTM DONNE MOI D BIZOU")

draw_balloon()

onkey(inflate_balloon, "Up")
listen()

done()