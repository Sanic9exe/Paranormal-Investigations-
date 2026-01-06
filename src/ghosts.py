"""
Ghost definitions and behaviors for Paranormal Investigations
"""

import random
import math
from constants import *


# Map behaviors to evidence types
BEHAVIOR_EVIDENCE_MAP = {
    # Cold evidence
    "cold_spots": EVIDENCE_COLD,
    "cold_breath": EVIDENCE_COLD,
    # Light evidence
    "flicker_lights": EVIDENCE_LIGHTS,
    "darken_room": EVIDENCE_LIGHTS,
    # Object evidence
    "float_objects": EVIDENCE_OBJECTS,
    "throw_objects": EVIDENCE_OBJECTS,
    "move_furniture": EVIDENCE_OBJECTS,
    "slam_doors": EVIDENCE_OBJECTS,
    "scatter_items": EVIDENCE_OBJECTS,
    "toy_movement": EVIDENCE_OBJECTS,
    "flying_books": EVIDENCE_OBJECTS,
    "object_disappearing": EVIDENCE_OBJECTS,
    "strange_arrangements": EVIDENCE_OBJECTS,
    # Sound evidence
    "whispers": EVIDENCE_SOUNDS,
    "crying_sounds": EVIDENCE_SOUNDS,
    "sad_whispers": EVIDENCE_SOUNDS,
    "breathing_sounds": EVIDENCE_SOUNDS,
    "childish_laughter": EVIDENCE_SOUNDS,
    "knife_sounds": EVIDENCE_SOUNDS,
    "music_box_playing": EVIDENCE_SOUNDS,
    "dress_rustling": EVIDENCE_SOUNDS,
    "phantom_crying": EVIDENCE_SOUNDS,
    "page_turning": EVIDENCE_SOUNDS,
    "shushing_sounds": EVIDENCE_SOUNDS,
    "whispered_names": EVIDENCE_SOUNDS,
    "counting_sounds": EVIDENCE_SOUNDS,
    "coin_sounds": EVIDENCE_SOUNDS,
    "knock_on_walls": EVIDENCE_SOUNDS,
    "violent_door_slams": EVIDENCE_SOUNDS,
    # Visual evidence
    "mirror_reflection": EVIDENCE_VISUAL,
    "shadow_movement": EVIDENCE_VISUAL,
    "following_presence": EVIDENCE_VISUAL,
    "sudden_appearance": EVIDENCE_VISUAL,
    "handprints": EVIDENCE_VISUAL,
    "drawing_on_walls": EVIDENCE_VISUAL,
    "hide_and_seek": EVIDENCE_VISUAL,
    "bloody_footprints": EVIDENCE_VISUAL,
    "threatening_shadows": EVIDENCE_VISUAL,
    "mirror_appearances": EVIDENCE_VISUAL,
    "rose_petals": EVIDENCE_VISUAL,
    "glasses_reflection": EVIDENCE_VISUAL,
    "writing_appears": EVIDENCE_VISUAL,
    "visual_distortion": EVIDENCE_VISUAL,
    "hallucinations": EVIDENCE_VISUAL,
    "reality_blur": EVIDENCE_VISUAL,
    "multiple_eyes": EVIDENCE_VISUAL,
    "grabbing_shadows": EVIDENCE_VISUAL,
    # Water evidence
    "wet_footprints": EVIDENCE_WATER,
    "water_dripping": EVIDENCE_WATER,
    "meat_smell": EVIDENCE_VISUAL,  # Special case
}


