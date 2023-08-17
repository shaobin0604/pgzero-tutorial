import pgzrun
from pgzero.builtins import Actor, animate, keyboard, sounds, clock, Rect, images


WIDTH = 800
HEIGHT = 800


cat = Actor('cat', anchor=('left', 'top'))
cat.pos = (0, 0)


mouse = Actor('mouse', anchor=('left', 'top'))
mouse.pos = (60, 60)

def draw():
    screen.clear()
    cat.draw()
    mouse.draw()


pgzrun.go()