"""
Location definitions for Paranormal Investigations
Each location has multiple rooms and a set of themed ghosts
"""

from constants import *

# Location identifiers
LOCATION_HAUNTED_HOUSE = "haunted_house"
LOCATION_HOSPITAL = "hospital"
LOCATION_PRISON = "prison"
LOCATION_SCHOOL = "school"
LOCATION_CEMETERY = "cemetery"
LOCATION_ASYLUM = "asylum"
LOCATION_HOTEL = "hotel"
LOCATION_LIGHTHOUSE = "lighthouse"
LOCATION_MANSION = "mansion"
LOCATION_FARMHOUSE = "farmhouse"
LOCATION_CHURCH = "church"
LOCATION_THEATER = "theater"
LOCATION_FACTORY = "factory"
LOCATION_SHIP = "ship"
LOCATION_BUNKER = "bunker"
LOCATION_MINE = "mine"
LOCATION_TRAIN_STATION = "train_station"
LOCATION_MALL = "mall"
LOCATION_LIBRARY = "library"
LOCATION_MUSEUM = "museum"

# Location metadata
LOCATIONS = {
    LOCATION_HAUNTED_HOUSE: {
        "name": "Haunted House",
        "description": "An old Victorian house with a dark history. Includes indoor rooms and a creepy backyard.",
        "color": (90, 70, 60),
        "ghosts": ["Bonnie", "Poltergeist", "Weeping Lady", "Shadow Stalker", "Little Timmy", 
                   "The Butcher", "Ethereal Bride", "The Librarian", "Nightmare", "The Collector",
                   "The Burned Man", "The Doll", "The Hanged Man", "The Mimic", "The Gardener"],
        "difficulty_bonus": 0,
        "has_outdoor": True,
    },
    LOCATION_HOSPITAL: {
        "name": "Abandoned Hospital",
        "description": "A derelict medical facility where patients suffered and died. Medical equipment still hums with ghostly energy.",
        "color": (200, 200, 210),
        "ghosts": ["The Nurse", "The Doctor", "The Plague Doctor", "Nightmare", "Shadow Stalker",
                   "Weeping Lady", "The Mimic", "The Collector"],
        "difficulty_bonus": 0.1,
        "has_outdoor": False,
    },
    LOCATION_PRISON: {
        "name": "Old Prison",
        "description": "A maximum security prison that was shut down after a violent riot. The cells still echo with screams.",
        "color": (60, 60, 65),
        "ghosts": ["The Jailer", "The Hanged Man", "Shadow Stalker", "The Butcher", "Nightmare",
                   "Poltergeist", "The Arsonist"],
        "difficulty_bonus": 0.15,
        "has_outdoor": True,
    },
    LOCATION_SCHOOL: {
        "name": "Haunted School",
        "description": "An elementary school closed after a tragic incident. Children's laughter still echoes in the halls.",
        "color": (180, 160, 140),
        "ghosts": ["The Teacher", "Little Timmy", "The Twins", "The Doll", "Poltergeist",
                   "The Librarian", "The Jester"],
        "difficulty_bonus": 0,
        "has_outdoor": True,
    },
    LOCATION_CEMETERY: {
        "name": "Cemetery & Mausoleum",
        "description": "An ancient graveyard with a family mausoleum. The dead here do not rest peacefully.",
        "color": (50, 55, 50),
        "ghosts": ["Weeping Lady", "The Preacher", "Nightmare", "Shadow Stalker", "The Collector",
                   "The Gravedigger", "Ethereal Bride"],
        "difficulty_bonus": 0.1,
        "has_outdoor": True,
    },
    LOCATION_ASYLUM: {
        "name": "Abandoned Asylum",
        "description": "A psychiatric hospital known for inhumane treatments. The walls remember the suffering.",
        "color": (170, 180, 175),
        "ghosts": ["The Doctor", "Nightmare", "The Mimic", "Shadow Stalker", "The Nurse",
                   "Poltergeist", "The Hanged Man", "The Twins"],
        "difficulty_bonus": 0.2,
        "has_outdoor": False,
    },
    LOCATION_HOTEL: {
        "name": "Old Hotel",
        "description": "A once-grand hotel where a famous murder took place. Room 237 is always cold.",
        "color": (120, 90, 90),
        "ghosts": ["Ethereal Bride", "The Collector", "The Drunkard", "The Servant", "Shadow Stalker",
                   "The Butcher", "Nightmare", "The Mimic"],
        "difficulty_bonus": 0.1,
        "has_outdoor": False,
    },
    LOCATION_LIGHTHOUSE: {
        "name": "Lighthouse",
        "description": "A remote lighthouse where the keeper vanished. The light still turns at night.",
        "color": (100, 120, 140),
        "ghosts": ["The Drowned", "Shadow Stalker", "The Mariner", "Nightmare", "Weeping Lady"],
        "difficulty_bonus": 0.05,
        "has_outdoor": True,
    },
    LOCATION_MANSION: {
        "name": "Victorian Mansion",
        "description": "A wealthy family's estate with dark secrets hidden in every room.",
        "color": (100, 80, 70),
        "ghosts": ["The Librarian", "Ethereal Bride", "The Collector", "The Servant", "Shadow Stalker",
                   "Nightmare", "The Artist", "Poltergeist", "The Butcher"],
        "difficulty_bonus": 0.15,
        "has_outdoor": True,
    },
    LOCATION_FARMHOUSE: {
        "name": "Farmhouse",
        "description": "A remote farm where the family disappeared one autumn night. Scarecrows watch the fields.",
        "color": (140, 120, 90),
        "ghosts": ["The Gardener", "The Butcher", "The Scarecrow", "Shadow Stalker", "The Twins",
                   "Little Timmy", "Poltergeist"],
        "difficulty_bonus": 0.1,
        "has_outdoor": True,
    },
    LOCATION_CHURCH: {
        "name": "Old Church",
        "description": "A deconsecrated church where unholy rituals were performed. The bells ring at midnight.",
        "color": (80, 70, 65),
        "ghosts": ["The Preacher", "The Witch", "The Choir", "Shadow Stalker", "Nightmare",
                   "Ethereal Bride", "Weeping Lady"],
        "difficulty_bonus": 0.15,
        "has_outdoor": True,
    },
    LOCATION_THEATER: {
        "name": "Abandoned Theater",
        "description": "An opera house where the lead actress died on stage. The show must go on.",
        "color": (130, 50, 50),
        "ghosts": ["The Musician", "The Artist", "The Jester", "Ethereal Bride", "Nightmare",
                   "The Collector", "Shadow Stalker", "Poltergeist"],
        "difficulty_bonus": 0.1,
        "has_outdoor": False,
    },
    LOCATION_FACTORY: {
        "name": "Old Factory",
        "description": "An industrial complex where workers died in a fire. Machines still operate at night.",
        "color": (70, 65, 60),
        "ghosts": ["The Burned Man", "The Arsonist", "The Worker", "Shadow Stalker", "Poltergeist",
                   "The Foreman", "Nightmare"],
        "difficulty_bonus": 0.15,
        "has_outdoor": True,
    },
    LOCATION_SHIP: {
        "name": "Ghost Ship",
        "description": "A cargo vessel found adrift with no crew. Something lurks in the hold.",
        "color": (60, 80, 90),
        "ghosts": ["The Drowned", "The Captain", "The Sailor", "Shadow Stalker", "The Stowaway",
                   "Nightmare", "Poltergeist"],
        "difficulty_bonus": 0.2,
        "has_outdoor": True,
    },
    LOCATION_BUNKER: {
        "name": "Underground Bunker",
        "description": "A Cold War bunker where soldiers waited for an attack that never came. Or did it?",
        "color": (55, 60, 55),
        "ghosts": ["The Soldier", "Shadow Stalker", "The General", "Nightmare", "The Radio Operator",
                   "Poltergeist"],
        "difficulty_bonus": 0.2,
        "has_outdoor": False,
    },
    LOCATION_MINE: {
        "name": "Abandoned Mine",
        "description": "A collapsed mine where dozens of workers were trapped. Their lights still flicker below.",
        "color": (45, 40, 35),
        "ghosts": ["The Miner", "Shadow Stalker", "The Canary", "Nightmare", "The Foreman",
                   "Poltergeist", "The Burned Man"],
        "difficulty_bonus": 0.25,
        "has_outdoor": True,
    },
    LOCATION_TRAIN_STATION: {
        "name": "Train Station",
        "description": "An old station where a tragic collision occurred. Trains still arrive at midnight.",
        "color": (90, 80, 70),
        "ghosts": ["The Conductor", "The Waiting Woman", "The Hobo", "Shadow Stalker", "Weeping Lady",
                   "Nightmare", "The Collector"],
        "difficulty_bonus": 0.1,
        "has_outdoor": True,
    },
    LOCATION_MALL: {
        "name": "Abandoned Mall",
        "description": "A shopping center that closed after several disappearances. Mannequins watch from every window.",
        "color": (180, 180, 185),
        "ghosts": ["The Thief", "The Gambler", "The Mannequin", "Shadow Stalker", "The Jester",
                   "Poltergeist", "Nightmare", "The Collector"],
        "difficulty_bonus": 0.1,
        "has_outdoor": False,
    },
    LOCATION_LIBRARY: {
        "name": "Old Library",
        "description": "A vast library with forbidden texts. Knowledge has a price.",
        "color": (100, 90, 75),
        "ghosts": ["The Librarian", "The Scholar", "The Archivist", "Shadow Stalker", "Nightmare",
                   "The Witch", "The Collector"],
        "difficulty_bonus": 0.1,
        "has_outdoor": False,
    },
    LOCATION_MUSEUM: {
        "name": "Museum",
        "description": "A natural history museum with cursed artifacts. The exhibits come alive at night.",
        "color": (160, 150, 140),
        "ghosts": ["The Collector", "The Artist", "The Pharaoh", "The Mummy", "Shadow Stalker",
                   "Nightmare", "The Curator", "Poltergeist"],
        "difficulty_bonus": 0.15,
        "has_outdoor": False,
    },
}

