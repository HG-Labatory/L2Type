
```bash

typing_dodge_game/
│
├── main.py              # Startpunkt & Game Loop
│
├── game/
│   ├── game_state.py    # Spielzustände (START, ACTIVE, ...)
│   ├── game_manager.py  # Orchestriert alles
│
├── entities/
│   ├── player.py        # Männchen + Player-Zustände
│   ├── obstacle.py      # Hindernis + Bewegung
│
├── typing/
│   ├── word.py          # Aktuelles Wort + Vergleichslogik
│   └── input_handler.py   # Getippter Text (keine Grafik!)
│
├── render/
│   └── renderer.py      # Alles, was gezeichnet wird
│
└── data/
    └── words.txt

```
