"""
Location-specific room layouts for Paranormal Investigations
Each location has unique rooms with themed objects and descriptions
"""

import pygame
import math
import random
from constants import *
from rooms import Room, InteractiveObject


# ===============================================================================
# ABANDONED HOSPITAL ROOMS
# ===============================================================================

class HospitalReceptionRoom(Room):
    """Hospital reception area"""
    
    def __init__(self):
        super().__init__(
            name="reception",
            display_name="Reception",
            connections={"right": "waiting_room", "up": "doctors_office"},
            base_color=(200, 200, 210),
            description="The hospital reception desk. Papers are scattered everywhere, and the phone keeps ringing."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Reception Desk", (400, 300, 300, 120),
            "A large reception desk covered in dust and old patient files.",
            "examine",
            "Patient files are scattered about. One is marked 'DECEASED - DO NOT RELEASE'."
        ))
        self.add_object(InteractiveObject(
            "Phone", (500, 280, 50, 40),
            "An old rotary phone. It rings occasionally but no one is calling.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Wheelchair", (100, 350, 100, 120),
            "An old wheelchair. Its wheels squeak as if moving on their own.",
            "examine"
        ))
        self.add_hidden_clue(600, 450, "PATIENT ZERO", "The Plague Doctor")
    
    def draw_details(self, surface):
        # Reception desk
        pygame.draw.rect(surface, (180, 180, 190), (400, 300, 300, 120))
        pygame.draw.rect(surface, (160, 160, 170), (410, 310, 280, 100))
        # Papers
        for i in range(5):
            pygame.draw.rect(surface, CREAM, (420 + i * 50, 290, 40, 30))
        # Wheelchair
        pygame.draw.circle(surface, (100, 100, 100), (120, 450), 30, 3)
        pygame.draw.circle(surface, (100, 100, 100), (180, 450), 30, 3)
        pygame.draw.rect(surface, (80, 80, 80), (110, 370, 80, 60))


class HospitalWaitingRoom(Room):
    """Hospital waiting room with chairs"""
    
    def __init__(self):
        super().__init__(
            name="waiting_room",
            display_name="Waiting Room",
            connections={"left": "reception", "right": "emergency_room", "down": "patient_ward"},
            base_color=(190, 195, 200),
            description="Rows of plastic chairs face a flickering TV. Magazines from decades ago litter the floor."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Waiting Chairs", (200, 350, 400, 100),
            "Rows of uncomfortable plastic chairs. Some are stained.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "TV", (900, 200, 150, 100),
            "An old CRT television showing static. Sometimes faces appear.",
            "examine",
            "The static forms a face. It's screaming silently."
        ))
        self.add_object(InteractiveObject(
            "Magazines", (650, 400, 80, 50),
            "Old magazines. The dates are from before you were born.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "VISITING HOURS OVER", "The Nurse")
    
    def draw_details(self, surface):
        # Chairs
        for i in range(6):
            pygame.draw.rect(surface, (100, 150, 200), (200 + i * 65, 350, 60, 80))
        # TV
        pygame.draw.rect(surface, (50, 50, 55), (900, 200, 150, 100))
        pygame.draw.rect(surface, (100, 100, 110), (910, 210, 130, 80))
        # Static effect
        if random.random() > 0.5:
            pygame.draw.rect(surface, (150, 150, 150), (910, 210, 130, 80))


class HospitalEmergencyRoom(Room):
    """Emergency room with medical equipment"""
    
    def __init__(self):
        super().__init__(
            name="emergency_room",
            display_name="Emergency Room",
            connections={"left": "waiting_room", "up": "operating_theater"},
            base_color=(200, 210, 210),
            description="The ER is a mess of overturned gurneys and scattered medical supplies."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Gurney", (400, 300, 200, 80),
            "A blood-stained gurney. The restraints are still buckled.",
            "examine",
            "Someone was strapped down here. The leather is torn from struggling."
        ))
        self.add_object(InteractiveObject(
            "Heart Monitor", (700, 250, 80, 120),
            "A heart monitor showing a flatline. It beeps occasionally.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Medical Cabinet", (100, 200, 150, 200),
            "A cabinet full of expired medications.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Defibrillator", (900, 350, 80, 80),
            "An old defibrillator. It sparks on its own.",
            "examine"
        ))
        self.add_hidden_clue(500, 450, "SAVE ME", "The Doctor")
    
    def draw_details(self, surface):
        # Gurney
        pygame.draw.rect(surface, (180, 180, 180), (400, 300, 200, 80))
        pygame.draw.rect(surface, (150, 150, 155), (410, 310, 180, 60))
        # Blood stain
        pygame.draw.ellipse(surface, (120, 40, 40), (450, 320, 80, 40))
        # Heart monitor
        pygame.draw.rect(surface, (50, 60, 70), (700, 250, 80, 120))
        pygame.draw.line(surface, (0, 255, 0), (710, 310), (770, 310), 2)
        # Medical cabinet
        pygame.draw.rect(surface, (200, 200, 205), (100, 200, 150, 200))


class HospitalOperatingTheater(Room):
    """Operating theater with surgical equipment"""
    
    def __init__(self):
        super().__init__(
            name="operating_theater",
            display_name="Operating Theater",
            connections={"down": "emergency_room", "left": "radiology"},
            base_color=(180, 200, 200),
            description="The operating theater. Surgical lights flicker overhead, casting dancing shadows."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Operating Table", (450, 280, 250, 120),
            "A stainless steel operating table. It's still stained.",
            "examine",
            "Straps hang from the sides. Someone was held down here against their will."
        ))
        self.add_object(InteractiveObject(
            "Surgical Light", (550, 100, 100, 80),
            "A large surgical lamp. It flickers ominously.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Surgical Tools", (800, 300, 100, 80),
            "A tray of rusted surgical instruments.",
            "zoom",
            "Among the scalpels and clamps, you find teeth. Human teeth."
        ))
        self.add_hidden_clue(400, 450, "THE OPERATION FAILED", "The Doctor")
    
    def draw_details(self, surface):
        # Operating table
        pygame.draw.rect(surface, (180, 180, 190), (450, 280, 250, 120))
        pygame.draw.rect(surface, (160, 160, 170), (460, 290, 230, 100))
        # Surgical light
        pygame.draw.ellipse(surface, (200, 200, 210), (500, 100, 200, 100))
        if self.lights_on:
            pygame.draw.ellipse(surface, (255, 255, 220), (520, 110, 160, 80))


