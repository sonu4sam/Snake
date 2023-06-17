import pygame
import sys
from grid import Grid
from food import Food
from score import Score
from snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.grid = Grid(40, 30)
        self.food = Food(10, 10)
        self.snake = Snake(20, 15)
        self.score = Score()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.move("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.move("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.move("RIGHT")

    def update(self):
        self.snake.update(self.grid.width, self.grid.height)
        if self.snake.collides_with_self() or self.snake.collides_with_boundary(self.grid.width, self.grid.height):
            self.game_over()
        elif self.snake.collides_with_food(self.food):
            self.snake.grow()
            self.food.regenerate(self.grid.width, self.grid.height)  # Move the food to a new random position
            self.score.update_score(10)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.grid.draw(self.screen)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()

    def game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (400, 300)  # Center of the screen
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before restarting
        self.restart_game()

    def restart_game(self):
        self.snake = Snake(20, 15)  # Resetting the snake by creating a new instance
        self.food = Food(10, 10)  # Resetting the food by creating a new instance
        self.score.reset()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(10)
