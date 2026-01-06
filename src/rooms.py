"""
Room definitions and rendering for Paranormal Investigations
"""

import pygame
import math
import random
from constants import *


class InteractiveObject:
    """An object in a room that can be interacted with"""
    
    def __init__(self, name, rect, description, interaction_type, zoom_description=None, 
                 ghost_descriptions=None, affected_descriptions=None):
        self.name = name
        self.rect = pygame.Rect(rect)
        self.description = description  # Normal description
        self.interaction_type = interaction_type  # "toggle", "examine", "zoom"
        self.zoom_description = zoom_description
        self.ghost_descriptions = ghost_descriptions or {}  # {ghost_name: special_description}
        # NEW: Descriptions when ghost has affected this object
        self.affected_descriptions = affected_descriptions or {}  # {behavior_type: description}
        self.state = False  # For toggleable objects
        self.hovered = False
        self.clue_revealed = False
        # NEW: Track if ghost has affected this object
        self.ghost_affected = False
        self.affected_by_behavior = None  # Which behavior affected it
        self.affect_timer = 0  # How long the effect lasts
        
    def apply_ghost_effect(self, behavior):
        """Apply a ghost behavior effect to this object"""
        self.ghost_affected = True
        self.affected_by_behavior = behavior
        self.affect_timer = 30.0  # Effect lasts 30 seconds
        
    def update(self, dt):
        """Update object state"""
        if self.affect_timer > 0:
            self.affect_timer -= dt
            if self.affect_timer <= 0:
                self.ghost_affected = False
                self.affected_by_behavior = None
        
    def get_description(self, ghost=None, flashlight_on=False):
        """Get the appropriate description based on state"""
        # If ghost affected this object, show affected description
        if self.ghost_affected and self.affected_by_behavior:
            if self.affected_by_behavior in self.affected_descriptions:
                return self.affected_descriptions[self.affected_by_behavior]
            # Generic affected descriptions based on behavior type
            return self._get_generic_affected_description()
        
        # If using flashlight and ghost-specific description exists
        if flashlight_on and ghost and ghost.name in self.ghost_descriptions:
            return self.ghost_descriptions[ghost.name]
            
        return self.zoom_description if self.zoom_description else self.description
    
    def _get_generic_affected_description(self):
        """Get a generic description based on the behavior that affected it"""
        behavior = self.affected_by_behavior
        if 'cold' in behavior:
            return f"The {self.name} is ice cold to the touch. Frost covers its surface."
        elif 'throw' in behavior or 'move' in behavior or 'float' in behavior:
            return f"The {self.name} has been violently displaced. It's still vibrating slightly."
        elif 'slam' in behavior:
            return f"The {self.name} shows signs of violent force. Something slammed it."
        elif 'water' in behavior or 'wet' in behavior:
            return f"The {self.name} is soaking wet. Water drips from it unnaturally."
        elif 'blood' in behavior:
            return f"The {self.name} has dark stains on it. They look fresh..."
        elif 'scratch' in behavior:
            return f"Deep scratch marks cover the {self.name}. They weren't there before."
        elif 'whisper' in behavior:
            return f"You hear faint whispers coming from the {self.name}..."
        elif 'flicker' in behavior or 'dark' in behavior:
            return f"The {self.name} flickers with an unnatural energy."
        else:
            return f"Something is wrong with the {self.name}. It feels... different."
        
    def get_description_for_ghost(self, ghost_name, flashlight_on=False):
        """Get description based on current ghost and flashlight state"""
        if flashlight_on and ghost_name in self.ghost_descriptions:
            return self.ghost_descriptions[ghost_name]
        return self.zoom_description if self.zoom_description else self.description
        
    def draw_highlight(self, surface):
        """Draw highlight when hovered"""
        if self.hovered:
            highlight_surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            # Different highlight color if ghost affected
            if self.ghost_affected:
                highlight_surf.fill((255, 100, 100, 80))  # Red tint for affected objects
                pygame.draw.rect(surface, (255, 100, 100), self.rect, 2)
            else:
                highlight_surf.fill((255, 255, 100, 60))
                pygame.draw.rect(surface, (255, 255, 100), self.rect, 2)
            surface.blit(highlight_surf, self.rect)


