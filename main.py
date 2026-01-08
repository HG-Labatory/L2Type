import pygame
from entities.player import Player
from entities.obstacle import Obstacle
from game.game_manager import GameManager

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Tipp-Lernspiel")
clock = pygame.time.Clock()

running = True

# player
player = Player(x=700, y=160, width=40, height=60, color="green")
obstacle = Obstacle(x=10, y=180, width=40, height=40, speed=200, color="red")

delta_time = clock.tick(60) / 1000

game_state = "ACTIVE"

# word
font = pygame.font.SysFont(None, 48)
word = "Hund"
typed_text = ""

while running:

    delta_time = clock.tick(60) / 1000
    # ---reset screen---
    screen.fill("black")

    # --- LOGIK ---
    if game_state == "ACTIVE":
        obstacle.x += obstacle.speed * delta_time # type: ignore

        if obstacle.x > 800:
            obstacle.x = -obstacle.width

    if game_state == "HIT":
        obstacle.x = -obstacle.width
        game_state = "ACTIVE"

    # ---word input-----
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            elif event.key != pygame.K_RETURN:
                if len(typed_text) < len(word):
                    typed_text += event.unicode
        if event.type == pygame.QUIT:
            running = False

    # ----word vergleich---
    if typed_text == word:
        obstacle.x = -obstacle.width
        typed_text = ""

    # --- RECTs (für Kollision & Zeichnen) ---

    if obstacle.get_rect().colliderect(player.get_rect()):
        game_state = "HIT"
        print("TREFFER")

    # --- ZEICHNEN ---

    player.draw(screen)
    obstacle.draw(screen)

    # ---draw text---
    word_surface = font.render(word, True, (255, 255, 255))
    input_surface = font.render(typed_text, True, (0, 200, 0))

    screen.blit(input_surface, (10, 10))
    screen.blit(word_surface, (10, 50))

    # ---update screen---
    pygame.display.flip()

pygame.quit()
