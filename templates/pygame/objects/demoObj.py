import pygame


class Object:
    def __init__(self):
        self.x = 100
        self.y = 100

    def update(self):
        pass  # Add update logic here

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 50, 50))
