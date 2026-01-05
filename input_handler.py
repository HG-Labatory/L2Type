import pygame


class InputHandler:
    def __init__(self):
        self.text = ""

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                pass  # Enter wird im main.py behandelt
            else:
                self.text += event.unicode

    def reset(self):
        self.text = ""
