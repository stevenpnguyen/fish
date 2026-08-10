import random
import pygame

WIDTH = 1750
HEIGHT = 1000
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
money = 0
clicked = False
message = "You have unlocked this achievement"
show_trophy = False

bg = None
fox = None
fish = None
fish2 = None
trophy = None
trophy_no = 0
first_trophy = False


def init():
    global bg, fox, fish, fish2, trophy
    bg = pygame.transform.scale(
        pygame.image.load("images/ocean.png").convert(), (WIDTH, HEIGHT)
    )
    fox = Actor("penguin")
    fox.pos = (875, 300)
    fish = Actor("fish")
    fish.pos = (random.randint(0, 1750), random.randint(500, 1000))
    fish2 = Actor("fish2")
    fish2.pos = (random.randint(0, 1750), random.randint(500, 1000))
    trophy = Actor("trophy")
    clock.schedule(hide_fish, 5.0)
    clock.schedule(hide_fish2, 3.0)


def draw():
    if bg is None:
        init()
    screen.blit(bg, (0, 0))
    fox.draw()
    if fish.x != -1000:
        fish.draw()
    if fish2.x != -1000:
        fish2.draw()
    screen.draw.text("money:  " + str(money), color="green", bottomleft=(10, 990))
    if clicked:
        screen.draw.text(message, (300, 10), fontsize=30, color="black")
    if show_trophy:
        trophy_x = 1700
        for no in range(trophy_no):
            trophy.draw()
            trophy.pos = (trophy_x, 50)
            trophy_x = trophy_x - 100


def update():
    if keyboard.right:
        fox.x += 5
    elif keyboard.left:
        fox.x -= 5
    elif keyboard.down:
        fox.y += 5
    fish.x -= 1
    fish2.x -= 2


def hide_fish():
    fish.x = -1000
    clock.schedule(show_fish, 2.0)


def hide_fish2():
    fish2.x = -1000
    clock.schedule(show_fish2, 2.0)


def show_fish():
    fish.pos = (random.randint(0, 1750), random.randint(500, 1000))
    clock.schedule(hide_fish, 5.0)


def show_fish2():
    fish2.pos = (random.randint(0, 1750), random.randint(500, 1000))
    clock.schedule(hide_fish2, 3.0)


def hide_text():
    global clicked
    clicked = False


def add_trophy():
    global trophy_no
    trophy_no = trophy_no + 1


def hide_trophy():
    show_trophy = False


def on_mouse_down(pos):
    global money
    global message
    global clicked
    global show_trophy
    global trophy_no
    global first_trophy
    if fish2.collidepoint(pos):
        money = money + (random.randint(50, 500))
        fish2.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money >= 5000:
            if not first_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                first_trophy = True
                show_trophy = True
        if money >= 50000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
        if money >= 500000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
        if money >= 1000000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()

    if fish.collidepoint(pos):
        money = money + (random.randint(25, 350))
        fish.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money >= 5000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
            first_trophy = True
            show_trophy = True
        if money >= 50000:
            clicked = True
            clock.schedule(hide_text, 3.0)
        if money >= 500000:
            clicked = True
            clock.schedule(hide_text, 3.0)
        if money >= 1000000:
            clicked = True
            clock.schedule(hide_text, 3.0)