# Room definitions for each location
# These will be expanded in the rooms.py file
LOCATION_ROOMS = {
    LOCATION_HAUNTED_HOUSE: [
        ROOM_ENTRANCE, ROOM_LIVING_ROOM, ROOM_KITCHEN, ROOM_DINING_ROOM,
        ROOM_HALLWAY, ROOM_BEDROOM, ROOM_BATHROOM, ROOM_STUDY,
        ROOM_ATTIC, ROOM_BASEMENT,
        # New outdoor rooms
        "backyard", "garden", "patio", "toolshed"
    ],
    LOCATION_HOSPITAL: [
        "reception", "waiting_room", "emergency_room", "operating_theater",
        "patient_ward", "morgue", "pharmacy", "doctors_office",
        "radiology", "basement"
    ],
    LOCATION_PRISON: [
        "entrance_checkpoint", "cell_block_a", "cell_block_b", "cafeteria",
        "exercise_yard", "solitary", "warden_office", "execution_chamber",
        "guard_room", "basement"
    ],
    LOCATION_SCHOOL: [
        "entrance_hall", "classroom_1", "classroom_2", "gymnasium",
        "cafeteria", "library", "principal_office", "bathroom",
        "playground", "basement"
    ],
    LOCATION_CEMETERY: [
        "entrance_gates", "main_path", "old_graves", "mausoleum",
        "crypt", "groundskeeper_shed", "chapel", "new_graves"
    ],
    LOCATION_ASYLUM: [
        "reception", "waiting_room", "treatment_room", "padded_cell",
        "patient_ward", "hydrotherapy", "electroshock_room", "doctors_office",
        "morgue", "basement"
    ],
    LOCATION_HOTEL: [
        "lobby", "reception", "room_237", "hallway",
        "ballroom", "kitchen", "basement", "penthouse",
        "elevator", "laundry"
    ],
    LOCATION_LIGHTHOUSE: [
        "entrance", "living_quarters", "storage", "lamp_room",
        "observation_deck", "dock"
    ],
    LOCATION_MANSION: [
        "grand_entrance", "parlor", "dining_hall", "kitchen",
        "library", "master_bedroom", "guest_room", "bathroom",
        "ballroom", "wine_cellar", "garden", "greenhouse"
    ],
    LOCATION_FARMHOUSE: [
        "farmhouse_entrance", "kitchen", "living_room", "bedroom",
        "bathroom", "barn", "cornfield", "chicken_coop",
        "silo", "cellar"
    ],
    LOCATION_CHURCH: [
        "entrance", "nave", "altar", "confessional",
        "bell_tower", "crypt", "cemetery", "rectory"
    ],
    LOCATION_THEATER: [
        "lobby", "auditorium", "stage", "backstage",
        "dressing_rooms", "orchestra_pit", "balcony", "projection_room",
        "basement", "roof"
    ],
    LOCATION_FACTORY: [
        "entrance", "assembly_line", "furnace_room", "storage",
        "foreman_office", "break_room", "loading_dock", "basement",
        "rooftop", "parking_lot"
    ],
    LOCATION_SHIP: [
        "deck", "bridge", "captains_quarters", "crew_quarters",
        "cargo_hold", "engine_room", "galley", "lifeboat_deck"
    ],
    LOCATION_BUNKER: [
        "entrance_tunnel", "command_center", "barracks", "armory",
        "communications", "medical_bay", "storage", "generator_room"
    ],
    LOCATION_MINE: [
        "mine_entrance", "shaft_1", "shaft_2", "ore_processing",
        "elevator", "collapsed_tunnel", "underground_lake", "exit_tunnel"
    ],
    LOCATION_TRAIN_STATION: [
        "main_hall", "platform_1", "platform_2", "ticket_office",
        "waiting_room", "luggage_storage", "maintenance", "tunnel",
        "parking_lot", "conductors_office"
    ],
    LOCATION_MALL: [
        "main_entrance", "food_court", "department_store", "clothing_store",
        "electronics", "toy_store", "movie_theater", "parking_garage",
        "security_office", "storage"
    ],
    LOCATION_LIBRARY: [
        "entrance_hall", "main_reading_room", "reference_section", "archives",
        "rare_books", "study_rooms", "basement_stacks", "librarian_office",
        "restoration_room", "attic"
    ],
    LOCATION_MUSEUM: [
        "main_hall", "egyptian_exhibit", "dinosaur_hall", "art_gallery",
        "natural_history", "storage", "restoration_lab", "gift_shop",
        "security_office", "basement"
    ],
}


def get_location_info(location_id):
    """Get information about a location"""
    return LOCATIONS.get(location_id, LOCATIONS[LOCATION_HAUNTED_HOUSE])


def get_all_locations():
    """Get list of all location IDs"""
    return list(LOCATIONS.keys())


def get_location_ghosts(location_id):
    """Get list of ghost names for a location"""
    location = LOCATIONS.get(location_id, LOCATIONS[LOCATION_HAUNTED_HOUSE])
    return location.get("ghosts", [])


def get_location_rooms(location_id):
    """Get list of room IDs for a location"""
    return LOCATION_ROOMS.get(location_id, LOCATION_ROOMS[LOCATION_HAUNTED_HOUSE])
