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
        LOCATION_THEATER
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
    
    # For other locations, generate themed rooms
    location_data = LOCATIONS.get(location_id, LOCATIONS[LOCATION_HAUNTED_HOUSE])
    room_names = LOCATION_ROOMS.get(location_id, LOCATION_ROOMS[LOCATION_HAUNTED_HOUSE])
    theme_color = location_data.get('color', (100, 100, 100))
    ghosts = location_data.get('ghosts', [])
    
    return generate_location_rooms(location_id, room_names, theme_color, ghosts)
