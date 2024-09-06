from pygame import *
import time as t

init()

WIDTH = 500
HEIGHT = 500
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
font1 = font.Font(None, 40)


start_time = t.time()
text_list = 'Hello World!'
x = 0
i=0


def print_text(text):
    global start_time, x, i
    new_time = t.time()
    if new_time - start_time > 0.1:
        if i < len(text):
            text = font1.render(f'{text[i]}', True, (255, 255, 255))
            text_rect = text.get_rect()
            window.blit(text, (x, 200))
            x += text_rect.width
            i += 1
            start_time = t.time()



while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    #window.fill((0, 0, 0))
    print_text('Hello World!')

    display.update()
    clock.tick(60)