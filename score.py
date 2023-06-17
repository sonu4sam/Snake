import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.timer = 0
        self.font = pygame.font.Font(None, 36)

    def update_score(self, points):
        self.score += points

    def start_timer(self):
        self.timer = pygame.time.get_ticks()

    def stop_timer(self):
        self.timer = 0

    def get_elapsed_time(self):
        if self.timer > 0:
            return (pygame.time.get_ticks() - self.timer) // 1000
        return 0

    def draw(self, surface):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        time_text = self.font.render(f"Time: {self.get_elapsed_time()}", True, (0, 0, 0))
        surface.blit(score_text, (10, 10))
        surface.blit(time_text, (10, 50))