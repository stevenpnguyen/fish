import asyncio
import pygame
import game

pygame.init()
screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
clock = pygame.time.Clock()


class DrawShim:
    def __init__(self, surface):
        self._surface = surface

    def text(self, text, pos=(0, 0), color="white", fontsize=28, **kwargs):
        font = pygame.font.Font(None, fontsize)
        image = font.render(str(text), True, pygame.Color(color))
        x, y = pos
        if "bottomleft" in kwargs:
            x, y = kwargs["bottomleft"]
            y -= image.get_height()
        elif "topleft" in kwargs:
            x, y = kwargs["topleft"]
        self._surface.blit(image, (x, y))


class ScreenShim:
    def __init__(self, surface):
        self._surface = surface
        self.draw = DrawShim(surface)

    def blit(self, *args, **kwargs):
        self._surface.blit(*args, **kwargs)


class GameClock:
    def __init__(self):
        self._events = []

    def schedule(self, callback, seconds):
        self._events.append((pygame.time.get_ticks() + seconds * 1000, callback))

    def update(self):
        now = pygame.time.get_ticks()
        due = [callback for (at, callback) in self._events if at <= now]
        self._events = [(at, callback) for (at, callback) in self._events if at > now]
        for callback in due:
            callback()


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

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)


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

    @property
    def down(self):
        return self._keys[pygame.K_DOWN]


class Sounds:
    def __init__(self):
        self.coin = pygame.mixer.Sound("sounds/coin.ogg")
        self.wrong = pygame.mixer.Sound("sounds/wrong.ogg")


game.screen = ScreenShim(screen)
game.Actor = Actor
keyboard = Keyboard()
game.keyboard = keyboard
game.clock = GameClock()
game.sounds = Sounds()

game.init()


def draw():
    game.draw()


def update():
    keyboard.update()
    game.clock.update()
    game.update()


async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.on_mouse_down(event.pos)
        update()
        draw()
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)


asyncio.run(main())
