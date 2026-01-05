import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)


    def draw(self, word, typed_text, score):
        self.screen.fill((30, 30, 30))


        word_surface = self.font.render(word, True, (255, 255, 255))
        input_surface = self.font.render(typed_text, True, (0, 200, 0))
        score_surface = self.font.render(f"Score: {score.score}", True, (200, 200, 0))


        self.screen.blit(word_surface, (50, 50))
        self.screen.blit(input_surface, (50, 150))
        self.screen.blit(score_surface, (50, 250))


        pygame.display.flip()