class Room:
    """A room in the haunted house"""
    
    def __init__(self, name, display_name, connections, base_color, description):
        self.name = name
        self.display_name = display_name
        self.connections = connections  # Dict of direction: room_name
        self.base_color = base_color
        self.description = description
        self.objects = []
        self.ghost_effects = []
        self.ambient_darkness = 0
        self.lights_on = True  # Room lighting state
        self.effect_frame = 0  # For stable animations
        # Hidden clues that only show with flashlight
        self.hidden_clues = []  # List of (x, y, text, ghost_name) tuples
        self.setup_room()
        
    def setup_room(self):
        """Override in subclasses to set up room-specific elements"""
        pass
    
    def add_object(self, obj):
        """Add an interactive object to the room"""
        self.objects.append(obj)
    
    def add_hidden_clue(self, x, y, text, ghost_name=None):
        """Add a hidden clue only visible with flashlight"""
        self.hidden_clues.append((x, y, text, ghost_name))
    
    def toggle_lights(self):
        """Toggle room lights"""
        self.lights_on = not self.lights_on
        
    def get_object_at(self, pos):
        """Get the interactive object at a position"""
        for obj in self.objects:
            if obj.rect.collidepoint(pos):
                return obj
        return None
    
    def apply_ghost_behavior_to_object(self, behavior):
        """Apply a ghost behavior to a random object in this room"""
        if not self.objects:
            return None
        # Pick a random object
        obj = random.choice(self.objects)
        obj.apply_ghost_effect(behavior)
        return obj
    
    def get_affected_objects(self):
        """Get list of objects currently affected by ghost"""
        return [obj for obj in self.objects if obj.ghost_affected]
    
    def update(self, dt):
        """Update room state"""
        self.effect_frame += 1
        # Update all objects
        for obj in self.objects:
            obj.update(dt)
    
    def update_hover(self, mouse_pos):
        """Update hover state of objects"""
        for obj in self.objects:
            obj.hovered = obj.rect.collidepoint(mouse_pos)
    
    def draw_base(self, surface):
        """Draw the basic room structure"""
        # Floor
        floor_rect = pygame.Rect(0, SCREEN_HEIGHT * 0.6, SCREEN_WIDTH, SCREEN_HEIGHT * 0.4)
        pygame.draw.rect(surface, self.darken_color(self.base_color, 0.7), floor_rect)
        
        # Draw floor boards
        for i in range(0, SCREEN_WIDTH, 80):
            pygame.draw.line(surface, self.darken_color(self.base_color, 0.5), 
                           (i, SCREEN_HEIGHT * 0.6), (i, SCREEN_HEIGHT), 1)
        
        # Walls
        wall_color = self.base_color
        pygame.draw.rect(surface, wall_color, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.6))
        
        # Wall texture lines
        for i in range(0, SCREEN_HEIGHT, 40):
            pygame.draw.line(surface, self.darken_color(wall_color, 0.95),
                           (0, i), (SCREEN_WIDTH, i), 1)
        
        # Ceiling line
        pygame.draw.line(surface, self.darken_color(wall_color, 0.6),
                        (0, 50), (SCREEN_WIDTH, 50), 3)
        
        # Corner shadows for depth
        for i in range(20):
            alpha = 100 - i * 5
            shadow_color = self.darken_color(BLACK, 0.5)
            pygame.draw.line(surface, shadow_color, 
                           (i, 0), (i, SCREEN_HEIGHT), 1)
            pygame.draw.line(surface, shadow_color,
                           (SCREEN_WIDTH - i, 0), (SCREEN_WIDTH - i, SCREEN_HEIGHT), 1)
    
    def draw_navigation_hints(self, surface, font):
        """Draw arrows showing available navigation directions"""
        arrow_color = (200, 200, 200, 180)
        
        for direction, room in self.connections.items():
            if room:
                if direction == "left":
                    # Left arrow
                    points = [(30, SCREEN_HEIGHT // 2), (70, SCREEN_HEIGHT // 2 - 30), 
                             (70, SCREEN_HEIGHT // 2 + 30)]
                    pygame.draw.polygon(surface, arrow_color, points)
                    pygame.draw.polygon(surface, WHITE, points, 2)
                elif direction == "right":
                    # Right arrow
                    points = [(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2), 
                             (SCREEN_WIDTH - 70, SCREEN_HEIGHT // 2 - 30),
                             (SCREEN_WIDTH - 70, SCREEN_HEIGHT // 2 + 30)]
                    pygame.draw.polygon(surface, arrow_color, points)
                    pygame.draw.polygon(surface, WHITE, points, 2)
                elif direction == "up":
                    # Up arrow (for attic)
                    points = [(SCREEN_WIDTH // 2, 30), (SCREEN_WIDTH // 2 - 30, 70),
                             (SCREEN_WIDTH // 2 + 30, 70)]
                    pygame.draw.polygon(surface, arrow_color, points)
                    pygame.draw.polygon(surface, WHITE, points, 2)
                elif direction == "down":
                    # Down arrow (for basement)
                    points = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30),
                             (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT - 70),
                             (SCREEN_WIDTH // 2 + 30, SCREEN_HEIGHT - 70)]
                    pygame.draw.polygon(surface, arrow_color, points)
                    pygame.draw.polygon(surface, WHITE, points, 2)
    
    def draw(self, surface, font):
        """Draw the complete room"""
        self.draw_base(surface)
        self.draw_details(surface)
        
        # Draw darkness overlay if lights are off (before highlights)
        if not self.lights_on:
            darkness_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            darkness_overlay.fill((0, 0, 0, 180))  # Significant darkness
            surface.blit(darkness_overlay, (0, 0))
        
        for obj in self.objects:
            obj.draw_highlight(surface)
        self.draw_navigation_hints(surface, font)
        
        # Draw room name
        name_text = font.render(self.display_name, True, WHITE)
        name_rect = name_text.get_rect(center=(SCREEN_WIDTH // 2, 25))
        pygame.draw.rect(surface, (0, 0, 0, 128), name_rect.inflate(20, 10))
        surface.blit(name_text, name_rect)
    
    def draw_hidden_clues(self, surface, flashlight_pos, flashlight_on, ghost=None):
        """Draw hidden clues only visible in flashlight beam"""
        if not flashlight_on:
            return
            
        fx, fy = flashlight_pos
        font = pygame.font.Font(None, 20)
        
        for x, y, text, ghost_name in self.hidden_clues:
            # Check if in flashlight radius
            dist = math.sqrt((x - fx) ** 2 + (y - fy) ** 2)
            if dist < FLASHLIGHT_RADIUS:
                # Calculate alpha based on distance
                alpha = int(255 * (1 - dist / FLASHLIGHT_RADIUS))
                
                # Only show clue if ghost matches or ghost_name is None
                if ghost_name is None or (ghost and ghost.name == ghost_name):
                    clue_surf = font.render(text, True, (200, 100, 100))
                    clue_surf.set_alpha(alpha)
                    surface.blit(clue_surf, (x, y))
    
    def draw_details(self, surface):
        """Override in subclasses for room-specific details"""
        pass
    
    def darken_color(self, color, factor):
        """Darken a color by a factor"""
        return tuple(int(c * factor) for c in color[:3])
    
    def lighten_color(self, color, factor):
        """Lighten a color by a factor"""
        return tuple(min(255, int(c + (255 - c) * factor)) for c in color[:3])


class EntranceRoom(Room):
    """The entrance/foyer of the haunted house"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_ENTRANCE,
            display_name="Entrance Hall",
            connections={"right": ROOM_LIVING_ROOM, "up": ROOM_HALLWAY},
            base_color=(90, 70, 60),
            description="The grand entrance of the manor. A dusty chandelier hangs overhead, and an old grandfather clock stands against the wall."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Grandfather Clock",
            (100, 200, 120, 280),
            "An antique grandfather clock. It stopped at 3:33 AM.",
            "examine",
            "The clock face shows 3:33. Strange scratch marks surround the clock hands."
        ))
        self.add_object(InteractiveObject(
            "Front Door",
            (550, 150, 180, 300),
            "The front door. It's locked from the outside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Coat Rack",
            (900, 250, 80, 200),
            "An old coat rack with dusty coats.",
            "examine",
            "One of the coats seems to move slightly on its own..."
        ))
        self.add_object(InteractiveObject(
            "Light Switch",
            (50, 300, 30, 50),
            "A light switch.",
            "toggle"
        ))
        # Hidden clues only visible with flashlight
        self.add_hidden_clue(300, 400, "HELP ME", "Bonnie")
        self.add_hidden_clue(700, 350, "GET OUT", "Shadow Stalker")
        self.add_hidden_clue(150, 500, "3:33 AM", None)  # Always visible with flashlight
    
    def draw_details(self, surface):
        # Grandfather clock
        pygame.draw.rect(surface, DARK_BROWN, (100, 200, 120, 280))
        pygame.draw.rect(surface, BROWN, (110, 210, 100, 100))
        pygame.draw.circle(surface, CREAM, (160, 260), 40)
        pygame.draw.circle(surface, BLACK, (160, 260), 40, 2)
        # Clock hands
        pygame.draw.line(surface, BLACK, (160, 260), (160, 230), 2)
        pygame.draw.line(surface, BLACK, (160, 260), (180, 270), 2)
        
        # Chandelier
        pygame.draw.polygon(surface, GRAY, [(640, 0), (600, 80), (680, 80)])
        for i in range(5):
            x = 580 + i * 30
            pygame.draw.line(surface, DARK_GRAY, (640, 60), (x, 100), 2)
            # Flickering lights when on
            if self.lights_on:
                light_color = YELLOW if random.random() > 0.1 else ORANGE
            else:
                light_color = DARK_GRAY
            pygame.draw.circle(surface, light_color, (x, 110), 8)
        
        # Front door
        pygame.draw.rect(surface, (60, 40, 30), (550, 150, 180, 300))
        pygame.draw.rect(surface, (80, 50, 40), (560, 160, 160, 280))
        pygame.draw.circle(surface, (180, 150, 50), (690, 310), 12)
        
        # Coat rack
        pygame.draw.rect(surface, DARK_BROWN, (935, 250, 10, 200))
        pygame.draw.polygon(surface, DARK_BROWN, [(900, 250), (980, 250), (940, 200)])
        # Coats
        pygame.draw.ellipse(surface, (40, 40, 50), (895, 260, 40, 100))
        pygame.draw.ellipse(surface, (60, 30, 30), (935, 270, 45, 90))
        
        # Welcome mat
        pygame.draw.rect(surface, (100, 80, 60), (580, 460, 120, 40))
        
        # Light switch - show state
        pygame.draw.rect(surface, CREAM, (50, 300, 30, 50))
        switch_y = 310 if self.lights_on else 325
        pygame.draw.rect(surface, GRAY, (58, switch_y, 14, 20))


class LivingRoom(Room):
    """The living room with fireplace and furniture"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_LIVING_ROOM,
            display_name="Living Room",
            connections={"left": ROOM_ENTRANCE, "right": ROOM_KITCHEN, "up": ROOM_BEDROOM},
            base_color=(85, 75, 70),
            description="A once-cozy living room. A cold fireplace dominates one wall, surrounded by dusty furniture."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Fireplace",
            (500, 200, 280, 250),
            "An old stone fireplace. The ashes are cold.",
            "examine",
            "Among the ashes, you notice strange symbols drawn in the soot."
        ))
        self.add_object(InteractiveObject(
            "Old Sofa",
            (100, 380, 300, 120),
            "A worn Victorian sofa. Something moved in the cushions.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Portrait",
            (900, 150, 150, 200),
            "A family portrait. The faces seem to follow you.",
            "zoom",
            "The portrait shows a family of four. One face has been scratched out violently."
        ))
        self.add_object(InteractiveObject(
            "Coffee Table",
            (200, 350, 150, 80),
            "A dusty coffee table with old magazines.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(550, 450, "IT BURNS", "The Burned Man")
        self.add_hidden_clue(920, 380, "WATCHING YOU", "The Mimic")
        self.add_hidden_clue(350, 520, "I SEE YOU", None)
    
    def draw_details(self, surface):
        # Fireplace
        pygame.draw.rect(surface, (60, 60, 60), (500, 200, 280, 250))
        pygame.draw.rect(surface, (40, 40, 40), (520, 220, 240, 200))
        # Mantle
        pygame.draw.rect(surface, BROWN, (480, 180, 320, 25))
        # Fire grate
        pygame.draw.rect(surface, (30, 30, 30), (540, 350, 200, 60))
        
        # Sofa
        pygame.draw.rect(surface, (100, 50, 50), (100, 380, 300, 120))
        pygame.draw.rect(surface, (120, 60, 60), (100, 380, 300, 40))
        pygame.draw.rect(surface, (90, 45, 45), (100, 380, 50, 120))
        pygame.draw.rect(surface, (90, 45, 45), (350, 380, 50, 120))
        
        # Portrait frame
        pygame.draw.rect(surface, (120, 80, 40), (900, 150, 150, 200))
        pygame.draw.rect(surface, (180, 160, 140), (915, 165, 120, 170))
        # Simple figures in portrait
        for i, x in enumerate([945, 985, 1005, 965]):
            color = (180, 150, 140) if i != 2 else (50, 50, 50)
            pygame.draw.circle(surface, color, (x, 210 + (i % 2) * 30), 15)
        
        # Coffee table
        pygame.draw.rect(surface, (80, 50, 30), (200, 350, 150, 10))
        pygame.draw.rect(surface, (70, 45, 25), (210, 360, 10, 60))
        pygame.draw.rect(surface, (70, 45, 25), (330, 360, 10, 60))
        
        # Lamp
        pygame.draw.rect(surface, DARK_BROWN, (430, 330, 20, 80))
        pygame.draw.polygon(surface, CREAM, [(400, 330), (480, 330), (460, 280), (420, 280)])
        
        # Rug
        pygame.draw.ellipse(surface, (120, 80, 80), (150, 450, 400, 150))
        pygame.draw.ellipse(surface, (100, 60, 60), (180, 470, 340, 110))


class KitchenRoom(Room):
    """The kitchen with appliances and cabinets"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_KITCHEN,
            display_name="Kitchen",
            connections={"left": ROOM_LIVING_ROOM, "right": ROOM_DINING_ROOM, "down": ROOM_BASEMENT},
            base_color=(80, 85, 75),
            description="A dated kitchen with rusty appliances. Something drips from the faucet."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Refrigerator",
            (100, 180, 120, 280),
            "An old refrigerator. It's humming strangely.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Sink",
            (500, 280, 150, 100),
            "A stained sink. The water runs red momentarily.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Knife Block",
            (700, 300, 60, 80),
            "A knife block. One knife is missing.",
            "examine",
            "The empty slot is stained with something dark..."
        ))
        self.add_object(InteractiveObject(
            "Cabinet",
            (850, 150, 200, 150),
            "Kitchen cabinets. Something scratches inside.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Stove",
            (300, 280, 150, 120),
            "An old gas stove. The burners flicker on their own.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(550, 400, "THE KNIFE...", "The Butcher")
        self.add_hidden_clue(150, 480, "MEAT", "The Butcher")
        self.add_hidden_clue(800, 350, "MEDICINE TIME", "The Nurse")
    
    def draw_details(self, surface):
        # Counter
        pygame.draw.rect(surface, (60, 60, 65), (250, 280, 550, 30))
        pygame.draw.rect(surface, (70, 70, 75), (250, 310, 550, 150))
        
        # Refrigerator
        pygame.draw.rect(surface, (200, 200, 200), (100, 180, 120, 280))
        pygame.draw.rect(surface, (180, 180, 180), (105, 185, 110, 135))
        pygame.draw.rect(surface, (180, 180, 180), (105, 325, 110, 130))
        pygame.draw.rect(surface, (100, 100, 100), (200, 250, 10, 30))
        pygame.draw.rect(surface, (100, 100, 100), (200, 380, 10, 30))
        
        # Sink
        pygame.draw.rect(surface, (150, 150, 155), (500, 280, 150, 100))
        pygame.draw.rect(surface, (80, 80, 85), (515, 295, 120, 70))
        # Faucet
        pygame.draw.rect(surface, (160, 160, 170), (570, 260, 20, 40))
        pygame.draw.rect(surface, (160, 160, 170), (560, 250, 40, 15))
        
        # Stove
        pygame.draw.rect(surface, (50, 50, 55), (300, 280, 150, 120))
        for i in range(4):
            x = 330 + (i % 2) * 60
            y = 300 + (i // 2) * 40
            pygame.draw.circle(surface, (30, 30, 35), (x, y), 20)
            pygame.draw.circle(surface, (60, 60, 65), (x, y), 15)
        
        # Knife block
        pygame.draw.rect(surface, DARK_BROWN, (700, 300, 60, 80))
        for i in range(4):
            pygame.draw.rect(surface, (150, 150, 160) if i != 2 else DARK_BROWN, 
                           (710 + i * 12, 280, 8, 25))
        
        # Cabinets
        pygame.draw.rect(surface, (100, 80, 60), (250, 150, 600, 120))
        for i in range(6):
            pygame.draw.rect(surface, (120, 100, 80), (260 + i * 98, 160, 90, 100))
            pygame.draw.circle(surface, (80, 80, 60), (305 + i * 98, 210), 5)
        
        # Window above sink
        pygame.draw.rect(surface, (40, 50, 60), (520, 100, 110, 100))
        pygame.draw.rect(surface, (60, 70, 90), (525, 105, 100, 90))
        pygame.draw.line(surface, (40, 50, 60), (575, 105), (575, 195), 2)
        pygame.draw.line(surface, (40, 50, 60), (525, 150), (625, 150), 2)


class DiningRoom(Room):
    """The dining room with a large table"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_DINING_ROOM,
            display_name="Dining Room",
            connections={"left": ROOM_KITCHEN, "up": ROOM_STUDY},
            base_color=(95, 80, 70),
            description="A formal dining room. The table is set for a dinner that never happened."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dining Table",
            (300, 300, 600, 200),
            "A long oak table with dusty place settings.",
            "examine",
            "The plates are set for six, but only five chairs remain. The sixth appears to have been thrown."
        ))
        self.add_object(InteractiveObject(
            "China Cabinet",
            (50, 150, 150, 300),
            "A cabinet full of fine china. Some pieces are shattered.",
            "zoom",
            "The broken pieces form a pattern... almost like letters."
        ))
        self.add_object(InteractiveObject(
            "Candelabra",
            (580, 280, 60, 80),
            "A silver candelabra. The candles flicker without wind.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Wine Rack",
            (1050, 200, 100, 200),
            "A wine rack. One bottle is half empty and fresh.",
            "examine"
        ))
    
    def draw_details(self, surface):
        # Dining table
        pygame.draw.rect(surface, (100, 70, 40), (300, 300, 600, 200))
        pygame.draw.rect(surface, (80, 55, 30), (320, 280, 560, 25))
        # Table legs
        for x in [320, 860]:
            pygame.draw.rect(surface, (90, 60, 35), (x, 480, 30, 100))
        
        # Place settings
        for i in range(6):
            x = 380 + i * 90
            if i != 5:  # Skip one setting
                pygame.draw.circle(surface, CREAM, (x, 370), 25)
                pygame.draw.circle(surface, (200, 200, 200), (x, 370), 20)
        
        # Chairs
        for i in range(3):
            x = 350 + i * 120
            pygame.draw.rect(surface, DARK_BROWN, (x, 500, 50, 60))
            pygame.draw.rect(surface, DARK_BROWN, (x, 450, 50, 20))
        for i in range(3):
            x = 650 + i * 120
            if i != 2:
                pygame.draw.rect(surface, DARK_BROWN, (x, 220, 50, 60))
        
        # China cabinet
        pygame.draw.rect(surface, (80, 50, 30), (50, 150, 150, 300))
        pygame.draw.rect(surface, (100, 120, 140), (60, 160, 130, 140))
        pygame.draw.rect(surface, (80, 50, 30), (60, 310, 130, 130))
        # China pieces - some broken (fixed positions)
        china_positions = [(80, 180), (120, 180), (160, 180), (80, 220), (160, 220), (80, 260), (120, 260), (160, 260)]
        for x, y in china_positions:
            pygame.draw.circle(surface, WHITE, (x, y), 12)
        
        # Candelabra with flickering candles
        pygame.draw.rect(surface, (180, 180, 190), (600, 320, 20, 60))
        for i in range(3):
            pygame.draw.rect(surface, (180, 180, 190), (580 + i * 20, 300, 10, 30))
            if self.lights_on:
                candle_color = YELLOW if random.random() > 0.15 else ORANGE
            else:
                candle_color = DARK_GRAY
            pygame.draw.circle(surface, candle_color, (585 + i * 20, 295), 6)
        
        # Wine rack
        pygame.draw.rect(surface, DARK_BROWN, (1050, 200, 100, 200))
        for y in range(5):
            for x in range(3):
                pygame.draw.circle(surface, (60, 20, 30), (1070 + x * 30, 220 + y * 35), 10)
        
        # Chandelier
        pygame.draw.polygon(surface, (120, 100, 80), [(600, 0), (550, 60), (650, 60)])
        pygame.draw.rect(surface, (150, 130, 100), (580, 60, 40, 30))


class HallwayRoom(Room):
    """The upstairs hallway connecting rooms"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_HALLWAY,
            display_name="Upstairs Hallway",
            connections={"left": ROOM_BEDROOM, "right": ROOM_BATHROOM, 
                        "up": ROOM_ATTIC, "down": ROOM_ENTRANCE},
            base_color=(75, 70, 80),
            description="A long, dark hallway. The floorboards creak with every step."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Mirror",
            (550, 180, 180, 250),
            "An ornate mirror. Your reflection seems delayed.",
            "zoom",
            "For a moment, you see someone standing behind you in the reflection..."
        ))
        self.add_object(InteractiveObject(
            "Hallway Light",
            (640, 50, 40, 60),
            "A flickering hallway light.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Old Rug",
            (400, 480, 400, 100),
            "A worn oriental rug. There's a lump underneath.",
            "examine",
            "Lifting the rug reveals scratch marks on the floor, leading to the attic stairs."
        ))
        self.add_object(InteractiveObject(
            "Family Photos",
            (100, 200, 200, 100),
            "A collection of family photographs.",
            "zoom",
            "In each photo, one person's face appears blurred or distorted."
        ))
    
    def draw_details(self, surface):
        # Wainscoting
        pygame.draw.rect(surface, (60, 55, 65), (0, 350, SCREEN_WIDTH, 100))
        for i in range(0, SCREEN_WIDTH, 100):
            pygame.draw.rect(surface, (70, 65, 75), (i + 10, 360, 80, 80))
        
        # Mirror with ornate frame
        pygame.draw.rect(surface, (120, 90, 50), (540, 170, 200, 270))
        pygame.draw.rect(surface, (140, 140, 160), (560, 190, 160, 230))
        # Reflection effect
        pygame.draw.rect(surface, (120, 120, 140), (570, 200, 140, 210))
        
        # Light fixture
        pygame.draw.rect(surface, (60, 60, 70), (655, 50, 10, 30))
        if self.lights_on:
            light_color = (255, 250, 200) if random.random() > 0.1 else (200, 180, 100)
        else:
            light_color = (100, 90, 50)
        pygame.draw.circle(surface, light_color, (660, 90), 20)
        
        # Rug
        pygame.draw.rect(surface, (100, 60, 60), (400, 480, 400, 100))
        pygame.draw.rect(surface, (120, 80, 80), (420, 500, 360, 60))
        # Pattern
        for i in range(6):
            pygame.draw.rect(surface, (80, 40, 40), (440 + i * 55, 510, 40, 40))
        
        # Family photos
        for i in range(3):
            pygame.draw.rect(surface, DARK_BROWN, (100 + i * 70, 200, 60, 80))
            pygame.draw.rect(surface, (150, 140, 130), (105 + i * 70, 205, 50, 70))
        
        # Doors to other rooms
        pygame.draw.rect(surface, (60, 40, 35), (50, 200, 100, 250))
        pygame.draw.rect(surface, (60, 40, 35), (1130, 200, 100, 250))
        pygame.draw.circle(surface, (180, 150, 50), (135, 330), 8)
        pygame.draw.circle(surface, (180, 150, 50), (1145, 330), 8)


class BedroomRoom(Room):
    """The master bedroom"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_BEDROOM,
            display_name="Master Bedroom",
            connections={"right": ROOM_HALLWAY, "down": ROOM_LIVING_ROOM},
            base_color=(80, 70, 90),
            description="The master bedroom. The bed is unmade, as if someone left in a hurry."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bed",
            (400, 280, 400, 250),
            "A large four-poster bed. The sheets are tangled.",
            "examine",
            "There are handprints pressed into the pillow... from the inside."
        ))
        self.add_object(InteractiveObject(
            "Wardrobe",
            (50, 180, 150, 300),
            "An antique wardrobe. Something rustles inside.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Nightstand",
            (850, 350, 80, 100),
            "A nightstand with a diary on top.",
            "zoom",
            "The last entry: 'It watches me while I sleep. Tonight I will end this.'"
        ))
        self.add_object(InteractiveObject(
            "Window",
            (1000, 150, 150, 200),
            "A large window. The curtains move without wind.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(500, 500, "DON'T SLEEP", "Nightmare")
        self.add_hidden_clue(100, 450, "I'M IN HERE", "The Doll")
        self.add_hidden_clue(1050, 400, "ROPE", "The Hanged Man")
    
    def draw_details(self, surface):
        # Bed
        pygame.draw.rect(surface, (60, 45, 35), (380, 280, 440, 250))  # Frame
        pygame.draw.rect(surface, (200, 180, 160), (400, 300, 400, 180))  # Mattress
        pygame.draw.rect(surface, (180, 170, 160), (400, 300, 400, 60))  # Pillow area
        # Bedposts
        for x in [380, 800]:
            pygame.draw.rect(surface, (60, 45, 35), (x, 200, 20, 330))
            pygame.draw.circle(surface, (80, 60, 45), (x + 10, 200), 15)
        # Canopy frame
        pygame.draw.rect(surface, (60, 45, 35), (380, 200, 440, 10))
        
        # Wardrobe
        pygame.draw.rect(surface, (70, 50, 40), (50, 180, 150, 300))
        pygame.draw.rect(surface, (80, 60, 50), (55, 185, 68, 290))
        pygame.draw.rect(surface, (80, 60, 50), (127, 185, 68, 290))
        pygame.draw.circle(surface, (180, 150, 50), (115, 330), 6)
        pygame.draw.circle(surface, (180, 150, 50), (135, 330), 6)
        
        # Nightstand
        pygame.draw.rect(surface, (70, 50, 40), (850, 350, 80, 100))
        pygame.draw.rect(surface, (90, 70, 55), (855, 380, 70, 30))
        # Diary
        pygame.draw.rect(surface, (100, 50, 50), (865, 355, 50, 35))
        
        # Window
        pygame.draw.rect(surface, (40, 45, 55), (1000, 150, 150, 200))
        pygame.draw.rect(surface, (50, 55, 70), (1010, 160, 130, 180))
        pygame.draw.line(surface, (40, 45, 55), (1075, 160), (1075, 340), 3)
        pygame.draw.line(surface, (40, 45, 55), (1010, 250), (1140, 250), 3)
        # Curtains
        pygame.draw.rect(surface, (120, 80, 100), (990, 140, 40, 220))
        pygame.draw.rect(surface, (120, 80, 100), (1120, 140, 40, 220))
        
        # Dresser with mirror
        pygame.draw.rect(surface, (70, 50, 40), (250, 300, 100, 150))
        pygame.draw.rect(surface, (60, 60, 70), (265, 200, 70, 100))


class BathroomRoom(Room):
    """The bathroom"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_BATHROOM,
            display_name="Bathroom",
            connections={"left": ROOM_HALLWAY},
            base_color=(180, 180, 185),
            description="A tiled bathroom. The mirror is fogged, and words seem to appear in the condensation."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bathtub",
            (600, 280, 350, 200),
            "A claw-foot bathtub. The water is murky.",
            "examine",
            "Something dark moves beneath the surface of the water..."
        ))
        self.add_object(InteractiveObject(
            "Bathroom Mirror",
            (200, 180, 200, 150),
            "A foggy mirror. Writing appears in the steam.",
            "zoom",
            "Words form in the fog: 'BEHIND YOU' - but there's nothing there."
        ))
        self.add_object(InteractiveObject(
            "Medicine Cabinet",
            (450, 200, 100, 120),
            "A medicine cabinet. Pills are scattered inside.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Toilet",
            (100, 350, 80, 120),
            "The toilet. The water occasionally bubbles.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(220, 250, "LOOK", "The Hanged Man")
        self.add_hidden_clue(700, 400, "DROWN", "Weeping Lady")
        self.add_hidden_clue(460, 320, "OVERDOSE", "The Nurse")
    
    def draw_details(self, surface):
        # Tile pattern on walls
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 40):
            for x in range(0, SCREEN_WIDTH, 40):
                color = (170, 170, 175) if (x + y) % 80 == 0 else (180, 180, 185)
                pygame.draw.rect(surface, color, (x, y, 38, 38))
        
        # Bathtub
        pygame.draw.ellipse(surface, (220, 220, 225), (600, 280, 350, 200))
        pygame.draw.ellipse(surface, (180, 200, 190), (620, 300, 310, 160))
        # Claw feet
        for x in [620, 920]:
            pygame.draw.ellipse(surface, (150, 140, 130), (x, 470, 30, 20))
        # Faucet
        pygame.draw.rect(surface, (180, 180, 190), (750, 260, 40, 30))
        
        # Mirror
        pygame.draw.rect(surface, (100, 80, 60), (195, 175, 210, 160))
        pygame.draw.rect(surface, (200, 210, 220), (205, 185, 190, 140))
        # Fog effect
        fog_surf = pygame.Surface((190, 140), pygame.SRCALPHA)
        fog_surf.fill((255, 255, 255, 100))
        surface.blit(fog_surf, (205, 185))
        
        # Sink below mirror
        pygame.draw.ellipse(surface, (220, 220, 225), (250, 350, 100, 60))
        pygame.draw.ellipse(surface, (180, 180, 185), (265, 360, 70, 40))
        pygame.draw.rect(surface, (180, 180, 190), (295, 320, 20, 40))
        
        # Medicine cabinet
        pygame.draw.rect(surface, (180, 180, 185), (450, 200, 100, 120))
        pygame.draw.rect(surface, (200, 200, 205), (455, 205, 90, 110))
        pygame.draw.circle(surface, (160, 160, 165), (540, 260), 6)
        
        # Toilet
        pygame.draw.ellipse(surface, (220, 220, 225), (100, 380, 80, 100))
        pygame.draw.ellipse(surface, (200, 210, 220), (110, 400, 60, 60))
        pygame.draw.rect(surface, (220, 220, 225), (100, 350, 80, 40))
        pygame.draw.rect(surface, (200, 200, 205), (110, 340, 60, 20))
        
        # Shower curtain
        pygame.draw.rect(surface, (150, 100, 100), (580, 120, 20, 360))
        pygame.draw.rect(surface, (170, 130, 130, 180), (600, 120, 100, 360))


class StudyRoom(Room):
    """The study/library"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_STUDY,
            display_name="Study",
            connections={"down": ROOM_DINING_ROOM},
            base_color=(60, 50, 45),
            description="A wood-paneled study filled with books. The smell of old paper fills the air."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Desk",
            (400, 320, 350, 150),
            "A mahogany desk. Papers are scattered about.",
            "zoom",
            "Research notes about spirits and how to identify them. One page is circled: 'They cannot hide their nature.'"
        ))
        self.add_object(InteractiveObject(
            "Bookshelf",
            (50, 120, 250, 350),
            "Towering bookshelves. Some books float briefly.",
            "examine",
            "One book is warm to the touch: 'A History of This House'"
        ))
        self.add_object(InteractiveObject(
            "Globe",
            (900, 300, 100, 100),
            "An antique globe. It spins on its own.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Fireplace",
            (1050, 200, 180, 250),
            "A small fireplace. Cold ashes remain.",
            "examine"
        ))
    
    def draw_details(self, surface):
        # Wood paneling
        for i in range(0, SCREEN_WIDTH, 120):
            pygame.draw.rect(surface, (55, 45, 40), (i, 0, 2, int(SCREEN_HEIGHT * 0.6)))
        
        # Desk
        pygame.draw.rect(surface, (90, 60, 40), (400, 320, 350, 20))
        pygame.draw.rect(surface, (80, 50, 35), (410, 340, 100, 130))
        pygame.draw.rect(surface, (80, 50, 35), (640, 340, 100, 130))
        # Papers - fixed positions
        paper_positions = [430, 480, 530, 580, 670]
        for x in paper_positions:
            pygame.draw.rect(surface, CREAM, (x, 300, 40, 30))
        # Ink pot
        pygame.draw.rect(surface, (20, 20, 30), (650, 305, 20, 20))
        
        # Bookshelf
        pygame.draw.rect(surface, (70, 45, 30), (50, 120, 250, 350))
        book_colors = [(100, 50, 50), (50, 100, 50), (50, 50, 100), (100, 80, 50), (80, 50, 80)]
        for row in range(5):
            y = 140 + row * 65
            pygame.draw.rect(surface, (60, 40, 25), (55, y, 240, 5))
            for col in range(10):
                color = book_colors[(row + col) % len(book_colors)]
                pygame.draw.rect(surface, color, (60 + col * 23, y + 5, 20, 55))
        
        # Globe
        pygame.draw.rect(surface, (80, 50, 35), (945, 400, 10, 50))
        pygame.draw.circle(surface, (100, 130, 160), (950, 350), 50)
        pygame.draw.circle(surface, (80, 110, 140), (950, 350), 45)
        # Globe stand
        pygame.draw.arc(surface, (80, 50, 35), (900, 300, 100, 100), 0, 3.14, 3)
        
        # Fireplace
        pygame.draw.rect(surface, (50, 50, 55), (1050, 200, 180, 250))
        pygame.draw.rect(surface, (30, 30, 35), (1070, 220, 140, 200))
        pygame.draw.rect(surface, (80, 55, 40), (1040, 180, 200, 25))
        
        # Desk lamp
        pygame.draw.rect(surface, (60, 60, 50), (500, 280, 15, 50))
        pygame.draw.ellipse(surface, (80, 100, 50), (480, 265, 50, 25))
        
        # Chair
        pygame.draw.rect(surface, (80, 50, 35), (520, 450, 80, 80))
        pygame.draw.rect(surface, (100, 60, 45), (520, 390, 80, 70))


class AtticRoom(Room):
    """The attic"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_ATTIC,
            display_name="Attic",
            connections={"down": ROOM_HALLWAY},
            base_color=(70, 65, 60),
            description="A dusty attic filled with forgotten memories. Cobwebs cover everything."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Old Trunk",
            (200, 350, 180, 120),
            "A locked trunk. Something inside wants out.",
            "toggle",
            "The trunk contains children's toys and a photograph of a boy named 'Timmy'."
        ))
        self.add_object(InteractiveObject(
            "Rocking Horse",
            (600, 320, 150, 150),
            "A child's rocking horse. It rocks by itself.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Dusty Mirror",
            (900, 180, 120, 200),
            "A covered mirror. They say mirrors are portals.",
            "toggle",
            "Removing the cloth reveals a face that isn't yours staring back."
        ))
        self.add_object(InteractiveObject(
            "Old Boxes",
            (100, 200, 150, 100),
            "Stacked boxes with old labels.",
            "examine",
            "One box is labeled 'DO NOT OPEN - 1923'"
        ))
        self.add_object(InteractiveObject(
            "Attic Window",
            (1050, 100, 150, 150),
            "A grimy window. Lightning flashes outside.",
            "examine"
        ))
    
    def draw_details(self, surface):
        # Sloped ceiling
        pygame.draw.polygon(surface, (60, 55, 50), 
                          [(0, 100), (640, 20), (1280, 100), (1280, 0), (0, 0)])
        # Ceiling beams
        for x in range(0, SCREEN_WIDTH, 200):
            pygame.draw.line(surface, (50, 45, 40), (x, 100), (640, 20), 8)
        
        # Old trunk
        pygame.draw.rect(surface, (80, 50, 35), (200, 350, 180, 120))
        pygame.draw.rect(surface, (70, 45, 30), (200, 350, 180, 20))
        pygame.draw.rect(surface, (60, 40, 25), (210, 360, 160, 10))
        pygame.draw.rect(surface, (150, 130, 50), (285, 400, 20, 30))  # Lock
        
        # Rocking horse
        pygame.draw.ellipse(surface, (100, 70, 50), (600, 420, 150, 40))  # Rockers
        pygame.draw.rect(surface, (120, 80, 60), (650, 350, 50, 80))  # Body
        pygame.draw.polygon(surface, (120, 80, 60), [(650, 350), (620, 300), (640, 310)])  # Head
        pygame.draw.circle(surface, (40, 30, 20), (625, 310), 5)  # Eye
        pygame.draw.rect(surface, (80, 60, 40), (660, 430, 10, 30))  # Legs
        pygame.draw.rect(surface, (80, 60, 40), (700, 430, 10, 30))
        
        # Covered mirror
        pygame.draw.rect(surface, (60, 55, 50), (900, 180, 120, 200))
        pygame.draw.rect(surface, (150, 140, 130), (905, 185, 110, 190))
        # Dust sheet partially covering
        pygame.draw.polygon(surface, (180, 170, 160), 
                          [(895, 180), (1025, 180), (1025, 280), (920, 260)])
        
        # Old boxes
        pygame.draw.rect(surface, (120, 100, 80), (100, 200, 80, 60))
        pygame.draw.rect(surface, (100, 80, 60), (130, 180, 90, 70))
        pygame.draw.rect(surface, (110, 90, 70), (110, 160, 70, 50))
        
        # Cobwebs
        for x, y in [(50, 50), (1200, 50), (400, 100)]:
            for i in range(6):
                angle = i * 0.5
                pygame.draw.line(surface, (200, 200, 200, 100), 
                               (x, y), (x + math.cos(angle) * 60, y + math.sin(angle) * 60), 1)
        
        # Attic window
        pygame.draw.rect(surface, (40, 45, 55), (1050, 100, 150, 150))
        pygame.draw.rect(surface, (30, 35, 50), (1060, 110, 130, 130))
        pygame.draw.line(surface, (40, 45, 55), (1125, 110), (1125, 240), 3)
        
        # Dust particles effect - fixed positions
        dust_positions = [(100, 150), (300, 200), (500, 180), (700, 250), (900, 170),
                         (200, 350), (400, 400), (600, 320), (800, 380), (1000, 300),
                         (150, 500), (350, 450), (550, 520), (750, 480), (950, 440),
                         (250, 600), (450, 550), (650, 580), (850, 620), (1050, 560)]
        for x, y in dust_positions:
            pygame.draw.circle(surface, (200, 190, 170), (x, y), 1)


class BasementRoom(Room):
    """The basement"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_BASEMENT,
            display_name="Basement",
            connections={"up": ROOM_KITCHEN},
            base_color=(45, 45, 50),
            description="A cold, damp basement. Something drips in the darkness."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Furnace",
            (100, 200, 200, 280),
            "An old furnace. It rumbles ominously.",
            "examine",
            "The furnace door is slightly ajar. Inside, you see... bones."
        ))
        self.add_object(InteractiveObject(
            "Wine Cellar",
            (800, 200, 250, 200),
            "Racks of old wine bottles covered in dust.",
            "examine",
            "One bottle has a message inside: 'HE'S IN THE WALLS'"
        ))
        self.add_object(InteractiveObject(
            "Workbench",
            (400, 350, 200, 100),
            "A bloody workbench with rusty tools.",
            "zoom",
            "The stains are old but deep. Scratched into the wood: tally marks. Hundreds of them."
        ))
        self.add_object(InteractiveObject(
            "Chains",
            (650, 150, 100, 200),
            "Chains hanging from the ceiling.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Drain",
            (550, 550, 80, 80),
            "A floor drain. Strange sounds come from below.",
            "examine",
            "Looking into the drain, two eyes look back at you."
        ))
    
    def draw_details(self, surface):
        # Brick walls
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 30):
            offset = 30 if (y // 30) % 2 else 0
            for x in range(-30 + offset, SCREEN_WIDTH, 60):
                pygame.draw.rect(surface, (55, 40, 40), (x, y, 58, 28))
                pygame.draw.rect(surface, (45, 35, 35), (x, y, 58, 28), 1)
        
        # Furnace
        pygame.draw.rect(surface, (50, 50, 55), (100, 200, 200, 280))
        pygame.draw.rect(surface, (40, 40, 45), (120, 300, 80, 100))  # Door
        pygame.draw.circle(surface, (30, 30, 35), (160, 350), 30)  # Porthole
        # Furnace glow based on effect frame for smooth animation
        if (self.effect_frame // 30) % 3 == 0:
            pygame.draw.circle(surface, (200, 100, 50), (160, 350), 25)  # Glow
        pygame.draw.rect(surface, (60, 60, 65), (180, 200, 100, 30))  # Pipe
        
        # Wine cellar rack
        pygame.draw.rect(surface, (60, 40, 30), (800, 200, 250, 200))
        for row in range(4):
            for col in range(6):
                pygame.draw.circle(surface, (40, 20, 25), 
                                 (830 + col * 35, 230 + row * 45), 12)
        
        # Workbench
        pygame.draw.rect(surface, (80, 60, 45), (400, 350, 200, 20))
        pygame.draw.rect(surface, (70, 50, 35), (410, 370, 30, 100))
        pygame.draw.rect(surface, (70, 50, 35), (560, 370, 30, 100))
        # Blood stains
        pygame.draw.ellipse(surface, (80, 30, 30), (450, 330, 60, 30))
        pygame.draw.ellipse(surface, (70, 25, 25), (420, 340, 40, 20))
        # Tools
        pygame.draw.rect(surface, (120, 120, 130), (500, 340, 40, 15))
        pygame.draw.rect(surface, (100, 100, 110), (540, 335, 10, 25))
        
        # Chains
        for x in [660, 700, 740]:
            for y in range(150, 350, 15):
                pygame.draw.circle(surface, (100, 100, 110), (x, y), 5, 2)
        
        # Drain
        pygame.draw.circle(surface, (30, 30, 35), (590, 590), 40)
        pygame.draw.circle(surface, (20, 20, 25), (590, 590), 30)
        # Grate
        for i in range(5):
            pygame.draw.line(surface, (50, 50, 55), 
                           (560 + i * 15, 560), (560 + i * 15, 620), 2)
        
        # Pipes on ceiling
        for y in [60, 90]:
            pygame.draw.rect(surface, (80, 80, 85), (0, y, SCREEN_WIDTH, 15))
        
        # Water drips - fixed positions
        drip_positions = [200, 600, 1000]
        for x in drip_positions:
            drip_length = 8 + (self.effect_frame // 10) % 8
            pygame.draw.line(surface, (100, 120, 150), (x, 100), (x, 100 + drip_length), 2)
        
        # Light bulb with flickering
        pygame.draw.line(surface, (60, 60, 60), (640, 0), (640, 80), 2)
        if self.lights_on:
            light_color = (200, 180, 100) if random.random() > 0.2 else (100, 90, 50)
        else:
            light_color = (100, 90, 50)
        pygame.draw.circle(surface, light_color, (640, 90), 15)


def create_all_rooms():
    """Create and return a dictionary of all rooms"""
    rooms = {
        ROOM_ENTRANCE: EntranceRoom(),
        ROOM_LIVING_ROOM: LivingRoom(),
        ROOM_KITCHEN: KitchenRoom(),
        ROOM_DINING_ROOM: DiningRoom(),
        ROOM_HALLWAY: HallwayRoom(),
        ROOM_BEDROOM: BedroomRoom(),
        ROOM_BATHROOM: BathroomRoom(),
        ROOM_STUDY: StudyRoom(),
        ROOM_ATTIC: AtticRoom(),
        ROOM_BASEMENT: BasementRoom(),
    }
    return rooms
