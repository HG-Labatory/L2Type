import pygame
from game_state import GameStateManager
from input_handler import InputHandler
from word_manager import WordManager
from score_manager import ScoreManager
from renderer import Renderer


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Tipp-Lernspiel")
clock = pygame.time.Clock()


state = GameStateManager()
input_handler = InputHandler()
words = WordManager("words.txt")
score = ScoreManager()
renderer = Renderer(screen)


current_word = words.get_word()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print(event.type)
            input_handler.handle_event(event)

            if event.key == pygame.K_RETURN:
                if input_handler.text == current_word:
                    score.correct()
                else:
                    score.wrong()
                input_handler.reset()
                current_word = words.get_word()

    renderer.draw(current_word, input_handler.text, score)
    clock.tick(60)

pygame.quit()
