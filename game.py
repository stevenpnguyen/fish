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
bg2 = None
fox = None
fish = None
fish2 = None
whale = None
penguin = None
trophy = None
trophy_no = 0
first_trophy = False
second_trophy = False
third_trophy = False
fourth_trophy = False


def init():
    global bg, bg2, fox, fish, fish2, whale, penguin, trophy
    bg = pygame.transform.scale(
        pygame.image.load("images/ocean.png").convert(), (WIDTH, HEIGHT)
    )
    bg2 = pygame.transform.scale(
        pygame.image.load("images/ocean_l2.jpg").convert(), (WIDTH, HEIGHT)
    )
    fox = Actor("penguin")
    fox.pos = (875, 300)
    fish = Actor("fish")
    fish.pos = (random.randint(0, 1750), random.randint(500, 1000))
    fish2 = Actor("fish2")
    fish2.pos = (random.randint(0, 1750), random.randint(500, 1000))
    whale = Actor("whale.png")
    whale.pos = (random.randint(0, 1750), random.randint(500, 1000))
    penguin = Actor("penguin_sliding.png")
    penguin.pos = (random.randint(0, 1750), random.randint(500, 1000))
    trophy = Actor("trophy")
    clock.schedule(hide_fish, 5.0)
    clock.schedule(hide_fish2, 3.0)
    clock.schedule(hide_whale, 1.9)
    clock.schedule(hide_penguin, 2.5)


def draw():
    if bg is None:
        init()
    screen.blit(bg, (0, 0))
    if money >= 10000:
        screen.blit(bg2, (0, 0))
        if whale.x != -1000:
            whale.draw()
        if penguin.x != -1000:
            penguin.draw()
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
    whale.x += 4
    penguin.x -= 3


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


def hide_whale():
    whale.x = -1000
    clock.schedule(show_whale, 2.0)


def hide_penguin():
    penguin.x = -1000
    clock.schedule(show_penguin, 2.0)


def show_whale():
    whale.pos = (random.randint(0, 1750), random.randint(500, 1000))
    clock.schedule(hide_whale, 1.9)


def show_penguin():
    penguin.pos = (random.randint(0, 1750), random.randint(500, 1000))
    clock.schedule(hide_penguin, 2.5)


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
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 500000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 1000000:
            if not fourth_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                fourth_trophy = True
                show_trophy = True

    if fish.collidepoint(pos):
        sounds.coin.play()
        money = money + (random.randint(25, 350))
        fish.pos = (random.randint(10, 1740), random.randint(340, 990))
        if money >= 5000:
            if not first_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                first_trophy = True
                show_trophy = True
        if money >= 50000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 500000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 1000000:
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
        if money >= 50000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 500000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 1000000:
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
        if money >= 50000:
            if not second_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                second_trophy = True
                show_trophy = True
        if money >= 500000:
            if not third_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                third_trophy = True
                show_trophy = True
        if money >= 1000000:
            if not fourth_trophy:
                clicked = True
                clock.schedule(hide_text, 3.0)
                add_trophy()
                fourth_trophy = True
                show_trophy = True
