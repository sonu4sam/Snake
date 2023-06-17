import pygame

class Controls:
    def __init__(self):
        self.key_mapping = {
            pygame.K_UP: "UP",
            pygame.K_DOWN: "DOWN",
            pygame.K_LEFT: "LEFT",
            pygame.K_RIGHT: "RIGHT"
        }

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_mapping:
                    direction = self.key_mapping[event.key]
                    self.snake.move(direction)