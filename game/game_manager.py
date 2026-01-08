class GameManager:
    def __init__(self, player, obstacle, word):
        # Spielzustand
        self.state = "SPAWN"  # SPAWN, ACTIVE, SUCCESS, HIT, GAME_OVER
        self.state_timer = 0.0

        # Spielobjekte
        self.player = player
        self.obstacle = obstacle
        self.word = word

        # Spielwerte
        self.lives = 3

    def update(self, delta_time):
        # Timer läuft IMMER für den aktuellen Zustand
        self.state_timer += delta_time

        if self.state == "SPAWN":
            self._spawn()

        elif self.state == "ACTIVE":
            self._active(delta_time)

        elif self.state == "SUCCESS":
            self._success()

        elif self.state == "HIT":
            self._hit()

        elif self.state == "GAME_OVER":
            pass  # nichts tun

    # ---------------- STATES ----------------

    def _spawn(self):
        # Neue Runde vorbereiten
        self.word.reset()
        self.obstacle.reset()
        self.player.set_idle()

        # Timer zurücksetzen
        self.state_timer = 0.0

        # Sofort spielen
        self.state = "ACTIVE"

    def _active(self, delta_time):
        # Hindernis bewegt sich
        self.obstacle.update(delta_time)

        # WORT ZUERST prüfen (Fairness!)
        if self.word.is_completed():
            self.state = "SUCCESS"
            self.state_timer = 0.0
            self.player.dodge()
            return

        # DANACH prüfen: Treffer
        if self.obstacle.hit_player(self.player):
            self.state = "HIT"
            self.state_timer = 0.0
            self.player.hit()
            return

    def _success(self):
        # Ausweichen dauert 0.4 Sekunden
        if self.state_timer >= 0.4:
            self.state = "SPAWN"
            self.state_timer = 0.0

    def _hit(self):
        # Trefferreaktion dauert 0.5 Sekunden
        if self.state_timer >= 0.5:
            self.lives -= 1

            if self.lives > 0:
                self.state = "SPAWN"
            else:
                self.state = "GAME_OVER"

            self.state_timer = 0.0