class Ghost:
    """Base class for all ghosts"""
    
    def __init__(self, name, description, appearance, behaviors, base_aggression, 
                 time_limit, color, sketch_data):
        self.name = name
        self.description = description
        self.appearance = appearance
        self.behaviors = behaviors  # List of behavior strings
        self.base_aggression = base_aggression  # 0.0 to 1.0
        self.time_limit = time_limit  # Base time in seconds (5-20 minutes)
        self.color = color
        self.sketch_data = sketch_data  # Data for drawing the ghost sketch
        self.current_aggression = base_aggression
        self.active_behaviors = []
        # Calculate evidence signature for this ghost
        self.evidence_types = self._calculate_evidence_types()
        
    def _calculate_evidence_types(self):
        """Get unique evidence types this ghost produces"""
        evidence = set()
        for behavior in self.behaviors:
            if behavior in BEHAVIOR_EVIDENCE_MAP:
                evidence.add(BEHAVIOR_EVIDENCE_MAP[behavior])
        return evidence
        
    def get_random_behavior(self):
        """Get a random behavior from this ghost's behavior list"""
        return random.choice(self.behaviors)
    
    def get_evidence_for_behavior(self, behavior):
        """Get the evidence type for a specific behavior"""
        return BEHAVIOR_EVIDENCE_MAP.get(behavior, None)
    
    def increase_aggression(self, amount):
        """Increase ghost aggression"""
        self.current_aggression = min(1.0, self.current_aggression + amount)
        
    def reset(self):
        """Reset ghost state for new game"""
        self.current_aggression = self.base_aggression
        self.active_behaviors = []


