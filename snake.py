import pygame

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 3
        self.body = [(x, y)]
        self.direction = "RIGHT"

    def move(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def update(self, grid_width, grid_height):
        if self.direction == "UP":
            self.y = (self.y - 1) % grid_height
        elif self.direction == "DOWN":
            self.y = (self.y + 1) % grid_height
        elif self.direction == "LEFT":
            self.x = (self.x - 1) % grid_width
        elif self.direction == "RIGHT":
            self.x = (self.x + 1) % grid_width
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, surface):
        cell_size = 20
        for x, y in self.body:
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def collides_with_self(self):
        return len(self.body) != len(set(self.body))

    def collides_with_boundary(self, width, height):
        return self.x < 0 or self.x >= width or self.y < 0 or self.y >= height

    def collides_with_food(self, food):
        return self.x == food.x and self.y == food.y

    def grow(self):
        self.length += 1

    def reset(self):
        self.x = 0
        self.y = 0
        self.length = 1
        self.body = [(self.x, self.y)]
        self.direction = "RIGHT"