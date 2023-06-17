import pygame
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
        self.snake.update()
        if self.snake.collides_with_self() or self.snake.collides_with_boundary(self.grid.width, self.grid.height):
            self.game_over()
        elif self.snake.collides_with_food(self.food):
            self.snake.grow()
            self.food = Food.generate_food(self.grid.width, self.grid.height)
            self.score.update_score(10)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.grid.draw(self.screen)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.flip()

    def game_over(self):
        # Display game over screen with final score and options to restart or quit
        pass

    def restart_game(self):
        self.snake.reset()
        self.food = Food.generate_food(self.grid.width, self.grid.height)
        self.score.reset()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(10)