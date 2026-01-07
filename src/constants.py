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
STATE_JUMPSCARE_GALLERY = "jumpscare_gallery"  # NEW: View jumpscares mode

# Difficulty settings
DIFFICULTY_EASY = "easy"
DIFFICULTY_NORMAL = "normal"
DIFFICULTY_HARD = "hard"
DIFFICULTY_NIGHTMARE = "nightmare"

DIFFICULTY_SETTINGS = {
    DIFFICULTY_EASY: {
        "name": "Easy",
        "guesses": 3,
        "time_multiplier": 1.3,  # Reduced from 1.5
        "aggression_rate": 0.5,
        "grace_period": (20, 35),  # Reduced from (30, 50)
        "equipment_slots": 2,  # Can carry 2 equipment
    },
    DIFFICULTY_NORMAL: {
        "name": "Normal",
        "guesses": 2,
        "time_multiplier": 1.0,
        "aggression_rate": 1.0,
        "grace_period": (15, 25),  # Reduced from (20, 40)
        "equipment_slots": 2,  # Can carry 2 equipment
    },
    DIFFICULTY_HARD: {
        "name": "Hard",
        "guesses": 1,
        "time_multiplier": 0.65,  # Reduced from 0.7
        "aggression_rate": 1.5,
        "grace_period": (10, 20),  # Unchanged
        "equipment_slots": 1,  # Can only carry 1 equipment
    },
    DIFFICULTY_NIGHTMARE: {
        "name": "Nightmare",
        "guesses": 1,
        "time_multiplier": 0.45,  # Reduced from 0.5
        "aggression_rate": 2.0,
        "grace_period": (5, 15),  # Reduced lower bound
        "equipment_slots": 1,  # Can only carry 1 equipment
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
BEHAVIOR_MIN_INTERVAL = 8  # Increased from 5 - slower behaviors
BEHAVIOR_MAX_INTERVAL = 35  # Increased from 30
BEHAVIOR_AGGRESSION_FACTOR = 30  # Increased from 25 - slower scaling
BEHAVIOR_MIN_DURATION = 2.0
BEHAVIOR_MAX_DURATION = 5.0
MAX_ACTIVE_EFFECTS = 5

# Ghost hint balance
GHOST_HINT_BASE_CHANCE = 0.0008  # Reduced from 0.005 (~0.5 hints per minute)
GHOST_HINT_AGGRESSION_MULTIPLIER = 2.0  # More hints when aggressive

# Evidence collection balance
EVIDENCE_CHANCE_EXAMINE = 0.15  # 15% on regular examine
EVIDENCE_CHANCE_ZOOM = 0.25  # 25% on zoom (more thorough)
EVIDENCE_CHANCE_AFFECTED = 0.40  # 40% if ghost affected this object
EVIDENCE_CHANCE_EQUIPMENT = 0.20  # 20% additional with relevant equipment

# Wrong guess penalties
WRONG_GUESS_AGGRESSION_1 = 0.15  # First wrong guess
WRONG_GUESS_AGGRESSION_2 = 0.3  # Second wrong guess
WRONG_GUESS_BLIND_1 = 1.5  # Blind duration for first wrong
WRONG_GUESS_BLIND_2 = 2.5  # Blind duration for second wrong
WRONG_GUESS_TIME_PENALTY_1 = 30  # Lose 30 seconds
WRONG_GUESS_TIME_PENALTY_2 = 60  # Lose 60 seconds

# Ghost effect visual settings
GHOST_EFFECT_DURATION = 20.0  # Reduced from 30
GHOST_EFFECT_FADE_START = 15.0  # Start fading at 15s
GHOST_AFFECTED_COLOR = (200, 100, 100, 50)  # Subtler red highlight

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

# === NEW FEATURES ===

# Equipment types
EQUIPMENT_FLASHLIGHT = "flashlight"
EQUIPMENT_EMF = "emf_reader"
EQUIPMENT_THERMOMETER = "thermometer"
EQUIPMENT_SPIRIT_BOX = "spirit_box"
EQUIPMENT_UV_LIGHT = "uv_light"
EQUIPMENT_CAMERA = "camera"

# Flashlight battery
FLASHLIGHT_BATTERY_MAX = 100
FLASHLIGHT_DRAIN_RATE = 3.5  # Increased from 2.0 - drains faster
FLASHLIGHT_FLICKER_THRESHOLD = 20  # Battery level when flickering starts
FLASHLIGHT_GHOST_DRAIN_MULTIPLIER = 2.5  # Increased from 2.0

# EMF balance
EMF_FALSE_POSITIVE_CHANCE = 0.15  # 15% chance of false spike

# Thermometer balance
TEMP_CHANGE_SPEED = 1.0  # Reduced from 2.0 (half as responsive)

# Spirit box balance
SPIRIT_BOX_RESPONSE_COOLDOWN = 5.0  # Must wait 5s between responses

# EMF levels
EMF_LEVEL_0 = 0  # No activity
EMF_LEVEL_1 = 1  # Minimal
EMF_LEVEL_2 = 2  # Low
EMF_LEVEL_3 = 3  # Medium
EMF_LEVEL_4 = 4  # High
EMF_LEVEL_5 = 5  # Extreme (ghost nearby!)

# Temperature ranges (Fahrenheit)
TEMP_NORMAL_MIN = 65
TEMP_NORMAL_MAX = 75
TEMP_COLD_MIN = 32
TEMP_COLD_MAX = 50
TEMP_FREEZING = 28  # Ghost freezing temp indicator

# Particle types
PARTICLE_DUST = "dust"
PARTICLE_FOG = "fog"
PARTICLE_RAIN = "rain"
PARTICLE_ORBS = "orbs"
PARTICLE_BREATH = "breath"

# Tutorial state
STATE_TUTORIAL = "tutorial"

# New game states
STATE_EQUIPMENT = "equipment"
STATE_DEATH_RECAP = "death_recap"

# Achievement categories
ACHIEVEMENT_FIRST_GHOST = "first_ghost"
ACHIEVEMENT_SPEED_RUN = "speed_run"
ACHIEVEMENT_NO_FLASHLIGHT = "no_flashlight"
ACHIEVEMENT_ALL_EVIDENCE = "all_evidence"
ACHIEVEMENT_SURVIVOR = "survivor"
ACHIEVEMENT_NIGHTMARE_WIN = "nightmare_win"

# Ghost hints/whispers
GHOST_HINTS = {
    "Bonnie": ["...the fire... it hurts...", "...my face... don't look...", "...performer..."],
    "Poltergeist": ["...everything must move...", "...chaos...", "...throw it all..."],
    "Weeping Lady": ["...my love... where are you...", "...tears... so many tears...", "...the wedding..."],
    "Shadow Stalker": ["...in the darkness...", "...watching... always watching...", "...corners..."],
    "Little Timmy": ["...wanna play?...", "...hide and seek...", "...toys..."],
    "The Butcher": ["...meat... fresh meat...", "...the cleaver...", "...kitchen..."],
    "Ethereal Bride": ["...my wedding day...", "...he never came...", "...waiting forever..."],
    "The Librarian": ["...silence!...", "...the books must be quiet...", "...shhhh..."],
    "Nightmare": ["...your fears...", "...I see everything...", "...reality bends..."],
    "The Collector": ["...so many things...", "...mine... all mine...", "...precious items..."],
    "The Burned Man": ["...the flames...", "...I can still feel it...", "...burn with me..."],
    "The Doll": ["...play with me...", "...don't leave me alone...", "...I'm a good girl..."],
    "The Hanged Man": ["...the rope... so tight...", "...they made me do it...", "...look up..."],
    "The Mimic": ["...I know your face...", "...who are you really?...", "...let me in..."],
    "The Nurse": ["...time for your medicine...", "...this won't hurt...", "...visiting hours are over..."]
}

# Minimap settings
MINIMAP_SIZE = 150
MINIMAP_MARGIN = 10
MINIMAP_ALPHA = 180

# Ambient event probabilities
AMBIENT_CREAK_CHANCE = 0.002  # Per frame
AMBIENT_THUNDER_CHANCE = 0.0005
AMBIENT_WHISPER_CHANCE = 0.001

# Colors for new features
EMF_COLOR = (0, 255, 0)
COLD_COLOR = (100, 150, 255)
EQUIPMENT_BG = (30, 30, 40, 200)
