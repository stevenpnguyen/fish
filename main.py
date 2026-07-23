import asyncio
import pygame
import game

pygame.init()
screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
clock = pygame.time.Clock()


class Actor:
    def __init__(self, image_name):
        if not image_name.endswith(".png"):
            image_name += ".png"
        self.image = pygame.image.load(f"images/{image_name}").convert_alpha()
        self.rect = self.image.get_rect()

    @property
    def x(self):
        return self.rect.centerx

    @x.setter
    def x(self, val):
        self.rect.centerx = val

    @property
    def y(self):
        return self.rect.centery

    @y.setter
    def y(self, val):
        self.rect.centery = val

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, val):
        self.rect.center = val

    def draw(self):
        screen.blit(self.image, self.rect)

    def colliderect(self, other):
        return self.rect.colliderect(other.rect)


class Keyboard:
    def __init__(self):
        self._keys = pygame.key.get_pressed()

    def update(self):
        self._keys = pygame.key.get_pressed()

    @property
    def right(self):
        return self._keys[pygame.K_RIGHT]

    @property
    def left(self):
        return self._keys[pygame.K_LEFT]


game.screen = screen
game.Actor = Actor
keyboard = Keyboard()
game.keyboard = keyboard

game.init()


def draw():
    game.draw()


def update():
    keyboard.update()
    game.update()


async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        update()
        draw()
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())
