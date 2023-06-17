import pygame
import random

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        cell_size = 20
        rect = pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)

    @staticmethod
    def generate_food(width, height):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        return Food(x, y)