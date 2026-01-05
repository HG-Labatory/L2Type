class InputHandler:
    def __init__(self):
        self.text = ""


    def handle_event(self, event):
        if event.type == event.KEYDOWN:
            if event.key == event.K_BACKSPACE:
            self.text = self.text[:-1]
        elif event.key != event.K_RETURN:
            self.text += event.unicode


    def reset(self):
    self.text = ""