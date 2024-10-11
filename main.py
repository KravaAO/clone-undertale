from pygame import *
import time as t

init()

WIDTH = 500
HEIGHT = 500
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()
font1 = font.Font(None, 40)

text_list = 'Hello World!'


class TextPrinter:
    def __init__(self, text, font, speed=0.1, start_x=0, start_y=200):
        self.text = text
        self.font = font
        self.speed = speed
        self.x = start_x
        self.y = start_y
        self.index = 0
        self.start_time = t.time()

    def print_text(self, surface):
        new_time = t.time()
        if new_time - self.start_time > self.speed:
            if self.index < len(self.text):
                letter = self.font.render(f'{self.text[self.index]}', True, (255, 255, 255))
                letter_rect = letter.get_rect()
                surface.blit(letter, (self.x, self.y))
                self.x += letter_rect.width
                self.index += 1
                self.start_time = t.time()


printer = TextPrinter(text_list, font1)
test = TextPrinter('test1', font1, start_x=200, start_y=100)

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    printer.print_text(window)
    test.print_text(window)

    display.update()
    clock.tick(60)
