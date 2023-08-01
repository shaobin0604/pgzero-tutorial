import pgzrun
from pgzero.builtins import Actor, animate, keyboard, sounds, clock

alien = Actor('alien')
alien.topleft = 0, 0

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

# def update():
#     alien.left += 2
#     if alien.left > WIDTH:
#         alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'


pgzrun.go()