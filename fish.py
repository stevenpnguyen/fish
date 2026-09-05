import random
import time
import pygame
from playsound import playsound

pygame.init()


WIDTH = 1000
HEIGHT = 700
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2
money = -100
clicked = False
show = True
message = "You have unlocked this achievement"
message2 = "Click the fish avoid the sea snake goal get to level 2 achieve up to 4 trophies for every 5000"
show_trophy = False
bg = pygame.transform.scale(pygame.image.load("images/ocean.jpg").convert(), (WIDTH, HEIGHT))
bg2 = pygame.transform.scale(pygame.image.load("images/ocean_l2.jpg").convert(), (WIDTH, HEIGHT))
first_trophy = False
second_trophy = False
third_trophy = False
fourth_trophy = False
sea_snake = Actor("sea-snake.png")
sea_snake.pos = (random.randint(0, WIDTH), random.randint(0, 700))
whale = Actor("whale.png")
whale.pos = (random.randint(0, 1000), random.randint(0, 700))
penguin = Actor("penguin_sliding.png")
penguin.pos = (random.randint(0, 1000), random.randint(0, 700))
fish = Actor("fish.png")
fish.pos = (random.randint(0, 1000), random.randint(0, 700))
fish2 = Actor("fish2.png")
fish2.pos = (random.randint(0, 1000), random.randint(0, 700))
trophy_no = 0
fish_no = 1
trophy = Actor("trophy.png")
def draw():
    global trophy_no
    screen.blit(bg, (0, 0))
    sea_snake.draw()
    fish2.draw()
    fish.draw()
    if show:
        screen.draw.text(message2, (10, 10), fontsize=30, color="green")

    screen.draw.text("money:  " + str(money), fontsize=50, color="red", bottomleft=(10, 690))

    if show_trophy == True:
        trophy_x = WIDTH - 50;
        for no in range(trophy_no):
            trophy.draw()
            trophy.pos = (trophy_x, 50)
            trophy_x = trophy_x - 100

    if money >= 10000:
        screen.blit(bg2, (0, 0))
        whale.draw()
        penguin.draw()
        screen.draw.text("money:  " + str(money), fontsize=50, color="red", bottomleft=(10, 690))
        if clicked:
            screen.draw.text(message, (500, 50), fontsize=30, color="red")

    sea_snake.draw()
    fish2.draw()
    fish.draw()
    if show_trophy == True:
        trophy_x = WIDTH - 50;
        for no in range(trophy_no):
            trophy.draw()
            trophy.pos = (trophy_x, 50)
            trophy_x = trophy_x - 100

def update():

    fish.x -= 1
    fish2.x -= 2
    whale.x += 3.2
    penguin.x -= 2.9
    sea_snake.x -= 2

    clock.schedule(hide_text2, 50.0)

def hide_fish():
    fish.x = -1000
    clock.schedule(show_fish, 2.0)

def hide_fish2():
    fish2.x = -1000
    clock.schedule(show_fish2, 2.0)

def hide_whale():
    whale.x = -1000
    clock.schedule(show_whale, 2.0)

def hide_penguin():
    penguin.x = -1000
    clock.schedule(show_penguin, 2.0)

def hide_sea_snake():
    sea_snake.x = -1000
    clock.schedule(show_sea_snake, 2.0)

def show_fish():
    fish.pos = (random.randint(0, 1000), random.randint(0, 700))
    clock.schedule(hide_fish, 5.0)

def show_fish2():
    fish2.pos = (random.randint(0, 1000), random.randint(0, 700))
    clock.schedule(hide_fish2, 3.0)

def show_whale():
    whale.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    clock.schedule(hide_whale, 1.9)

def show_penguin():
    penguin.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    clock.schedule(hide_penguin, 2.5)

def show_sea_snake():
    sea_snake.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    clock.schedule(hide_sea_snake, 3.5)

def hide_text2():
    global show
    show = False

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
    global second_trophy
    global third_trophy
    global fourth_trophy
    if fish2.collidepoint(pos):
        sounds.coin.play()
        money = money + (random.randint(50, 1000))
        fish2.x -= 1 + 0.5
        fish2.pos = (random.randint(10, 1740), random.randint(330, 990))
        if money >= 5000:
            if not first_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                first_trophy = True
                show_trophy = True
        if money >= 10000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 15000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 20000:
            if not fourth_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                fourth_trophy = True
                show_trophy = True

    if fish.collidepoint(pos):
        sounds.coin.play()
        money = money + (random.randint(25, 500))
        fish.pos = (random.randint(10, 1740), random.randint(340, 990))
        fish.x -= 0.5 + 0.5
        if money >= 5000:
            if not first_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                first_trophy = True
                show_trophy = True
        if money >= 10000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 15000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 20000:
            if not fourth_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                fourth_trophy = True
                show_trophy = True

    if whale.collidepoint(pos):
        sounds.coin.play()
        money = money + (random.randint(600, 3500))
        whale.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money >= 10000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 15000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 20000:
            if not fourth_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                fourth_trophy = True
                show_trophy = True

    if penguin.collidepoint(pos):
        sounds.coin.play()
        money = money + (random.randint(500, 2540))
        penguin.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money >= 10000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 15000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 20000:
            if not fourth_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                fourth_trophy = True
                show_trophy = True

    if sea_snake.collidepoint(pos):
        sounds.wrong.play()
        money = money - (random.randint(25, 540))
        sea_snake.pos = (random.randint(10, 1740), random.randint(340, 990))

clock.schedule(hide_fish, 5.0)
clock.schedule(hide_fish2, 3.0)
clock.schedule(hide_whale, 1.9)
clock.schedule(hide_penguin, 2.5)
clock.schedule(hide_sea_snake, 3.5)