class HospitalPatientWard(Room):
    """Ward with hospital beds"""
    
    def __init__(self):
        super().__init__(
            name="patient_ward",
            display_name="Patient Ward",
            connections={"up": "waiting_room", "right": "morgue", "down": "basement"},
            base_color=(190, 200, 195),
            description="Rows of empty hospital beds with drawn curtains. Something moves behind them."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Hospital Bed 1", (100, 300, 150, 100),
            "An old hospital bed with stained sheets.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Hospital Bed 2", (400, 300, 150, 100),
            "This bed's restraints are still attached.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Curtain", (300, 200, 50, 250),
            "A privacy curtain. Something is behind it.",
            "toggle",
            "You pull back the curtain... nothing there. But you feel watched."
        ))
        self.add_object(InteractiveObject(
            "IV Stand", (600, 280, 40, 180),
            "An IV stand with dried fluid in the bag.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "BED 13", "The Nurse")
    
    def draw_details(self, surface):
        # Hospital beds
        for x in [100, 400, 700]:
            pygame.draw.rect(surface, (200, 200, 205), (x, 300, 150, 100))
            pygame.draw.rect(surface, (180, 180, 185), (x + 10, 310, 130, 80))
        # Curtains
        pygame.draw.rect(surface, (150, 200, 180), (300, 200, 10, 250))
        pygame.draw.rect(surface, (150, 200, 180), (550, 200, 10, 250))


class HospitalMorgue(Room):
    """The hospital morgue"""
    
    def __init__(self):
        super().__init__(
            name="morgue",
            display_name="Morgue",
            connections={"left": "patient_ward"},
            base_color=(160, 170, 180),
            description="The morgue. Body drawers line the walls. Some are open. Some are occupied."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Body Drawers", (100, 200, 300, 250),
            "Rows of body storage drawers. One is slightly open.",
            "toggle",
            "You pull open a drawer. Empty. But the metal is ice cold."
        ))
        self.add_object(InteractiveObject(
            "Examination Table", (500, 320, 200, 100),
            "A steel examination table with drain holes.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Freezer", (800, 200, 150, 200),
            "A large walk-in freezer. Frost covers the window.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "NOT DEAD", "Nightmare")
    
    def draw_details(self, surface):
        # Body drawers
        for row in range(3):
            for col in range(4):
                pygame.draw.rect(surface, (150, 155, 160), 
                               (110 + col * 70, 210 + row * 75, 60, 65))
        # Examination table
        pygame.draw.rect(surface, (180, 180, 185), (500, 320, 200, 100))
        # Freezer
        pygame.draw.rect(surface, (140, 150, 160), (800, 200, 150, 200))
        pygame.draw.rect(surface, (100, 120, 140), (820, 220, 60, 80))


class HospitalPharmacy(Room):
    """Hospital pharmacy"""
    
    def __init__(self):
        super().__init__(
            name="pharmacy",
            display_name="Pharmacy",
            connections={"down": "doctors_office"},
            base_color=(200, 195, 190),
            description="The pharmacy. Shelves of expired medications and broken glass everywhere."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Medicine Shelves", (100, 150, 400, 300),
            "Rows of medication shelves. Most bottles are empty or broken.",
            "examine",
            "One bottle is labeled 'EXPERIMENTAL - DO NOT ADMINISTER'. It's empty."
        ))
        self.add_object(InteractiveObject(
            "Prescription Counter", (600, 300, 200, 100),
            "The prescription counter. A pharmacist's coat hangs on a hook.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Safe", (900, 350, 100, 100),
            "A locked safe for controlled substances.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "OVERDOSE", "The Nurse")
    
    def draw_details(self, surface):
        # Shelves
        for i in range(4):
            pygame.draw.rect(surface, (180, 175, 170), (100, 150 + i * 75, 400, 10))
        # Bottles
        for i in range(10):
            color = random.choice([(200, 100, 100), (100, 200, 100), (100, 100, 200), (200, 200, 100)])
            pygame.draw.rect(surface, color, (120 + i * 38, 130, 30, 50))


class HospitalDoctorsOffice(Room):
    """Doctor's private office"""
    
    def __init__(self):
        super().__init__(
            name="doctors_office",
            display_name="Doctor's Office",
            connections={"down": "reception", "up": "pharmacy", "right": "radiology"},
            base_color=(180, 160, 140),
            description="The head doctor's office. Medical degrees line the walls, but the names are scratched out."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Doctor's Desk", (400, 300, 250, 120),
            "A mahogany desk covered in patient files.",
            "zoom",
            "One file is labeled 'Project Rebirth'. The contents are heavily redacted."
        ))
        self.add_object(InteractiveObject(
            "Medical Diploma", (800, 150, 100, 80),
            "A framed medical diploma. The name has been violently scratched out.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Skeleton Model", (100, 200, 80, 280),
            "An anatomical skeleton model. It seems to watch you.",
            "examine"
        ))
        self.add_hidden_clue(500, 450, "MALPRACTICE", "The Doctor")
    
    def draw_details(self, surface):
        # Desk
        pygame.draw.rect(surface, (100, 70, 50), (400, 300, 250, 120))
        # Chair
        pygame.draw.rect(surface, (80, 50, 30), (480, 430, 80, 80))
        # Skeleton
        pygame.draw.circle(surface, CREAM, (140, 230), 25)
        pygame.draw.line(surface, CREAM, (140, 255), (140, 400), 3)


class HospitalRadiology(Room):
    """X-ray and imaging room"""
    
    def __init__(self):
        super().__init__(
            name="radiology",
            display_name="Radiology",
            connections={"left": "doctors_office", "right": "operating_theater"},
            base_color=(170, 180, 190),
            description="The radiology department. X-ray images hang on light boxes, showing things inside people."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "X-Ray Machine", (400, 250, 200, 200),
            "An old X-ray machine. It hums with residual energy.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Light Box", (100, 200, 200, 150),
            "X-ray images on a light box. Some show... extra bones.",
            "zoom",
            "The X-rays show patients with extra limbs growing inside them."
        ))
        self.add_object(InteractiveObject(
            "Lead Apron", (800, 300, 80, 120),
            "A heavy lead apron for radiation protection.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "EXPOSED", "The Plague Doctor")
    
    def draw_details(self, surface):
        # X-ray machine
        pygame.draw.rect(surface, (100, 100, 110), (400, 250, 200, 200))
        pygame.draw.ellipse(surface, (80, 80, 90), (420, 270, 160, 100))
        # Light box
        pygame.draw.rect(surface, (200, 220, 240), (100, 200, 200, 150))
        # X-ray silhouettes
        pygame.draw.ellipse(surface, (50, 50, 60), (130, 220, 60, 100))
        pygame.draw.ellipse(surface, (50, 50, 60), (210, 220, 60, 100))


class HospitalBasement(Room):
    """Hospital basement - boiler room and storage"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Hospital Basement",
            connections={"up": "patient_ward"},
            base_color=(60, 65, 70),
            description="The hospital basement. Old records and broken equipment fill the darkness."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Boiler", (100, 200, 200, 280),
            "An old industrial boiler. It rumbles and groans.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Filing Cabinets", (500, 250, 200, 200),
            "Rows of filing cabinets with patient records.",
            "zoom",
            "One drawer is labeled 'DECEASED - UNNATURAL CAUSES'. It's overflowing."
        ))
        self.add_object(InteractiveObject(
            "Incinerator", (800, 300, 150, 180),
            "A medical waste incinerator. Something is still smoldering.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "BURN THE RECORDS", None)
    
    def draw_details(self, surface):
        # Boiler
        pygame.draw.rect(surface, (80, 70, 60), (100, 200, 200, 280))
        pygame.draw.ellipse(surface, (60, 50, 40), (120, 220, 160, 100))
        # Pipes
        for y in [150, 180]:
            pygame.draw.rect(surface, (100, 90, 80), (0, y, SCREEN_WIDTH, 15))
        # Filing cabinets
        for i in range(4):
            pygame.draw.rect(surface, (120, 120, 125), (510 + i * 45, 250, 40, 200))


# ===============================================================================
# OLD PRISON ROOMS
# ===============================================================================

class PrisonEntranceCheckpoint(Room):
    """Prison entrance checkpoint"""
    
    def __init__(self):
        super().__init__(
            name="entrance_checkpoint",
            display_name="Entrance Checkpoint",
            connections={"right": "cell_block_a", "up": "warden_office"},
            base_color=(60, 60, 65),
            description="The prison entrance. Metal detectors and guard stations stand abandoned."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Metal Detector", (400, 250, 100, 300),
            "An old metal detector. It beeps randomly.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Guard Booth", (100, 200, 150, 200),
            "An empty guard booth. Coffee cup still warm.",
            "examine",
            "The logbook shows the last entry was decades ago. The date is circled in red."
        ))
        self.add_object(InteractiveObject(
            "Visitor Sign-In", (700, 300, 150, 80),
            "A visitor sign-in sheet. The last visitor never signed out.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "NO ESCAPE", "The Jailer")
    
    def draw_details(self, surface):
        # Metal detector
        pygame.draw.rect(surface, (100, 100, 105), (400, 250, 100, 300))
        pygame.draw.rect(surface, (80, 80, 85), (440, 260, 20, 280))
        # Guard booth
        pygame.draw.rect(surface, (80, 70, 65), (100, 200, 150, 200))
        pygame.draw.rect(surface, (60, 80, 100), (110, 210, 130, 100))


class PrisonCellBlockA(Room):
    """Cell Block A - general population"""
    
    def __init__(self):
        super().__init__(
            name="cell_block_a",
            display_name="Cell Block A",
            connections={"left": "entrance_checkpoint", "right": "cell_block_b", "down": "cafeteria"},
            base_color=(70, 70, 75),
            description="Cell Block A. Rows of cells stretch into darkness. Bars rattle without wind."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Cell Door 1", (100, 200, 100, 250),
            "A cell door. Scratch marks cover the inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cell Door 2", (300, 200, 100, 250),
            "This cell has writing on the walls.",
            "zoom",
            "THEY'RE WATCHING is written hundreds of times in tiny letters."
        ))
        self.add_object(InteractiveObject(
            "Guard Station", (600, 300, 150, 120),
            "A central guard station with monitors.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "CELL 13", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Cell bars
        for x in [100, 300, 500, 700, 900]:
            pygame.draw.rect(surface, (60, 60, 65), (x, 200, 100, 250))
            for i in range(6):
                pygame.draw.rect(surface, (100, 100, 105), (x + 10 + i * 15, 200, 5, 250))


class PrisonCellBlockB(Room):
    """Cell Block B - maximum security"""
    
    def __init__(self):
        super().__init__(
            name="cell_block_b",
            display_name="Cell Block B (Max Security)",
            connections={"left": "cell_block_a", "right": "solitary", "up": "guard_room"},
            base_color=(50, 50, 55),
            description="Maximum security. The cells are smaller, darker. The screams are louder."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Reinforced Cell", (200, 220, 150, 200),
            "A heavily reinforced cell. The door is dented from the inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Security Camera", (600, 150, 80, 60),
            "A broken security camera. It still tracks movement.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Contraband Locker", (800, 300, 120, 150),
            "A locker for confiscated items.",
            "toggle"
        ))
        self.add_hidden_clue(400, 550, "INNOCENT", "The Hanged Man")
    
    def draw_details(self, surface):
        # Reinforced doors
        for x in [200, 450, 700]:
            pygame.draw.rect(surface, (80, 80, 85), (x, 220, 150, 200))
            pygame.draw.rect(surface, (100, 100, 105), (x + 20, 240, 110, 160))


class PrisonCafeteria(Room):
    """Prison cafeteria"""
    
    def __init__(self):
        super().__init__(
            name="cafeteria",
            display_name="Cafeteria",
            connections={"up": "cell_block_a", "down": "basement"},
            base_color=(150, 145, 140),
            description="The prison cafeteria. Trays of rotten food still sit on tables."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Lunch Tables", (300, 320, 400, 150),
            "Long metal tables bolted to the floor.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Serving Counter", (600, 200, 300, 80),
            "The food serving counter. Something moves in the trays.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Kitchen Door", (100, 250, 100, 200),
            "The kitchen door. It swings on its own.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "LAST MEAL", "The Butcher")
    
    def draw_details(self, surface):
        # Tables
        for i in range(4):
            pygame.draw.rect(surface, (140, 140, 145), (200 + i * 200, 320, 180, 20))
            # Benches
            pygame.draw.rect(surface, (130, 130, 135), (200 + i * 200, 360, 180, 30))


class PrisonExerciseYard(Room):
    """Outdoor exercise yard"""
    
    def __init__(self):
        super().__init__(
            name="exercise_yard",
            display_name="Exercise Yard",
            connections={"left": "cell_block_a"},
            base_color=(80, 90, 80),
            description="The exercise yard. High fences with razor wire surround dead grass."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Basketball Hoop", (400, 200, 100, 200),
            "A rusted basketball hoop. A ball bounces on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Weight Bench", (700, 350, 150, 80),
            "A concrete weight bench. Blood stains the ground around it.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Guard Tower", (100, 100, 100, 300),
            "A guard tower. The searchlight still works.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "RIOT", "Poltergeist")
    
    def draw_base(self, surface):
        # Gray sky
        pygame.draw.rect(surface, (100, 100, 110), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.3))
        # Ground
        pygame.draw.rect(surface, (70, 80, 70), (0, SCREEN_HEIGHT * 0.3, SCREEN_WIDTH, SCREEN_HEIGHT * 0.7))
        # Fence
        for x in range(0, SCREEN_WIDTH, 30):
            pygame.draw.line(surface, (100, 100, 100), (x, int(SCREEN_HEIGHT * 0.2)), 
                           (x, int(SCREEN_HEIGHT * 0.7)), 2)
        # Razor wire
        pygame.draw.line(surface, (150, 150, 150), (0, int(SCREEN_HEIGHT * 0.2)), 
                        (SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.2)), 4)
    
    def draw_details(self, surface):
        # Basketball hoop
        pygame.draw.rect(surface, (150, 100, 80), (440, 200, 20, 200))
        pygame.draw.rect(surface, (200, 200, 205), (420, 200, 60, 50))
        pygame.draw.circle(surface, (200, 100, 50), (450, 250), 20, 3)


class PrisonSolitary(Room):
    """Solitary confinement"""
    
    def __init__(self):
        super().__init__(
            name="solitary",
            display_name="Solitary Confinement",
            connections={"left": "cell_block_b"},
            base_color=(30, 30, 35),
            description="The hole. Solitary confinement. The silence is deafening."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Solitary Cell", (400, 200, 200, 300),
            "A tiny cell with no windows. Scratch marks cover every surface.",
            "zoom",
            "Days are counted on the walls. The count reaches 3,287. Then stops."
        ))
        self.add_object(InteractiveObject(
            "Food Slot", (600, 350, 50, 30),
            "A tiny slot for food trays. Something peers through.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "NEVER LEAVE", "The Jailer")
    
    def draw_details(self, surface):
        # Solitary cell
        pygame.draw.rect(surface, (40, 40, 45), (400, 200, 200, 300))
        pygame.draw.rect(surface, (50, 50, 55), (420, 220, 160, 260))
        # Scratch marks
        for i in range(20):
            x = 430 + i * 8
            pygame.draw.line(surface, (80, 80, 85), (x, 240), (x, 440), 1)


class PrisonWardenOffice(Room):
    """Warden's office"""
    
    def __init__(self):
        super().__init__(
            name="warden_office",
            display_name="Warden's Office",
            connections={"down": "entrance_checkpoint", "right": "execution_chamber"},
            base_color=(100, 80, 70),
            description="The warden's office. Awards and photos line the walls. All the faces are scratched out."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Warden's Desk", (400, 300, 250, 120),
            "A large oak desk covered in files.",
            "zoom",
            "Execution orders. Dozens of them. Many were never signed."
        ))
        self.add_object(InteractiveObject(
            "Trophy Case", (100, 200, 150, 250),
            "A case of awards. 'Excellence in Corrections'.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Safe", (800, 300, 100, 120),
            "A wall safe. The combination is scratched into the wall nearby.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "CORRUPTION", None)
    
    def draw_details(self, surface):
        # Desk
        pygame.draw.rect(surface, (80, 50, 35), (400, 300, 250, 120))
        # Chair
        pygame.draw.rect(surface, (100, 60, 40), (480, 430, 90, 80))
        # Trophy case
        pygame.draw.rect(surface, (90, 60, 40), (100, 200, 150, 250))
        pygame.draw.rect(surface, (120, 140, 160), (110, 210, 130, 230))


class PrisonExecutionChamber(Room):
    """The execution chamber"""
    
    def __init__(self):
        super().__init__(
            name="execution_chamber",
            display_name="Execution Chamber",
            connections={"left": "warden_office"},
            base_color=(50, 45, 45),
            description="The execution chamber. The electric chair sits waiting. It still works."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Electric Chair", (500, 280, 150, 200),
            "THE chair. Leather straps are worn from struggling.",
            "zoom",
            "The last occupant left claw marks in the armrests. They were innocent."
        ))
        self.add_object(InteractiveObject(
            "Control Panel", (800, 300, 100, 150),
            "The execution control panel. The switch is warm.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Witness Window", (200, 200, 200, 150),
            "The witness viewing window. Faces press against the glass.",
            "examine"
        ))
        self.add_hidden_clue(600, 550, "WRONGFULLY EXECUTED", "The Hanged Man")
    
    def draw_details(self, surface):
        # Electric chair
        pygame.draw.rect(surface, (80, 60, 50), (500, 280, 150, 200))
        pygame.draw.rect(surface, (100, 80, 70), (510, 290, 130, 80))
        # Straps
        pygame.draw.rect(surface, (60, 40, 30), (510, 320, 130, 10))
        # Witness window
        pygame.draw.rect(surface, (40, 40, 45), (200, 200, 200, 150))
        pygame.draw.rect(surface, (60, 80, 100), (210, 210, 180, 130))


class PrisonGuardRoom(Room):
    """Guard break room"""
    
    def __init__(self):
        super().__init__(
            name="guard_room",
            display_name="Guard Room",
            connections={"down": "cell_block_b"},
            base_color=(120, 110, 100),
            description="The guard break room. Lockers and a TV showing static."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Lockers", (100, 200, 300, 250),
            "Guard lockers. One is still locked.",
            "toggle",
            "Inside: a journal. 'They're planning something. I can feel it.'"
        ))
        self.add_object(InteractiveObject(
            "Break Table", (500, 320, 200, 100),
            "A table with cold coffee and playing cards.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Weapons Locker", (800, 200, 150, 280),
            "A weapons locker. Empty. The lock was forced.",
            "examine"
        ))
    
    def draw_details(self, surface):
        # Lockers
        for i in range(5):
            pygame.draw.rect(surface, (140, 130, 120), (100 + i * 58, 200, 55, 250))
            pygame.draw.rect(surface, (120, 110, 100), (110 + i * 58, 210, 35, 230))


class PrisonBasement(Room):
    """Prison basement - maintenance and tunnels"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Prison Basement",
            connections={"up": "cafeteria"},
            base_color=(40, 40, 45),
            description="Maintenance tunnels beneath the prison. They say prisoners tried to escape through here."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Tunnel Entrance", (300, 250, 150, 200),
            "A dark tunnel leading somewhere. Scratch marks line the walls.",
            "examine",
            "The tunnel is collapsed halfway. Bones protrude from the rubble."
        ))
        self.add_object(InteractiveObject(
            "Fuse Box", (700, 280, 80, 120),
            "An old fuse box. Sparks occasionally fly.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Pipes", (100, 150, SCREEN_WIDTH - 200, 40),
            "Old pipes running along the ceiling. They drip constantly.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "ESCAPE ROUTE", None)
    
    def draw_details(self, surface):
        # Tunnel
        pygame.draw.rect(surface, (30, 30, 35), (300, 250, 150, 200))
        pygame.draw.ellipse(surface, (20, 20, 25), (310, 260, 130, 100))
        # Pipes
        pygame.draw.rect(surface, (100, 90, 80), (100, 150, SCREEN_WIDTH - 200, 20))
        # Drips
        for x in range(200, SCREEN_WIDTH - 200, 100):
            pygame.draw.line(surface, (100, 120, 150), (x, 170), (x, 180), 2)


# ===============================================================================
# HAUNTED SCHOOL ROOMS
# ===============================================================================

class SchoolEntranceHall(Room):
    """School entrance hall"""
    
    def __init__(self):
        super().__init__(
            name="entrance_hall",
            display_name="School Entrance",
            connections={"right": "classroom_1", "up": "principal_office"},
            base_color=(180, 160, 140),
            description="The school entrance. Lockers line the walls. Some are dented from the inside."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Lockers", (100, 200, 200, 280),
            "Rows of rusted lockers. One swings open on its own.",
            "toggle",
            "Inside: old textbooks and a child's lunchbox. The food is fresh."
        ))
        self.add_object(InteractiveObject(
            "Trophy Case", (600, 200, 200, 250),
            "A trophy case showing sports achievements from decades ago.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Bulletin Board", (900, 250, 150, 150),
            "A bulletin board with faded announcements. One reads 'SCHOOL CLOSING'.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "RECESS", "Little Timmy")
    
    def draw_details(self, surface):
        # Lockers
        for i in range(8):
            pygame.draw.rect(surface, (140, 150, 160), (100 + i * 25, 200, 23, 280))
            pygame.draw.rect(surface, (120, 130, 140), (102 + i * 25, 210, 19, 260))
        # Trophy case
        pygame.draw.rect(surface, (100, 70, 50), (600, 200, 200, 250))
        pygame.draw.rect(surface, (150, 170, 190), (610, 210, 180, 230))


class SchoolClassroom1(Room):
    """First classroom"""
    
    def __init__(self):
        super().__init__(
            name="classroom_1",
            display_name="Classroom 101",
            connections={"left": "entrance_hall", "right": "classroom_2", "down": "cafeteria"},
            base_color=(170, 165, 150),
            description="An empty classroom. Desks are arranged in rows. Chalk writes on the board by itself."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Chalkboard", (400, 150, 350, 200),
            "A dusty chalkboard. Words appear and disappear.",
            "zoom",
            "The board reads: 'I WILL NOT TELL - I WILL NOT TELL - I WILL NOT TELL'"
        ))
        self.add_object(InteractiveObject(
            "Teacher's Desk", (100, 300, 150, 80),
            "The teacher's desk. An apple sits rotting on top.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Student Desks", (400, 350, 400, 150),
            "Rows of old wooden desks. Names are carved into them.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "TEST TODAY", "The Teacher")
    
    def draw_details(self, surface):
        # Chalkboard
        pygame.draw.rect(surface, (50, 80, 60), (400, 150, 350, 200))
        pygame.draw.rect(surface, (80, 60, 40), (390, 140, 370, 220), 5)
        # Desks
        for row in range(3):
            for col in range(5):
                pygame.draw.rect(surface, (120, 90, 60), 
                               (400 + col * 75, 350 + row * 50, 60, 35))


class SchoolClassroom2(Room):
    """Second classroom"""
    
    def __init__(self):
        super().__init__(
            name="classroom_2",
            display_name="Classroom 102",
            connections={"left": "classroom_1", "right": "gymnasium", "up": "library"},
            base_color=(165, 160, 145),
            description="Another classroom. Children's drawings cover the walls. They're all the same face."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Art Wall", (100, 180, 300, 200),
            "Children's drawings. They all show the same figure.",
            "zoom",
            "Every drawing shows a tall figure with no face. 'MR. NOBODY' is written underneath."
        ))
        self.add_object(InteractiveObject(
            "Projector", (600, 250, 100, 80),
            "An old film projector. It flickers on by itself sometimes.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Coat Hooks", (900, 200, 100, 200),
            "Coat hooks with children's jackets still hanging.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "PLAY WITH US", "The Twins")
    
    def draw_details(self, surface):
        # Art wall - drawings
        for i in range(6):
            pygame.draw.rect(surface, CREAM, (120 + i * 45, 200, 40, 50))
            pygame.draw.circle(surface, (200, 180, 160), (140 + i * 45, 215), 10)


class SchoolGymnasium(Room):
    """School gymnasium"""
    
    def __init__(self):
        super().__init__(
            name="gymnasium",
            display_name="Gymnasium",
            connections={"left": "classroom_2", "down": "playground"},
            base_color=(160, 150, 140),
            description="The gymnasium. Bleachers face an empty basketball court. A ball bounces on its own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Basketball Hoop", (500, 150, 100, 150),
            "A basketball hoop. A ball keeps going through it with no one shooting.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Bleachers", (100, 250, 250, 200),
            "Wooden bleachers. You can hear cheering from empty seats.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Gym Storage", (800, 300, 150, 180),
            "A storage closet for gym equipment.",
            "toggle"
        ))
        self.add_hidden_clue(600, 500, "DODGEBALL", "Little Timmy")
    
    def draw_base(self, surface):
        # Walls
        pygame.draw.rect(surface, (140, 135, 130), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
        # Gym floor
        pygame.draw.rect(surface, (180, 140, 100), (0, int(SCREEN_HEIGHT * 0.4), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
        # Court lines
        pygame.draw.circle(surface, (200, 160, 120), (SCREEN_WIDTH // 2, int(SCREEN_HEIGHT * 0.6)), 100, 3)
        pygame.draw.line(surface, (200, 160, 120), (0, int(SCREEN_HEIGHT * 0.6)), 
                        (SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)), 3)
    
    def draw_details(self, surface):
        # Basketball hoop
        pygame.draw.rect(surface, (200, 200, 205), (540, 150, 60, 50))
        pygame.draw.circle(surface, (200, 100, 50), (570, 200), 25, 4)
        # Bleachers
        for i in range(5):
            pygame.draw.rect(surface, (120, 90, 60), (100, 250 + i * 40, 250, 35))


class SchoolCafeteria(Room):
    """School cafeteria"""
    
    def __init__(self):
        super().__init__(
            name="cafeteria",
            display_name="Cafeteria",
            connections={"up": "classroom_1", "right": "bathroom", "down": "basement"},
            base_color=(175, 170, 160),
            description="The cafeteria. Long tables are still set with trays of rotting food."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Lunch Tables", (300, 320, 500, 120),
            "Long cafeteria tables. Trays of food still sit on them.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Serving Counter", (100, 200, 300, 100),
            "The food serving counter. Something moves in the trays.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Vending Machine", (900, 250, 100, 200),
            "An old vending machine. It dispenses things that aren't food.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "LUNCH LADY", None)
    
    def draw_details(self, surface):
        # Tables
        for i in range(3):
            pygame.draw.rect(surface, (180, 180, 185), (200, 320 + i * 70, 600, 20))
        # Serving counter
        pygame.draw.rect(surface, (150, 150, 155), (100, 200, 300, 100))
        pygame.draw.rect(surface, (140, 140, 145), (110, 210, 280, 80))


class SchoolLibrary(Room):
    """School library"""
    
    def __init__(self):
        super().__init__(
            name="library",
            display_name="Library",
            connections={"down": "classroom_2"},
            base_color=(140, 120, 100),
            description="The school library. Books fly off shelves. Pages turn on their own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bookshelves", (100, 150, 400, 350),
            "Towering bookshelves. Books slide out on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Reading Tables", (600, 350, 250, 100),
            "Study tables with open books. The pages turn by themselves.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Card Catalog", (900, 250, 100, 150),
            "An old card catalog. All entries are for books that don't exist.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "SILENCE", "The Librarian")
    
    def draw_details(self, surface):
        # Bookshelves
        for i in range(5):
            pygame.draw.rect(surface, (100, 70, 50), (100, 150 + i * 70, 400, 10))
            for j in range(15):
                color = [(100, 50, 50), (50, 100, 50), (50, 50, 100), (100, 80, 50)][j % 4]
                pygame.draw.rect(surface, color, (110 + j * 26, 160 + i * 70, 24, 60))


class SchoolPrincipalOffice(Room):
    """Principal's office"""
    
    def __init__(self):
        super().__init__(
            name="principal_office",
            display_name="Principal's Office",
            connections={"down": "entrance_hall"},
            base_color=(120, 100, 85),
            description="The principal's office. Detention slips cover the desk. All for the same student."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Principal's Desk", (400, 300, 250, 120),
            "A large wooden desk covered in paperwork.",
            "zoom",
            "Detention slips for 'TIMMY' dated every day for the past 50 years."
        ))
        self.add_object(InteractiveObject(
            "Filing Cabinet", (100, 200, 100, 250),
            "A filing cabinet of student records.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Waiting Chairs", (800, 350, 150, 100),
            "Chairs for students waiting to see the principal.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "EXPELLED", "The Teacher")
    
    def draw_details(self, surface):
        # Desk
        pygame.draw.rect(surface, (90, 60, 40), (400, 300, 250, 120))
        pygame.draw.rect(surface, (80, 50, 30), (410, 310, 230, 100))
        # Chair
        pygame.draw.rect(surface, (100, 70, 50), (480, 430, 80, 80))


class SchoolBathroom(Room):
    """School bathroom"""
    
    def __init__(self):
        super().__init__(
            name="bathroom",
            display_name="Bathroom",
            connections={"left": "cafeteria"},
            base_color=(180, 185, 180),
            description="The school bathroom. Faucets run by themselves. Someone is crying in the last stall."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bathroom Stalls", (600, 200, 300, 280),
            "A row of bathroom stalls. One is always locked.",
            "examine",
            "The locked stall has no feet visible underneath. But you hear sobbing."
        ))
        self.add_object(InteractiveObject(
            "Mirrors", (100, 200, 300, 120),
            "Cracked mirrors above the sinks.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Sinks", (100, 350, 300, 80),
            "A row of sinks. Water runs red occasionally.",
            "toggle"
        ))
        self.add_hidden_clue(700, 500, "BLOODY MARY", None)
    
    def draw_details(self, surface):
        # Tiles
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 40):
            for x in range(0, SCREEN_WIDTH, 40):
                color = (175, 180, 175) if (x + y) % 80 == 0 else (180, 185, 180)
                pygame.draw.rect(surface, color, (x, y, 38, 38))
        # Stalls
        for i in range(4):
            pygame.draw.rect(surface, (140, 140, 145), (600 + i * 75, 200, 70, 280))


class SchoolPlayground(Room):
    """Outdoor playground"""
    
    def __init__(self):
        super().__init__(
            name="playground",
            display_name="Playground",
            connections={"up": "gymnasium"},
            base_color=(60, 80, 60),
            description="The playground. Equipment rusts in the moonlight. Children's laughter echoes."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Swing Set", (300, 280, 200, 200),
            "An old swing set. One swing moves on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Slide", (700, 250, 150, 220),
            "A rusted metal slide. It's too cold to touch.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Sandbox", (100, 400, 150, 80),
            "A sandbox. Something is buried in it.",
            "zoom"
        ))
        self.add_hidden_clue(500, 550, "HIDE AND SEEK", "The Twins")
    
    def draw_base(self, surface):
        # Night sky
        pygame.draw.rect(surface, (15, 20, 35), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        # Ground
        pygame.draw.rect(surface, (50, 70, 50), (0, int(SCREEN_HEIGHT * 0.3), 
                                                   SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        # Swing set
        pygame.draw.rect(surface, (120, 80, 60), (350, 280, 10, 200))
        pygame.draw.rect(surface, (120, 80, 60), (490, 280, 10, 200))
        pygame.draw.rect(surface, (120, 80, 60), (340, 280, 170, 10))
        # Swing
        pygame.draw.line(surface, (100, 100, 100), (400, 290), (400, 380), 2)
        pygame.draw.line(surface, (100, 100, 100), (420, 290), (420, 380), 2)
        pygame.draw.rect(surface, (80, 50, 30), (390, 380, 40, 10))


class SchoolBasement(Room):
    """School basement"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="School Basement",
            connections={"up": "cafeteria"},
            base_color=(50, 50, 55),
            description="The school basement. Old desks and equipment are stored here. Something scurries in the dark."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Storage Boxes", (100, 200, 200, 200),
            "Boxes of old school supplies. Some are labeled from the 1950s.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Boiler", (600, 250, 200, 200),
            "An old school boiler. It rumbles ominously.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Old Desks", (900, 300, 150, 150),
            "Stacked old desks. Names are carved into every surface.",
            "zoom"
        ))
        self.add_hidden_clue(500, 550, "FIRE DRILL", None)
    
    def draw_details(self, surface):
        # Boxes
        for i in range(3):
            pygame.draw.rect(surface, (100, 80, 60), (100 + i * 60, 200 + i * 30, 80, 60))
        # Boiler
        pygame.draw.rect(surface, (70, 70, 75), (600, 250, 200, 200))
        pygame.draw.ellipse(surface, (60, 60, 65), (620, 270, 160, 80))


# ===============================================================================
# LIGHTHOUSE ROOMS
# ===============================================================================

class LighthouseEntrance(Room):
    """Lighthouse entrance"""
    
    def __init__(self):
        super().__init__(
            name="entrance",
            display_name="Lighthouse Entrance",
            connections={"up": "living_quarters", "right": "storage"},
            base_color=(100, 120, 140),
            description="The lighthouse entrance. Salt air fills your lungs. Water drips constantly."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Entrance Door", (500, 200, 150, 280),
            "The heavy iron door. It moans in the wind.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Coat Hooks", (100, 250, 100, 150),
            "Coat hooks with an old raincoat. Still dripping.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Lantern", (800, 300, 60, 80),
            "An old oil lantern. It flickers with no oil.",
            "toggle"
        ))
        self.add_hidden_clue(400, 500, "THE KEEPER", "The Mariner")
    
    def draw_details(self, surface):
        # Stone walls
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 40):
            offset = 20 if (y // 40) % 2 else 0
            for x in range(offset, SCREEN_WIDTH, 80):
                pygame.draw.rect(surface, (90, 110, 130), (x, y, 78, 38))
        # Door
        pygame.draw.rect(surface, (60, 50, 45), (500, 200, 150, 280))
        pygame.draw.rect(surface, (80, 70, 60), (510, 210, 130, 260))


class LighthouseLivingQuarters(Room):
    """Living quarters"""
    
    def __init__(self):
        super().__init__(
            name="living_quarters",
            display_name="Living Quarters",
            connections={"down": "entrance", "up": "lamp_room"},
            base_color=(110, 100, 90),
            description="The keeper's living quarters. A bed and desk sit untouched for decades."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Keeper's Bed", (100, 300, 200, 120),
            "A narrow cot. The sheets are still tucked in.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Writing Desk", (500, 280, 180, 100),
            "A desk with a logbook. Entries stop mid-sentence.",
            "zoom",
            "Last entry: 'The light calls to me. Tonight I will finally-'"
        ))
        self.add_object(InteractiveObject(
            "Porthole Window", (800, 200, 100, 100),
            "A round window looking out to sea. Something floats in the waves.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "DROWNED", "The Drowned")
    
    def draw_details(self, surface):
        # Bed
        pygame.draw.rect(surface, (80, 60, 50), (100, 300, 200, 120))
        pygame.draw.rect(surface, (150, 140, 130), (110, 310, 180, 100))
        # Desk
        pygame.draw.rect(surface, (90, 70, 55), (500, 280, 180, 100))
        # Porthole
        pygame.draw.circle(surface, (60, 80, 100), (850, 250), 50)
        pygame.draw.circle(surface, (40, 60, 80), (850, 250), 40)


class LighthouseStorage(Room):
    """Storage room"""
    
    def __init__(self):
        super().__init__(
            name="storage",
            display_name="Storage Room",
            connections={"left": "entrance"},
            base_color=(90, 95, 100),
            description="A cramped storage room. Supplies for a lighthouse keeper who never returned."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Oil Barrels", (200, 280, 200, 180),
            "Barrels of lighthouse oil. They leak onto the floor.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Rope Coils", (600, 300, 150, 150),
            "Coils of thick rope. One is tied into a noose.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Toolbox", (900, 350, 100, 80),
            "A rusty toolbox. Tools are missing.",
            "toggle"
        ))
        self.add_hidden_clue(400, 550, "STORM COMING", None)
    
    def draw_details(self, surface):
        # Barrels
        for i in range(3):
            pygame.draw.ellipse(surface, (80, 60, 50), (200 + i * 70, 280, 60, 180))


class LighthouseLampRoom(Room):
    """The lamp room at the top"""
    
    def __init__(self):
        super().__init__(
            name="lamp_room",
            display_name="Lamp Room",
            connections={"down": "living_quarters", "up": "observation_deck"},
            base_color=(140, 150, 160),
            description="The lamp room. The massive lens rotates on its own. The light never goes out."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Fresnel Lens", (450, 200, 200, 250),
            "The massive rotating lens. It projects light that shouldn't exist.",
            "zoom",
            "Looking into the lens, you see ships that sank decades ago."
        ))
        self.add_object(InteractiveObject(
            "Light Controls", (800, 300, 100, 120),
            "Controls for the lighthouse lamp. They move on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Windows", (100, 180, SCREEN_WIDTH - 200, 100),
            "Windows overlooking the sea. Faces press against them from outside.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "GUIDE THEM HOME", "The Mariner")
    
    def draw_details(self, surface):
        # Lens
        pygame.draw.ellipse(surface, (200, 210, 220), (450, 200, 200, 250))
        pygame.draw.ellipse(surface, (240, 250, 255), (480, 230, 140, 190))
        # Glow
        glow_surf = pygame.Surface((200, 250), pygame.SRCALPHA)
        pygame.draw.ellipse(glow_surf, (255, 255, 200, 100), (0, 0, 200, 250))
        surface.blit(glow_surf, (450, 200))


class LighthouseObservationDeck(Room):
    """Outdoor observation deck"""
    
    def __init__(self):
        super().__init__(
            name="observation_deck",
            display_name="Observation Deck",
            connections={"down": "lamp_room"},
            base_color=(80, 100, 120),
            description="The observation deck. Wind howls. The sea stretches endlessly. Something watches from below."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Railing", (100, 350, SCREEN_WIDTH - 200, 50),
            "A rusted iron railing. Handprints are worn into the metal.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Telescope", (500, 280, 100, 150),
            "An old telescope. It shows things that aren't there.",
            "zoom",
            "Through the lens, you see ships. Ghost ships. Coming for the lighthouse."
        ))
        self.add_object(InteractiveObject(
            "Weather Vane", (800, 200, 80, 100),
            "A spinning weather vane. It points the same direction regardless of wind.",
            "examine"
        ))
        self.add_hidden_clue(600, 450, "JUMP", "Nightmare")
    
    def draw_base(self, surface):
        # Dark stormy sky
        pygame.draw.rect(surface, (30, 40, 60), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.4))
        # Sea
        pygame.draw.rect(surface, (20, 40, 70), (0, int(SCREEN_HEIGHT * 0.4), 
                                                  SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
        # Waves
        for i in range(0, SCREEN_WIDTH, 50):
            y = int(SCREEN_HEIGHT * 0.4) + 20
            pygame.draw.arc(surface, (40, 60, 90), (i, y, 60, 30), 0, 3.14, 2)
    
    def draw_details(self, surface):
        # Railing
        for x in range(100, SCREEN_WIDTH - 100, 50):
            pygame.draw.rect(surface, (100, 90, 80), (x, 350, 5, 50))
        pygame.draw.rect(surface, (100, 90, 80), (100, 350, SCREEN_WIDTH - 200, 5))


class LighthouseDock(Room):
    """The dock area"""
    
    def __init__(self):
        super().__init__(
            name="dock",
            display_name="Dock",
            connections={"up": "entrance"},
            base_color=(60, 80, 100),
            description="The lighthouse dock. Waves crash against rotting wood. A boat sways empty."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Rowboat", (400, 350, 250, 120),
            "A small rowboat. It's filling with water but never sinks.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Dock Pillars", (100, 300, 100, 200),
            "Barnacle-covered pillars. They groan in the waves.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Fishing Net", (800, 280, 150, 180),
            "An old fishing net. Something is tangled in it.",
            "zoom",
            "Bones. Human bones tangled in the netting."
        ))
        self.add_hidden_clue(500, 500, "SAILOR'S GRAVE", "The Drowned")
    
    def draw_base(self, surface):
        # Sky
        pygame.draw.rect(surface, (40, 50, 70), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        # Sea
        pygame.draw.rect(surface, (30, 50, 80), (0, int(SCREEN_HEIGHT * 0.3), 
                                                  SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
        # Dock
        pygame.draw.rect(surface, (80, 60, 50), (200, int(SCREEN_HEIGHT * 0.55), 
                                                  SCREEN_WIDTH - 400, 100))
    
    def draw_details(self, surface):
        # Dock planks
        for x in range(200, SCREEN_WIDTH - 200, 40):
            pygame.draw.rect(surface, (70, 55, 45), (x, int(SCREEN_HEIGHT * 0.55), 35, 100))
        # Boat
        pygame.draw.ellipse(surface, (100, 70, 50), (400, 380, 250, 80))
        pygame.draw.ellipse(surface, (80, 60, 45), (420, 390, 210, 60))


# ===============================================================================
# THEATER ROOMS
# ===============================================================================

class TheaterLobby(Room):
    """Theater lobby"""
    
    def __init__(self):
        super().__init__(
            name="lobby",
            display_name="Theater Lobby",
            connections={"right": "auditorium"},
            base_color=(130, 50, 50),
            description="The grand theater lobby. Velvet curtains and faded posters of shows long forgotten."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Ticket Booth", (100, 250, 150, 200),
            "The ticket booth. A figure sits inside, motionless.",
            "examine",
            "It's a mannequin. But it wasn't here a moment ago."
        ))
        self.add_object(InteractiveObject(
            "Show Posters", (500, 180, 300, 200),
            "Posters for 'The Final Act' - running since 1923.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Chandelier", (640, 50, 100, 100),
            "A crystal chandelier. It sways without wind.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "THE SHOW", "The Musician")
    
    def draw_details(self, surface):
        # Ticket booth
        pygame.draw.rect(surface, (100, 40, 40), (100, 250, 150, 200))
        pygame.draw.rect(surface, (80, 100, 120), (110, 260, 130, 100))
        # Chandelier
        pygame.draw.circle(surface, (200, 180, 100), (690, 100), 40)
        for i in range(6):
            angle = i * 0.5
            pygame.draw.line(surface, (180, 160, 80), (690, 100), 
                           (690 + int(50 * math.cos(angle)), 100 + int(50 * math.sin(angle))), 2)


class TheaterAuditorium(Room):
    """Main auditorium"""
    
    def __init__(self):
        super().__init__(
            name="auditorium",
            display_name="Auditorium",
            connections={"left": "lobby", "up": "stage", "right": "balcony"},
            base_color=(100, 40, 40),
            description="Rows of velvet seats face the dark stage. Applause echoes from an invisible audience."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Theater Seats", (200, 300, 600, 200),
            "Rows of red velvet seats. Some fold down on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Aisle", (500, 300, 100, 300),
            "The center aisle. Footsteps echo but no one walks.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Emergency Exit", (1000, 300, 100, 200),
            "An emergency exit. It's locked from the outside.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "ENCORE", "The Artist")
    
    def draw_details(self, surface):
        # Seats
        for row in range(5):
            for col in range(15):
                if col != 7:  # Aisle
                    pygame.draw.rect(surface, (150, 50, 50), 
                                   (200 + col * 40, 300 + row * 40, 35, 35))


class TheaterStage(Room):
    """The main stage"""
    
    def __init__(self):
        super().__init__(
            name="stage",
            display_name="Stage",
            connections={"down": "auditorium", "left": "backstage", "right": "orchestra_pit"},
            base_color=(80, 60, 50),
            description="The stage. Spotlights follow you. The curtain moves on its own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stage Curtain", (0, 100, 100, 400),
            "Heavy red velvet curtains. They part for you alone.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Spotlight", (640, 50, 80, 80),
            "A spotlight that follows your movement.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Props", (800, 300, 200, 150),
            "Stage props from countless productions. Some are stained red.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "FINAL ACT", "The Jester")
    
    def draw_base(self, surface):
        # Stage floor
        pygame.draw.rect(surface, (120, 90, 70), (0, int(SCREEN_HEIGHT * 0.4), 
                                                   SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
        # Back wall
        pygame.draw.rect(surface, (80, 60, 50), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
    
    def draw_details(self, surface):
        # Curtains on sides
        pygame.draw.rect(surface, (140, 40, 40), (0, 100, 100, 500))
        pygame.draw.rect(surface, (140, 40, 40), (SCREEN_WIDTH - 100, 100, 100, 500))
        # Spotlight glow
        glow_surf = pygame.Surface((200, 400), pygame.SRCALPHA)
        pygame.draw.polygon(glow_surf, (255, 255, 200, 50), 
                          [(100, 0), (0, 400), (200, 400)])
        surface.blit(glow_surf, (540, 100))


class TheaterBackstage(Room):
    """Backstage area"""
    
    def __init__(self):
        super().__init__(
            name="backstage",
            display_name="Backstage",
            connections={"right": "stage", "down": "dressing_rooms"},
            base_color=(60, 55, 50),
            description="Backstage chaos. Costumes and props litter the floor. Shadows move on their own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Costume Rack", (100, 200, 200, 280),
            "A rack of period costumes. One is your size.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Rope System", (500, 150, 100, 350),
            "Ropes for raising and lowering scenery. They move on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Prop Table", (800, 320, 200, 100),
            "A table of props. The dagger is real.",
            "zoom"
        ))
        self.add_hidden_clue(400, 550, "BREAK A LEG", "The Jester")
    
    def draw_details(self, surface):
        # Costume rack
        pygame.draw.rect(surface, (100, 80, 60), (150, 200, 10, 280))
        pygame.draw.rect(surface, (100, 80, 60), (250, 200, 10, 280))
        pygame.draw.rect(surface, (100, 80, 60), (150, 200, 110, 10))
        # Costumes
        for i in range(4):
            pygame.draw.ellipse(surface, [(120, 50, 50), (50, 50, 120), (50, 120, 50), (120, 120, 50)][i], 
                              (160 + i * 25, 220, 30, 150))


class TheaterDressingRooms(Room):
    """Dressing rooms"""
    
    def __init__(self):
        super().__init__(
            name="dressing_rooms",
            display_name="Dressing Rooms",
            connections={"up": "backstage"},
            base_color=(120, 100, 90),
            description="The dressing rooms. Mirrors show reflections of actors long dead."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Vanity Mirror", (400, 200, 200, 180),
            "A lighted vanity mirror. Your reflection doesn't match.",
            "zoom",
            "Your reflection wears theatrical makeup. It waves when you don't."
        ))
        self.add_object(InteractiveObject(
            "Makeup Table", (400, 380, 200, 80),
            "A table of old makeup. Some containers are still wet.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Wardrobe", (100, 200, 120, 280),
            "A wardrobe of costumes. One is missing.",
            "toggle"
        ))
        self.add_hidden_clue(600, 500, "LEADING LADY", "Ethereal Bride")
    
    def draw_details(self, surface):
        # Vanity mirror with lights
        pygame.draw.rect(surface, (180, 180, 190), (400, 200, 200, 180))
        for i in range(8):
            x = 410 + i * 25
            pygame.draw.circle(surface, YELLOW if self.lights_on else DARK_GRAY, (x, 210), 8)


class TheaterOrchestraPit(Room):
    """Orchestra pit"""
    
    def __init__(self):
        super().__init__(
            name="orchestra_pit",
            display_name="Orchestra Pit",
            connections={"left": "stage"},
            base_color=(50, 45, 40),
            description="The orchestra pit. Instruments play themselves. The conductor's stand is empty."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Conductor's Stand", (500, 250, 80, 120),
            "The conductor's stand. The baton moves on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Piano", (200, 300, 200, 150),
            "A grand piano. Keys press down by invisible fingers.",
            "zoom",
            "It plays a melody you've never heard but somehow know."
        ))
        self.add_object(InteractiveObject(
            "Music Stands", (700, 280, 200, 150),
            "Music stands with sheet music. The notes change.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "SYMPHONY", "The Musician")
    
    def draw_details(self, surface):
        # Piano
        pygame.draw.rect(surface, (30, 25, 20), (200, 300, 200, 150))
        pygame.draw.rect(surface, (40, 35, 30), (210, 310, 180, 60))
        # Keys
        for i in range(20):
            pygame.draw.rect(surface, WHITE, (215 + i * 8, 320, 7, 40))
        # Conductor's stand
        pygame.draw.rect(surface, (60, 50, 40), (530, 250, 20, 120))
        pygame.draw.rect(surface, (80, 70, 60), (510, 240, 60, 20))


class TheaterBalcony(Room):
    """Upper balcony seating"""
    
    def __init__(self):
        super().__init__(
            name="balcony",
            display_name="Balcony",
            connections={"left": "auditorium", "up": "projection_room"},
            base_color=(90, 35, 35),
            description="The balcony seating. The best view in the house. Also the most haunted."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Balcony Seats", (200, 300, 500, 150),
            "Plush balcony seats. Someone is sitting in the dark.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Balcony Railing", (200, 450, 500, 30),
            "An ornate railing. Worn from gripping hands.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Private Box", (800, 250, 150, 200),
            "A private viewing box. Reserved for eternity.",
            "zoom"
        ))
        self.add_hidden_clue(500, 400, "THE PHANTOM", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Balcony seats
        for row in range(2):
            for col in range(8):
                pygame.draw.rect(surface, (130, 45, 45), 
                               (220 + col * 55, 320 + row * 60, 50, 50))


class TheaterProjectionRoom(Room):
    """Projection room"""
    
    def __init__(self):
        super().__init__(
            name="projection_room",
            display_name="Projection Room",
            connections={"down": "balcony"},
            base_color=(60, 55, 50),
            description="The projection room. Old film reels show movies that were never made."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Film Projector", (400, 250, 200, 180),
            "An ancient film projector. It shows scenes of the future.",
            "toggle",
            "The film shows this building burning. The date is tomorrow."
        ))
        self.add_object(InteractiveObject(
            "Film Reels", (100, 200, 200, 200),
            "Shelves of film reels. Some are labeled with names of missing people.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Projection Window", (700, 250, 200, 150),
            "The window overlooking the auditorium. You can see them all.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "FILM AT 11", None)
    
    def draw_details(self, surface):
        # Projector
        pygame.draw.rect(surface, (80, 70, 60), (400, 250, 200, 180))
        pygame.draw.circle(surface, (100, 90, 80), (500, 300), 50)
        # Film reels
        for i in range(6):
            pygame.draw.circle(surface, (40, 35, 30), (130 + i * 35, 250 + (i % 2) * 40), 20)


class TheaterBasement(Room):
    """Theater basement"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Theater Basement",
            connections={"up": "backstage"},
            base_color=(40, 35, 30),
            description="The theater basement. Old sets and forgotten props decay in darkness."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Old Sets", (100, 200, 300, 250),
            "Forgotten stage sets from productions past. They rearrange themselves.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Trap Door Mechanism", (600, 300, 150, 150),
            "The mechanism for stage trap doors. It's been modified.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Storage Trunks", (900, 280, 150, 180),
            "Antique trunks full of costumes. One is locked from inside.",
            "toggle"
        ))
        self.add_hidden_clue(400, 550, "THE UNDERSTUDY", None)
    
    def draw_details(self, surface):
        # Old sets
        pygame.draw.rect(surface, (100, 80, 60), (100, 200, 150, 250))
        pygame.draw.rect(surface, (80, 60, 45), (260, 220, 140, 230))
        # Trunks
        pygame.draw.rect(surface, (90, 60, 40), (900, 280, 150, 100))


class TheaterRoof(Room):
    """Theater roof"""
    
    def __init__(self):
        super().__init__(
            name="roof",
            display_name="Roof",
            connections={"down": "projection_room"},
            base_color=(60, 70, 80),
            description="The theater roof. The city spreads below. Someone is always watching."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Roof Access", (500, 350, 100, 100),
            "The roof access hatch. It opens by itself.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Marquee Sign", (200, 200, 400, 100),
            "The theater marquee. The letters rearrange to spell warnings.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "HVAC Units", (800, 280, 200, 150),
            "Old air conditioning units. They whisper.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "DON'T LOOK DOWN", "Nightmare")
    
    def draw_base(self, surface):
        # Night sky
        pygame.draw.rect(surface, (20, 25, 40), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
        # Roof
        pygame.draw.rect(surface, (60, 65, 70), (0, int(SCREEN_HEIGHT * 0.4), 
                                                   SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
    
    def draw_details(self, surface):
        # Marquee
        pygame.draw.rect(surface, (150, 50, 50), (200, 200, 400, 100))
        pygame.draw.rect(surface, (40, 35, 30), (210, 210, 380, 80))


# ===============================================================================
# CEMETERY ROOMS
# ===============================================================================

class CemeteryEntranceGates(Room):
    """Cemetery entrance with iron gates"""
    
    def __init__(self):
        super().__init__(
            name="entrance_gates",
            display_name="Cemetery Gates",
            connections={"right": "main_path"},
            base_color=(50, 55, 50),
            description="Rusted iron gates creak in the wind. 'ETERNAL REST' is carved above."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Iron Gates", (500, 150, 200, 350),
            "Massive iron gates. They're locked, but you got in somehow.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cemetery Sign", (200, 200, 150, 100),
            "A weathered sign. 'Eternal Rest Cemetery - Est. 1823'",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Dead Flowers", (800, 350, 100, 80),
            "Withered flowers left for someone long forgotten.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "NO EXIT", "Shadow Stalker")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (20, 25, 35), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (40, 50, 40), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        # Iron gates
        pygame.draw.rect(surface, (60, 55, 50), (500, 150, 20, 350))
        pygame.draw.rect(surface, (60, 55, 50), (680, 150, 20, 350))
        for i in range(8):
            pygame.draw.rect(surface, (50, 45, 40), (520 + i * 20, 180, 5, 300))


class CemeteryMainPath(Room):
    """Main path through the cemetery"""
    
    def __init__(self):
        super().__init__(
            name="main_path",
            display_name="Main Path",
            connections={"left": "entrance_gates", "right": "old_graves", "up": "mausoleum"},
            base_color=(45, 50, 45),
            description="A gravel path winds between headstones. Fog rolls across the ground."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Headstone 1", (200, 300, 80, 120),
            "A weathered headstone. The name is worn away.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Headstone 2", (400, 280, 80, 140),
            "This headstone has fresh flowers. The death date is today.",
            "zoom",
            "The epitaph reads: 'Here lies [YOUR NAME]'. That's impossible."
        ))
        self.add_object(InteractiveObject(
            "Grave Lantern", (700, 320, 60, 100),
            "A lantern by a grave. It flickers with ghostly light.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "WEEPING", "Weeping Lady")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (20, 25, 35), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (40, 50, 40), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
        # Gravel path
        pygame.draw.rect(surface, (80, 75, 70), (400, int(SCREEN_HEIGHT * 0.4), 200, int(SCREEN_HEIGHT * 0.6)))
    
    def draw_details(self, surface):
        # Headstones
        for x, h in [(200, 120), (400, 140), (800, 100), (900, 130)]:
            pygame.draw.rect(surface, (120, 120, 125), (x, 350 - h, 80, h))
            pygame.draw.rect(surface, (100, 100, 105), (x + 5, 355 - h, 70, 20))


class CemeteryOldGraves(Room):
    """Old section with ancient graves"""
    
    def __init__(self):
        super().__init__(
            name="old_graves",
            display_name="Old Graves",
            connections={"left": "main_path", "down": "crypt"},
            base_color=(40, 45, 40),
            description="The oldest part of the cemetery. Some graves date back centuries."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Crumbling Headstone", (300, 280, 100, 150),
            "An ancient headstone. The inscription is in a dead language.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Open Grave", (600, 350, 150, 100),
            "An open grave. Fresh dirt is piled beside it.",
            "zoom",
            "Looking in, you see a coffin. The lid is open from the inside."
        ))
        self.add_object(InteractiveObject(
            "Dead Tree", (900, 200, 150, 300),
            "A gnarled dead tree. Crows watch from its branches.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "DIG", "The Gravedigger")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (15, 20, 30), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (35, 45, 35), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        # Crumbling headstones
        pygame.draw.rect(surface, (100, 100, 105), (300, 280, 100, 150))
        # Open grave
        pygame.draw.rect(surface, (30, 25, 20), (600, 350, 150, 100))
        # Dirt pile
        pygame.draw.ellipse(surface, (60, 50, 40), (760, 380, 80, 50))


class CemeteryMausoleum(Room):
    """Family mausoleum"""
    
    def __init__(self):
        super().__init__(
            name="mausoleum",
            display_name="Mausoleum",
            connections={"down": "main_path", "right": "crypt"},
            base_color=(60, 65, 70),
            description="A grand family mausoleum. The door stands open, inviting you in."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stone Door", (500, 180, 180, 320),
            "A heavy stone door. Names are carved around the frame.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Family Crest", (590, 150, 100, 80),
            "An ornate family crest. The family died out long ago.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Stone Angels", (200, 250, 100, 200),
            "Stone angels guard the entrance. Their faces are worn smooth.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "THE COLLECTOR", "The Collector")
    
    def draw_details(self, surface):
        # Mausoleum front
        pygame.draw.rect(surface, (80, 85, 90), (450, 150, 280, 400))
        pygame.draw.polygon(surface, (90, 95, 100), [(450, 150), (590, 80), (730, 150)])
        # Door
        pygame.draw.rect(surface, (40, 35, 30), (530, 220, 120, 280))
        # Columns
        pygame.draw.rect(surface, (100, 105, 110), (460, 150, 40, 400))
        pygame.draw.rect(surface, (100, 105, 110), (680, 150, 40, 400))


class CemeteryCrypt(Room):
    """Underground crypt"""
    
    def __init__(self):
        super().__init__(
            name="crypt",
            display_name="Crypt",
            connections={"up": "old_graves", "left": "mausoleum"},
            base_color=(40, 40, 45),
            description="An underground crypt. Stone coffins line the walls. It's cold."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stone Coffin", (400, 280, 250, 120),
            "A stone sarcophagus. The lid has been moved recently.",
            "zoom",
            "Inside: empty. But there are scratch marks on the inside of the lid."
        ))
        self.add_object(InteractiveObject(
            "Wall Niches", (100, 180, 200, 300),
            "Burial niches in the wall. Some are occupied.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Altar", (800, 300, 150, 100),
            "A stone altar with melted candles. Someone still comes here.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "UNDEAD", "Nightmare")
    
    def draw_details(self, surface):
        # Stone walls
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 40):
            for x in range(0, SCREEN_WIDTH, 80):
                pygame.draw.rect(surface, (50, 50, 55), (x, y, 78, 38))
        # Coffin
        pygame.draw.rect(surface, (70, 70, 75), (400, 280, 250, 120))
        pygame.draw.rect(surface, (60, 60, 65), (410, 290, 230, 100))


class CemeteryGroundskeeperShed(Room):
    """Groundskeeper's shed"""
    
    def __init__(self):
        super().__init__(
            name="groundskeeper_shed",
            display_name="Groundskeeper's Shed",
            connections={"right": "chapel"},
            base_color=(70, 60, 50),
            description="The groundskeeper's shed. Tools for digging graves hang on the walls."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Shovels", (100, 200, 100, 280),
            "Grave-digging shovels. They're well-used.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Grave Register", (500, 300, 150, 80),
            "A book listing all burials. Some names are crossed out.",
            "zoom",
            "The crossed-out names... they walked away."
        ))
        self.add_object(InteractiveObject(
            "Wheelbarrow", (800, 350, 120, 100),
            "A wheelbarrow with dried dirt. And something else.",
            "examine"
        ))
        self.add_hidden_clue(400, 500, "FRESH GRAVE", "The Gravedigger")
    
    def draw_details(self, surface):
        # Wooden walls
        for x in range(0, SCREEN_WIDTH, 50):
            pygame.draw.rect(surface, (65, 55, 45), (x, 0, 48, int(SCREEN_HEIGHT * 0.6)))
        # Shovels
        pygame.draw.rect(surface, (80, 60, 40), (120, 200, 10, 250))
        pygame.draw.rect(surface, (100, 100, 100), (110, 430, 30, 40))


class CemeteryChapel(Room):
    """Small cemetery chapel"""
    
    def __init__(self):
        super().__init__(
            name="chapel",
            display_name="Cemetery Chapel",
            connections={"left": "groundskeeper_shed", "right": "new_graves"},
            base_color=(80, 75, 70),
            description="A small chapel for funeral services. The organ plays by itself."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Pews", (300, 350, 400, 150),
            "Wooden pews for mourners. Someone is sitting in the front.",
            "examine",
            "You approach... but the pew is empty. A cold spot remains."
        ))
        self.add_object(InteractiveObject(
            "Altar", (550, 200, 150, 100),
            "A simple altar with a cross. Flowers wilt instantly here.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Organ", (900, 220, 150, 200),
            "A pipe organ. Keys press down without a player.",
            "toggle"
        ))
        self.add_hidden_clue(600, 500, "SERMON", "The Preacher")
    
    def draw_details(self, surface):
        # Pews
        for i in range(4):
            pygame.draw.rect(surface, (90, 70, 55), (300, 350 + i * 35, 400, 30))
        # Altar
        pygame.draw.rect(surface, (100, 95, 90), (550, 200, 150, 100))
        # Cross
        pygame.draw.rect(surface, (120, 100, 80), (615, 120, 20, 80))
        pygame.draw.rect(surface, (120, 100, 80), (595, 150, 60, 15))


class CemeteryNewGraves(Room):
    """New section with recent burials"""
    
    def __init__(self):
        super().__init__(
            name="new_graves",
            display_name="New Graves",
            connections={"left": "chapel"},
            base_color=(50, 55, 50),
            description="Recent burials. The dirt is still fresh on some graves."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Fresh Grave", (400, 350, 150, 80),
            "A very fresh grave. The flowers haven't wilted yet.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Mourning Statue", (700, 250, 100, 200),
            "A statue of a weeping woman. Real tears run down her face.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Grave Marker", (200, 320, 100, 130),
            "A temporary grave marker. The name matches someone you know.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "SOON", "Nightmare")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (20, 25, 35), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (45, 55, 45), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        # Fresh dirt mounds
        pygame.draw.ellipse(surface, (70, 55, 45), (380, 380, 190, 60))
        # Mourning statue
        pygame.draw.ellipse(surface, (150, 150, 155), (720, 260, 60, 180))
        pygame.draw.circle(surface, (160, 160, 165), (750, 280), 25)


# ===============================================================================
# HOTEL ROOMS
# ===============================================================================

class HotelLobby(Room):
    """Grand hotel lobby"""
    
    def __init__(self):
        super().__init__(
            name="lobby",
            display_name="Hotel Lobby",
            connections={"right": "reception", "up": "elevator"},
            base_color=(120, 90, 90),
            description="A once-grand lobby, now faded. Crystal chandeliers gather dust."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Grand Chandelier", (600, 50, 150, 150),
            "A massive crystal chandelier. It sways without wind.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Lobby Couch", (200, 350, 250, 100),
            "Velvet couches for waiting guests. The cushions sink as if sat upon.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Grand Staircase", (800, 200, 200, 300),
            "A sweeping staircase. Footsteps echo from above.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "CHECK IN", "The Servant")
    
    def draw_details(self, surface):
        # Chandelier
        pygame.draw.ellipse(surface, (200, 180, 150), (550, 50, 200, 150))
        # Staircase
        for i in range(10):
            pygame.draw.rect(surface, (100, 70, 60), (800 + i * 10, 450 - i * 25, 190 - i * 10, 20))


class HotelReception(Room):
    """Hotel reception desk"""
    
    def __init__(self):
        super().__init__(
            name="reception",
            display_name="Reception",
            connections={"left": "lobby", "right": "room_237", "down": "kitchen"},
            base_color=(110, 85, 80),
            description="The reception desk. The bell rings on its own. No one answers."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Reception Desk", (400, 280, 300, 120),
            "The main desk. Keys hang on a board behind it.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Guest Book", (500, 300, 80, 50),
            "The guest register. Your name is already written in it.",
            "zoom",
            "Your check-in date was 50 years ago. You never checked out."
        ))
        self.add_object(InteractiveObject(
            "Service Bell", (550, 280, 30, 20),
            "A service bell. Ring it and wait. Forever.",
            "toggle"
        ))
        self.add_hidden_clue(600, 500, "ROOM SERVICE", "The Servant")
    
    def draw_details(self, surface):
        # Reception desk
        pygame.draw.rect(surface, (80, 55, 45), (400, 280, 300, 120))
        # Key board
        pygame.draw.rect(surface, (90, 65, 55), (420, 150, 260, 120))
        for i in range(12):
            pygame.draw.rect(surface, (180, 150, 50), (430 + (i % 4) * 60, 160 + (i // 4) * 35, 15, 25))


class HotelRoom237(Room):
    """The infamous Room 237"""
    
    def __init__(self):
        super().__init__(
            name="room_237",
            display_name="Room 237",
            connections={"left": "reception", "right": "hallway"},
            base_color=(100, 80, 80),
            description="Room 237. The most haunted room in the hotel. The door was locked."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Hotel Bed", (400, 280, 300, 180),
            "A king-size bed. Someone has been sleeping here recently.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Bathroom Door", (800, 200, 100, 280),
            "The bathroom door is slightly ajar. Steam seeps out.",
            "toggle",
            "You open the door. The bathtub is full. Someone is in there."
        ))
        self.add_object(InteractiveObject(
            "Room 237 Window", (100, 200, 150, 200),
            "The window shows impossible views. A maze that shouldn't exist.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "FOREVER", "Nightmare")
    
    def draw_details(self, surface):
        # Bed
        pygame.draw.rect(surface, (60, 45, 40), (400, 280, 300, 180))
        pygame.draw.rect(surface, (150, 120, 100), (410, 290, 280, 160))
        # Bathroom door
        pygame.draw.rect(surface, (80, 60, 50), (800, 200, 100, 280))


class HotelHallway(Room):
    """Long hotel hallway"""
    
    def __init__(self):
        super().__init__(
            name="hallway",
            display_name="Hallway",
            connections={"left": "room_237", "right": "ballroom", "up": "penthouse"},
            base_color=(100, 75, 75),
            description="An endless hallway. Identical doors stretch into darkness."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Room Doors", (200, 200, 800, 250),
            "Endless identical doors. Some open as you pass.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Hallway Carpet", (0, 450, SCREEN_WIDTH, 100),
            "Ornate carpet with a hypnotic pattern. It seems to move.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Fire Extinguisher", (1000, 280, 50, 100),
            "A fire extinguisher. The pressure gauge is in the red.",
            "examine"
        ))
        self.add_hidden_clue(600, 400, "REDRUM", "Nightmare")
    
    def draw_details(self, surface):
        # Doors on both sides
        for i in range(6):
            pygame.draw.rect(surface, (80, 55, 45), (150 + i * 160, 200, 80, 200))
            pygame.draw.circle(surface, (180, 150, 50), (210 + i * 160, 300), 8)


class HotelBallroom(Room):
    """Grand ballroom"""
    
    def __init__(self):
        super().__init__(
            name="ballroom",
            display_name="Ballroom",
            connections={"left": "hallway"},
            base_color=(130, 100, 90),
            description="The grand ballroom. Music plays. Ghostly couples dance in the moonlight."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dance Floor", (300, 350, 500, 200),
            "A polished dance floor. Footprints appear and disappear.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Stage", (500, 180, 250, 100),
            "A stage for the orchestra. Instruments play themselves.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Bar", (900, 280, 150, 150),
            "The ballroom bar. Glasses fill with champagne on their own.",
            "toggle"
        ))
        self.add_hidden_clue(600, 550, "MAY I HAVE THIS DANCE", "Ethereal Bride")
    
    def draw_details(self, surface):
        # Dance floor
        for y in range(350, 550, 40):
            for x in range(300, 800, 40):
                color = (160, 140, 120) if (x + y) % 80 == 0 else (140, 120, 100)
                pygame.draw.rect(surface, color, (x, y, 38, 38))
        # Stage
        pygame.draw.rect(surface, (80, 60, 50), (500, 180, 250, 100))


class HotelKitchen(Room):
    """Hotel kitchen"""
    
    def __init__(self):
        super().__init__(
            name="kitchen",
            display_name="Kitchen",
            connections={"up": "reception", "down": "basement"},
            base_color=(150, 145, 140),
            description="The hotel kitchen. Knives line the walls. Something cooks eternally."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Industrial Stove", (400, 280, 250, 150),
            "A massive stove. Pots boil with no one watching.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Knife Rack", (800, 220, 100, 150),
            "Chef's knives. All pointing at you when you look away.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Walk-in Freezer", (100, 200, 150, 250),
            "A walk-in freezer. Something is hanging inside.",
            "toggle",
            "Inside: frozen meats. But one shape is too human."
        ))
        self.add_hidden_clue(500, 500, "TONIGHT'S SPECIAL", "The Butcher")
    
    def draw_details(self, surface):
        # Stove
        pygame.draw.rect(surface, (80, 80, 85), (400, 280, 250, 150))
        for i in range(4):
            pygame.draw.circle(surface, (60, 60, 65), (450 + i * 50, 330), 20)
        # Freezer door
        pygame.draw.rect(surface, (140, 145, 150), (100, 200, 150, 250))


class HotelBasement(Room):
    """Hotel basement"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Hotel Basement",
            connections={"up": "kitchen"},
            base_color=(50, 50, 55),
            description="The hotel basement. Boilers and bad memories are stored here."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Boiler Room", (200, 220, 250, 250),
            "Old boilers. They rumble with pressure.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Storage Cages", (600, 280, 200, 180),
            "Wire storage cages. Some contain forgotten luggage.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Fuse Box", (900, 300, 80, 120),
            "The main electrical panel. It sparks dangerously.",
            "toggle"
        ))
        self.add_hidden_clue(400, 550, "THE FIRE", "The Arsonist")
    
    def draw_details(self, surface):
        # Boilers
        pygame.draw.rect(surface, (70, 60, 55), (200, 220, 250, 250))
        pygame.draw.ellipse(surface, (80, 70, 65), (220, 240, 210, 150))


class HotelPenthouse(Room):
    """Penthouse suite"""
    
    def __init__(self):
        super().__init__(
            name="penthouse",
            display_name="Penthouse",
            connections={"down": "hallway"},
            base_color=(140, 110, 100),
            description="The penthouse suite. Luxury and death share this space."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Grand Piano", (300, 300, 250, 150),
            "A grand piano. It plays a mournful melody by itself.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Panoramic Windows", (600, 150, 400, 250),
            "Floor-to-ceiling windows. The view changes each time you look.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Champagne Table", (900, 350, 120, 80),
            "A table with champagne. Two glasses, eternally full.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "TILL DEATH", "Ethereal Bride")
    
    def draw_details(self, surface):
        # Piano
        pygame.draw.rect(surface, (20, 20, 25), (300, 300, 250, 150))
        pygame.draw.rect(surface, (30, 30, 35), (310, 310, 230, 60))
        # Windows
        pygame.draw.rect(surface, (60, 80, 100), (600, 150, 400, 250))


class HotelElevator(Room):
    """Hotel elevator"""
    
    def __init__(self):
        super().__init__(
            name="elevator",
            display_name="Elevator",
            connections={"down": "lobby", "up": "penthouse"},
            base_color=(160, 130, 100),
            description="The old elevator. The doors open and close on their own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Elevator Buttons", (800, 280, 60, 200),
            "Brass elevator buttons. One glows without being pressed.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Elevator Mirror", (400, 200, 200, 300),
            "A mirror covering the back wall. Your reflection is delayed.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Floor Indicator", (600, 150, 100, 50),
            "The floor indicator. It shows floors that don't exist.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "GOING DOWN", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Elevator walls
        pygame.draw.rect(surface, (150, 120, 90), (300, 100, 600, 500))
        # Mirror
        pygame.draw.rect(surface, (180, 180, 190), (400, 200, 200, 300))
        # Buttons
        for i in range(8):
            pygame.draw.circle(surface, (200, 180, 100), (830, 300 + i * 22), 8)


class HotelLaundry(Room):
    """Hotel laundry room"""
    
    def __init__(self):
        super().__init__(
            name="laundry",
            display_name="Laundry Room",
            connections={"up": "basement"},
            base_color=(170, 170, 175),
            description="The laundry room. Sheets fold themselves. Blood stains never wash out."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Industrial Washers", (200, 280, 300, 200),
            "Industrial washing machines. They spin endlessly.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Folding Table", (600, 320, 200, 80),
            "Sheets fold themselves on this table. Perfectly.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Laundry Chute", (900, 200, 80, 150),
            "A laundry chute. Things fall in but never come out.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "BLOOD STAINS", "The Butcher")
    
    def draw_details(self, surface):
        # Washers
        for i in range(3):
            pygame.draw.rect(surface, (200, 200, 205), (200 + i * 100, 280, 90, 120))
            pygame.draw.circle(surface, (150, 150, 155), (245 + i * 100, 340), 30)


# ===============================================================================
# GHOST SHIP ROOMS
# ===============================================================================

class ShipDeck(Room):
    """Main deck of the ghost ship"""
    
    def __init__(self):
        super().__init__(
            name="deck",
            display_name="Main Deck",
            connections={"right": "bridge", "down": "cargo_hold"},
            base_color=(60, 80, 90),
            description="The main deck. Waves crash. The ship creaks. No crew in sight."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Ship's Wheel", (500, 200, 100, 100),
            "The ship's wheel. It turns on its own, steering to nowhere.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Life Boats", (100, 280, 200, 150),
            "Empty lifeboats. They were never used.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Mast", (800, 100, 50, 400),
            "The main mast. Tattered sails hang limply.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "ABANDON SHIP", "The Captain")
    
    def draw_base(self, surface):
        # Stormy sky
        pygame.draw.rect(surface, (40, 50, 70), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        # Ocean
        pygame.draw.rect(surface, (30, 50, 80), (0, int(SCREEN_HEIGHT * 0.7), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        # Deck
        pygame.draw.rect(surface, (80, 60, 50), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
    
    def draw_details(self, surface):
        # Wheel
        pygame.draw.circle(surface, (90, 70, 55), (550, 250), 50, 5)
        # Mast
        pygame.draw.rect(surface, (100, 80, 60), (810, 100, 30, 400))


class ShipBridge(Room):
    """Ship's bridge"""
    
    def __init__(self):
        super().__init__(
            name="bridge",
            display_name="Bridge",
            connections={"left": "deck", "down": "captains_quarters"},
            base_color=(70, 65, 60),
            description="The bridge. Maps are spread out. The last course was never finished."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Navigation Charts", (400, 280, 250, 150),
            "Navigation charts. The route ends in the middle of the ocean.",
            "zoom",
            "The final notation: 'Something in the water. God help us.'"
        ))
        self.add_object(InteractiveObject(
            "Ship's Log", (700, 300, 80, 60),
            "The captain's log. The last entry is smeared with blood.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Compass", (200, 320, 80, 80),
            "A ship's compass. It spins endlessly.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "WE ARE LOST", "The Mariner")
    
    def draw_details(self, surface):
        # Chart table
        pygame.draw.rect(surface, (90, 70, 55), (400, 280, 250, 150))
        # Charts
        pygame.draw.rect(surface, CREAM, (420, 300, 210, 110))


class ShipCaptainsQuarters(Room):
    """Captain's private quarters"""
    
    def __init__(self):
        super().__init__(
            name="captains_quarters",
            display_name="Captain's Quarters",
            connections={"up": "bridge", "right": "crew_quarters"},
            base_color=(80, 65, 55),
            description="The captain's quarters. Luxurious but abandoned. His ghost remains."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Captain's Bed", (400, 300, 250, 150),
            "The captain's bed. Sheets are thrown aside hastily.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Personal Safe", (800, 280, 100, 120),
            "A locked safe. Something valuable is inside.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Portrait", (200, 180, 120, 180),
            "A portrait of the captain. His eyes follow you.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "THE CAPTAIN", "The Captain")
    
    def draw_details(self, surface):
        # Bed
        pygame.draw.rect(surface, (70, 55, 45), (400, 300, 250, 150))
        pygame.draw.rect(surface, (150, 130, 110), (410, 310, 230, 130))
        # Portrait
        pygame.draw.rect(surface, (100, 80, 60), (200, 180, 120, 180))


class ShipCrewQuarters(Room):
    """Crew sleeping quarters"""
    
    def __init__(self):
        super().__init__(
            name="crew_quarters",
            display_name="Crew Quarters",
            connections={"left": "captains_quarters", "down": "galley"},
            base_color=(60, 55, 50),
            description="Cramped bunks for the crew. Personal effects are scattered about."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bunk Beds", (200, 200, 200, 280),
            "Stacked bunks. Blankets are still warm.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Sea Chest", (500, 350, 150, 100),
            "A sailor's chest. Letters to loved ones, never sent.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Hammock", (800, 250, 150, 100),
            "A swaying hammock. It moves as if occupied.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "SHIPMATES", "The Sailor")
    
    def draw_details(self, surface):
        # Bunks
        for i in range(3):
            pygame.draw.rect(surface, (80, 60, 50), (200, 200 + i * 90, 200, 80))


class ShipCargoHold(Room):
    """Cargo hold"""
    
    def __init__(self):
        super().__init__(
            name="cargo_hold",
            display_name="Cargo Hold",
            connections={"up": "deck", "right": "engine_room"},
            base_color=(40, 40, 45),
            description="The cargo hold. Crates are stacked high. Something moves between them."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Cargo Crates", (200, 250, 400, 200),
            "Stacked shipping crates. Some have been pried open.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Chains", (700, 200, 100, 250),
            "Heavy chains hanging from hooks. They swing on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cargo Manifest", (900, 300, 80, 100),
            "The cargo manifest. One item is listed as 'PASSENGER - DO NOT OPEN'.",
            "zoom"
        ))
        self.add_hidden_clue(500, 550, "STOWAWAY", "The Stowaway")
    
    def draw_details(self, surface):
        # Crates
        for i in range(4):
            for j in range(2):
                pygame.draw.rect(surface, (90, 70, 55), (200 + i * 100, 300 - j * 80, 90, 70))


class ShipEngineRoom(Room):
    """Engine room"""
    
    def __init__(self):
        super().__init__(
            name="engine_room",
            display_name="Engine Room",
            connections={"left": "cargo_hold"},
            base_color=(50, 50, 55),
            description="The engine room. Machines grind. Steam hisses. Heat is unbearable."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Steam Engine", (400, 200, 300, 280),
            "The ship's engine. It runs without fuel.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Coal Furnace", (100, 280, 200, 200),
            "A furnace for coal. It burns eternally.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Pressure Gauges", (800, 250, 100, 150),
            "Pressure gauges. All in the red zone.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "OVERHEATING", "The Burned Man")
    
    def draw_details(self, surface):
        # Engine
        pygame.draw.rect(surface, (70, 70, 75), (400, 200, 300, 280))
        # Pistons
        pygame.draw.rect(surface, (100, 100, 105), (430, 220, 50, 200))
        pygame.draw.rect(surface, (100, 100, 105), (530, 220, 50, 200))
        pygame.draw.rect(surface, (100, 100, 105), (630, 220, 50, 200))


class ShipGalley(Room):
    """Ship's kitchen (galley)"""
    
    def __init__(self):
        super().__init__(
            name="galley",
            display_name="Galley",
            connections={"up": "crew_quarters", "right": "lifeboat_deck"},
            base_color=(80, 75, 70),
            description="The ship's galley. A meal was being prepared. It never finished."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stove", (400, 280, 200, 150),
            "A wood-burning stove. Something still cooks in the pot.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Food Stores", (100, 200, 200, 250),
            "Barrels and crates of provisions. Some are empty.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cutting Board", (700, 300, 100, 60),
            "A cutting board with a knife. Vegetables half-chopped.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "LAST SUPPER", "The Drowned")
    
    def draw_details(self, surface):
        # Stove
        pygame.draw.rect(surface, (60, 55, 50), (400, 280, 200, 150))
        # Pot
        pygame.draw.ellipse(surface, (70, 70, 75), (450, 260, 100, 50))


class ShipLifeboatDeck(Room):
    """Lifeboat deck"""
    
    def __init__(self):
        super().__init__(
            name="lifeboat_deck",
            display_name="Lifeboat Deck",
            connections={"left": "galley"},
            base_color=(50, 70, 80),
            description="The lifeboat deck. All boats are still here. No one escaped."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Lifeboats", (300, 280, 400, 150),
            "Four lifeboats. Never launched. Why?",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Ship's Railing", (100, 400, SCREEN_WIDTH - 200, 50),
            "The ship's railing. Deep scratch marks in the wood.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Life Preservers", (800, 250, 100, 100),
            "Life preservers. 'S.S. SPECTRE' is printed on them.",
            "examine"
        ))
        self.add_hidden_clue(500, 350, "WOMEN AND CHILDREN", "The Drowned")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (40, 50, 70), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
        pygame.draw.rect(surface, (30, 50, 80), (0, int(SCREEN_HEIGHT * 0.7), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (70, 55, 45), (0, int(SCREEN_HEIGHT * 0.4), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
    
    def draw_details(self, surface):
        # Lifeboats
        for i in range(4):
            pygame.draw.ellipse(surface, (90, 70, 55), (300 + i * 100, 300, 90, 40))


# ===============================================================================
# ABANDONED MINE ROOMS
# ===============================================================================

class MineEntrance(Room):
    """Mine entrance"""
    
    def __init__(self):
        super().__init__(
            name="mine_entrance",
            display_name="Mine Entrance",
            connections={"right": "shaft_1"},
            base_color=(45, 40, 35),
            description="The mine entrance. Wooden beams creak ominously. Darkness awaits below."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Warning Sign", (200, 200, 150, 100),
            "A weathered sign: 'DANGER - MINE CLOSED - NO ENTRY'",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Mine Cart", (500, 350, 200, 100),
            "An old mine cart. Rust and ore residue cover it.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Tool Shed", (800, 250, 150, 200),
            "A shed with mining tools. Picks and shovels line the walls.",
            "toggle"
        ))
        self.add_hidden_clue(600, 500, "CAVE IN", "The Miner")
    
    def draw_details(self, surface):
        # Mine entrance frame
        pygame.draw.rect(surface, (70, 55, 45), (450, 150, 250, 350))
        pygame.draw.rect(surface, (20, 18, 15), (470, 170, 210, 310))
        # Support beams
        pygame.draw.rect(surface, (80, 60, 50), (450, 150, 20, 350))
        pygame.draw.rect(surface, (80, 60, 50), (680, 150, 20, 350))
        pygame.draw.rect(surface, (80, 60, 50), (450, 150, 250, 25))


class MineShaft1(Room):
    """First mine shaft"""
    
    def __init__(self):
        super().__init__(
            name="shaft_1",
            display_name="Shaft 1",
            connections={"left": "mine_entrance", "right": "shaft_2", "down": "ore_processing"},
            base_color=(35, 32, 28),
            description="A dark mine shaft. Miner's lights flicker in the distance."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Rail Tracks", (200, 450, 800, 50),
            "Rusted rail tracks for ore carts. They disappear into darkness.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Support Beam", (500, 100, 50, 400),
            "A wooden support beam. It groans under the weight.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Miner's Lamp", (700, 250, 60, 80),
            "An abandoned lamp. It flickers with ghostly light.",
            "toggle"
        ))
        self.add_hidden_clue(400, 350, "TRAPPED", "The Miner")
    
    def draw_details(self, surface):
        # Rock walls
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 50):
            for x in range(0, SCREEN_WIDTH, 70):
                pygame.draw.ellipse(surface, (45, 40, 35), (x, y, 65, 45))
        # Tracks
        pygame.draw.rect(surface, (80, 70, 60), (200, 470, 800, 10))
        pygame.draw.rect(surface, (80, 70, 60), (200, 490, 800, 10))


class MineShaft2(Room):
    """Second mine shaft"""
    
    def __init__(self):
        super().__init__(
            name="shaft_2",
            display_name="Shaft 2",
            connections={"left": "shaft_1", "down": "collapsed_tunnel"},
            base_color=(30, 28, 25),
            description="A deeper shaft. The air is thin. Whispers echo off the walls."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Ore Vein", (300, 200, 200, 250),
            "A vein of ore glitters in the wall. Worth dying for?",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Pickaxe", (700, 300, 80, 120),
            "An abandoned pickaxe. Still embedded in the wall.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Canary Cage", (900, 250, 60, 80),
            "An empty canary cage. The bird is long gone.",
            "examine"
        ))
        self.add_hidden_clue(500, 450, "GAS LEAK", "The Canary")
    
    def draw_details(self, surface):
        # Rock walls with ore
        for y in range(0, int(SCREEN_HEIGHT * 0.6), 50):
            for x in range(0, SCREEN_WIDTH, 70):
                pygame.draw.ellipse(surface, (40, 38, 33), (x, y, 65, 45))
        # Ore vein sparkles
        pygame.draw.ellipse(surface, (120, 100, 50), (300, 200, 200, 250))


class MineOreProcessing(Room):
    """Ore processing area"""
    
    def __init__(self):
        super().__init__(
            name="ore_processing",
            display_name="Ore Processing",
            connections={"up": "shaft_1", "right": "elevator"},
            base_color=(50, 45, 40),
            description="Where ore was crushed and sorted. Machinery still rumbles."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Crusher", (400, 250, 250, 200),
            "A massive ore crusher. It still operates on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Conveyor Belt", (100, 350, 300, 80),
            "A conveyor belt. Ore moves along it... but there's no ore.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Control Panel", (800, 280, 100, 150),
            "Controls for the machinery. Dials spin erratically.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "FOREMAN", "The Foreman")
    
    def draw_details(self, surface):
        # Crusher
        pygame.draw.rect(surface, (80, 75, 70), (400, 250, 250, 200))
        pygame.draw.ellipse(surface, (70, 65, 60), (420, 270, 210, 100))


class MineElevator(Room):
    """Mine elevator shaft"""
    
    def __init__(self):
        super().__init__(
            name="elevator",
            display_name="Mine Elevator",
            connections={"left": "ore_processing", "down": "underground_lake"},
            base_color=(40, 38, 35),
            description="The mine elevator. Cables creak. Going down is the only option."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Elevator Cage", (450, 200, 200, 300),
            "A rickety elevator cage. It sways dangerously.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cable System", (640, 50, 50, 200),
            "Frayed cables hold the elevator. How much longer?",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Level Indicator", (700, 300, 80, 120),
            "Shows mining levels. The deepest level is marked 'FORBIDDEN'.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "GOING DOWN", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Elevator cage
        pygame.draw.rect(surface, (70, 65, 60), (450, 200, 200, 300))
        pygame.draw.rect(surface, (50, 45, 40), (460, 210, 180, 280))
        # Cables
        pygame.draw.line(surface, (100, 95, 90), (550, 0), (550, 200), 5)


class MineCollapsedTunnel(Room):
    """Collapsed tunnel section"""
    
    def __init__(self):
        super().__init__(
            name="collapsed_tunnel",
            display_name="Collapsed Tunnel",
            connections={"up": "shaft_2"},
            base_color=(35, 32, 28),
            description="A collapsed section. Rocks block the way. But voices come from behind."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Rubble Pile", (400, 250, 300, 250),
            "Massive rocks block the tunnel. Someone is trapped behind.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Miner's Helmet", (200, 380, 80, 60),
            "A miner's helmet. The light is still on. The owner is not.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Exposed Bones", (800, 350, 100, 80),
            "Bones protrude from the rubble. The rescue never came.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "STILL ALIVE", "The Miner")
    
    def draw_details(self, surface):
        # Rubble
        for i in range(10):
            x = 400 + random.randint(0, 250)
            y = 280 + random.randint(0, 180)
            pygame.draw.ellipse(surface, (60, 55, 50), (x, y, 50 + i * 5, 40 + i * 3))


class MineUndergroundLake(Room):
    """Underground lake"""
    
    def __init__(self):
        super().__init__(
            name="underground_lake",
            display_name="Underground Lake",
            connections={"up": "elevator", "right": "exit_tunnel"},
            base_color=(30, 40, 50),
            description="An underground lake. Black water reflects nothing. Something swims below."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dark Water", (200, 350, 600, 200),
            "Black, still water. Your reflection doesn't appear.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Boat", (500, 380, 150, 60),
            "An old rowboat. Would you trust it?",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Phosphorescent Rocks", (900, 280, 100, 150),
            "Glowing rocks. They pulse with an eerie rhythm.",
            "examine"
        ))
        self.add_hidden_clue(600, 300, "DROWNED", "The Drowned")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (25, 30, 40), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
        pygame.draw.rect(surface, (20, 30, 45), (0, int(SCREEN_HEIGHT * 0.4), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
    
    def draw_details(self, surface):
        # Water
        pygame.draw.rect(surface, (15, 25, 40), (100, 350, 900, 250))


class MineExitTunnel(Room):
    """Exit tunnel"""
    
    def __init__(self):
        super().__init__(
            name="exit_tunnel",
            display_name="Exit Tunnel",
            connections={"left": "underground_lake"},
            base_color=(40, 38, 35),
            description="A tunnel promising escape. But the exit keeps getting further away."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Light Ahead", (800, 200, 200, 300),
            "Light from outside! Or is it?",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cave Drawings", (200, 200, 200, 200),
            "Crude drawings on the wall. Miners left messages.",
            "zoom",
            "The drawings show figures fleeing from something in the dark."
        ))
        self.add_object(InteractiveObject(
            "Discarded Tools", (500, 400, 150, 80),
            "Tools dropped in haste. They were running.",
            "examine"
        ))
        self.add_hidden_clue(600, 350, "NO ESCAPE", "Nightmare")
    
    def draw_details(self, surface):
        # Light at end
        pygame.draw.ellipse(surface, (150, 160, 170), (800, 200, 200, 300))
        pygame.draw.ellipse(surface, (200, 210, 220), (850, 250, 100, 200))


# ===============================================================================
# MUSEUM ROOMS
# ===============================================================================

class MuseumMainHall(Room):
    """Museum main hall"""
    
    def __init__(self):
        super().__init__(
            name="main_hall",
            display_name="Main Hall",
            connections={"right": "egyptian_exhibit", "up": "dinosaur_hall"},
            base_color=(160, 150, 140),
            description="The grand entrance hall. Marble floors echo your footsteps. And others."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Information Desk", (500, 300, 200, 100),
            "The main desk. Brochures are scattered about.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Dinosaur Skeleton", (200, 150, 300, 350),
            "A T-Rex skeleton dominates the hall. Its head turns to follow you.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Donation Box", (900, 350, 80, 100),
            "A donation box. Coins jingle inside on their own.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "EXHIBITS", "The Collector")
    
    def draw_details(self, surface):
        # Marble floor pattern
        for y in range(int(SCREEN_HEIGHT * 0.6), SCREEN_HEIGHT, 60):
            for x in range(0, SCREEN_WIDTH, 60):
                color = (170, 165, 160) if (x + y) % 120 == 0 else (155, 150, 145)
                pygame.draw.rect(surface, color, (x, y, 58, 58))
        # Dino skeleton
        pygame.draw.ellipse(surface, (220, 215, 210), (200, 200, 150, 100))
        pygame.draw.rect(surface, (220, 215, 210), (250, 300, 20, 150))


class MuseumEgyptianExhibit(Room):
    """Egyptian exhibit"""
    
    def __init__(self):
        super().__init__(
            name="egyptian_exhibit",
            display_name="Egyptian Exhibit",
            connections={"left": "main_hall", "right": "art_gallery"},
            base_color=(180, 160, 120),
            description="Ancient Egyptian artifacts. Sarcophagi line the walls. One is open."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Sarcophagus", (400, 200, 150, 300),
            "An ornate sarcophagus. The lid is slightly ajar.",
            "toggle",
            "Inside: bandaged remains. They move when you look away."
        ))
        self.add_object(InteractiveObject(
            "Canopic Jars", (700, 300, 150, 100),
            "Jars for organs. They're warm to the touch.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Hieroglyphics", (100, 150, 200, 300),
            "Wall hieroglyphics. They tell of a curse.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "THE CURSE", "The Pharaoh")
    
    def draw_details(self, surface):
        # Sarcophagus
        pygame.draw.rect(surface, (180, 150, 80), (400, 200, 150, 300))
        pygame.draw.rect(surface, (200, 170, 100), (410, 210, 130, 150))
        # Hieroglyphics
        pygame.draw.rect(surface, (170, 150, 110), (100, 150, 200, 300))


class MuseumDinosaurHall(Room):
    """Dinosaur hall"""
    
    def __init__(self):
        super().__init__(
            name="dinosaur_hall",
            display_name="Dinosaur Hall",
            connections={"down": "main_hall", "right": "natural_history"},
            base_color=(150, 145, 140),
            description="Massive dinosaur skeletons tower above. They seem to watch you."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Triceratops", (200, 250, 300, 200),
            "A Triceratops skeleton. Its horns gleam menacingly.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Pterodactyl", (600, 100, 250, 150),
            "A suspended Pterodactyl. It sways without wind.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Fossil Display", (900, 300, 150, 150),
            "Fossil fragments. Some don't match any known species.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "EXTINCT", "Nightmare")
    
    def draw_details(self, surface):
        # Triceratops
        pygame.draw.ellipse(surface, (210, 205, 200), (200, 280, 200, 120))
        pygame.draw.polygon(surface, (210, 205, 200), [(200, 340), (150, 320), (200, 300)])


class MuseumArtGallery(Room):
    """Art gallery"""
    
    def __init__(self):
        super().__init__(
            name="art_gallery",
            display_name="Art Gallery",
            connections={"left": "egyptian_exhibit", "down": "storage"},
            base_color=(180, 175, 170),
            description="Classical paintings line the walls. The subjects move when not watched."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Portrait", (300, 200, 150, 200),
            "A Renaissance portrait. The eyes follow you.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Abstract Art", (600, 220, 180, 150),
            "Abstract modern art. Shapes shift when you blink.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Sculpture", (900, 280, 100, 200),
            "A marble sculpture. It moves to new positions.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "MASTERPIECE", "The Artist")
    
    def draw_details(self, surface):
        # Paintings
        pygame.draw.rect(surface, (120, 90, 60), (290, 190, 170, 220))
        pygame.draw.rect(surface, (200, 180, 160), (300, 200, 150, 200))


class MuseumNaturalHistory(Room):
    """Natural history section"""
    
    def __init__(self):
        super().__init__(
            name="natural_history",
            display_name="Natural History",
            connections={"left": "dinosaur_hall", "down": "restoration_lab"},
            base_color=(140, 150, 130),
            description="Taxidermied animals in dioramas. Their glass eyes follow you."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bear Display", (200, 250, 200, 250),
            "A stuffed bear in attack pose. It seems closer each time you look.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Bird Collection", (600, 200, 250, 200),
            "Stuffed birds on branches. Their wings rustle.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Gemstone Display", (900, 300, 150, 150),
            "Precious gems behind glass. One glows with inner light.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "COLLECTION", "The Collector")
    
    def draw_details(self, surface):
        # Bear
        pygame.draw.ellipse(surface, (100, 70, 50), (220, 280, 160, 180))
        pygame.draw.circle(surface, (100, 70, 50), (300, 280), 50)


class MuseumStorage(Room):
    """Museum storage"""
    
    def __init__(self):
        super().__init__(
            name="storage",
            display_name="Storage",
            connections={"up": "art_gallery", "right": "gift_shop"},
            base_color=(80, 75, 70),
            description="Where artifacts are stored. Crates from every era. Some move on their own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Crates", (200, 250, 300, 200),
            "Wooden crates labeled from around the world.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Covered Statues", (600, 200, 200, 300),
            "Statues under sheets. Different positions each time.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Cursed Items Box", (900, 300, 120, 120),
            "A box labeled 'DO NOT DISPLAY - CURSED'.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "CURSED", "The Witch")
    
    def draw_details(self, surface):
        # Crates
        for i in range(4):
            pygame.draw.rect(surface, (100, 80, 60), (200 + i * 70, 280, 65, 60))


class MuseumRestorationLab(Room):
    """Restoration laboratory"""
    
    def __init__(self):
        super().__init__(
            name="restoration_lab",
            display_name="Restoration Lab",
            connections={"up": "natural_history", "right": "security_office"},
            base_color=(180, 180, 185),
            description="Where artifacts are restored. Tools and chemicals. And things being rebuilt."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Work Table", (400, 300, 300, 120),
            "A restoration table. Pieces of something are being reassembled.",
            "zoom",
            "It's a mummy. It's almost complete. It blinks."
        ))
        self.add_object(InteractiveObject(
            "Chemical Cabinet", (800, 200, 100, 250),
            "Preservation chemicals. Some combinations are dangerous.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "UV Light", (200, 280, 80, 100),
            "A UV examination light. It reveals hidden things.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "PRESERVED", "The Mummy")
    
    def draw_details(self, surface):
        # Work table
        pygame.draw.rect(surface, (200, 200, 205), (400, 300, 300, 120))
        # Mummy parts
        pygame.draw.rect(surface, (180, 160, 120), (450, 310, 200, 40))


class MuseumGiftShop(Room):
    """Museum gift shop"""
    
    def __init__(self):
        super().__init__(
            name="gift_shop",
            display_name="Gift Shop",
            connections={"left": "storage"},
            base_color=(150, 140, 130),
            description="The gift shop. Souvenirs and replicas. Some are more authentic than they should be."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Display Shelves", (200, 200, 400, 280),
            "Shelves of souvenirs. Miniature mummies and dinosaurs.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Cash Register", (700, 300, 100, 80),
            "An old cash register. It rings on its own.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Postcards", (900, 280, 100, 150),
            "Postcards of exhibits. One shows you standing in this room.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "TAKE ONE", "The Thief")
    
    def draw_details(self, surface):
        # Shelves
        for i in range(4):
            pygame.draw.rect(surface, (120, 100, 80), (200, 200 + i * 70, 400, 10))


class MuseumSecurityOffice(Room):
    """Security office"""
    
    def __init__(self):
        super().__init__(
            name="security_office",
            display_name="Security Office",
            connections={"left": "restoration_lab", "down": "basement"},
            base_color=(100, 95, 90),
            description="The security office. Monitors show exhibits. And things that shouldn't be moving."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Security Monitors", (400, 200, 300, 200),
            "Banks of monitors showing all exhibits. Something moves on each screen.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Guard's Desk", (800, 300, 150, 100),
            "The guard's desk. Coffee is still warm. Guard is gone.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Key Cabinet", (100, 250, 80, 150),
            "A cabinet of keys to all exhibits. One is missing.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "WATCHING", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Monitors
        for row in range(2):
            for col in range(4):
                pygame.draw.rect(surface, (40, 50, 60), (410 + col * 70, 210 + row * 90, 60, 80))


class MuseumBasement(Room):
    """Museum basement"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Museum Basement",
            connections={"up": "security_office"},
            base_color=(60, 55, 50),
            description="The museum basement. Artifacts deemed too dangerous for display."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Sealed Crates", (200, 250, 250, 200),
            "Crates marked 'CLASSIFIED' and 'DANGER'.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Ritual Circle", (600, 300, 200, 200),
            "A circle drawn on the floor. Candles burn eternally.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Chained Artifact", (900, 280, 100, 150),
            "Something in chains. It moves. It shouldn't.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "FORBIDDEN", "The Curator")
    
    def draw_details(self, surface):
        # Ritual circle
        pygame.draw.circle(surface, (100, 50, 50), (700, 400), 100, 3)


# ===============================================================================
# LIBRARY ROOMS
# ===============================================================================

class LibraryEntranceHall(Room):
    """Library entrance hall"""
    
    def __init__(self):
        super().__init__(
            name="entrance_hall",
            display_name="Library Entrance",
            connections={"right": "main_reading_room", "up": "reference_section"},
            base_color=(100, 90, 75),
            description="The library entrance. The smell of old books is overwhelming."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Card Catalog", (200, 250, 200, 200),
            "An old card catalog. Cards shuffle themselves.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Return Desk", (600, 300, 250, 100),
            "The book return desk. Overdue books pile up.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Library Rules", (900, 200, 100, 150),
            "Rules posted. 'SILENCE' is underlined multiple times.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "SILENCE", "The Librarian")
    
    def draw_details(self, surface):
        # Card catalog
        pygame.draw.rect(surface, (80, 60, 45), (200, 250, 200, 200))
        for row in range(5):
            for col in range(4):
                pygame.draw.rect(surface, (100, 80, 60), (210 + col * 45, 260 + row * 38, 40, 35))


class LibraryMainReadingRoom(Room):
    """Main reading room"""
    
    def __init__(self):
        super().__init__(
            name="main_reading_room",
            display_name="Main Reading Room",
            connections={"left": "entrance_hall", "right": "archives", "up": "study_rooms"},
            base_color=(110, 100, 85),
            description="A vast reading room. Books everywhere. Pages turn on their own."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Reading Tables", (300, 350, 500, 120),
            "Long reading tables with green lamps. Some books are open.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Towering Shelves", (100, 150, 150, 350),
            "Shelves reaching to the ceiling. Ladders roll on tracks.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Librarian's Desk", (900, 300, 150, 100),
            "The head librarian's desk. 'SHHHH' is carved into it.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "OVERDUE", "The Librarian")
    
    def draw_details(self, surface):
        # Tables with lamps
        for i in range(3):
            pygame.draw.rect(surface, (90, 70, 55), (300 + i * 170, 350, 160, 100))
            pygame.draw.ellipse(surface, (100, 180, 100), (360 + i * 170, 340, 40, 20))


class LibraryReferenceSection(Room):
    """Reference section"""
    
    def __init__(self):
        super().__init__(
            name="reference_section",
            display_name="Reference Section",
            connections={"down": "entrance_hall", "right": "rare_books"},
            base_color=(105, 95, 80),
            description="The reference section. Encyclopedias and dictionaries. Knowledge has a price."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Encyclopedia Set", (300, 200, 300, 300),
            "A complete encyclopedia set. Entries change when you're not looking.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Dictionary Stand", (700, 280, 100, 150),
            "A massive dictionary. New words appear that shouldn't exist.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Microfiche Reader", (900, 300, 100, 120),
            "An old microfiche machine. It shows newspapers from the future.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "KNOWLEDGE", "The Scholar")
    
    def draw_details(self, surface):
        # Encyclopedia shelves
        for i in range(8):
            pygame.draw.rect(surface, [(100, 50, 50), (50, 100, 50), (50, 50, 100), (100, 80, 50)][i % 4], 
                           (310 + i * 35, 220, 32, 260))


class LibraryArchives(Room):
    """Archives section"""
    
    def __init__(self):
        super().__init__(
            name="archives",
            display_name="Archives",
            connections={"left": "main_reading_room", "down": "basement_stacks"},
            base_color=(90, 85, 75),
            description="The archives. Historical documents and records. Some are classified forever."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Filing Cabinets", (200, 200, 300, 280),
            "Endless filing cabinets. Some drawers open by themselves.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Microfilm Storage", (600, 280, 200, 150),
            "Rolls of microfilm. Records of things that never happened.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Sealed Records", (900, 250, 120, 180),
            "Records sealed for 100 years. The seal is broken.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "RECORDS", "The Archivist")
    
    def draw_details(self, surface):
        # Filing cabinets
        for i in range(6):
            pygame.draw.rect(surface, (100, 95, 90), (200 + i * 50, 200, 48, 280))


class LibraryRareBooks(Room):
    """Rare books section"""
    
    def __init__(self):
        super().__init__(
            name="rare_books",
            display_name="Rare Books Room",
            connections={"left": "reference_section"},
            base_color=(80, 70, 60),
            description="The rare books room. Protected by glass cases. Some books fight their bindings."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Glass Display Case", (400, 250, 300, 200),
            "A glass case with priceless books. One book vibrates.",
            "zoom",
            "The Necronomicon. Its pages turn on their own. Don't read it."
        ))
        self.add_object(InteractiveObject(
            "Illuminated Manuscripts", (100, 200, 200, 250),
            "Medieval manuscripts. The illustrations move.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Chained Book", (800, 280, 100, 150),
            "A book chained to its pedestal. For good reason.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "FORBIDDEN", "The Witch")
    
    def draw_details(self, surface):
        # Glass case
        pygame.draw.rect(surface, (150, 170, 180), (400, 250, 300, 200))
        pygame.draw.rect(surface, (80, 60, 45), (420, 350, 260, 80))


class LibraryStudyRooms(Room):
    """Private study rooms"""
    
    def __init__(self):
        super().__init__(
            name="study_rooms",
            display_name="Study Rooms",
            connections={"down": "main_reading_room", "right": "librarian_office"},
            base_color=(115, 105, 90),
            description="Private study rooms. Someone is always in the last one. Never leaves."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Study Carrels", (200, 250, 500, 200),
            "Individual study spaces. Some are eternally occupied.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Locked Room", (800, 220, 150, 260),
            "A study room that's always locked. Light underneath the door.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Bulletin Board", (1000, 280, 100, 150),
            "A board with study group postings. Some dates are decades old.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "STUDYING", "The Scholar")
    
    def draw_details(self, surface):
        # Study carrels
        for i in range(4):
            pygame.draw.rect(surface, (100, 80, 65), (200 + i * 125, 280, 120, 150))


class LibraryBasementStacks(Room):
    """Basement book stacks"""
    
    def __init__(self):
        super().__init__(
            name="basement_stacks",
            display_name="Basement Stacks",
            connections={"up": "archives", "right": "restoration_room"},
            base_color=(60, 55, 50),
            description="The basement stacks. Endless rows of books. Easy to get lost forever."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Endless Shelves", (100, 150, 800, 350),
            "Rows and rows of books. They seem to go on forever.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Flickering Light", (640, 100, 60, 60),
            "A dying fluorescent light. It reveals shadows between shelves.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Book Cart", (950, 300, 100, 120),
            "An abandoned book cart. It rolls on its own.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "LOST", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Shelves
        for i in range(10):
            pygame.draw.rect(surface, (70, 55, 45), (100 + i * 80, 150, 75, 350))


class LibraryLibrarianOffice(Room):
    """Librarian's office"""
    
    def __init__(self):
        super().__init__(
            name="librarian_office",
            display_name="Librarian's Office",
            connections={"left": "study_rooms"},
            base_color=(95, 85, 70),
            description="The head librarian's office. Books are her only friends. Dead or alive."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Librarian's Desk", (400, 300, 250, 120),
            "A neat desk. Overdue notices are being written. By no one.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Personal Library", (100, 150, 200, 350),
            "The librarian's personal collection. First editions and rarities.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Typewriter", (700, 320, 100, 80),
            "An old typewriter. It types on its own. 'SHHHH...'",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "QUIET", "The Librarian")
    
    def draw_details(self, surface):
        # Desk
        pygame.draw.rect(surface, (85, 65, 50), (400, 300, 250, 120))
        # Personal library
        pygame.draw.rect(surface, (80, 60, 45), (100, 150, 200, 350))


class LibraryRestorationRoom(Room):
    """Book restoration room"""
    
    def __init__(self):
        super().__init__(
            name="restoration_room",
            display_name="Restoration Room",
            connections={"left": "basement_stacks", "down": "attic"},
            base_color=(140, 130, 115),
            description="Where damaged books are restored. Some books resist being fixed."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Restoration Table", (400, 280, 300, 150),
            "A table with book restoration tools. A book is being rebuilt.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Binding Equipment", (800, 250, 150, 180),
            "Book binding tools. Needles and thread. And something else.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Damaged Books", (100, 300, 200, 150),
            "Stacks of damaged books awaiting restoration.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "REPAIR", "The Archivist")
    
    def draw_details(self, surface):
        # Restoration table
        pygame.draw.rect(surface, (160, 150, 140), (400, 280, 300, 150))


class LibraryAttic(Room):
    """Library attic"""
    
    def __init__(self):
        super().__init__(
            name="attic",
            display_name="Library Attic",
            connections={"up": "restoration_room"},
            base_color=(70, 65, 60),
            description="The library attic. Discarded books and forgotten knowledge."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Forgotten Boxes", (200, 250, 300, 200),
            "Boxes of books deemed unfit for circulation.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Dusty Tomes", (600, 280, 200, 180),
            "Ancient tomes covered in dust. They haven't been read in centuries.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Attic Window", (900, 200, 150, 150),
            "A dirty window. Something watches from outside.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "FORGOTTEN", "Nightmare")
    
    def draw_details(self, surface):
        # Boxes
        for i in range(4):
            pygame.draw.rect(surface, (90, 70, 55), (200 + i * 75, 280, 70, 60))


# ===============================================================================
# ABANDONED ASYLUM ROOMS
# ===============================================================================

class AsylumEntrance(Room):
    """Asylum main entrance"""
    
    def __init__(self):
        super().__init__(
            name="entrance",
            display_name="Asylum Entrance",
            connections={"right": "reception", "up": "ward_a"},
            base_color=(120, 130, 130),
            description="The asylum entrance. 'MENTAL HEALTH FACILITY' is painted over something darker."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Welcome Sign", (200, 200, 150, 100),
            "An old sign welcoming visitors. 'Treatments Available'.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Reception Window", (500, 250, 200, 150),
            "A thick glass window with a speaking slot.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Wheelchair", (800, 350, 100, 120),
            "An old wheelchair. It moves on its own.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "COMMITTED", "The Doctor")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 110, 110), (500, 250, 200, 150))
        pygame.draw.rect(surface, (80, 90, 90), (520, 300, 160, 80))


class AsylumReception(Room):
    """Reception area"""
    
    def __init__(self):
        super().__init__(
            name="reception",
            display_name="Reception",
            connections={"left": "entrance", "right": "therapy_room", "down": "isolation"},
            base_color=(130, 135, 135),
            description="Patient records and intake forms. Some are blank. Some are yours."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Patient Files", (400, 280, 250, 120),
            "Stacks of patient files. Diagnoses that make no sense.",
            "zoom",
            "One file is labeled with your name. Admitted decades ago."
        ))
        self.add_object(InteractiveObject(
            "Intake Forms", (700, 300, 120, 80),
            "Blank intake forms. A pen writes on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Medication Window", (100, 250, 100, 150),
            "A window for dispensing medication. Pills spill out.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "TREATMENT", "The Doctor")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (140, 140, 145), (400, 280, 250, 120))


class AsylumWardA(Room):
    """Ward A - patient rooms"""
    
    def __init__(self):
        super().__init__(
            name="ward_a",
            display_name="Ward A",
            connections={"down": "entrance", "right": "ward_b", "up": "electroshock"},
            base_color=(140, 145, 140),
            description="Patient rooms line the hallway. Screaming from behind closed doors."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Patient Rooms", (200, 200, 600, 250),
            "Padded rooms with small windows. Eyes watch from inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Nurse Station", (850, 280, 150, 150),
            "The nurse's station. Charts track strange experiments.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Straitjacket", (100, 350, 80, 120),
            "A discarded straitjacket. Still warm.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "PATIENT ZERO", "The Plague Doctor")
    
    def draw_details(self, surface):
        for i in range(5):
            pygame.draw.rect(surface, (130, 135, 130), (200 + i * 120, 200, 110, 250))


class AsylumWardB(Room):
    """Ward B - violent patients"""
    
    def __init__(self):
        super().__init__(
            name="ward_b",
            display_name="Ward B (Violent)",
            connections={"left": "ward_a", "down": "morgue"},
            base_color=(120, 120, 125),
            description="The violent ward. Reinforced doors. Blood on the walls."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Reinforced Door", (400, 200, 150, 300),
            "A door with extra locks. Dents from the inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Restraint Chair", (700, 280, 120, 180),
            "A chair with leather restraints. Worn from struggling.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Blood Stains", (200, 400, 150, 80),
            "Old blood stains on the floor. They form words.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "VIOLENT", "Nightmare")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 100, 105), (400, 200, 150, 300))


class AsylumTherapyRoom(Room):
    """Therapy room"""
    
    def __init__(self):
        super().__init__(
            name="therapy_room",
            display_name="Therapy Room",
            connections={"left": "reception", "up": "basement"},
            base_color=(150, 145, 140),
            description="A therapy room. The couch still has an impression of someone lying there."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Therapy Couch", (400, 320, 250, 100),
            "A leather therapy couch. You feel compelled to lie down.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Doctor's Chair", (700, 280, 100, 120),
            "The therapist's chair. Notes are scribbled madly.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Inkblot Tests", (100, 200, 150, 200),
            "Rorschach inkblots. They all look like the same thing.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "DIAGNOSIS", "The Doctor")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (80, 60, 50), (400, 320, 250, 100))


class AsylumIsolation(Room):
    """Isolation cells"""
    
    def __init__(self):
        super().__init__(
            name="isolation",
            display_name="Isolation",
            connections={"up": "reception"},
            base_color=(80, 80, 85),
            description="Isolation cells for the most troubled patients. Padded walls absorb all sound."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Padded Cell", (400, 200, 200, 300),
            "A completely padded room. Scratch marks in the padding.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Food Slot", (600, 350, 50, 30),
            "A tiny slot for food trays. Something looks back.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Observation Window", (700, 250, 100, 100),
            "A one-way mirror. Someone watches from both sides.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "SOLITARY", "Nightmare")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (170, 160, 150), (400, 200, 200, 300))


class AsylumElectroshock(Room):
    """Electroshock therapy room"""
    
    def __init__(self):
        super().__init__(
            name="electroshock",
            display_name="Electroshock Room",
            connections={"down": "ward_a", "right": "hydrotherapy"},
            base_color=(150, 150, 155),
            description="The electroshock room. Leather straps on the table. The machine still hums."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Treatment Table", (400, 280, 250, 150),
            "A table with restraints. The leather is bitten through.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Electroshock Machine", (700, 250, 120, 180),
            "An old ECT machine. Dials spin on their own.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Bite Guard", (200, 350, 60, 30),
            "A rubber bite guard. Teeth marks embedded deep.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "SHOCK", "The Burned Man")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (160, 160, 165), (400, 280, 250, 150))


class AsylumHydrotherapy(Room):
    """Hydrotherapy room"""
    
    def __init__(self):
        super().__init__(
            name="hydrotherapy",
            display_name="Hydrotherapy",
            connections={"left": "electroshock"},
            base_color=(160, 170, 175),
            description="Hydrotherapy room. Ice baths and steam cabinets. Treatment or torture?"
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Ice Bath", (400, 300, 200, 150),
            "A large tub for ice baths. The water is frozen solid.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Steam Cabinet", (700, 250, 120, 200),
            "A steam cabinet. Someone is locked inside.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Pressure Hose", (100, 300, 80, 150),
            "A high-pressure hose for 'treatments'.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "DROWNING", "The Drowned")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (120, 140, 150), (400, 300, 200, 150))


class AsylumMorgue(Room):
    """Asylum morgue"""
    
    def __init__(self):
        super().__init__(
            name="morgue",
            display_name="Morgue",
            connections={"up": "ward_b"},
            base_color=(100, 105, 110),
            description="The asylum morgue. Many patients 'died of natural causes'."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Body Drawers", (200, 200, 300, 280),
            "Steel body drawers. Some are not quite closed.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Autopsy Table", (600, 300, 200, 100),
            "A stainless steel table. Stains that won't wash away.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Death Records", (900, 280, 100, 120),
            "Records of patient deaths. 'Natural causes' on every one.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "EXPERIMENTS", "The Doctor")
    
    def draw_details(self, surface):
        for i in range(4):
            for j in range(2):
                pygame.draw.rect(surface, (130, 135, 140), (210 + i * 70, 210 + j * 130, 65, 120))


class AsylumBasement(Room):
    """Asylum basement"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Basement",
            connections={"down": "therapy_room"},
            base_color=(60, 60, 65),
            description="The asylum basement. Secret experiments. Unmarked graves."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Surgery Table", (400, 280, 250, 120),
            "An operating table down here? Unauthorized procedures.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Chemical Drums", (100, 250, 150, 200),
            "Drums of chemicals. For disposal of... evidence.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Hidden Graves", (800, 350, 200, 100),
            "Disturbed earth. Hasty burials.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "LOBOTOMY", "The Doctor")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (80, 80, 85), (400, 280, 250, 120))


# ===============================================================================
# FARMHOUSE ROOMS
# ===============================================================================

class FarmhouseKitchen(Room):
    """Farmhouse kitchen"""
    
    def __init__(self):
        super().__init__(
            name="kitchen",
            display_name="Kitchen",
            connections={"right": "living_room", "down": "cellar"},
            base_color=(160, 140, 120),
            description="The farmhouse kitchen. Fresh bread smell. But no one's baked in decades."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Wood Stove", (200, 280, 200, 180),
            "An old wood-burning stove. Still warm.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Butcher Block", (500, 320, 150, 80),
            "A butcher's block. Deep cut marks. Some are fresh.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Pantry", (800, 220, 120, 260),
            "A walk-in pantry. Jars of preserved... things.",
            "toggle"
        ))
        self.add_hidden_clue(600, 500, "DINNER TIME", "The Butcher")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 80, 60), (200, 280, 200, 180))


class FarmhouseLivingRoom(Room):
    """Farmhouse living room"""
    
    def __init__(self):
        super().__init__(
            name="living_room",
            display_name="Living Room",
            connections={"left": "kitchen", "up": "bedroom", "right": "porch"},
            base_color=(150, 135, 115),
            description="A cozy living room. Family photos watch you. They're all facing away."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Rocking Chair", (300, 320, 100, 130),
            "An old rocking chair. It rocks on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Family Photos", (500, 180, 200, 150),
            "Photos of the family. Their faces are scratched out.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Fireplace", (800, 220, 200, 200),
            "A stone fireplace. Something burns even with no wood.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "FAMILY", "The Servant")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (80, 60, 50), (800, 220, 200, 200))


class FarmhouseBedroom(Room):
    """Farmhouse master bedroom"""
    
    def __init__(self):
        super().__init__(
            name="bedroom",
            display_name="Master Bedroom",
            connections={"down": "living_room", "right": "childrens_room"},
            base_color=(140, 125, 105),
            description="The master bedroom. The bed is made perfectly. Too perfectly."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Four-Poster Bed", (400, 260, 300, 200),
            "An antique bed. Someone is under the covers.",
            "zoom",
            "You pull back the covers. Nothing. But it's still warm."
        ))
        self.add_object(InteractiveObject(
            "Wardrobe", (100, 200, 120, 280),
            "A large wardrobe. Clothes from another era.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Vanity Mirror", (800, 250, 120, 180),
            "A vanity mirror. Your reflection is wearing different clothes.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "REST", "Nightmare")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (80, 55, 40), (400, 260, 300, 200))


class FarmhouseChildrensRoom(Room):
    """Children's room"""
    
    def __init__(self):
        super().__init__(
            name="childrens_room",
            display_name="Children's Room",
            connections={"left": "bedroom"},
            base_color=(150, 140, 130),
            description="A child's room. Toys are scattered about. Playing sounds echo."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Toy Chest", (300, 320, 180, 100),
            "A wooden toy chest. Toys move inside.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Rocking Horse", (600, 280, 120, 150),
            "A rocking horse. It rocks as you watch.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Child's Drawing", (850, 200, 100, 150),
            "Crayon drawings on the wall. A happy family... and something else.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "PLAYTIME", "Little Timmy")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 70, 50), (300, 320, 180, 100))


class FarmhouseBarn(Room):
    """The barn"""
    
    def __init__(self):
        super().__init__(
            name="barn",
            display_name="Barn",
            connections={"left": "porch", "up": "hayloft"},
            base_color=(120, 90, 70),
            description="The barn. Empty stalls. The smell of animals long gone."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Horse Stalls", (200, 220, 400, 250),
            "Empty stalls. Hay still fresh. Hoofprints in the dust.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Farm Tools", (700, 250, 150, 200),
            "Pitchforks and scythes. Some are stained.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Tractor", (900, 300, 150, 150),
            "An old tractor. Engine still warm.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "HARVEST", "The Scarecrow")
    
    def draw_details(self, surface):
        for i in range(4):
            pygame.draw.rect(surface, (100, 75, 55), (200 + i * 100, 220, 95, 250))


class FarmhouseHayloft(Room):
    """Barn hayloft"""
    
    def __init__(self):
        super().__init__(
            name="hayloft",
            display_name="Hayloft",
            connections={"down": "barn"},
            base_color=(130, 100, 75),
            description="The hayloft above the barn. Hay bales and darkness. Something hides here."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Hay Bales", (300, 280, 400, 180),
            "Stacked hay bales. Something moves behind them.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Rope", (800, 200, 50, 250),
            "A rope hanging from the rafters. Tied in a noose.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Barn Window", (100, 220, 120, 150),
            "A window overlooking the fields. A figure stands in the corn.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "HANGING", "The Hanged Man")
    
    def draw_details(self, surface):
        for i in range(3):
            pygame.draw.rect(surface, (180, 150, 80), (300 + i * 130, 300, 120, 80))


class FarmhouseCellar(Room):
    """Farm cellar"""
    
    def __init__(self):
        super().__init__(
            name="cellar",
            display_name="Root Cellar",
            connections={"up": "kitchen"},
            base_color=(70, 65, 60),
            description="The root cellar. Preserved vegetables. And other preserved things."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Preserve Jars", (200, 200, 300, 250),
            "Jars of preserved vegetables. One contains something else.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Wine Barrels", (600, 280, 200, 180),
            "Old wine barrels. The wine is thick and dark.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Root Vegetables", (900, 300, 120, 150),
            "Bins of root vegetables. Some have faces.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "BURIED", None)
    
    def draw_details(self, surface):
        for i in range(8):
            pygame.draw.rect(surface, (150, 100, 50), (210 + i * 35, 220, 30, 50))


class FarmhousePorch(Room):
    """Front porch"""
    
    def __init__(self):
        super().__init__(
            name="porch",
            display_name="Front Porch",
            connections={"left": "living_room", "right": "barn", "down": "cornfield"},
            base_color=(100, 90, 80),
            description="The front porch. A swing sways in no wind. Fields stretch endlessly."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Porch Swing", (400, 300, 200, 80),
            "A wooden porch swing. Moving on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Wind Chimes", (700, 150, 50, 150),
            "Wind chimes that play a discordant melody.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Welcome Mat", (500, 450, 100, 40),
            "A welcome mat. Muddy footprints lead inside.",
            "examine"
        ))
        self.add_hidden_clue(600, 400, "VISITOR", None)
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (60, 80, 60), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
        pygame.draw.rect(surface, (80, 70, 60), (0, int(SCREEN_HEIGHT * 0.4), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (90, 70, 55), (400, 300, 200, 80))


class FarmhouseCornfield(Room):
    """The cornfield"""
    
    def __init__(self):
        super().__init__(
            name="cornfield",
            display_name="Cornfield",
            connections={"up": "porch", "right": "scarecrow_hill"},
            base_color=(60, 80, 50),
            description="Endless rows of dead corn. Something walks between the stalks."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Corn Rows", (200, 150, 800, 400),
            "Rows of dead corn stalks. Rustling without wind.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Crow", (600, 200, 80, 60),
            "A crow watches you. It doesn't move. Ever.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Trail", (500, 400, 100, 150),
            "A path through the corn. Footprints go in. None come out.",
            "examine"
        ))
        self.add_hidden_clue(700, 300, "CHILDREN", "Little Timmy")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (40, 50, 60), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (50, 70, 40), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        for i in range(20):
            x = 200 + i * 50
            pygame.draw.line(surface, (120, 100, 60), (x, 200), (x, 550), 3)


class FarmhouseScarecrowHill(Room):
    """Scarecrow hill"""
    
    def __init__(self):
        super().__init__(
            name="scarecrow_hill",
            display_name="Scarecrow Hill",
            connections={"left": "cornfield"},
            base_color=(50, 60, 50),
            description="A hill overlooking the farm. The scarecrow watches everything."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Scarecrow", (500, 150, 100, 350),
            "The scarecrow. It's in a different position each time you look.",
            "zoom",
            "Up close, the face is too detailed. Too human. It blinks."
        ))
        self.add_object(InteractiveObject(
            "Cross", (600, 200, 20, 250),
            "The wooden cross holding the scarecrow. Stained with something.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Crows", (200, 200, 200, 100),
            "A murder of crows. They spell out words.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "GUARDIAN", "The Scarecrow")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (30, 40, 50), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))
        pygame.draw.ellipse(surface, (60, 70, 55), (200, int(SCREEN_HEIGHT * 0.3), 800, 400))
    
    def draw_details(self, surface):
        # Cross
        pygame.draw.rect(surface, (90, 70, 55), (540, 200, 20, 300))
        pygame.draw.rect(surface, (90, 70, 55), (480, 250, 140, 15))
        # Scarecrow body
        pygame.draw.circle(surface, (120, 100, 80), (550, 290), 30)


# ===============================================================================
# TRAIN STATION ROOMS
# ===============================================================================

class TrainStationPlatform(Room):
    """Main platform"""
    
    def __init__(self):
        super().__init__(
            name="platform",
            display_name="Platform",
            connections={"right": "ticket_office", "up": "waiting_room"},
            base_color=(100, 95, 90),
            description="Platform 1. A train that never arrives. Passengers that never leave."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Train Tracks", (0, 500, SCREEN_WIDTH, 100),
            "Empty tracks stretching into fog. Distant whistle sounds.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Platform Bench", (400, 350, 200, 80),
            "A waiting bench. A suitcase sits abandoned.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Schedule Board", (700, 200, 150, 200),
            "Arrival and departure times. All show the same date.",
            "zoom"
        ))
        self.add_hidden_clue(500, 450, "ARRIVING", "The Conductor")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (60, 70, 80), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (90, 85, 80), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, 280))
        pygame.draw.rect(surface, (70, 65, 60), (0, int(SCREEN_HEIGHT * 0.7), SCREEN_WIDTH, 150))
    
    def draw_details(self, surface):
        # Tracks
        pygame.draw.rect(surface, (60, 55, 50), (0, 520, SCREEN_WIDTH, 10))
        pygame.draw.rect(surface, (60, 55, 50), (0, 560, SCREEN_WIDTH, 10))


class TrainStationTicketOffice(Room):
    """Ticket office"""
    
    def __init__(self):
        super().__init__(
            name="ticket_office",
            display_name="Ticket Office",
            connections={"left": "platform", "right": "baggage_claim"},
            base_color=(130, 120, 100),
            description="The ticket office. Buy a ticket to anywhere. You'll never leave."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Ticket Window", (400, 250, 200, 200),
            "The ticket window. Someone sits behind the glass.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Ticket Machine", (700, 280, 100, 180),
            "An old ticket machine. It prints tickets for destinations that don't exist.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Schedule Poster", (100, 200, 150, 200),
            "A poster of train schedules. All trains are 'DELAYED'.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "ONE WAY", "The Conductor")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (150, 140, 120), (400, 250, 200, 200))
        pygame.draw.rect(surface, (100, 110, 120), (420, 270, 160, 100))


class TrainStationWaitingRoom(Room):
    """Main waiting room"""
    
    def __init__(self):
        super().__init__(
            name="waiting_room",
            display_name="Waiting Room",
            connections={"down": "platform", "right": "restaurant", "up": "office"},
            base_color=(140, 130, 115),
            description="A grand waiting room. Passengers sit frozen in time. Waiting forever."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Waiting Benches", (200, 350, 500, 120),
            "Rows of wooden benches. Some have luggage that's never claimed.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Clock", (600, 120, 100, 100),
            "A grand clock. The hands move backward.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Newspaper Stand", (900, 280, 100, 180),
            "Old newspapers. Headlines from different decades.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "DELAYED", "The Waiting Woman")
    
    def draw_details(self, surface):
        for i in range(4):
            pygame.draw.rect(surface, (100, 80, 60), (200 + i * 130, 380, 120, 60))


class TrainStationRestaurant(Room):
    """Station restaurant"""
    
    def __init__(self):
        super().__init__(
            name="restaurant",
            display_name="Station Restaurant",
            connections={"left": "waiting_room"},
            base_color=(150, 135, 120),
            description="The station restaurant. Meals served cold. The diners never eat."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dining Tables", (300, 320, 400, 150),
            "Tables set for dinner. Food grows cold eternally.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Counter", (800, 280, 200, 100),
            "The lunch counter. Stools spin on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Menu Board", (100, 200, 150, 200),
            "Today's specials from decades ago.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "ORDER UP", "The Chef")
    
    def draw_details(self, surface):
        for i in range(3):
            pygame.draw.ellipse(surface, (160, 150, 140), (300 + i * 140, 340, 120, 80))


class TrainStationBaggageClaim(Room):
    """Baggage claim area"""
    
    def __init__(self):
        super().__init__(
            name="baggage_claim",
            display_name="Baggage Claim",
            connections={"left": "ticket_office", "down": "tunnel"},
            base_color=(110, 105, 100),
            description="The baggage claim. Suitcases from trips never completed."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Baggage Carousel", (300, 300, 400, 150),
            "A carousel of unclaimed luggage. Your bag is there.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Lost & Found", (800, 250, 150, 200),
            "A cage of lost items. Some belonged to the missing.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Locker Room", (100, 280, 120, 180),
            "Storage lockers. One has been locked for 50 years.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "LOST", "The Hobo")
    
    def draw_details(self, surface):
        pygame.draw.ellipse(surface, (90, 85, 80), (300, 320, 400, 100))


class TrainStationTunnel(Room):
    """Underground tunnel"""
    
    def __init__(self):
        super().__init__(
            name="tunnel",
            display_name="Pedestrian Tunnel",
            connections={"up": "baggage_claim", "right": "platform_2"},
            base_color=(70, 70, 75),
            description="The tunnel between platforms. Footsteps echo that aren't yours."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Tunnel Walls", (0, 150, SCREEN_WIDTH, 350),
            "Tiled walls covered in old advertisements.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Flickering Light", (640, 100, 60, 60),
            "A dying light. Shadows move in the dark patches.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Busker Spot", (400, 350, 100, 80),
            "A spot where musicians played. An instrument case remains.",
            "examine"
        ))
        self.add_hidden_clue(600, 450, "PASSAGE", "Shadow Stalker")
    
    def draw_details(self, surface):
        # Tiles
        for y in range(150, 500, 30):
            for x in range(0, SCREEN_WIDTH, 30):
                pygame.draw.rect(surface, (80, 80, 85), (x, y, 28, 28))


class TrainStationPlatform2(Room):
    """Second platform"""
    
    def __init__(self):
        super().__init__(
            name="platform_2",
            display_name="Platform 2",
            connections={"left": "tunnel", "up": "freight_yard"},
            base_color=(95, 90, 85),
            description="Platform 2. For trains that were cancelled. Permanently."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Abandoned Train", (200, 200, 600, 300),
            "An abandoned train car. Passengers still inside.",
            "zoom",
            "Through foggy windows, figures sit motionless. They turn to look."
        ))
        self.add_object(InteractiveObject(
            "Platform Clock", (900, 200, 100, 100),
            "A broken clock. Stopped at 11:59.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Warning Sign", (100, 300, 80, 120),
            "'DANGER - DO NOT BOARD' - The paint is fresh.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "FINAL STOP", "The Conductor")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (60, 60, 65), (200, 250, 600, 200))
        for i in range(6):
            pygame.draw.rect(surface, (100, 110, 120), (220 + i * 95, 280, 80, 60))


class TrainStationOffice(Room):
    """Station master's office"""
    
    def __init__(self):
        super().__init__(
            name="office",
            display_name="Station Master's Office",
            connections={"down": "waiting_room"},
            base_color=(120, 110, 95),
            description="The station master's office. Schedules and incident reports."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Master's Desk", (400, 300, 250, 120),
            "The station master's desk. A schedule is being written.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Telegraph", (700, 280, 80, 100),
            "An old telegraph. It clicks on its own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Incident Reports", (100, 200, 150, 250),
            "Reports of accidents. Many have the same date.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "DERAILED", None)
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (90, 70, 55), (400, 300, 250, 120))


class TrainStationFreightYard(Room):
    """Freight yard"""
    
    def __init__(self):
        super().__init__(
            name="freight_yard",
            display_name="Freight Yard",
            connections={"down": "platform_2", "right": "maintenance"},
            base_color=(80, 75, 70),
            description="The freight yard. Old cargo cars rust. Workers that never left."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Cargo Cars", (200, 250, 400, 200),
            "Rusted cargo cars. Some are sealed. Some should stay that way.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Loading Dock", (700, 320, 200, 100),
            "A loading dock. Crates that were never shipped.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Water Tower", (950, 150, 100, 300),
            "An old water tower. Dripping endlessly.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "CARGO", "The Hobo")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (50, 60, 70), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (60, 55, 50), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (70, 60, 55), (200, 280, 400, 150))


class TrainStationMaintenance(Room):
    """Maintenance shed"""
    
    def __init__(self):
        super().__init__(
            name="maintenance",
            display_name="Maintenance Shed",
            connections={"left": "freight_yard"},
            base_color=(90, 85, 80),
            description="Where trains were repaired. Tools and oil. And things left behind."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Tool Wall", (100, 200, 200, 280),
            "Tools for train maintenance. Some are covered in rust.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Engine Parts", (500, 280, 250, 180),
            "Disassembled engine parts. Something is being rebuilt.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Oil Drums", (850, 300, 150, 150),
            "Drums of locomotive oil. One leaks something red.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "REPAIR", None)
    
    def draw_details(self, surface):
        # Tools
        for i in range(8):
            pygame.draw.rect(surface, (120, 100, 80), (110 + i * 22, 220, 18, 240))


# ===============================================================================
# MALL ROOMS
# ===============================================================================

class MallMainEntrance(Room):
    """Mall main entrance"""
    
    def __init__(self):
        super().__init__(
            name="main_entrance",
            display_name="Mall Entrance",
            connections={"right": "food_court", "up": "department_store"},
            base_color=(180, 175, 170),
            description="The mall entrance after hours. Escalators run endlessly to nowhere."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Escalators", (400, 200, 200, 300),
            "Escalators running up and down. With no one on them.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Directory", (700, 280, 120, 200),
            "A mall directory. Some stores aren't listed. They still exist.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Fountain", (150, 320, 200, 150),
            "A decorative fountain. Coins from wishes that never came true.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "AFTER HOURS", "The Mannequin")
    
    def draw_details(self, surface):
        # Escalators
        pygame.draw.rect(surface, (150, 150, 155), (400, 200, 200, 300))
        for i in range(10):
            pygame.draw.rect(surface, (170, 170, 175), (410, 210 + i * 28, 180, 25))


class MallFoodCourt(Room):
    """Food court"""
    
    def __init__(self):
        super().__init__(
            name="food_court",
            display_name="Food Court",
            connections={"left": "main_entrance", "right": "clothing_store"},
            base_color=(170, 165, 160),
            description="The food court. Empty restaurants. Food still cooking."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Food Stalls", (200, 200, 500, 200),
            "Abandoned food stalls. Orders never picked up.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Tables", (300, 400, 400, 100),
            "Dining tables with half-eaten meals. Still warm.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Trash Compactor", (800, 300, 120, 180),
            "A large trash compactor. Something moves inside.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "HUNGRY", "The Chef")
    
    def draw_details(self, surface):
        for i in range(4):
            pygame.draw.rect(surface, (160, 155, 150), (200 + i * 125, 220, 120, 160))


class MallDepartmentStore(Room):
    """Department store"""
    
    def __init__(self):
        super().__init__(
            name="department_store",
            display_name="Department Store",
            connections={"down": "main_entrance", "right": "electronics"},
            base_color=(190, 185, 180),
            description="A huge department store. Mannequins pose in impossible positions."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Mannequins", (300, 200, 400, 300),
            "Mannequins modeling clothes. They move when you don't look.",
            "zoom",
            "One mannequin has your face. It's wearing tomorrow's clothes."
        ))
        self.add_object(InteractiveObject(
            "Clothing Racks", (800, 280, 200, 180),
            "Racks of clothing. Sizes that fit no human body.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Perfume Counter", (100, 300, 150, 120),
            "A perfume counter. Scents that trigger impossible memories.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "FITTING", "The Mannequin")
    
    def draw_details(self, surface):
        for i in range(4):
            pygame.draw.ellipse(surface, (180, 160, 140), (320 + i * 80, 350, 40, 120))
            pygame.draw.circle(surface, (200, 180, 160), (340 + i * 80, 330), 25)


class MallClothingStore(Room):
    """Clothing store"""
    
    def __init__(self):
        super().__init__(
            name="clothing_store",
            display_name="Clothing Store",
            connections={"left": "food_court", "up": "toy_store"},
            base_color=(185, 180, 175),
            description="A trendy clothing store. Fitting rooms with no reflection."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Fitting Rooms", (700, 200, 200, 280),
            "Fitting room curtains. Someone is always in there.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Mirror Wall", (100, 200, 200, 300),
            "Full-length mirrors. Your reflection wears different clothes.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Sale Rack", (400, 350, 200, 100),
            "Sale items. Clothes from decades past.",
            "examine"
        ))
        self.add_hidden_clue(600, 550, "TRY ME", "The Mimic")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (160, 170, 180), (100, 200, 200, 300))


class MallElectronics(Room):
    """Electronics store"""
    
    def __init__(self):
        super().__init__(
            name="electronics",
            display_name="Electronics Store",
            connections={"left": "department_store", "right": "movie_theater"},
            base_color=(160, 165, 170),
            description="An electronics store. TVs all show the same channel. Static."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "TV Wall", (300, 200, 400, 250),
            "A wall of televisions. They all show your face.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Computers", (800, 280, 150, 150),
            "Display computers. They're running programs on their own.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Audio Equipment", (100, 300, 150, 150),
            "Speakers playing music. The same song for decades.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "WATCHING", "Shadow Stalker")
    
    def draw_details(self, surface):
        for row in range(2):
            for col in range(4):
                pygame.draw.rect(surface, (50, 50, 55), (310 + col * 95, 210 + row * 120, 85, 100))


class MallToyStore(Room):
    """Toy store"""
    
    def __init__(self):
        super().__init__(
            name="toy_store",
            display_name="Toy Store",
            connections={"down": "clothing_store", "right": "storage"},
            base_color=(200, 180, 180),
            description="A toy store. Dolls blink. Toy soldiers march. Jack-in-boxes pop open."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Doll Aisle", (200, 200, 250, 280),
            "Shelves of dolls. They all face you.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Toy Train", (600, 350, 200, 100),
            "A display train running on tracks. It whistles a warning.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Stuffed Animals", (900, 280, 120, 180),
            "Stuffed animals with knowing eyes.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "PLAYTIME", "The Doll")
    
    def draw_details(self, surface):
        for i in range(6):
            for j in range(4):
                pygame.draw.circle(surface, (255, 200, 200), (230 + i * 40, 230 + j * 65), 15)


class MallMovieTheater(Room):
    """Movie theater"""
    
    def __init__(self):
        super().__init__(
            name="movie_theater",
            display_name="Movie Theater",
            connections={"left": "electronics", "down": "parking_garage"},
            base_color=(80, 50, 50),
            description="The mall theater. Old movies play on loop. The audience never leaves."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Movie Screen", (300, 150, 500, 280),
            "A massive screen. Playing a film that was never released.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Theater Seats", (250, 450, 600, 100),
            "Rows of seats. Some are occupied by shadows.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Popcorn Machine", (900, 280, 100, 180),
            "A popcorn machine. Producing popcorn endlessly.",
            "examine"
        ))
        self.add_hidden_clue(550, 380, "FINAL SHOWING", "The Artist")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, WHITE, (300, 150, 500, 280))
        for row in range(2):
            for col in range(10):
                pygame.draw.rect(surface, (100, 50, 50), (270 + col * 60, 460 + row * 40, 50, 35))


class MallParkingGarage(Room):
    """Underground parking garage"""
    
    def __init__(self):
        super().__init__(
            name="parking_garage",
            display_name="Parking Garage",
            connections={"up": "movie_theater", "right": "security_office"},
            base_color=(80, 80, 85),
            description="Underground parking. Cars from owners who never returned."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Parked Cars", (200, 300, 500, 150),
            "Rows of abandoned cars. Keys still in ignitions.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Elevator", (800, 250, 100, 200),
            "An elevator that goes to floors that don't exist.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Exit Sign", (100, 200, 100, 50),
            "An exit sign. It leads deeper in.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "NO EXIT", "Shadow Stalker")
    
    def draw_details(self, surface):
        for i in range(4):
            pygame.draw.rect(surface, [(150, 50, 50), (50, 50, 150), (50, 150, 50), (150, 150, 50)][i], 
                           (200 + i * 130, 320, 120, 100))


class MallSecurityOffice(Room):
    """Security office"""
    
    def __init__(self):
        super().__init__(
            name="security_office",
            display_name="Security Office",
            connections={"left": "parking_garage", "up": "storage"},
            base_color=(100, 100, 105),
            description="Mall security. Monitors show empty stores. But the counters say otherwise."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Security Monitors", (400, 200, 300, 200),
            "Screens showing every store. Figures move in empty aisles.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Lost Child Board", (800, 280, 120, 180),
            "Photos of lost children. Dates span decades.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Guard's Log", (100, 300, 120, 80),
            "The security log. Last entry was mid-sentence.",
            "examine"
        ))
        self.add_hidden_clue(550, 550, "MISSING", "The Thief")
    
    def draw_details(self, surface):
        for row in range(2):
            for col in range(3):
                pygame.draw.rect(surface, (50, 60, 70), (410 + col * 95, 210 + row * 95, 85, 85))


class MallStorage(Room):
    """Storage and loading area"""
    
    def __init__(self):
        super().__init__(
            name="storage",
            display_name="Storage Area",
            connections={"down": "security_office", "left": "toy_store"},
            base_color=(90, 85, 80),
            description="Mall storage. Boxes of merchandise never sold. And things better left boxed."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stacked Boxes", (200, 200, 350, 300),
            "Towers of boxes. Some are moving.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Loading Dock", (700, 320, 200, 100),
            "A loading dock. Trucks that never left.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Mannequin Parts", (950, 250, 100, 200),
            "Boxes of mannequin parts. Arms and heads. Staring.",
            "zoom"
        ))
        self.add_hidden_clue(500, 550, "MERCHANDISE", "The Mannequin")
    
    def draw_details(self, surface):
        for i in range(5):
            for j in range(3):
                pygame.draw.rect(surface, (120, 100, 80), (200 + i * 70, 280 - j * 60, 65, 55))


# ===============================================================================
# VICTORIAN MANSION ROOMS
# ===============================================================================

class MansionFoyer(Room):
    """Mansion foyer"""
    
    def __init__(self):
        super().__init__(
            name="foyer",
            display_name="Grand Foyer",
            connections={"right": "dining_room", "up": "gallery"},
            base_color=(140, 110, 100),
            description="A grand foyer with dual staircases. Portraits watch from above."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Grand Staircase", (400, 150, 400, 350),
            "Twin staircases curving upward. Footsteps echo from above.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Crystal Chandelier", (580, 50, 120, 120),
            "A massive crystal chandelier. It sways without wind.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Coat Rack", (100, 280, 80, 200),
            "An antique coat rack. Coats from guests long dead.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "WELCOME", "The Servant")
    
    def draw_details(self, surface):
        # Stairs
        for i in range(8):
            pygame.draw.rect(surface, (120, 90, 80), (400 + i * 15, 450 - i * 35, 200 - i * 10, 25))


class MansionDiningRoom(Room):
    """Formal dining room"""
    
    def __init__(self):
        super().__init__(
            name="dining_room",
            display_name="Dining Room",
            connections={"left": "foyer", "down": "kitchen", "right": "ballroom"},
            base_color=(130, 100, 90),
            description="A formal dining room. Places are set for a dinner that ended badly."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dining Table", (300, 280, 500, 180),
            "A long mahogany table. Plates of rotting food.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "China Cabinet", (900, 220, 120, 260),
            "Fine china. Some plates are cracked. Some are bloody.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Candelabra", (550, 250, 100, 80),
            "Silver candelabras. Candles burn but never melt.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "DINNER PARTY", "The Collector")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 70, 60), (300, 280, 500, 180))


class MansionBallroom(Room):
    """Grand ballroom"""
    
    def __init__(self):
        super().__init__(
            name="ballroom",
            display_name="Ballroom",
            connections={"left": "dining_room", "up": "master_suite"},
            base_color=(150, 120, 110),
            description="The grand ballroom. Ghostly music plays. Dancers twirl in moonlight."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dance Floor", (250, 300, 600, 250),
            "A polished floor. Footprints appear and fade.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Grand Piano", (900, 300, 150, 150),
            "A grand piano playing itself. A waltz from 1889.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Wall Mirrors", (100, 180, 100, 300),
            "Floor-to-ceiling mirrors. Dancers reflect but you don't.",
            "zoom"
        ))
        self.add_hidden_clue(550, 550, "MAY I DANCE", "Ethereal Bride")
    
    def draw_details(self, surface):
        # Checkered floor
        for y in range(300, 550, 50):
            for x in range(250, 850, 50):
                color = (180, 150, 140) if (x + y) % 100 == 0 else (160, 130, 120)
                pygame.draw.rect(surface, color, (x, y, 48, 48))


class MansionGallery(Room):
    """Art gallery"""
    
    def __init__(self):
        super().__init__(
            name="gallery",
            display_name="Portrait Gallery",
            connections={"down": "foyer", "right": "library"},
            base_color=(120, 105, 95),
            description="Family portraits line the walls. Their eyes follow. Their expressions change."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Family Portraits", (200, 150, 700, 250),
            "Generations of the family. All died tragically.",
            "zoom",
            "The newest portrait is blank. But you see yourself forming."
        ))
        self.add_object(InteractiveObject(
            "Sculpture", (950, 300, 80, 180),
            "A marble bust. It whispers when you're not looking.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Velvet Rope", (100, 400, 200, 30),
            "Velvet ropes blocking off a section. What are they hiding?",
            "examine"
        ))
        self.add_hidden_clue(500, 450, "BLOODLINE", "The Collector")
    
    def draw_details(self, surface):
        # Portraits
        for i in range(5):
            pygame.draw.rect(surface, (80, 60, 50), (220 + i * 130, 160, 110, 160))


class MansionLibrary(Room):
    """Private library"""
    
    def __init__(self):
        super().__init__(
            name="library",
            display_name="Library",
            connections={"left": "gallery", "down": "study"},
            base_color=(100, 85, 70),
            description="A vast private library. Knowledge and dark secrets on every shelf."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bookshelves", (100, 150, 300, 350),
            "Ceiling-high bookshelves. Some books are bound in leather. Some in other things.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Reading Chair", (600, 320, 150, 130),
            "A leather reading chair. Still warm. Book left open.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Globe", (850, 300, 100, 150),
            "An antique globe. It shows countries that don't exist.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "KNOWLEDGE", "The Librarian")
    
    def draw_details(self, surface):
        # Bookshelves
        for i in range(10):
            pygame.draw.rect(surface, (80, 50, 35), (110 + i * 28, 180, 25, 300))


class MansionKitchen(Room):
    """Mansion kitchen"""
    
    def __init__(self):
        super().__init__(
            name="kitchen",
            display_name="Kitchen",
            connections={"up": "dining_room", "right": "servants_quarters"},
            base_color=(150, 145, 140),
            description="A grand kitchen. Meals for the master. Poison for the unwanted."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Cast Iron Stove", (300, 250, 250, 200),
            "A massive stove. Something simmers eternally.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Knife Block", (700, 300, 80, 100),
            "A block of knives. One is missing. Always.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Pantry Door", (100, 220, 120, 260),
            "The pantry. Preserved foods from decades past.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "SPECIAL INGREDIENT", "The Butcher")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (60, 60, 65), (300, 250, 250, 200))


class MansionServants(Room):
    """Servants quarters"""
    
    def __init__(self):
        super().__init__(
            name="servants_quarters",
            display_name="Servants' Quarters",
            connections={"left": "kitchen"},
            base_color=(110, 105, 100),
            description="Where the servants lived. Small rooms. Big secrets."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Servant Beds", (200, 280, 300, 180),
            "Narrow beds for servants. Some never left.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Service Bell", (700, 250, 60, 60),
            "A bell that still rings, summoning no one.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Hidden Diary", (900, 350, 80, 60),
            "A servant's diary. Secrets of the master's crimes.",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "OBEY", "The Servant")
    
    def draw_details(self, surface):
        for i in range(3):
            pygame.draw.rect(surface, (80, 65, 55), (200 + i * 100, 300, 90, 140))


class MansionStudy(Room):
    """Master's study"""
    
    def __init__(self):
        super().__init__(
            name="study",
            display_name="Study",
            connections={"up": "library", "right": "conservatory"},
            base_color=(90, 75, 65),
            description="The master's private study. Business deals and dark rituals."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Mahogany Desk", (400, 300, 280, 150),
            "A massive desk. Contracts signed in unusual ink.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Safe", (800, 280, 100, 150),
            "A wall safe. What could be worth hiding here?",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Fireplace", (100, 220, 180, 200),
            "A fireplace with ashes. Papers recently burned.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "INHERITANCE", "The Collector")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (70, 55, 45), (400, 300, 280, 150))


class MansionConservatory(Room):
    """Glass conservatory"""
    
    def __init__(self):
        super().__init__(
            name="conservatory",
            display_name="Conservatory",
            connections={"left": "study", "down": "garden"},
            base_color=(120, 140, 120),
            description="A glass conservatory. Dead plants that still grow. Flowers that bloom at midnight."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Dead Plants", (300, 250, 400, 250),
            "Withered plants in ornate pots. They reach toward you.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Glass Ceiling", (200, 100, 800, 100),
            "A glass ceiling showing the sky. Even during the day, it's night.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Fountain", (850, 320, 120, 150),
            "A small fountain. The water runs black.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "GROWTH", "The Gardener")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (200, 220, 230), (200, 100, 800, 100))


class MansionGarden(Room):
    """Mansion garden"""
    
    def __init__(self):
        super().__init__(
            name="garden",
            display_name="Garden",
            connections={"up": "conservatory", "right": "maze"},
            base_color=(50, 70, 50),
            description="The mansion gardens. Overgrown and wild. Statues hide among the hedges."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Rose Garden", (300, 280, 300, 200),
            "Red roses. They smell like blood.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Stone Angel", (750, 250, 100, 220),
            "A weeping angel statue. It moves when you blink.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Garden Bench", (100, 380, 150, 80),
            "An old bench. A forgotten doll sits there.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "BURIED", "The Gardener")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (30, 40, 50), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (40, 60, 40), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        # Hedges
        for i in range(4):
            pygame.draw.ellipse(surface, (30, 50, 30), (100 + i * 200, 400, 150, 80))


class MansionMaze(Room):
    """Hedge maze"""
    
    def __init__(self):
        super().__init__(
            name="maze",
            display_name="Hedge Maze",
            connections={"left": "garden"},
            base_color=(40, 55, 40),
            description="An impossible maze. Those who enter rarely leave. Those who leave are changed."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Hedge Walls", (100, 150, 800, 350),
            "Towering hedges that seem to move. The path changes.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Center Fountain", (500, 300, 150, 150),
            "The maze center. A fountain with dark water.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Skeleton", (900, 350, 80, 120),
            "Someone who never found the exit.",
            "examine"
        ))
        self.add_hidden_clue(600, 450, "LOST FOREVER", "Nightmare")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (20, 30, 40), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (30, 45, 30), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        # Maze walls
        pygame.draw.rect(surface, (25, 40, 25), (200, 200, 50, 300))
        pygame.draw.rect(surface, (25, 40, 25), (400, 150, 50, 250))
        pygame.draw.rect(surface, (25, 40, 25), (600, 250, 50, 300))


class MansionMasterSuite(Room):
    """Master bedroom suite"""
    
    def __init__(self):
        super().__init__(
            name="master_suite",
            display_name="Master Suite",
            connections={"down": "ballroom"},
            base_color=(100, 70, 70),
            description="The master's bedroom. A bed where many died. The canopy still moves."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Four-Poster Bed", (350, 250, 350, 250),
            "A massive canopy bed. Sheets stained with history.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Vanity", (800, 280, 150, 150),
            "A lady's vanity. The mirror shows a different time.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Jewelry Box", (900, 300, 60, 40),
            "A music box. It plays a lullaby for the dead.",
            "toggle"
        ))
        self.add_hidden_clue(525, 500, "BRIDE", "Ethereal Bride")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (80, 50, 50), (350, 250, 350, 250))
        pygame.draw.rect(surface, (60, 35, 35), (340, 200, 370, 60))


# ===============================================================================
# OLD CHURCH ROOMS
# ===============================================================================

class ChurchEntrance(Room):
    """Church entrance"""
    
    def __init__(self):
        super().__init__(
            name="entrance",
            display_name="Church Entrance",
            connections={"right": "nave"},
            base_color=(110, 100, 90),
            description="The church entrance. Holy water has dried up. Prayers go unanswered."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Holy Water Font", (300, 300, 80, 100),
            "An empty font. The holy water evaporated long ago.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Notice Board", (700, 220, 150, 200),
            "Announcements for services that never happened.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Wooden Doors", (400, 200, 200, 300),
            "Heavy oak doors. Something tries to keep them closed.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "FORSAKEN", "The Preacher")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (90, 70, 60), (400, 200, 200, 300))


class ChurchNave(Room):
    """Main nave"""
    
    def __init__(self):
        super().__init__(
            name="nave",
            display_name="Nave",
            connections={"left": "entrance", "up": "altar", "right": "confessional"},
            base_color=(120, 110, 100),
            description="The nave. Pews in rows. Congregation of the dead."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Pews", (200, 300, 600, 180),
            "Rows of pews. Some are occupied by shadows.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Stained Glass", (500, 100, 200, 150),
            "Stained glass windows. They show scenes of torment.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Hymn Books", (850, 350, 100, 60),
            "Open hymn books. The pages turn by themselves.",
            "examine"
        ))
        self.add_hidden_clue(600, 500, "WORSHIP", "The Choir")
    
    def draw_details(self, surface):
        for i in range(5):
            pygame.draw.rect(surface, (100, 80, 65), (200 + i * 120, 320, 115, 60))


class ChurchAltar(Room):
    """Church altar"""
    
    def __init__(self):
        super().__init__(
            name="altar",
            display_name="Altar",
            connections={"down": "nave", "right": "vestry"},
            base_color=(130, 120, 105),
            description="The altar. Where prayers were made. Where sacrifices were hidden."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Altar", (450, 280, 250, 120),
            "The main altar. Stained with more than wine.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Cross", (575, 150, 50, 150),
            "A large cross. It hangs upside down now.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Candles", (850, 300, 100, 120),
            "Altar candles. They burn with black flame.",
            "examine"
        ))
        self.add_hidden_clue(575, 500, "SACRIFICE", "The Preacher")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (150, 140, 130), (450, 280, 250, 120))


class ChurchConfessional(Room):
    """Confessional booths"""
    
    def __init__(self):
        super().__init__(
            name="confessional",
            display_name="Confessional",
            connections={"left": "nave", "down": "crypt"},
            base_color=(80, 70, 65),
            description="The confessional. Sins whispered here. Something still listens."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Confession Booth", (400, 200, 200, 300),
            "A wooden confessional. Someone is always inside.",
            "toggle",
            "You open the door. Empty. But breathing from the other side."
        ))
        self.add_object(InteractiveObject(
            "Kneeler", (650, 350, 100, 60),
            "A worn kneeler. Impressions of countless sinners.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Prayer Candles", (100, 280, 120, 180),
            "Candles for prayers. Some burn for the damned.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "FORGIVE ME", "Shadow Stalker")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (70, 55, 45), (400, 200, 200, 300))


class ChurchVestry(Room):
    """Priest's vestry"""
    
    def __init__(self):
        super().__init__(
            name="vestry",
            display_name="Vestry",
            connections={"left": "altar", "up": "bell_tower"},
            base_color=(100, 90, 80),
            description="The vestry. Where the priest prepared. And hid his secrets."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Robes Closet", (200, 200, 150, 280),
            "Priest's vestments. Some are stained with blood.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Prayer Book", (500, 320, 100, 60),
            "A personal prayer book. Notes in the margins reveal heresy.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Wine Cabinet", (800, 280, 100, 180),
            "Communion wine. Some bottles contain something else.",
            "examine"
        ))
        self.add_hidden_clue(550, 500, "HERESY", "The Preacher")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (80, 60, 50), (200, 200, 150, 280))


class ChurchCrypt(Room):
    """Church crypt"""
    
    def __init__(self):
        super().__init__(
            name="crypt",
            display_name="Crypt",
            connections={"up": "confessional"},
            base_color=(60, 60, 65),
            description="The crypt beneath the church. Priests and sinners buried together."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stone Tombs", (200, 250, 400, 200),
            "Ancient tombs. Some have been opened from inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Wall Niches", (700, 200, 200, 280),
            "Burial niches. Skulls stare from dark recesses.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Altar Stone", (950, 350, 80, 100),
            "A stone altar for rituals not approved by the church.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "RISEN", "Nightmare")
    
    def draw_details(self, surface):
        for i in range(3):
            pygame.draw.rect(surface, (80, 80, 85), (200 + i * 140, 280, 130, 150))


class ChurchBellTower(Room):
    """Bell tower"""
    
    def __init__(self):
        super().__init__(
            name="bell_tower",
            display_name="Bell Tower",
            connections={"down": "vestry"},
            base_color=(90, 85, 80),
            description="The bell tower. Bells that ring for the dead. A long way down."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Church Bells", (450, 150, 200, 200),
            "Massive bronze bells. They ring at midnight for no reason.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Bell Rope", (350, 150, 30, 350),
            "The bell pull. It moves on its own sometimes.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Tower Window", (800, 200, 150, 200),
            "A window overlooking the graveyard. Figures walk below.",
            "examine"
        ))
        self.add_hidden_clue(550, 450, "TOLL", "The Preacher")
    
    def draw_details(self, surface):
        pygame.draw.ellipse(surface, (150, 120, 60), (450, 180, 200, 150))


class ChurchGraveyard(Room):
    """Church graveyard"""
    
    def __init__(self):
        super().__init__(
            name="graveyard",
            display_name="Graveyard",
            connections={"up": "entrance"},
            base_color=(50, 55, 50),
            description="The church graveyard. Crooked headstones. Not all stay buried."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Headstones", (200, 280, 600, 200),
            "Old headstones. Some dates are tomorrow.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Open Grave", (850, 350, 120, 100),
            "A freshly dug grave. Waiting for someone.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Dead Tree", (100, 200, 80, 280),
            "A twisted dead tree. Rope marks on the branches.",
            "examine"
        ))
        self.add_hidden_clue(500, 500, "REST IN PEACE", "Weeping Lady")
    
    def draw_base(self, surface):
        pygame.draw.rect(surface, (25, 30, 40), (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.3)))
        pygame.draw.rect(surface, (40, 50, 40), (0, int(SCREEN_HEIGHT * 0.3), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.7)))
    
    def draw_details(self, surface):
        for i in range(6):
            pygame.draw.rect(surface, (120, 120, 125), (220 + i * 100, 320, 60, 120))


# ===============================================================================
# OLD FACTORY ROOMS
# ===============================================================================

class FactoryFloor(Room):
    """Main factory floor"""
    
    def __init__(self):
        super().__init__(
            name="factory_floor",
            display_name="Factory Floor",
            connections={"right": "assembly_line", "up": "offices"},
            base_color=(80, 80, 85),
            description="The main factory floor. Machines that never stopped. Workers who never left."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Machinery", (200, 200, 400, 280),
            "Old industrial machines. Gears still turn. No power source.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Work Station", (700, 320, 200, 120),
            "A worker's station. Tools laid out as if ready to use.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Time Clock", (100, 280, 80, 120),
            "An old time clock. Cards show workers who never clocked out.",
            "zoom"
        ))
        self.add_hidden_clue(500, 550, "OVERTIME", "The Worker")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (70, 70, 75), (200, 200, 400, 280))
        for i in range(4):
            pygame.draw.circle(surface, (90, 90, 95), (280 + i * 80, 340), 40)


class FactoryAssemblyLine(Room):
    """Assembly line"""
    
    def __init__(self):
        super().__init__(
            name="assembly_line",
            display_name="Assembly Line",
            connections={"left": "factory_floor", "down": "loading_dock"},
            base_color=(85, 85, 90),
            description="The assembly line. Conveyor belts move. Nothing is being made."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Conveyor Belt", (200, 350, 700, 80),
            "An endless conveyor belt. It carries invisible products.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Robotic Arms", (500, 200, 200, 200),
            "Old robotic arms. They reach for workers no longer there.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Emergency Stop", (950, 300, 60, 100),
            "An emergency stop button. Someone pressed it too late.",
            "toggle"
        ))
        self.add_hidden_clue(600, 450, "ACCIDENT", "The Burned Man")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 100, 105), (200, 360, 700, 60))


class FactoryOffices(Room):
    """Factory offices"""
    
    def __init__(self):
        super().__init__(
            name="offices",
            display_name="Offices",
            connections={"down": "factory_floor", "right": "break_room"},
            base_color=(140, 135, 130),
            description="The factory offices. Management that made deadly decisions."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Manager's Desk", (400, 300, 250, 120),
            "A desk with production reports. Safety violations ignored.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Filing Cabinets", (100, 220, 150, 260),
            "Cabinets of records. Injury reports. Death certificates.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Window", (800, 200, 200, 200),
            "A window overlooking the floor. Watching the workers suffer.",
            "examine"
        ))
        self.add_hidden_clue(525, 500, "PROFIT", "The Foreman")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (90, 70, 55), (400, 300, 250, 120))


class FactoryBreakRoom(Room):
    """Workers' break room"""
    
    def __init__(self):
        super().__init__(
            name="break_room",
            display_name="Break Room",
            connections={"left": "offices"},
            base_color=(150, 145, 140),
            description="The break room. Where workers ate. Where some took their last meal."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Lunch Table", (400, 320, 250, 100),
            "Tables with packed lunches never finished.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Vending Machine", (800, 250, 100, 200),
            "An old vending machine. Still dispensing snacks from the 80s.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Lockers", (100, 200, 200, 280),
            "Worker lockers. Personal effects of the deceased.",
            "examine"
        ))
        self.add_hidden_clue(525, 500, "LUNCH BREAK", "The Worker")
    
    def draw_details(self, surface):
        for i in range(3):
            pygame.draw.rect(surface, (130, 125, 120), (400 + i * 85, 340, 80, 60))


class FactoryLoadingDock(Room):
    """Loading dock"""
    
    def __init__(self):
        super().__init__(
            name="loading_dock",
            display_name="Loading Dock",
            connections={"up": "assembly_line", "right": "warehouse"},
            base_color=(90, 85, 80),
            description="The loading dock. Shipments that never arrived. Workers that never left."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Loading Bay", (200, 300, 400, 180),
            "Large bay doors. Trucks are still backed in.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Forklift", (700, 350, 150, 100),
            "An abandoned forklift. Engine still warm.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Shipping Manifest", (950, 280, 80, 100),
            "Shipping records. Final shipment never completed.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "DELIVERY", None)
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (60, 55, 50), (200, 320, 400, 150))


class FactoryWarehouse(Room):
    """Factory warehouse"""
    
    def __init__(self):
        super().__init__(
            name="warehouse",
            display_name="Warehouse",
            connections={"left": "loading_dock", "down": "furnace_room"},
            base_color=(70, 70, 75),
            description="The warehouse. Stacked crates hide what shouldn't be stored."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Stacked Crates", (200, 200, 400, 300),
            "Towers of crates. Some are moving.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Shelf Racks", (700, 220, 200, 260),
            "Industrial shelving. Products from decades past.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Pallet Jack", (950, 380, 80, 80),
            "A pallet jack. It rolls on its own.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "STORED", None)
    
    def draw_details(self, surface):
        for i in range(4):
            for j in range(3):
                pygame.draw.rect(surface, (100, 80, 60), (200 + i * 100, 280 - j * 70, 95, 65))


class FactoryFurnaceRoom(Room):
    """Industrial furnace room"""
    
    def __init__(self):
        super().__init__(
            name="furnace_room",
            display_name="Furnace Room",
            connections={"up": "warehouse", "right": "basement"},
            base_color=(100, 60, 50),
            description="The furnace room. Industrial fire. Some things were disposed of here."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Industrial Furnace", (400, 200, 300, 280),
            "A massive furnace. Still burning. What fuel?",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Coal Pile", (100, 350, 200, 130),
            "Piles of coal. And bones mixed in.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Safety Poster", (800, 250, 100, 150),
            "'Safety First' - ironic given what happened.",
            "examine"
        ))
        self.add_hidden_clue(550, 550, "BURN", "The Arsonist")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (60, 40, 35), (400, 200, 300, 280))
        pygame.draw.ellipse(surface, (200, 100, 50), (420, 350, 260, 100))


class FactoryBasement(Room):
    """Factory basement"""
    
    def __init__(self):
        super().__init__(
            name="basement",
            display_name="Basement",
            connections={"left": "furnace_room", "right": "boiler_room"},
            base_color=(55, 55, 60),
            description="The factory basement. Storage for broken machines. And broken people."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Old Machinery", (200, 250, 300, 220),
            "Discarded machines. They still try to work.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Chemical Drums", (600, 280, 200, 180),
            "Drums of unknown chemicals. Improperly disposed.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Maintenance Tunnel", (900, 300, 120, 150),
            "A tunnel for maintenance access. Where does it lead?",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "BURIED", "Shadow Stalker")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (70, 70, 75), (200, 280, 300, 180))


class FactoryBoilerRoom(Room):
    """Boiler room"""
    
    def __init__(self):
        super().__init__(
            name="boiler_room",
            display_name="Boiler Room",
            connections={"left": "basement"},
            base_color=(90, 70, 60),
            description="The boiler room. Steam and heat. The heart of the factory beats still."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Boilers", (300, 200, 400, 280),
            "Massive industrial boilers. Pressure gauges in the red.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Steam Pipes", (100, 150, 100, 350),
            "Steam pipes running everywhere. Some leak.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Pressure Valve", (800, 300, 80, 120),
            "A pressure release valve. It screams when turned.",
            "toggle"
        ))
        self.add_hidden_clue(500, 550, "EXPLOSION", "The Burned Man")
    
    def draw_details(self, surface):
        pygame.draw.ellipse(surface, (80, 60, 50), (300, 220, 200, 240))
        pygame.draw.ellipse(surface, (80, 60, 50), (500, 220, 200, 240))


# ===============================================================================
# UNDERGROUND BUNKER ROOMS
# ===============================================================================

class BunkerEntrance(Room):
    """Bunker entrance"""
    
    def __init__(self):
        super().__init__(
            name="entrance",
            display_name="Bunker Entrance",
            connections={"right": "decontamination"},
            base_color=(80, 85, 80),
            description="The bunker entrance. A blast door that sealed people inside. Forever."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Blast Door", (400, 180, 250, 320),
            "A massive blast door. Meant to keep something out. Or in.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Security Panel", (700, 300, 80, 120),
            "A keypad entry system. Still requesting codes.",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Warning Signs", (100, 250, 150, 100),
            "Military warnings. 'AUTHORIZED PERSONNEL ONLY'",
            "examine"
        ))
        self.add_hidden_clue(525, 550, "LOCKDOWN", "The Soldier")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (100, 105, 100), (400, 180, 250, 320))
        pygame.draw.circle(surface, (80, 80, 85), (525, 340), 60)


class BunkerDecontamination(Room):
    """Decontamination chamber"""
    
    def __init__(self):
        super().__init__(
            name="decontamination",
            display_name="Decontamination",
            connections={"left": "entrance", "right": "living_quarters"},
            base_color=(180, 180, 185),
            description="The decontamination chamber. Chemical showers. What were they trying to clean?"
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Shower Heads", (400, 150, 200, 150),
            "Chemical decontamination showers. They still drip.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Hazmat Suits", (100, 220, 150, 260),
            "Hanging hazmat suits. Some are torn from the inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Radiation Detector", (700, 300, 80, 100),
            "A Geiger counter. It clicks constantly.",
            "toggle"
        ))
        self.add_hidden_clue(500, 500, "CONTAMINATED", "The Plague Doctor")
    
    def draw_details(self, surface):
        for i in range(4):
            pygame.draw.circle(surface, (150, 150, 155), (420 + i * 45, 180), 15)


class BunkerLivingQuarters(Room):
    """Living quarters"""
    
    def __init__(self):
        super().__init__(
            name="living_quarters",
            display_name="Living Quarters",
            connections={"left": "decontamination", "up": "command_center", "down": "storage"},
            base_color=(120, 115, 110),
            description="Living quarters for soldiers. Bunks for those who never woke up."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Bunks", (200, 250, 350, 230),
            "Military bunks. Perfectly made. Or never slept in.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Footlockers", (600, 380, 200, 80),
            "Personal footlockers. Letters to families never sent.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Calendar", (900, 250, 80, 100),
            "A calendar. Marking days that never came.",
            "examine"
        ))
        self.add_hidden_clue(500, 550, "WAITING", "The Soldier")
    
    def draw_details(self, surface):
        for i in range(3):
            pygame.draw.rect(surface, (80, 75, 70), (200 + i * 120, 280, 110, 180))


class BunkerCommandCenter(Room):
    """Command center"""
    
    def __init__(self):
        super().__init__(
            name="command_center",
            display_name="Command Center",
            connections={"down": "living_quarters", "right": "radio_room"},
            base_color=(60, 70, 80),
            description="The command center. Where orders were given. Where panic set in."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "War Table", (350, 280, 350, 180),
            "A tactical map table. Red pins everywhere.",
            "zoom"
        ))
        self.add_object(InteractiveObject(
            "Monitor Banks", (800, 200, 200, 200),
            "Screens showing static. Occasionally, faces.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Red Phone", (150, 320, 60, 40),
            "The emergency hotline. It rings. No one answers.",
            "toggle"
        ))
        self.add_hidden_clue(525, 500, "ORDERS", "The General")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (40, 50, 60), (350, 280, 350, 180))


class BunkerRadioRoom(Room):
    """Radio communications room"""
    
    def __init__(self):
        super().__init__(
            name="radio_room",
            display_name="Radio Room",
            connections={"left": "command_center"},
            base_color=(70, 75, 80),
            description="The radio room. Last messages sent. No responses received."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Radio Equipment", (300, 250, 400, 200),
            "Banks of radio equipment. Still transmitting. To whom?",
            "toggle"
        ))
        self.add_object(InteractiveObject(
            "Headphones", (750, 350, 60, 40),
            "Operator headphones. You can hear whispers.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Log Book", (100, 300, 100, 80),
            "Radio logs. Last entry: 'They're inside.'",
            "zoom"
        ))
        self.add_hidden_clue(500, 500, "MAYDAY", "The Radio Operator")
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (50, 55, 60), (300, 270, 400, 160))


class BunkerStorage(Room):
    """Supply storage"""
    
    def __init__(self):
        super().__init__(
            name="storage",
            display_name="Supply Storage",
            connections={"up": "living_quarters", "right": "armory"},
            base_color=(100, 95, 90),
            description="Emergency supplies. Food for years. No one left to eat it."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Supply Crates", (200, 230, 350, 250),
            "Crates of emergency rations. Still sealed. Still edible.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Water Tanks", (700, 280, 150, 180),
            "Water storage tanks. Something floats inside.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Medical Supplies", (950, 320, 80, 120),
            "Medical kit. Bandages. Morphine. All used.",
            "examine"
        ))
        self.add_hidden_clue(400, 550, "SUPPLIES", None)
    
    def draw_details(self, surface):
        for i in range(4):
            for j in range(2):
                pygame.draw.rect(surface, (90, 80, 70), (200 + i * 90, 280 + j * 80, 85, 75))


class BunkerArmory(Room):
    """Weapons armory"""
    
    def __init__(self):
        super().__init__(
            name="armory",
            display_name="Armory",
            connections={"left": "storage", "down": "generator"},
            base_color=(70, 70, 75),
            description="The armory. Weapons for a war that never came. Or did it?"
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Weapon Racks", (200, 200, 300, 280),
            "Racks of rifles. Some are missing. Where did they go?",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Ammunition", (600, 320, 200, 130),
            "Crates of ammunition. Some boxes are empty.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Locker", (900, 250, 100, 200),
            "A locked weapons locker. For special ordinance.",
            "toggle"
        ))
        self.add_hidden_clue(500, 550, "ARMED", "The Soldier")
    
    def draw_details(self, surface):
        for i in range(8):
            pygame.draw.rect(surface, (50, 50, 55), (210 + i * 35, 220, 30, 240))


class BunkerGenerator(Room):
    """Power generator room"""
    
    def __init__(self):
        super().__init__(
            name="generator",
            display_name="Generator Room",
            connections={"up": "armory"},
            base_color=(60, 65, 70),
            description="The generator room. Power for a hundred years. Who's been using it?"
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Generator", (350, 230, 400, 250),
            "A massive generator. Humming eternally.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Fuel Tanks", (100, 280, 150, 180),
            "Fuel reserves. Slowly draining.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Control Panel", (850, 300, 120, 150),
            "Power control systems. Running on automatic.",
            "toggle"
        ))
        self.add_hidden_clue(550, 550, "POWER", None)
    
    def draw_details(self, surface):
        pygame.draw.rect(surface, (50, 55, 60), (350, 260, 400, 200))


# ===============================================================================
# FACTORY FUNCTIONS TO CREATE ROOMS FOR EACH LOCATION
# ===============================================================================

def create_school_rooms():
    """Create all rooms for the Haunted School"""
    return {
        "entrance_hall": SchoolEntranceHall(),
        "classroom_1": SchoolClassroom1(),
        "classroom_2": SchoolClassroom2(),
        "gymnasium": SchoolGymnasium(),
        "cafeteria": SchoolCafeteria(),
        "library": SchoolLibrary(),
        "principal_office": SchoolPrincipalOffice(),
        "bathroom": SchoolBathroom(),
        "playground": SchoolPlayground(),
        "basement": SchoolBasement(),
    }


def create_lighthouse_rooms():
    """Create all rooms for the Lighthouse"""
    return {
        "entrance": LighthouseEntrance(),
        "living_quarters": LighthouseLivingQuarters(),
        "storage": LighthouseStorage(),
        "lamp_room": LighthouseLampRoom(),
        "observation_deck": LighthouseObservationDeck(),
        "dock": LighthouseDock(),
    }


def create_theater_rooms():
    """Create all rooms for the Abandoned Theater"""
    return {
        "lobby": TheaterLobby(),
        "auditorium": TheaterAuditorium(),
        "stage": TheaterStage(),
        "backstage": TheaterBackstage(),
        "dressing_rooms": TheaterDressingRooms(),
        "orchestra_pit": TheaterOrchestraPit(),
        "balcony": TheaterBalcony(),
        "projection_room": TheaterProjectionRoom(),
        "basement": TheaterBasement(),
        "roof": TheaterRoof(),
    }


def create_hospital_rooms():
    """Create all rooms for the Abandoned Hospital"""
    return {
        "reception": HospitalReceptionRoom(),
        "waiting_room": HospitalWaitingRoom(),
        "emergency_room": HospitalEmergencyRoom(),
        "operating_theater": HospitalOperatingTheater(),
        "patient_ward": HospitalPatientWard(),
        "morgue": HospitalMorgue(),
        "pharmacy": HospitalPharmacy(),
        "doctors_office": HospitalDoctorsOffice(),
        "radiology": HospitalRadiology(),
        "basement": HospitalBasement(),
    }


def create_prison_rooms():
    """Create all rooms for the Old Prison"""
    return {
        "entrance_checkpoint": PrisonEntranceCheckpoint(),
        "cell_block_a": PrisonCellBlockA(),
        "cell_block_b": PrisonCellBlockB(),
        "cafeteria": PrisonCafeteria(),
        "exercise_yard": PrisonExerciseYard(),
        "solitary": PrisonSolitary(),
        "warden_office": PrisonWardenOffice(),
        "execution_chamber": PrisonExecutionChamber(),
        "guard_room": PrisonGuardRoom(),
        "basement": PrisonBasement(),
    }


def create_cemetery_rooms():
    """Create all rooms for the Cemetery"""
    return {
        "entrance_gates": CemeteryEntranceGates(),
        "main_path": CemeteryMainPath(),
        "old_graves": CemeteryOldGraves(),
        "mausoleum": CemeteryMausoleum(),
        "crypt": CemeteryCrypt(),
        "groundskeeper_shed": CemeteryGroundskeeperShed(),
        "chapel": CemeteryChapel(),
        "new_graves": CemeteryNewGraves(),
    }


def create_hotel_rooms():
    """Create all rooms for the Old Hotel"""
    return {
        "lobby": HotelLobby(),
        "reception": HotelReception(),
        "room_237": HotelRoom237(),
        "hallway": HotelHallway(),
        "ballroom": HotelBallroom(),
        "kitchen": HotelKitchen(),
        "basement": HotelBasement(),
        "penthouse": HotelPenthouse(),
        "elevator": HotelElevator(),
        "laundry": HotelLaundry(),
    }


def create_ship_rooms():
    """Create all rooms for the Ghost Ship"""
    return {
        "deck": ShipDeck(),
        "bridge": ShipBridge(),
        "captains_quarters": ShipCaptainsQuarters(),
        "crew_quarters": ShipCrewQuarters(),
        "cargo_hold": ShipCargoHold(),
        "engine_room": ShipEngineRoom(),
        "galley": ShipGalley(),
        "lifeboat_deck": ShipLifeboatDeck(),
    }


def create_mine_rooms():
    """Create all rooms for the Abandoned Mine"""
    return {
        "mine_entrance": MineEntrance(),
        "shaft_1": MineShaft1(),
        "shaft_2": MineShaft2(),
        "ore_processing": MineOreProcessing(),
        "elevator": MineElevator(),
        "collapsed_tunnel": MineCollapsedTunnel(),
        "underground_lake": MineUndergroundLake(),
        "exit_tunnel": MineExitTunnel(),
    }


def create_museum_rooms():
    """Create all rooms for the Museum"""
    return {
        "main_hall": MuseumMainHall(),
        "egyptian_exhibit": MuseumEgyptianExhibit(),
        "dinosaur_hall": MuseumDinosaurHall(),
        "art_gallery": MuseumArtGallery(),
        "natural_history": MuseumNaturalHistory(),
        "storage": MuseumStorage(),
        "restoration_lab": MuseumRestorationLab(),
        "gift_shop": MuseumGiftShop(),
        "security_office": MuseumSecurityOffice(),
        "basement": MuseumBasement(),
    }


def create_library_rooms():
    """Create all rooms for the Old Library"""
    return {
        "entrance_hall": LibraryEntranceHall(),
        "main_reading_room": LibraryMainReadingRoom(),
        "reference_section": LibraryReferenceSection(),
        "archives": LibraryArchives(),
        "rare_books": LibraryRareBooks(),
        "study_rooms": LibraryStudyRooms(),
        "basement_stacks": LibraryBasementStacks(),
        "librarian_office": LibraryLibrarianOffice(),
        "restoration_room": LibraryRestorationRoom(),
        "attic": LibraryAttic(),
    }


def create_asylum_rooms():
    """Create all rooms for the Abandoned Asylum"""
    return {
        "entrance": AsylumEntrance(),
        "reception": AsylumReception(),
        "ward_a": AsylumWardA(),
        "ward_b": AsylumWardB(),
        "therapy_room": AsylumTherapyRoom(),
        "isolation": AsylumIsolation(),
        "electroshock": AsylumElectroshock(),
        "hydrotherapy": AsylumHydrotherapy(),
        "morgue": AsylumMorgue(),
        "basement": AsylumBasement(),
    }


def create_farmhouse_rooms():
    """Create all rooms for the Farmhouse"""
    return {
        "kitchen": FarmhouseKitchen(),
        "living_room": FarmhouseLivingRoom(),
        "bedroom": FarmhouseBedroom(),
        "childrens_room": FarmhouseChildrensRoom(),
        "barn": FarmhouseBarn(),
        "hayloft": FarmhouseHayloft(),
        "cellar": FarmhouseCellar(),
        "porch": FarmhousePorch(),
        "cornfield": FarmhouseCornfield(),
        "scarecrow_hill": FarmhouseScarecrowHill(),
    }


def create_train_station_rooms():
    """Create all rooms for the Train Station"""
    return {
        "platform": TrainStationPlatform(),
        "ticket_office": TrainStationTicketOffice(),
        "waiting_room": TrainStationWaitingRoom(),
        "restaurant": TrainStationRestaurant(),
        "baggage_claim": TrainStationBaggageClaim(),
        "tunnel": TrainStationTunnel(),
        "platform_2": TrainStationPlatform2(),
        "office": TrainStationOffice(),
        "freight_yard": TrainStationFreightYard(),
        "maintenance": TrainStationMaintenance(),
    }


def create_mall_rooms():
    """Create all rooms for the Abandoned Mall"""
    return {
        "main_entrance": MallMainEntrance(),
        "food_court": MallFoodCourt(),
        "department_store": MallDepartmentStore(),
        "clothing_store": MallClothingStore(),
        "electronics": MallElectronics(),
        "toy_store": MallToyStore(),
        "movie_theater": MallMovieTheater(),
        "parking_garage": MallParkingGarage(),
        "security_office": MallSecurityOffice(),
        "storage": MallStorage(),
    }


def create_mansion_rooms():
    """Create all rooms for the Victorian Mansion"""
    return {
        "foyer": MansionFoyer(),
        "dining_room": MansionDiningRoom(),
        "ballroom": MansionBallroom(),
        "gallery": MansionGallery(),
        "library": MansionLibrary(),
        "kitchen": MansionKitchen(),
        "servants_quarters": MansionServants(),
        "study": MansionStudy(),
        "conservatory": MansionConservatory(),
        "garden": MansionGarden(),
        "maze": MansionMaze(),
        "master_suite": MansionMasterSuite(),
    }


def create_church_rooms():
    """Create all rooms for the Old Church"""
    return {
        "entrance": ChurchEntrance(),
        "nave": ChurchNave(),
        "altar": ChurchAltar(),
        "confessional": ChurchConfessional(),
        "vestry": ChurchVestry(),
        "crypt": ChurchCrypt(),
        "bell_tower": ChurchBellTower(),
        "graveyard": ChurchGraveyard(),
    }


def create_factory_rooms():
    """Create all rooms for the Old Factory"""
    return {
        "factory_floor": FactoryFloor(),
        "assembly_line": FactoryAssemblyLine(),
        "offices": FactoryOffices(),
        "break_room": FactoryBreakRoom(),
        "loading_dock": FactoryLoadingDock(),
        "warehouse": FactoryWarehouse(),
        "furnace_room": FactoryFurnaceRoom(),
        "basement": FactoryBasement(),
        "boiler_room": FactoryBoilerRoom(),
    }


def create_bunker_rooms():
    """Create all rooms for the Underground Bunker"""
    return {
        "entrance": BunkerEntrance(),
        "decontamination": BunkerDecontamination(),
        "living_quarters": BunkerLivingQuarters(),
        "command_center": BunkerCommandCenter(),
        "radio_room": BunkerRadioRoom(),
        "storage": BunkerStorage(),
        "armory": BunkerArmory(),
        "generator": BunkerGenerator(),
    }


# ===============================================================================
# GENERIC ROOM GENERATOR FOR OTHER LOCATIONS
# Creates procedurally themed rooms based on location data
# ===============================================================================

class GenericLocationRoom(Room):
    """A generic room that can be themed for any location"""
    
    def __init__(self, name, display_name, connections, base_color, description, 
                 objects_data=None, clues_data=None):
        # Set data before calling super().__init__ since it calls setup_room()
        self.objects_data = objects_data or []
        self.clues_data = clues_data or []
        super().__init__(name, display_name, connections, base_color, description)
        
    def setup_room(self):
        for obj_data in self.objects_data:
            self.add_object(InteractiveObject(
                obj_data.get('name', 'Object'),
                obj_data.get('rect', (400, 300, 100, 100)),
                obj_data.get('description', 'An object.'),
                obj_data.get('interaction', 'examine'),
                obj_data.get('zoom_desc', None)
            ))
        for clue in self.clues_data:
            self.add_hidden_clue(clue[0], clue[1], clue[2], clue[3] if len(clue) > 3 else None)
    
    def draw_details(self, surface):
        # Draw basic room elements based on theme
        # Walls
        pygame.draw.rect(surface, self.darken_color(self.base_color, 0.9), 
                        (0, 0, SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.6)))
        # Floor
        pygame.draw.rect(surface, self.darken_color(self.base_color, 0.7),
                        (0, int(SCREEN_HEIGHT * 0.6), SCREEN_WIDTH, int(SCREEN_HEIGHT * 0.4)))


def generate_location_rooms(location_id, room_names, theme_color, ghosts):
    """Generate a set of themed rooms for a location"""
    rooms = {}
    
    # Create connections between rooms
    for i, room_name in enumerate(room_names):
        connections = {}
        if i > 0:
            connections["left"] = room_names[i - 1]
        if i < len(room_names) - 1:
            connections["right"] = room_names[i + 1]
        if i >= 2 and i < len(room_names) - 2:
            connections["up"] = room_names[i - 2] if i >= 2 else None
            connections["down"] = room_names[i + 2] if i < len(room_names) - 2 else None
        
        # Create display name
        display_name = room_name.replace('_', ' ').title()
        
        # Create description based on room name
        description = f"A {display_name.lower()} area. Something doesn't feel right here."
        
        # Create some basic objects for the room
        objects = [
            {'name': f'{display_name} Feature', 'rect': (400, 300, 150, 100),
             'description': f'A notable feature of the {display_name.lower()}.', 
             'interaction': 'examine'},
            {'name': 'Light Switch', 'rect': (50, 300, 30, 50),
             'description': 'A light switch.', 'interaction': 'toggle'},
        ]
        
        # Add clues from random ghosts for this location
        clues = []
        if ghosts and len(ghosts) > 0:
            ghost = ghosts[i % len(ghosts)]
            clues.append((random.randint(300, 800), random.randint(400, 550), 
                         ghost.upper()[:10], ghost))
        
        rooms[room_name] = GenericLocationRoom(
            room_name, display_name, connections, theme_color, description,
            objects, clues
        )
    
    return rooms


# ===============================================================================
# MAIN FUNCTION TO CREATE ROOMS FOR ANY LOCATION
# ===============================================================================

def create_rooms_for_location(location_id):
    """Create appropriate rooms for a given location"""
    from locations import LOCATIONS, LOCATION_ROOMS, LOCATION_HAUNTED_HOUSE, \
        LOCATION_HOSPITAL, LOCATION_PRISON, LOCATION_SCHOOL, LOCATION_LIGHTHOUSE, \
        LOCATION_THEATER, LOCATION_CEMETERY, LOCATION_HOTEL, LOCATION_SHIP, \
        LOCATION_MINE, LOCATION_MUSEUM, LOCATION_LIBRARY, LOCATION_ASYLUM, \
        LOCATION_FARMHOUSE, LOCATION_TRAIN_STATION, LOCATION_MALL, \
        LOCATION_MANSION, LOCATION_CHURCH, LOCATION_FACTORY, LOCATION_BUNKER
    from rooms import create_all_rooms
    
    # For haunted house, use the original detailed rooms
    if location_id == LOCATION_HAUNTED_HOUSE:
        return create_all_rooms()
    
    # For hospital, use custom hospital rooms
    if location_id == LOCATION_HOSPITAL:
        return create_hospital_rooms()
    
    # For prison, use custom prison rooms
    if location_id == LOCATION_PRISON:
        return create_prison_rooms()
    
    # For school, use custom school rooms
    if location_id == LOCATION_SCHOOL:
        return create_school_rooms()
    
    # For lighthouse, use custom lighthouse rooms
    if location_id == LOCATION_LIGHTHOUSE:
        return create_lighthouse_rooms()
    
    # For theater, use custom theater rooms
    if location_id == LOCATION_THEATER:
        return create_theater_rooms()
    
    # For cemetery, use custom cemetery rooms
    if location_id == LOCATION_CEMETERY:
        return create_cemetery_rooms()
    
    # For hotel, use custom hotel rooms
    if location_id == LOCATION_HOTEL:
        return create_hotel_rooms()
    
    # For ship, use custom ship rooms
    if location_id == LOCATION_SHIP:
        return create_ship_rooms()
    
    # For mine, use custom mine rooms
    if location_id == LOCATION_MINE:
        return create_mine_rooms()
    
    # For museum, use custom museum rooms
    if location_id == LOCATION_MUSEUM:
        return create_museum_rooms()
    
    # For library, use custom library rooms
    if location_id == LOCATION_LIBRARY:
        return create_library_rooms()
    
    # For asylum, use custom asylum rooms
    if location_id == LOCATION_ASYLUM:
        return create_asylum_rooms()
    
    # For farmhouse, use custom farmhouse rooms
    if location_id == LOCATION_FARMHOUSE:
        return create_farmhouse_rooms()
    
    # For train station, use custom train station rooms
    if location_id == LOCATION_TRAIN_STATION:
        return create_train_station_rooms()
    
    # For mall, use custom mall rooms
    if location_id == LOCATION_MALL:
        return create_mall_rooms()
    
    # For mansion, use custom mansion rooms
    if location_id == LOCATION_MANSION:
        return create_mansion_rooms()
    
    # For church, use custom church rooms
    if location_id == LOCATION_CHURCH:
        return create_church_rooms()
    
    # For factory, use custom factory rooms
    if location_id == LOCATION_FACTORY:
        return create_factory_rooms()
    
    # For bunker, use custom bunker rooms
    if location_id == LOCATION_BUNKER:
        return create_bunker_rooms()
    
    # For other locations, generate themed rooms
    # Use .get() with safe fallbacks
    default_color = (100, 100, 100)
    default_rooms = ["room_1", "room_2", "room_3"]
    
    location_data = LOCATIONS.get(location_id) or LOCATIONS.get(LOCATION_HAUNTED_HOUSE, {})
    room_names = LOCATION_ROOMS.get(location_id) or LOCATION_ROOMS.get(LOCATION_HAUNTED_HOUSE, default_rooms)
    theme_color = location_data.get('color', default_color)
    ghosts = location_data.get('ghosts', [])
    
    return generate_location_rooms(location_id, room_names, theme_color, ghosts)
