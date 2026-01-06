"""
Constants and configuration for Paranormal Investigations
"""

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
BROWN = (139, 69, 19)
DARK_BROWN = (101, 67, 33)
CREAM = (255, 253, 208)
SEPIA = (112, 66, 20)

# UI Colors
MENU_BG = (20, 20, 30)
MENU_HOVER = (40, 40, 60)
BUTTON_COLOR = (60, 60, 80)
BUTTON_HOVER = (80, 80, 100)
HIGHLIGHT_COLOR = (255, 255, 100, 128)

# Game states
STATE_MENU = "menu"
STATE_SETTINGS = "settings"
STATE_CREDITS = "credits"
STATE_DIFFICULTY = "difficulty"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_NOTEBOOK = "notebook"
STATE_GHOST_BOOK = "ghost_book"
STATE_IDENTIFY = "identify"
STATE_JUMPSCARE = "jumpscare"
STATE_GAME_OVER = "game_over"
STATE_VICTORY = "victory"
STATE_ZOOM = "zoom"

# Difficulty settings
DIFFICULTY_EASY = "easy"
DIFFICULTY_NORMAL = "normal"
DIFFICULTY_HARD = "hard"
DIFFICULTY_NIGHTMARE = "nightmare"

DIFFICULTY_SETTINGS = {
    DIFFICULTY_EASY: {
        "name": "Easy",
        "guesses": 3,
        "time_multiplier": 1.5,
        "aggression_rate": 0.5,
        "grace_period": (30, 50),
    },
    DIFFICULTY_NORMAL: {
        "name": "Normal",
        "guesses": 2,
        "time_multiplier": 1.0,
        "aggression_rate": 1.0,
        "grace_period": (20, 40),
    },
    DIFFICULTY_HARD: {
        "name": "Hard",
        "guesses": 1,
        "time_multiplier": 0.7,
        "aggression_rate": 1.5,
        "grace_period": (10, 30),
    },
    DIFFICULTY_NIGHTMARE: {
        "name": "Nightmare",
        "guesses": 1,
        "time_multiplier": 0.5,
        "aggression_rate": 2.0,
        "grace_period": (10, 20),
    },
}

# Room names
ROOM_ENTRANCE = "entrance"
ROOM_LIVING_ROOM = "living_room"
ROOM_KITCHEN = "kitchen"
ROOM_DINING_ROOM = "dining_room"
ROOM_HALLWAY = "hallway"
ROOM_BEDROOM = "bedroom"
ROOM_BATHROOM = "bathroom"
ROOM_STUDY = "study"
ROOM_ATTIC = "attic"
ROOM_BASEMENT = "basement"

# Navigation edge size
EDGE_SIZE = 80

# Flashlight settings
FLASHLIGHT_RADIUS = 150
FLASHLIGHT_OUTER_RADIUS = 200

# Jumpscare settings
JUMPSCARE_FLASH_PROBABILITY = 0.7
JUMPSCARE_DURATION = 3.0

# Ghost behavior settings
BEHAVIOR_MIN_INTERVAL = 5
BEHAVIOR_MAX_INTERVAL = 30
BEHAVIOR_AGGRESSION_FACTOR = 25
BEHAVIOR_MIN_DURATION = 2.0
BEHAVIOR_MAX_DURATION = 5.0
MAX_ACTIVE_EFFECTS = 5

# Evidence categories
EVIDENCE_COLD = "cold_evidence"
EVIDENCE_LIGHTS = "light_evidence"
EVIDENCE_OBJECTS = "object_evidence"
EVIDENCE_SOUNDS = "sound_evidence"
EVIDENCE_VISUAL = "visual_evidence"
EVIDENCE_WATER = "water_evidence"

# Font sizes
FONT_SMALL = 16
FONT_MEDIUM = 24
FONT_LARGE = 36
FONT_TITLE = 72

# FPS
FPS = 60
