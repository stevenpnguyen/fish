import pygame
from random import randint

WIDTH = 1000
HEIGHT = 800
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

bg = None
fox = None
fish = None
fish_list = []


def init():
    global bg, fox, fish
    bg = pygame.transform.scale(
        pygame.image.load("images/ocean.png").convert(), (WIDTH, HEIGHT)
    )
    fox = Actor("fox.png")
    fox.pos = 500, 200
    fish = Actor("fish")


def draw():
    if bg is None:
        init()
    screen.blit(bg, (0, 0))
    fox.draw()
    fish.draw()


def update():
    if keyboard.right:
        fox.x += 5
    elif keyboard.left:
        fox.x -= 5


def new_fish():
    global fish_list
    fish_new = Actor("fish")
    fish_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    fish_list.append(fish_new)


def catch():
    fish_caught = fox.colliderect(fish)
    if fish_caught:
        print("You caught a fsh")