# Define all ghost types
GHOST_ROSTER = [
    Ghost(
        name="Bonnie",
        description="A tragic spirit with a deformed visage and an extra limb. Once a performer who died in a fire, she now haunts with flickering lights and floating objects.",
        appearance="Blue-tinted translucent figure with a distorted face showing burn scars. Has three arms - two normal and one twisted emerging from her back. Wears a tattered Victorian dress.",
        behaviors=[
            "flicker_lights",
            "float_objects",
            "cold_spots",
            "whispers",
            "mirror_reflection"
        ],
        base_aggression=0.3,
        time_limit=900,  # 15 minutes
        color=(100, 150, 255),
        sketch_data={
            "type": "humanoid",
            "features": ["three_arms", "distorted_face", "dress", "burn_marks"],
            "style": "tragic"
        }
    ),
    Ghost(
        name="Poltergeist",
        description="A chaotic entity that delights in causing mayhem. It throws objects, slams doors, and creates general havoc throughout the house.",
        appearance="Rarely seen directly - appears as a swirling mass of dark energy with glowing red eyes. Objects around it levitate and spin.",
        behaviors=[
            "throw_objects",
            "slam_doors",
            "move_furniture",
            "knock_on_walls",
            "scatter_items"
        ],
        base_aggression=0.6,
        time_limit=600,  # 10 minutes
        color=(50, 50, 50),
        sketch_data={
            "type": "amorphous",
            "features": ["swirling_mass", "red_eyes", "floating_debris"],
            "style": "chaotic"
        }
    ),
    Ghost(
        name="The Weeping Lady",
        description="A sorrowful spirit who lost her children. Her presence is marked by the sound of crying and wet footprints appearing on the floor.",
        appearance="A pale woman in a white nightgown, perpetually crying. Her tears leave glowing trails, and water drips from her hair and clothes.",
        behaviors=[
            "crying_sounds",
            "wet_footprints",
            "water_dripping",
            "cold_breath",
            "sad_whispers"
        ],
        base_aggression=0.2,
        time_limit=1080,  # 18 minutes
        color=(200, 220, 255),
        sketch_data={
            "type": "humanoid",
            "features": ["long_hair", "nightgown", "tears", "water_drips"],
            "style": "sorrowful"
        }
    ),
    Ghost(
        name="Shadow Stalker",
        description="A malevolent entity that lurks in darkness. It feeds on fear and grows stronger the more frightened its victims become.",
        appearance="A tall, unnaturally thin humanoid shape made of pure darkness. Has no features except for two white pinprick eyes. Moves in jerky, unnatural motions.",
        behaviors=[
            "darken_room",
            "shadow_movement",
            "breathing_sounds",
            "following_presence",
            "sudden_appearance"
        ],
        base_aggression=0.7,
        time_limit=480,  # 8 minutes
        color=(20, 20, 40),
        sketch_data={
            "type": "humanoid",
            "features": ["tall_thin", "no_features", "white_eyes", "shadow_body"],
            "style": "menacing"
        }
    ),
    Ghost(
        name="Little Timmy",
        description="The ghost of a child who died in the house. Playful but lonely, he just wants someone to play with - forever.",
        appearance="A small boy around 8 years old, wearing old-fashioned clothes. Appears semi-transparent with a soft glow. Often seen with a red ball.",
        behaviors=[
            "toy_movement",
            "childish_laughter",
            "handprints",
            "drawing_on_walls",
            "hide_and_seek"
        ],
        base_aggression=0.15,
        time_limit=1200,  # 20 minutes
        color=(255, 200, 150),
        sketch_data={
            "type": "child",
            "features": ["small", "old_clothes", "ball", "innocent_face"],
            "style": "innocent"
        }
    ),
    Ghost(
        name="The Butcher",
        description="A violent spirit of a serial killer who used this house as his workshop. His presence brings the smell of blood and the sound of sharpening knives.",
        appearance="A large, imposing figure wearing a blood-stained apron. Face is obscured by shadow, but a gleaming cleaver is always visible in his hand.",
        behaviors=[
            "bloody_footprints",
            "knife_sounds",
            "meat_smell",
            "threatening_shadows",
            "violent_door_slams"
        ],
        base_aggression=0.8,
        time_limit=420,  # 7 minutes
        color=(139, 0, 0),
        sketch_data={
            "type": "humanoid",
            "features": ["large_build", "apron", "cleaver", "shadowed_face"],
            "style": "threatening"
        }
    ),
    Ghost(
        name="Ethereal Bride",
        description="A woman who died on her wedding day, still waiting for her groom. She appears in mirrors and reflective surfaces.",
        appearance="A beautiful woman in a flowing white wedding dress, now tattered and aged. Her face shifts between joy and despair. Surrounded by falling rose petals.",
        behaviors=[
            "mirror_appearances",
            "rose_petals",
            "music_box_playing",
            "dress_rustling",
            "phantom_crying"
        ],
        base_aggression=0.4,
        time_limit=780,  # 13 minutes
        color=(255, 240, 245),
        sketch_data={
            "type": "humanoid",
            "features": ["wedding_dress", "veil", "bouquet", "sad_eyes"],
            "style": "romantic_tragic"
        }
    ),
    Ghost(
        name="The Librarian",
        description="A scholarly ghost who guards the knowledge of the house. Books fly and pages turn on their own in their presence.",
        appearance="An elderly figure in academic robes, wearing spectacles that glow faintly. Always seen with floating books around them.",
        behaviors=[
            "flying_books",
            "page_turning",
            "writing_appears",
            "glasses_reflection",
            "shushing_sounds"
        ],
        base_aggression=0.25,
        time_limit=960,  # 16 minutes
        color=(180, 160, 140),
        sketch_data={
            "type": "humanoid",
            "features": ["robes", "spectacles", "books", "elderly"],
            "style": "scholarly"
        }
    ),
    Ghost(
        name="Nightmare",
        description="An entity that exists between sleep and waking. It causes hallucinations and makes reality blur at the edges.",
        appearance="Constantly shifting form - one moment human, the next a creature of impossible geometry. Eyes appear everywhere on its form.",
        behaviors=[
            "visual_distortion",
            "hallucinations",
            "reality_blur",
            "multiple_eyes",
            "whispered_names"
        ],
        base_aggression=0.65,
        time_limit=540,  # 9 minutes
        color=(128, 0, 128),
        sketch_data={
            "type": "shifting",
            "features": ["multiple_eyes", "distorted_form", "impossible_angles"],
            "style": "surreal"
        }
    ),
    Ghost(
        name="The Collector",
        description="A ghost obsessed with collecting things - especially souls. Small objects disappear around them, only to appear in strange arrangements.",
        appearance="A hunched figure in a long coat with many pockets. Face is partially hidden by a wide-brimmed hat. Hands are unnaturally long with too many fingers.",
        behaviors=[
            "object_disappearing",
            "strange_arrangements",
            "counting_sounds",
            "coin_sounds",
            "grabbing_shadows"
        ],
        base_aggression=0.5,
        time_limit=720,  # 12 minutes
        color=(70, 70, 90),
        sketch_data={
            "type": "humanoid",
            "features": ["long_coat", "hat", "long_fingers", "hunched"],
            "style": "creepy"
        }
    ),
    # NEW GHOSTS
    Ghost(
        name="The Burned Man",
        description="A vengeful spirit of a man who died in a house fire. His rage burns eternal, and he leaves scorch marks wherever he goes.",
        appearance="A charred humanoid figure with glowing embers in his eye sockets. Smoke constantly rises from his body, and patches of flame flicker across his form.",
        behaviors=[
            "flicker_lights",
            "darken_room",
            "breathing_sounds",
            "sudden_appearance",
            "meat_smell"
        ],
        base_aggression=0.75,
        time_limit=420,  # 7 minutes
        color=(255, 100, 50),
        sketch_data={
            "type": "humanoid",
            "features": ["charred_body", "ember_eyes", "smoke", "flames"],
            "style": "vengeful"
        }
    ),
    Ghost(
        name="The Doll",
        description="The spirit of a girl who was murdered, now possessing her favorite porcelain doll. She giggles in the darkness and moves when you're not looking.",
        appearance="A life-sized porcelain doll with cracked features and one missing eye. Wears a faded pink dress. Moves in jerky, mechanical motions.",
        behaviors=[
            "childish_laughter",
            "toy_movement",
            "whispers",
            "sudden_appearance",
            "mirror_appearances"
        ],
        base_aggression=0.55,
        time_limit=600,  # 10 minutes
        color=(255, 180, 200),
        sketch_data={
            "type": "humanoid",
            "features": ["porcelain_face", "cracked", "missing_eye", "pink_dress"],
            "style": "uncanny"
        }
    ),
    Ghost(
        name="The Hanged Man",
        description="A suicide victim who now wanders the house, rope still around his neck. He appears in doorways and high places, always watching.",
        appearance="A gaunt man with an elongated neck and a noose still tied around it. His head hangs at an unnatural angle. Eyes are bulging and bloodshot.",
        behaviors=[
            "shadow_movement",
            "following_presence",
            "breathing_sounds",
            "knock_on_walls",
            "darken_room"
        ],
        base_aggression=0.45,
        time_limit=780,  # 13 minutes
        color=(80, 70, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["long_neck", "noose", "tilted_head", "gaunt"],
            "style": "tragic"
        }
    ),
    Ghost(
        name="The Mimic",
        description="A shapeshifting entity that copies the appearance of loved ones to lure victims. It can never quite get the face right.",
        appearance="Changes constantly, but always has something wrong - a smile too wide, eyes that don't blink, movements that are slightly off.",
        behaviors=[
            "whispered_names",
            "mirror_reflection",
            "visual_distortion",
            "hallucinations",
            "following_presence"
        ],
        base_aggression=0.6,
        time_limit=540,  # 9 minutes
        color=(150, 150, 150),
        sketch_data={
            "type": "shifting",
            "features": ["wrong_face", "too_wide_smile", "unblinking_eyes"],
            "style": "uncanny"
        }
    ),
    Ghost(
        name="The Nurse",
        description="A nurse who killed her patients in this house when it was a hospital. She still 'cares' for the living, with deadly treatments.",
        appearance="A nurse in an old-fashioned uniform stained with blood. Carries rusted medical instruments. Her face is kind but her eyes are hollow.",
        behaviors=[
            "wet_footprints",
            "cold_spots",
            "whispers",
            "object_disappearing",
            "breathing_sounds"
        ],
        base_aggression=0.5,
        time_limit=660,  # 11 minutes
        color=(255, 255, 255),
        sketch_data={
            "type": "humanoid",
            "features": ["nurse_uniform", "blood_stains", "medical_tools", "hollow_eyes"],
            "style": "clinical"
        }
    ),
]


def get_random_ghost():
    """Select a random ghost from the roster"""
    return random.choice(GHOST_ROSTER)


def get_ghost_by_name(name):
    """Get a specific ghost by name"""
    for ghost in GHOST_ROSTER:
        if ghost.name.lower() == name.lower():
            return ghost
    return None


def get_all_ghosts():
    """Get all ghosts in the roster"""
    return GHOST_ROSTER.copy()
