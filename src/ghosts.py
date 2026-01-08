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
    # === 20 NEW GHOSTS ===
    Ghost(
        name="The Twins",
        description="Two child ghosts who died together and now haunt as one. They play tricks and games, but their games are deadly.",
        appearance="Two identical children in matching outfits, holding hands. Their faces are pale and their eyes are black voids. They move in perfect synchronization.",
        behaviors=[
            "childish_laughter",
            "whispers",
            "toy_movement",
            "hide_and_seek",
            "mirror_reflection"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(200, 180, 220),
        sketch_data={
            "type": "double",
            "features": ["two_children", "matching_outfits", "black_eyes", "holding_hands"],
            "style": "creepy_innocent"
        }
    ),
    Ghost(
        name="The Drowned",
        description="A victim of drowning who brings the cold embrace of water wherever they go. Water drips eternally from their bloated form.",
        appearance="A waterlogged figure with blue-gray skin, seaweed tangled in their hair. Water constantly drips and pools around them.",
        behaviors=[
            "water_dripping",
            "wet_footprints",
            "cold_spots",
            "breathing_sounds",
            "whispers"
        ],
        base_aggression=0.45,
        time_limit=660,
        color=(80, 120, 140),
        sketch_data={
            "type": "humanoid",
            "features": ["bloated", "seaweed", "dripping", "blue_skin"],
            "style": "waterlogged"
        }
    ),
    Ghost(
        name="The Soldier",
        description="A soldier who died in combat but never stopped fighting. Shell shock keeps him trapped in an eternal battle.",
        appearance="A uniformed soldier covered in mud and blood. His eyes dart constantly, and he moves in sudden, jerky motions as if dodging bullets.",
        behaviors=[
            "knock_on_walls",
            "slam_doors",
            "sudden_appearance",
            "shadow_movement",
            "breathing_sounds"
        ],
        base_aggression=0.6,
        time_limit=540,
        color=(100, 90, 70),
        sketch_data={
            "type": "humanoid",
            "features": ["uniform", "helmet", "mud", "dog_tags"],
            "style": "military"
        }
    ),
    Ghost(
        name="The Witch",
        description="A woman executed for witchcraft who returned to exact revenge. Her curses still echo through the ages.",
        appearance="A hunched figure in tattered robes, face hidden by a hood. Gnarled hands clutch a staff. Whispers of ancient languages follow her.",
        behaviors=[
            "whispered_names",
            "flicker_lights",
            "cold_spots",
            "visual_distortion",
            "hallucinations"
        ],
        base_aggression=0.55,
        time_limit=600,
        color=(50, 80, 50),
        sketch_data={
            "type": "humanoid",
            "features": ["robes", "hood", "staff", "gnarled_hands"],
            "style": "occult"
        }
    ),
    Ghost(
        name="The Plague Doctor",
        description="A physician from the Black Death who continued his grim work beyond the grave. His 'cures' are worse than any disease.",
        appearance="A tall figure in a black cloak with the iconic bird-like plague mask. Carries a cane and medicinal pouches. Moves with unsettling grace.",
        behaviors=[
            "breathing_sounds",
            "cold_spots",
            "following_presence",
            "whispers",
            "shadow_movement"
        ],
        base_aggression=0.65,
        time_limit=540,
        color=(30, 30, 35),
        sketch_data={
            "type": "humanoid",
            "features": ["plague_mask", "cloak", "cane", "pouches"],
            "style": "medieval"
        }
    ),
    Ghost(
        name="The Jester",
        description="A court fool who was executed for mocking the wrong person. His ghostly tricks are no longer amusing.",
        appearance="A colorful but faded motley outfit with bells that ring silently. His painted smile never changes, hiding the malice beneath.",
        behaviors=[
            "childish_laughter",
            "hallucinations",
            "visual_distortion",
            "toy_movement",
            "mirror_reflection"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(200, 100, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["motley", "bells", "painted_face", "staff"],
            "style": "theatrical"
        }
    ),
    Ghost(
        name="The Servant",
        description="A servant who died serving a cruel master. In death, their resentment has grown into something dangerous.",
        appearance="Dressed in simple servant's attire, head always bowed. But when they look up, their eyes burn with centuries of suppressed rage.",
        behaviors=[
            "object_disappearing",
            "strange_arrangements",
            "whispers",
            "following_presence",
            "cold_spots"
        ],
        base_aggression=0.35,
        time_limit=780,
        color=(120, 100, 90),
        sketch_data={
            "type": "humanoid",
            "features": ["servant_uniform", "bowed_head", "angry_eyes", "clasped_hands"],
            "style": "subservient"
        }
    ),
    Ghost(
        name="The Artist",
        description="A tortured artist who could never finish their masterpiece. Now they create with blood and shadows.",
        appearance="Paint-stained clothes and wild hair. Carries spectral brushes and canvas. Their eyes see things that aren't there - or shouldn't be.",
        behaviors=[
            "drawing_on_walls",
            "hallucinations",
            "visual_distortion",
            "writing_appears",
            "cold_spots"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(180, 150, 200),
        sketch_data={
            "type": "humanoid",
            "features": ["paint_stains", "wild_hair", "brushes", "canvas"],
            "style": "artistic"
        }
    ),
    Ghost(
        name="The Musician",
        description="A musician who died performing and now plays an eternal concert. Their music drives the living mad.",
        appearance="Formal concert attire from another era. Carries a translucent instrument. Music seems to emanate from the air around them.",
        behaviors=[
            "music_box_playing",
            "whispers",
            "cold_spots",
            "visual_distortion",
            "knock_on_walls"
        ],
        base_aggression=0.35,
        time_limit=780,
        color=(160, 140, 180),
        sketch_data={
            "type": "humanoid",
            "features": ["formal_wear", "instrument", "sheet_music", "closed_eyes"],
            "style": "theatrical"
        }
    ),
    Ghost(
        name="The Chef",
        description="A chef who took pride in their work - too much pride. Their secret ingredient was always... fresh.",
        appearance="Chef's whites stained with old blood. Carries a gleaming cleaver. Smells of cooking meat even when nothing is cooking.",
        behaviors=[
            "knife_sounds",
            "meat_smell",
            "throw_objects",
            "slam_doors",
            "breathing_sounds"
        ],
        base_aggression=0.7,
        time_limit=480,
        color=(255, 220, 200),
        sketch_data={
            "type": "humanoid",
            "features": ["chef_hat", "apron", "cleaver", "blood_stains"],
            "style": "culinary"
        }
    ),
    Ghost(
        name="The Gardener",
        description="A groundskeeper who loved their garden more than any living thing. Now they tend to the dead.",
        appearance="Muddy overalls and a wide-brimmed hat. Carries rusty garden tools. Flowers and vines seem to grow in their wake.",
        behaviors=[
            "cold_spots",
            "whispers",
            "following_presence",
            "object_disappearing",
            "strange_arrangements"
        ],
        base_aggression=0.3,
        time_limit=840,
        color=(90, 130, 70),
        sketch_data={
            "type": "humanoid",
            "features": ["overalls", "hat", "garden_tools", "muddy"],
            "style": "rural"
        }
    ),
    Ghost(
        name="The Arsonist",
        description="A pyromaniac who died in one of their own fires. They still seek to watch the world burn.",
        appearance="Charred and smoking figure with a gasoline can. Their eyes glow like embers, and fire flickers across their skin.",
        behaviors=[
            "flicker_lights",
            "darken_room",
            "breathing_sounds",
            "sudden_appearance",
            "throw_objects"
        ],
        base_aggression=0.75,
        time_limit=420,
        color=(255, 120, 50),
        sketch_data={
            "type": "humanoid",
            "features": ["charred", "gas_can", "ember_eyes", "flames"],
            "style": "burning"
        }
    ),
    Ghost(
        name="The Drunkard",
        description="A drunk who died in a bar fight and never sobered up. Their stumbling walk and slurred speech mask surprising violence.",
        appearance="Disheveled clothes reeking of alcohol. Carries a broken bottle. Staggers and weaves but moves with unsettling speed when angered.",
        behaviors=[
            "knock_on_walls",
            "throw_objects",
            "slam_doors",
            "whispers",
            "sudden_appearance"
        ],
        base_aggression=0.55,
        time_limit=600,
        color=(150, 100, 80),
        sketch_data={
            "type": "humanoid",
            "features": ["disheveled", "bottle", "staggering", "flushed_face"],
            "style": "inebriated"
        }
    ),
    Ghost(
        name="The Gambler",
        description="A gambler who bet their soul and lost. Now they play games with the living - games you can't win.",
        appearance="Sharp suit and fedora, but moth-eaten and faded. Always shuffling phantom cards or rolling invisible dice.",
        behaviors=[
            "coin_sounds",
            "whispers",
            "visual_distortion",
            "hallucinations",
            "object_disappearing"
        ],
        base_aggression=0.45,
        time_limit=660,
        color=(140, 80, 80),
        sketch_data={
            "type": "humanoid",
            "features": ["suit", "fedora", "cards", "dice"],
            "style": "noir"
        }
    ),
    Ghost(
        name="The Thief",
        description="A burglar who was killed by a homeowner. They still steal, but now they take more than possessions.",
        appearance="Dark clothes and a mask pulled down. Moves silently and appears suddenly. Objects vanish when they're near.",
        behaviors=[
            "object_disappearing",
            "shadow_movement",
            "cold_spots",
            "following_presence",
            "sudden_appearance"
        ],
        base_aggression=0.5,
        time_limit=600,
        color=(40, 40, 50),
        sketch_data={
            "type": "humanoid",
            "features": ["dark_clothes", "mask", "bag", "gloves"],
            "style": "sneaky"
        }
    ),
    Ghost(
        name="The Jailer",
        description="A prison guard who enjoyed their power too much. In death, everyone is their prisoner.",
        appearance="Old guard uniform with jangling keys. Face hidden in shadow beneath a cap. Carries a baton and chains.",
        behaviors=[
            "knock_on_walls",
            "slam_doors",
            "coin_sounds",
            "following_presence",
            "shadow_movement"
        ],
        base_aggression=0.6,
        time_limit=540,
        color=(70, 70, 80),
        sketch_data={
            "type": "humanoid",
            "features": ["uniform", "keys", "baton", "shadowed_face"],
            "style": "authoritarian"
        }
    ),
    Ghost(
        name="The Doctor",
        description="A doctor who experimented on patients without consent. Their 'treatments' continue beyond death.",
        appearance="Pristine white coat stained with old blood. Carries antiquated medical instruments. Eyes behind thick glasses are cold and calculating.",
        behaviors=[
            "whispers",
            "cold_spots",
            "object_disappearing",
            "following_presence",
            "breathing_sounds"
        ],
        base_aggression=0.55,
        time_limit=600,
        color=(230, 230, 235),
        sketch_data={
            "type": "humanoid",
            "features": ["white_coat", "glasses", "instruments", "clipboard"],
            "style": "medical"
        }
    ),
    Ghost(
        name="The Teacher",
        description="A strict teacher who punished students severely. Now class is always in session, and you're failing.",
        appearance="Formal old-fashioned teaching attire. Carries a ruler and chalk. Their lessons are written in blood on the blackboard.",
        behaviors=[
            "writing_appears",
            "whispers",
            "knock_on_walls",
            "cold_spots",
            "throw_objects"
        ],
        base_aggression=0.45,
        time_limit=660,
        color=(130, 110, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["formal_dress", "ruler", "chalk", "glasses"],
            "style": "academic"
        }
    ),
    Ghost(
        name="The Preacher",
        description="A fire-and-brimstone preacher who damned everyone around them. Their sermons echo from beyond the grave.",
        appearance="Black robes and a wide-brimmed hat. Holds a burning bible. Their voice booms even in whispers, condemning all who hear.",
        behaviors=[
            "whispers",
            "flicker_lights",
            "cold_spots",
            "visual_distortion",
            "sudden_appearance"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(30, 25, 40),
        sketch_data={
            "type": "humanoid",
            "features": ["robes", "hat", "bible", "stern_face"],
            "style": "religious"
        }
    ),
    Ghost(
        name="The Detective",
        description="A detective who became obsessed with a case and was killed for getting too close. Now YOU are their case.",
        appearance="Rumpled trench coat and fedora. Carries a notepad and magnifying glass. Follows you, studying, analyzing, judging.",
        behaviors=[
            "following_presence",
            "whispered_names",
            "writing_appears",
            "shadow_movement",
            "cold_spots"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(100, 95, 85),
        sketch_data={
            "type": "humanoid",
            "features": ["trench_coat", "fedora", "notepad", "magnifying_glass"],
            "style": "investigative"
        }
    ),
    # Additional location-specific ghosts
    Ghost(
        name="The Gravedigger",
        description="A gravedigger who buried people alive for profit. Now they dig graves that will never be filled.",
        appearance="Dirt-covered work clothes with a rusted shovel. Smells of fresh earth. Eyes glow from deep sockets.",
        behaviors=[
            "cold_spots",
            "whispers",
            "knock_on_walls",
            "breathing_sounds",
            "shadow_movement"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(80, 70, 60),
        sketch_data={
            "type": "humanoid",
            "features": ["dirty_clothes", "shovel", "glowing_eyes", "hunched"],
            "style": "morbid"
        }
    ),
    Ghost(
        name="The Mariner",
        description="A lighthouse keeper who led ships to their doom. The light still calls to the unwary.",
        appearance="Weathered rain gear and a captain's hat. Carries a lantern that glows with ghostly light. Salt water drips from their beard.",
        behaviors=[
            "flicker_lights",
            "water_dripping",
            "cold_spots",
            "whispers",
            "shadow_movement"
        ],
        base_aggression=0.45,
        time_limit=660,
        color=(70, 100, 120),
        sketch_data={
            "type": "humanoid",
            "features": ["rain_gear", "captains_hat", "lantern", "beard"],
            "style": "maritime"
        }
    ),
    Ghost(
        name="The Scarecrow",
        description="A man who was strung up as a scarecrow and left to die. Now they stand watch over fields of the damned.",
        appearance="Tattered clothes stuffed with straw. Face is a burlap sack with button eyes. Crows gather wherever they appear.",
        behaviors=[
            "sudden_appearance",
            "following_presence",
            "cold_spots",
            "shadow_movement",
            "whispers"
        ],
        base_aggression=0.55,
        time_limit=600,
        color=(160, 140, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["straw", "burlap_head", "button_eyes", "tattered_clothes"],
            "style": "rural_horror"
        }
    ),
    Ghost(
        name="The Choir",
        description="A group of singers who burned in a church fire. Their hymns are now screams of agony.",
        appearance="Multiple translucent figures in choir robes, mouths open in eternal song. Flames flicker around their forms.",
        behaviors=[
            "whispers",
            "flicker_lights",
            "cold_spots",
            "hallucinations",
            "visual_distortion"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(180, 160, 200),
        sketch_data={
            "type": "group",
            "features": ["robes", "multiple_figures", "flames", "open_mouths"],
            "style": "religious"
        }
    ),
    Ghost(
        name="The Worker",
        description="A factory worker killed in an industrial accident. The machinery still runs red with their blood.",
        appearance="Coveralls splattered with oil and blood. Missing limbs replaced by mechanical parts. Gears grind where their heart should be.",
        behaviors=[
            "knock_on_walls",
            "breathing_sounds",
            "cold_spots",
            "shadow_movement",
            "throw_objects"
        ],
        base_aggression=0.55,
        time_limit=600,
        color=(100, 90, 80),
        sketch_data={
            "type": "humanoid",
            "features": ["coveralls", "oil_stains", "mechanical_parts", "damaged"],
            "style": "industrial"
        }
    ),
    Ghost(
        name="The Foreman",
        description="A cruel foreman who worked their employees to death. Productivity continues beyond the grave.",
        appearance="Hard hat and work clothes. Carries a clipboard and whistle. Shouts orders that echo from empty rooms.",
        behaviors=[
            "whispers",
            "knock_on_walls",
            "following_presence",
            "cold_spots",
            "throw_objects"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(150, 130, 80),
        sketch_data={
            "type": "humanoid",
            "features": ["hard_hat", "clipboard", "whistle", "stern_face"],
            "style": "authoritarian"
        }
    ),
    Ghost(
        name="The Captain",
        description="A ship's captain who went down with their vessel. They command a ghost crew for eternity.",
        appearance="Naval uniform from a bygone era. Barnacles encrust their face. One hand grips an ancient compass, the other a cutlass.",
        behaviors=[
            "water_dripping",
            "cold_spots",
            "whispers",
            "following_presence",
            "shadow_movement"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(60, 80, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["naval_uniform", "barnacles", "compass", "cutlass"],
            "style": "maritime"
        }
    ),
    Ghost(
        name="The Sailor",
        description="A sailor lost at sea who never found shore. The salt water follows them everywhere.",
        appearance="Striped shirt and sailor's cap, both rotted by saltwater. Seaweed hangs from their limbs. Crabs skitter in their wake.",
        behaviors=[
            "wet_footprints",
            "water_dripping",
            "cold_spots",
            "whispers",
            "knock_on_walls"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(90, 110, 130),
        sketch_data={
            "type": "humanoid",
            "features": ["striped_shirt", "cap", "seaweed", "barnacles"],
            "style": "maritime"
        }
    ),
    Ghost(
        name="The Stowaway",
        description="A stowaway who was discovered and thrown overboard. They hide in the dark places, waiting.",
        appearance="Ragged clothes and desperate eyes. Thin and emaciated. Moves in dark corners, always watching from the shadows.",
        behaviors=[
            "shadow_movement",
            "following_presence",
            "breathing_sounds",
            "cold_spots",
            "sudden_appearance"
        ],
        base_aggression=0.45,
        time_limit=660,
        color=(50, 50, 55),
        sketch_data={
            "type": "humanoid",
            "features": ["ragged_clothes", "thin", "desperate_eyes", "hiding"],
            "style": "desperate"
        }
    ),
    Ghost(
        name="The General",
        description="A general who sent thousands to their deaths without remorse. Their war never ends.",
        appearance="Decorated military uniform from decades past. Medals gleam coldly. Maps of impossible battles float around them.",
        behaviors=[
            "knock_on_walls",
            "whispers",
            "cold_spots",
            "following_presence",
            "slam_doors"
        ],
        base_aggression=0.6,
        time_limit=540,
        color=(80, 70, 60),
        sketch_data={
            "type": "humanoid",
            "features": ["uniform", "medals", "maps", "stern_expression"],
            "style": "military"
        }
    ),
    Ghost(
        name="The Radio Operator",
        description="A communications officer who received a transmission from beyond. They're still trying to relay the message.",
        appearance="Military communications uniform with headphones fused to their skull. Static crackles around them constantly.",
        behaviors=[
            "whispers",
            "flicker_lights",
            "visual_distortion",
            "cold_spots",
            "breathing_sounds"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(100, 110, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["uniform", "headphones", "static", "wires"],
            "style": "military_tech"
        }
    ),
    Ghost(
        name="The Miner",
        description="A miner trapped in a cave-in who never saw daylight again. Their pickaxe still rings in the tunnels.",
        appearance="Coal-covered work clothes with a helmet lamp that flickers weakly. Their eyes have adjusted to eternal darkness.",
        behaviors=[
            "knock_on_walls",
            "cold_spots",
            "shadow_movement",
            "breathing_sounds",
            "darken_room"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(40, 35, 30),
        sketch_data={
            "type": "humanoid",
            "features": ["coal_covered", "helmet", "pickaxe", "dark_eyes"],
            "style": "underground"
        }
    ),
    Ghost(
        name="The Canary",
        description="The ghost of a canary that died warning miners of danger. It now warns of death itself.",
        appearance="A spectral yellow bird that glows faintly. Its silent song heralds doom for those who hear it.",
        behaviors=[
            "cold_spots",
            "flicker_lights",
            "whispers",
            "sudden_appearance",
            "following_presence"
        ],
        base_aggression=0.25,
        time_limit=840,
        color=(255, 220, 100),
        sketch_data={
            "type": "bird",
            "features": ["yellow", "glowing", "small", "cage"],
            "style": "ethereal"
        }
    ),
    Ghost(
        name="The Conductor",
        description="A train conductor killed in a crash. They still call out stations that no longer exist.",
        appearance="Formal conductor's uniform with a pocket watch that never tells the right time. Whistle hangs around their neck.",
        behaviors=[
            "whispers",
            "coin_sounds",
            "knock_on_walls",
            "cold_spots",
            "shadow_movement"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(60, 50, 70),
        sketch_data={
            "type": "humanoid",
            "features": ["uniform", "hat", "whistle", "pocket_watch"],
            "style": "railway"
        }
    ),
    Ghost(
        name="The Waiting Woman",
        description="A woman who waited at the station for a loved one who never came. She waits still.",
        appearance="Elegant but faded travel clothes from the 1920s. Clutches a letter. Eyes scan every face, searching.",
        behaviors=[
            "crying_sounds",
            "cold_spots",
            "following_presence",
            "whispers",
            "sad_whispers"
        ],
        base_aggression=0.3,
        time_limit=780,
        color=(180, 160, 170),
        sketch_data={
            "type": "humanoid",
            "features": ["travel_clothes", "hat", "letter", "sad_eyes"],
            "style": "vintage"
        }
    ),
    Ghost(
        name="The Hobo",
        description="A vagrant who froze to death in the train yard. They ride the ghost trains forever.",
        appearance="Layers of tattered clothes, face hidden by a beard and grime. Carries a bindle and a bottle. Fire flickers in their eyes.",
        behaviors=[
            "cold_spots",
            "whispers",
            "shadow_movement",
            "knock_on_walls",
            "sudden_appearance"
        ],
        base_aggression=0.35,
        time_limit=720,
        color=(100, 90, 70),
        sketch_data={
            "type": "humanoid",
            "features": ["tattered_clothes", "beard", "bindle", "bottle"],
            "style": "vagrant"
        }
    ),
    Ghost(
        name="The Mannequin",
        description="A display mannequin that houses something ancient and hungry. It moves when you're not looking.",
        appearance="A perfect store mannequin with a frozen smile. But the eyes follow you, and sometimes... it's in a different position.",
        behaviors=[
            "sudden_appearance",
            "following_presence",
            "cold_spots",
            "shadow_movement",
            "mirror_reflection"
        ],
        base_aggression=0.55,
        time_limit=600,
        color=(220, 200, 190),
        sketch_data={
            "type": "mannequin",
            "features": ["plastic_skin", "frozen_smile", "blank_eyes", "posed"],
            "style": "uncanny"
        }
    ),
    Ghost(
        name="The Scholar",
        description="A scholar who uncovered forbidden knowledge and paid the ultimate price. They seek to share what they learned.",
        appearance="Academic robes covered in arcane symbols. Carries ancient tomes. Their eyes glow with terrible knowledge.",
        behaviors=[
            "writing_appears",
            "flying_books",
            "whispers",
            "visual_distortion",
            "cold_spots"
        ],
        base_aggression=0.45,
        time_limit=660,
        color=(100, 80, 120),
        sketch_data={
            "type": "humanoid",
            "features": ["robes", "tomes", "glowing_eyes", "symbols"],
            "style": "academic"
        }
    ),
    Ghost(
        name="The Archivist",
        description="A record keeper who catalogued the dead. Now they add the living to their collection.",
        appearance="Dusty formal wear with ink-stained fingers. Carries endless scrolls and ledgers. Records your every move.",
        behaviors=[
            "writing_appears",
            "page_turning",
            "whispered_names",
            "cold_spots",
            "following_presence"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(140, 130, 120),
        sketch_data={
            "type": "humanoid",
            "features": ["formal_wear", "ink_stains", "scrolls", "quill"],
            "style": "bureaucratic"
        }
    ),
    Ghost(
        name="The Pharaoh",
        description="An ancient ruler whose tomb was disturbed. Their curse reaches across millennia.",
        appearance="Wrapped in ancient bandages with gold and lapis lazuli adornments. Eyes glow with ancient power.",
        behaviors=[
            "cold_spots",
            "visual_distortion",
            "whispers",
            "hallucinations",
            "shadow_movement"
        ],
        base_aggression=0.6,
        time_limit=540,
        color=(200, 170, 80),
        sketch_data={
            "type": "mummy",
            "features": ["bandages", "gold", "headdress", "glowing_eyes"],
            "style": "ancient"
        }
    ),
    Ghost(
        name="The Mummy",
        description="An ancient priest whose burial was incomplete. They shamble through eternity seeking rest.",
        appearance="Dried, wrapped corpse trailing ancient bandages. Moves slowly but inevitably. Smells of ancient spices and decay.",
        behaviors=[
            "cold_spots",
            "breathing_sounds",
            "following_presence",
            "whispers",
            "shadow_movement"
        ],
        base_aggression=0.5,
        time_limit=660,
        color=(180, 160, 120),
        sketch_data={
            "type": "mummy",
            "features": ["bandages", "dried", "slow", "ancient"],
            "style": "ancient"
        }
    ),
    Ghost(
        name="The Curator",
        description="A museum curator who died protecting their collection. They don't appreciate visitors touching the exhibits.",
        appearance="Formal attire with a monocle and white gloves. Carries a small flashlight. Watches everything with possessive intensity.",
        behaviors=[
            "following_presence",
            "whispers",
            "cold_spots",
            "object_disappearing",
            "strange_arrangements"
        ],
        base_aggression=0.4,
        time_limit=720,
        color=(120, 110, 100),
        sketch_data={
            "type": "humanoid",
            "features": ["formal_attire", "monocle", "gloves", "flashlight"],
            "style": "academic"
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


def get_ghosts_for_location(ghost_names):
    """Get ghost objects for a list of ghost names"""
    ghosts = []
    for name in ghost_names:
        ghost = get_ghost_by_name(name)
        if ghost:
            ghosts.append(ghost)
    return ghosts if ghosts else GHOST_ROSTER[:8]  # Fallback to first 8 ghosts


def get_random_ghost_for_location(ghost_names):
    """Get a random ghost from a specific list of ghost names"""
    ghosts = get_ghosts_for_location(ghost_names)
    if ghosts:
        return random.choice(ghosts)
    return get_random_ghost()
