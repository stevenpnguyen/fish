import random
import time
import pygame

pygame.init()

WIDTH = 1750
HEIGHT = 1000
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
money = 10
clicked = False
message = "You have unlocked this achievement"
show_trophy = False
bg = pygame.transform.scale(pygame.image.load("images/ocean.png").convert(), (WIDTH, HEIGHT))
fox = Actor("penguin")
fox.pos = (500, 300)
fish = Actor("fish")
fish2 = Actor("fish2")
fish2.pos = (random.randint(0, 1750), random.randint(500, 1000))
fish.pos = (random.randint(0, 1750), random.randint(500, 1000))
trophy = Actor("trophy")
trophy_no = 0

def draw():
    global trophy_no
    screen.blit(bg, (0, 0))
    fox.draw()
    fish.draw()
    fish2.draw()
    screen.draw.text("money:  " + str(money), color="black", bottomleft=(10, 990))
    if clicked:
        screen.draw.text(message, (300, 10), fontsize=30, color="black")
    if show_trophy == True:
        trophy_x = 950;
        for no in range(trophy_no):
    # Code to execute for each item
            trophy.draw()
            trophy.pos = (trophy_x, 50)
            trophy_x = trophy_x - 100

def update():
    if keyboard.right:
        fox.x += 5
    elif keyboard.left:
        fox.x -= 5


def hide_text():
    global clicked
    clicked = False

def add_trophy():
    global trophy_no
    trophy_no = trophy_no + 1


def on_mouse_down(pos):
    global money
    global message
    global clicked
    global show_trophy
    global trophy_no
    if fish2.collidepoint(pos):
        money = money + 250
        fish2.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money >= 500:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
            show_trophy = True
        if money >= 1000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
        if money >= 5000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
        if money >= 10000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()

    if fish.collidepoint(pos):
        money = money + 100
        fish.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money == 500:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
            show_trophy = True
        if money == 1000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
        if money == 5000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()
        if money == 10000:
            clicked = True
            clock.schedule(hide_text, 3.0)
            add_trophy()

