class GameStateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name):
        if name in self.states:
            self.current_state = self.states[name]
        else:
            raise ValueError(f"State '{name}' does not exist.")

    def get_current_state(self):
        return self.current_state
    
    