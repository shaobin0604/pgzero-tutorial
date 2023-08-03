import pgzrun
from pgzero.builtins import Actor, animate, keyboard, sounds, clock, Rect, images


RED = 200, 0, 0
BOX = Rect((20, 20), (100, 100))

def draw():
    screen.blit(images.alien, (10, 10))

def on_mouse_down():
    sounds.eep.play()


pgzrun.go()