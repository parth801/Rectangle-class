import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("white")
pygame.display.update()

class Rectangle():
    def __init__(self, color, size):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = size
    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    green_rect = Rectangle("green", (100, 100, 50, 30))
    blue_rect = Rectangle("blue", ( 200, 200, 60, 30))
    red_rect = Rectangle("red", (300, 300, 70, 40))
    green_rect.draw()
    blue_rect.draw()
    red_rect.draw()
    pygame.display.update()
