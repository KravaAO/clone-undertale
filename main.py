import time

from pygame import *

init()


class GameSprite:
    def __init__(self, img, x, y, width, height):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


def update():
    speed = 5
    keys = key.get_pressed()
    if keys[K_w] and player.rect.y >= 165:
        player.rect.y -= speed
    if keys[K_s] and player.rect.y <= 355:
        player.rect.y += speed
    if keys[K_a] and player.rect.x >= 190:
        player.rect.x -= speed
    if keys[K_d] and player.rect.x <= 380:
        player.rect.x += speed


size = 600, 600
window = display.set_mode(size)
clock = time.Clock()

scene = GameSprite('scene.png', 180, 150, 250, 250)
player = GameSprite('heart.png', 200, 200, 40, 30)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.fill((0, 0, 0))
    scene.reset()
    player.reset()
    update()

    display.update()
    clock.tick(60)
