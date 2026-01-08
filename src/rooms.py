"""
Room definitions and rendering for Paranormal Investigations
"""

import pygame
import math
import random
from constants import *


class InteractiveObject:
    """An object in a room that can be interacted with"""
    
    # Unique affected messages for each object + ghost combination
    GHOST_OBJECT_MESSAGES = {
        # Grandfather Clock messages
        ("Grandfather Clock", "Bonnie"): "The clock hands spin wildly, stopping at 3:33. Burn marks appear on the wood.",
        ("Grandfather Clock", "Poltergeist"): "The clock flies off the wall and crashes! The pendulum swings violently.",
        ("Grandfather Clock", "Weeping Lady"): "Tears stream down the clock face. The ticking sounds like sobbing.",
        ("Grandfather Clock", "Shadow Stalker"): "The clock is shrouded in darkness. You can't see the time anymore.",
        ("Grandfather Clock", "Little Timmy"): "Small handprints appear on the glass. The clock chimes a nursery rhyme.",
        ("Grandfather Clock", "The Butcher"): "Deep gouges appear in the wood, like cleaver marks. Blood drips from the hands.",
        ("Grandfather Clock", "Ethereal Bride"): "Wedding bells chime from within. The time shows the hour of a wedding.",
        ("Grandfather Clock", "The Librarian"): "A finger 'SHHHH' is etched into the glass. The ticking becomes silent.",
        ("Grandfather Clock", "Nightmare"): "The clock shows impossible times. Multiple hands point in all directions.",
        ("Grandfather Clock", "The Collector"): "Trinkets and coins spill from the clock's case. It's been stuffed full.",
        ("Grandfather Clock", "The Burned Man"): "The clock is charred and smoking. The fire smell is overwhelming.",
        ("Grandfather Clock", "The Doll"): "A tiny porcelain hand waves from behind the glass. Giggling echoes.",
        ("Grandfather Clock", "The Hanged Man"): "A noose hangs from the clock hands. It swings like a pendulum.",
        ("Grandfather Clock", "The Mimic"): "Your reflection appears in the glass, but it's smiling when you're not.",
        ("Grandfather Clock", "The Nurse"): "Medical charts are stuffed inside. The time reads 'Time of Death'.",
        
        # Front Door messages
        ("Front Door", "Bonnie"): "Scorch marks outline a figure on the door. It's reaching for the handle.",
        ("Front Door", "Poltergeist"): "The door slams repeatedly! Open-close-open-close at impossible speed!",
        ("Front Door", "Weeping Lady"): "Water seeps under the door. Wet footprints lead away into the house.",
        ("Front Door", "Shadow Stalker"): "The door is pure black. No light passes through the cracks.",
        ("Front Door", "Little Timmy"): "Crayon drawings of a family appear on the door. One figure is crossed out.",
        ("Front Door", "The Butcher"): "Bloody handprints cover the door. Scratch marks show someone tried to escape.",
        ("Front Door", "Ethereal Bride"): "Wedding flowers are nailed to the door. They're dead and wilted.",
        ("Front Door", "The Librarian"): "'SILENCE' is carved into the wood in angry letters.",
        ("Front Door", "Nightmare"): "The door leads to multiple places at once. Reality bends around it.",
        ("Front Door", "The Collector"): "Locks and chains cover the door. No one leaves with the collection.",
        ("Front Door", "The Burned Man"): "The door is on fire! No... wait... the flames aren't real. Are they?",
        ("Front Door", "The Doll"): "A doll's eye peeks through the mail slot. It blinks.",
        ("Front Door", "The Hanged Man"): "A shadow hangs from the door frame. It swings gently.",
        ("Front Door", "The Mimic"): "You see yourself on the other side, trying to get in.",
        ("Front Door", "The Nurse"): "'VISITING HOURS ARE OVER' is written in red on the door.",
        
        # Mirror messages
        ("Bathroom Mirror", "Bonnie"): "A burned face stares back at you. It's not your reflection.",
        ("Bathroom Mirror", "Poltergeist"): "The mirror cracks in a spider web pattern, then repairs itself!",
        ("Bathroom Mirror", "Weeping Lady"): "A woman weeps in the reflection. Her tears flow down the real glass.",
        ("Bathroom Mirror", "Shadow Stalker"): "Your reflection is gone. Only darkness stares back.",
        ("Bathroom Mirror", "Little Timmy"): "A child waves at you in the mirror. You're alone in the room.",
        ("Bathroom Mirror", "The Butcher"): "A cleaver appears in your reflection's hand. You're not holding anything.",
        ("Bathroom Mirror", "Ethereal Bride"): "A bride in white appears behind you. When you turn, no one is there.",
        ("Bathroom Mirror", "The Librarian"): "'QUIET!' is written backwards in the fog. It wasn't there before.",
        ("Bathroom Mirror", "Nightmare"): "Your reflection shows your deepest fear. You can't look away.",
        ("Bathroom Mirror", "The Collector"): "Faces of previous victims appear in the glass, trapped forever.",
        ("Bathroom Mirror", "The Burned Man"): "The mirror melts and warps from intense heat. Your reflection burns.",
        ("Bathroom Mirror", "The Doll"): "A porcelain face replaces your reflection. It smiles with cracked lips.",
        ("Bathroom Mirror", "The Hanged Man"): "Your reflection has a noose around its neck. It's turning blue.",
        ("Bathroom Mirror", "The Mimic"): "Your reflection moves independently. It's learning to be you.",
        ("Bathroom Mirror", "The Nurse"): "A nurse appears behind you with a syringe. 'Time for medicine.'",
        
        # Bed messages
        ("Bed", "Bonnie"): "The sheets are burned in the shape of a body. Smoke rises from the fabric.",
        ("Bed", "Poltergeist"): "The bed levitates and drops! The mattress spins like it's possessed!",
        ("Bed", "Weeping Lady"): "The pillows are soaked with tears. The sheets are cold and damp.",
        ("Bed", "Shadow Stalker"): "Something is under the covers. The shape moves toward you.",
        ("Bed", "Little Timmy"): "Toys are arranged on the pillow. A teddy bear watches you.",
        ("Bed", "The Butcher"): "The mattress is slashed open. Stuffing spills out like entrails.",
        ("Bed", "Ethereal Bride"): "Wedding dress fabric is woven into the sheets. It still smells of perfume.",
        ("Bed", "The Librarian"): "Books are stacked neatly on the pillow. Don't disturb them.",
        ("Bed", "Nightmare"): "The bed shows your worst sleeping fear. You'll never rest peacefully.",
        ("Bed", "The Collector"): "Strange objects are hidden under the mattress. They weren't yours.",
        ("Bed", "The Burned Man"): "The bed is smoldering. You can feel the heat from here.",
        ("Bed", "The Doll"): "Dolls are arranged around the bed, watching. Their eyes follow you.",
        ("Bed", "The Hanged Man"): "Rope marks are burned into the headboard. A noose hangs from the post.",
        ("Bed", "The Mimic"): "Someone who looks exactly like you is sleeping in the bed.",
        ("Bed", "The Nurse"): "Hospital restraints are attached to the bedframe. They're worn from use.",
        
        # Fireplace messages
        ("Fireplace", "Bonnie"): "Blue flames dance without fuel. A figure writhes in the fire.",
        ("Fireplace", "Poltergeist"): "Ashes explode outward! Soot covers everything in a violent burst!",
        ("Fireplace", "Weeping Lady"): "The fireplace weeps water instead of producing heat. Ashes float in puddles.",
        ("Fireplace", "Shadow Stalker"): "The fireplace is a portal to pure darkness. Cold emanates from within.",
        ("Fireplace", "Little Timmy"): "A child's toys are arranged in the ashes. A ball rolls out on its own.",
        ("Fireplace", "The Butcher"): "Bones are piled in the fireplace. They're not from animals.",
        ("Fireplace", "Ethereal Bride"): "Wedding photos burn eternally in the flames. The faces are scratched out.",
        ("Fireplace", "The Librarian"): "Burned books smolder in the hearth. The titles are all forbidden texts.",
        ("Fireplace", "Nightmare"): "The fire shows your fears. Images flicker in the flames.",
        ("Fireplace", "The Collector"): "Stolen treasures melt in the fire. Gold drips down the grate.",
        ("Fireplace", "The Burned Man"): "The fire roars to life! A charred hand reaches out from the flames!",
        ("Fireplace", "The Doll"): "Melted doll parts bubble in the flames. Their eyes are still intact.",
        ("Fireplace", "The Hanged Man"): "Rope burns in the fire, filling the room with an acrid smell.",
        ("Fireplace", "The Mimic"): "Your face appears in the flames, screaming silently.",
        ("Fireplace", "The Nurse"): "Medical waste burns in the fireplace. The smell is antiseptic and wrong.",
        
        # Knife Block messages
        ("Knife Block", "Bonnie"): "The knives are blackened and warped from heat. They still cut.",
        ("Knife Block", "Poltergeist"): "The knives hover in the air, pointing at you! Then clatter down.",
        ("Knife Block", "Weeping Lady"): "Rust (or is it blood?) drips from the knife handles. They weep metal tears.",
        ("Knife Block", "Shadow Stalker"): "The largest knife is missing. You feel watched.",
        ("Knife Block", "Little Timmy"): "Child-sized cuts are on the cutting board. 'I TRIED TO HELP' is carved.",
        ("Knife Block", "The Butcher"): "EVERY knife is missing. You hear chopping sounds nearby. RUN.",
        ("Knife Block", "Ethereal Bride"): "A wedding cake knife appears. It's covered in decades-old icing... and blood.",
        ("Knife Block", "The Librarian"): "Paper cuts appear on your hands just from looking. The knives are razor-sharp.",
        ("Knife Block", "Nightmare"): "The knives reflect your deepest fears. Each blade shows a different terror.",
        ("Knife Block", "The Collector"): "Antique knives from various eras fill the block. Each has a history.",
        ("Knife Block", "The Burned Man"): "The knife handles are too hot to touch. Metal glows orange.",
        ("Knife Block", "The Doll"): "Tiny knife marks cover the block. Like someone was making doll furniture.",
        ("Knife Block", "The Hanged Man"): "One knife has a rope wrapped around its handle. It swings gently.",
        ("Knife Block", "The Mimic"): "Your fingerprints are on every knife. But you never touched them.",
        ("Knife Block", "The Nurse"): "The knives have been 'sterilized.' Surgical tape wraps each handle.",
        
        # Portrait messages
        ("Portrait", "Bonnie"): "The painted face is burned beyond recognition. Eyes still watch.",
        ("Portrait", "Poltergeist"): "The portrait spins on the wall! The faces blur into screams!",
        ("Portrait", "Weeping Lady"): "The painted woman cries real tears. They pool on the floor.",
        ("Portrait", "Shadow Stalker"): "The background of the portrait is pure darkness. Figures lurk within.",
        ("Portrait", "Little Timmy"): "A child appears in the portrait that wasn't there before. He waves.",
        ("Portrait", "The Butcher"): "The family in the portrait has been 'butchered.' Red paint drips.",
        ("Portrait", "Ethereal Bride"): "A bride appears in the portrait. She's waiting at the altar alone.",
        ("Portrait", "The Librarian"): "The subjects in the portrait hold their fingers to their lips. Shhhh.",
        ("Portrait", "Nightmare"): "The portrait shows something different every time you look.",
        ("Portrait", "The Collector"): "Multiple portraits are stacked inside the frame. Collected faces.",
        ("Portrait", "The Burned Man"): "The canvas is charred. The painted eyes glow like embers.",
        ("Portrait", "The Doll"): "The subjects are replaced with porcelain dolls. They're arranged like a family.",
        ("Portrait", "The Hanged Man"): "All the subjects in the portrait are hanging. Their feet dangle.",
        ("Portrait", "The Mimic"): "Your face is painted over everyone in the portrait.",
        ("Portrait", "The Nurse"): "The subjects wear hospital gowns. Their wristbands are visible.",
        
        # Bathtub messages
        ("Bathtub", "Bonnie"): "Steam rises from the empty tub. The porcelain is heat-cracked.",
        ("Bathtub", "Poltergeist"): "Water explodes from the tub! It sloshes violently without stopping!",
        ("Bathtub", "Weeping Lady"): "The tub is filled with tears. A figure floats face-down in the water.",
        ("Bathtub", "Shadow Stalker"): "The water is black as ink. Something moves beneath the surface.",
        ("Bathtub", "Little Timmy"): "Rubber ducks float in the tub. They follow you with their eyes.",
        ("Bathtub", "The Butcher"): "The water is thick and red. You don't want to know what's in there.",
        ("Bathtub", "Ethereal Bride"): "A wedding dress floats in the water. It's stained with something dark.",
        ("Bathtub", "The Librarian"): "Waterlogged books float in the tub. The words bleed off the pages.",
        ("Bathtub", "Nightmare"): "Your drowned face stares up from the water. But you're not in the tub.",
        ("Bathtub", "The Collector"): "The tub is filled with stolen jewelry and trinkets, submerged in murky water.",
        ("Bathtub", "The Burned Man"): "The water is boiling hot! Steam fills the room!",
        ("Bathtub", "The Doll"): "Porcelain doll parts float in the water. Heads, hands, eyes...",
        ("Bathtub", "The Hanged Man"): "A rope trails from the tub to the ceiling. The water is still.",
        ("Bathtub", "The Mimic"): "You see yourself drowning in the tub. It's happening now.",
        ("Bathtub", "The Nurse"): "The tub is filled with medical equipment. 'HYDROTHERAPY' is written on the wall.",
        
        # Wardrobe messages
        ("Wardrobe", "Bonnie"): "Smoke seeps from the wardrobe cracks. Something burned inside.",
        ("Wardrobe", "Poltergeist"): "The doors burst open! Clothes fly out like escaping spirits!",
        ("Wardrobe", "Weeping Lady"): "Damp clothes hang inside. They smell of river water and sorrow.",
        ("Wardrobe", "Shadow Stalker"): "The wardrobe contains only darkness. It seems infinitely deep.",
        ("Wardrobe", "Little Timmy"): "Child's clothes appear among the adult clothing. They're from the 1950s.",
        ("Wardrobe", "The Butcher"): "Butcher's aprons hang inside. They're stained with old blood.",
        ("Wardrobe", "Ethereal Bride"): "A wedding dress hangs alone. It moves without wind.",
        ("Wardrobe", "The Librarian"): "The clothes are arranged by color and size. Perfectly. Obsessively.",
        ("Wardrobe", "Nightmare"): "The clothes inside belong to everyone you've ever feared.",
        ("Wardrobe", "The Collector"): "Hundreds of different outfits are crammed inside. From different eras.",
        ("Wardrobe", "The Burned Man"): "The clothes inside are all burned. Ashes fall when you touch them.",
        ("Wardrobe", "The Doll"): "Doll-sized clothes hang on tiny hangers. Hundreds of them.",
        ("Wardrobe", "The Hanged Man"): "Empty nooses hang among the clothes. Waiting.",
        ("Wardrobe", "The Mimic"): "All the clothes are exactly your size. Your style. Your life.",
        ("Wardrobe", "The Nurse"): "Hospital gowns hang in neat rows. Patient numbers are written on tags.",
        
        # Coat Rack messages
        ("Coat Rack", "Bonnie"): "The coats are scorched. A burned hand pokes from one sleeve.",
        ("Coat Rack", "Poltergeist"): "Coats fly off the rack and dance around the room!",
        ("Coat Rack", "Weeping Lady"): "The coats drip with water. Puddles form beneath them.",
        ("Coat Rack", "Shadow Stalker"): "A coat moves on its own. Someone invisible is wearing it.",
        ("Coat Rack", "Little Timmy"): "A child's jacket appears on the rack. It's well-worn and loved.",
        ("Coat Rack", "The Butcher"): "A butcher's coat hangs on the rack. It's covered in old stains.",
        ("Coat Rack", "Ethereal Bride"): "A veil hangs on the rack. It sways like someone just walked past.",
        ("Coat Rack", "The Librarian"): "A moth-eaten cardigan appears. It smells of old books.",
        ("Coat Rack", "Nightmare"): "The coats have no owners. They belonged to people who are gone.",
        ("Coat Rack", "The Collector"): "Dozens of coats are crammed on the rack. None of them match.",
        ("Coat Rack", "The Burned Man"): "The coats smolder gently. Smoke rises from the fabric.",
        ("Coat Rack", "The Doll"): "A tiny doll coat hangs among the full-sized ones. It moves.",
        ("Coat Rack", "The Hanged Man"): "The coat rack looks like a gallows. Coats hang like bodies.",
        ("Coat Rack", "The Mimic"): "Your favorite coat is here. But you never brought it.",
        ("Coat Rack", "The Nurse"): "A nurse's cape hangs on the rack. It's from another century.",
        
        # Stove messages
        ("Stove", "Bonnie"): "The burners glow with supernatural heat. Blue flames dance without gas.",
        ("Stove", "Poltergeist"): "Pots and pans fly off the stove! The burners click on and off rapidly!",
        ("Stove", "Weeping Lady"): "Water boils over endlessly from empty pots. The steam forms crying faces.",
        ("Stove", "Shadow Stalker"): "The stove produces only darkness. Cold shadows leak from the burners.",
        ("Stove", "Little Timmy"): "Tiny handprints cover the stovetop. A child's drawing is burned into the metal.",
        ("Stove", "The Butcher"): "The stove is covered in char and grease. Something was cooked here. Something wrong.",
        ("Stove", "Ethereal Bride"): "A wedding cake burns eternally on the stove. The smell of burnt sugar fills the air.",
        ("Stove", "The Librarian"): "Recipe books burn on the stove. The pages turn themselves.",
        ("Stove", "Nightmare"): "The stove shows you burning alive. The flames reach for you.",
        ("Stove", "The Collector"): "Melted jewelry drips from the burners. Gold and silver pool below.",
        ("Stove", "The Burned Man"): "The stove ROARS with fire! Flames lick the ceiling! Is this real?!",
        ("Stove", "The Doll"): "Tiny porcelain hands reach from the oven. They're waving.",
        ("Stove", "The Hanged Man"): "Rope burns in the flames. The smoke carries the smell of death.",
        ("Stove", "The Mimic"): "You see yourself cooking at the stove. But you're standing here.",
        ("Stove", "The Nurse"): "Syringes boil in a pot on the stove. 'STERILIZATION' is labeled.",
        
        # Refrigerator messages
        ("Refrigerator", "Bonnie"): "The fridge is unnaturally hot. Frost evaporates from inside.",
        ("Refrigerator", "Poltergeist"): "The fridge door slams open and shut! Contents fly out violently!",
        ("Refrigerator", "Weeping Lady"): "Water pools beneath the fridge. Inside, everything is waterlogged.",
        ("Refrigerator", "Shadow Stalker"): "Opening the fridge reveals only endless darkness. The light doesn't work.",
        ("Refrigerator", "Little Timmy"): "Child's drawings are stuck to the fridge with blood-red magnets.",
        ("Refrigerator", "The Butcher"): "The fridge is full of meat. Too much meat. It's not all from animals.",
        ("Refrigerator", "Ethereal Bride"): "A wedding cake sits inside, decades old but perfectly preserved.",
        ("Refrigerator", "The Librarian"): "Books are stored in the fridge to preserve them. They're all overdue.",
        ("Refrigerator", "Nightmare"): "Inside the fridge, you see your own severed head staring back.",
        ("Refrigerator", "The Collector"): "The fridge is stuffed with jars. Each contains something different. Something wrong.",
        ("Refrigerator", "The Burned Man"): "The fridge is hot to the touch. Inside, everything is charred.",
        ("Refrigerator", "The Doll"): "Doll parts are arranged neatly on each shelf. All staring out.",
        ("Refrigerator", "The Hanged Man"): "Rope coils fill the fridge. Each one is tied in a noose.",
        ("Refrigerator", "The Mimic"): "Photos of you are stuck to every surface inside. You didn't put them there.",
        ("Refrigerator", "The Nurse"): "Blood bags and organ containers fill the fridge. 'TRANSPLANT' labels everywhere.",
        
        # Bookshelf messages
        ("Bookshelf", "Bonnie"): "The books are singed. One is titled 'HOW I DIED IN THE FIRE.'",
        ("Bookshelf", "Poltergeist"): "Books fly off the shelf! Pages tear and flutter like angry birds!",
        ("Bookshelf", "Weeping Lady"): "The books are waterlogged and ruined. Ink tears stream down the spines.",
        ("Bookshelf", "Shadow Stalker"): "A dark gap appears between books. Something moves in the darkness.",
        ("Bookshelf", "Little Timmy"): "Children's books appear. 'GOODBYE MOMMY' is written inside each one.",
        ("Bookshelf", "The Butcher"): "Cookbooks with disturbing titles: 'TO SERVE MAN', 'LONG PIG RECIPES'.",
        ("Bookshelf", "Ethereal Bride"): "Wedding planners and romance novels fill the shelf. All underlined passages about betrayal.",
        ("Bookshelf", "The Librarian"): "Every book opens to the same page: 'OVERDUE. PENALTY: DEATH.'",
        ("Bookshelf", "Nightmare"): "The books contain your diary entries. Secrets you've never written.",
        ("Bookshelf", "The Collector"): "First editions, rare manuscripts, stolen texts. All catalogued obsessively.",
        ("Bookshelf", "The Burned Man"): "The books smolder. Titles are burned away but you can feel them watching.",
        ("Bookshelf", "The Doll"): "Tiny books for dolls are mixed with regular ones. The titles are disturbing.",
        ("Bookshelf", "The Hanged Man"): "Every book is about death by hanging. Historical, fictional, instructional.",
        ("Bookshelf", "The Mimic"): "Every book is about you. Your life story, written before you lived it.",
        ("Bookshelf", "The Nurse"): "Medical textbooks. Lobotomy, experimental surgery, patient zero.",
        
        # Old Sofa messages
        ("Old Sofa", "Bonnie"): "The cushions are scorched in a sitting pattern. Someone burned here.",
        ("Old Sofa", "Poltergeist"): "The sofa levitates and drops! Cushions explode with stuffing!",
        ("Old Sofa", "Weeping Lady"): "The sofa is soaked with tears. Sitting here makes you inexplicably sad.",
        ("Old Sofa", "Shadow Stalker"): "Someone is sitting on the sofa. You can see the indent. But no one is there.",
        ("Old Sofa", "Little Timmy"): "Toys are tucked between the cushions. A child's blanket is draped over the arm.",
        ("Old Sofa", "The Butcher"): "Dark stains soak through the fabric. The cushions squish wetly.",
        ("Old Sofa", "Ethereal Bride"): "A bride's bouquet rests on the cushions. The flowers are dead but arranged perfectly.",
        ("Old Sofa", "The Librarian"): "Books are stacked on every surface. Sitting here would damage them.",
        ("Old Sofa", "Nightmare"): "The sofa's pattern forms faces. They're screaming.",
        ("Old Sofa", "The Collector"): "Trinkets are stuffed in every crevice. Someone hoards here.",
        ("Old Sofa", "The Burned Man"): "The sofa smolders. Smoke rises from the fabric.",
        ("Old Sofa", "The Doll"): "Dolls are arranged sitting on the sofa. Having a tea party. They turn to watch you.",
        ("Old Sofa", "The Hanged Man"): "Rope marks are worn into the armrests. Like someone was tied here.",
        ("Old Sofa", "The Mimic"): "An indent shows someone your exact size was just sitting here.",
        ("Old Sofa", "The Nurse"): "A hospital gown is draped over the arm. A patient bracelet is on the cushion.",
        
        # Nightstand messages  
        ("Nightstand", "Bonnie"): "The diary entries describe a fire. The last page says 'IT'S SPREADING.'",
        ("Nightstand", "Poltergeist"): "The drawer flies open! Contents scatter everywhere!",
        ("Nightstand", "Weeping Lady"): "The diary is soaked with tears. The ink has run, but you can read 'WHY?'",
        ("Nightstand", "Shadow Stalker"): "The drawer contains only darkness. Your hand goes in further than possible.",
        ("Nightstand", "Little Timmy"): "A child's drawing is in the drawer. It shows a family. One member is crossed out.",
        ("Nightstand", "The Butcher"): "A cleaver is hidden in the drawer. It's well-used.",
        ("Nightstand", "Ethereal Bride"): "Wedding rings are scattered in the drawer. Dozens of them.",
        ("Nightstand", "The Librarian"): "Library cards fill the drawer. All are overdue by decades.",
        ("Nightstand", "Nightmare"): "The drawer contains photos of you sleeping. Taken from inside the room.",
        ("Nightstand", "The Collector"): "The drawer won't close. It's stuffed with random objects.",
        ("Nightstand", "The Burned Man"): "The drawer is ash. Everything inside has been incinerated.",
        ("Nightstand", "The Doll"): "A doll is tucked into the drawer like a bed. It blinks at you.",
        ("Nightstand", "The Hanged Man"): "Suicide notes fill the drawer. Different handwriting. Different dates.",
        ("Nightstand", "The Mimic"): "The diary is yours. But you didn't write these entries.",
        ("Nightstand", "The Nurse"): "Medication bottles fill the drawer. All are empty. All are yours.",
        
        # Medicine Cabinet messages
        ("Medicine Cabinet", "Bonnie"): "The mirror is cracked from heat. Burn cream fills every shelf.",
        ("Medicine Cabinet", "Poltergeist"): "Pills explode from bottles! Everything flies off the shelves!",
        ("Medicine Cabinet", "Weeping Lady"): "The bottles are filled with tears. Labels read 'FOR SORROW.'",
        ("Medicine Cabinet", "Shadow Stalker"): "The cabinet is empty. Just darkness. Something moves inside.",
        ("Medicine Cabinet", "Little Timmy"): "Children's vitamins spell out 'HELP ME' on the shelf.",
        ("Medicine Cabinet", "The Butcher"): "Surgical tools replace the medicine. They're recently used.",
        ("Medicine Cabinet", "Ethereal Bride"): "Wedding makeup fills the cabinet. Lipstick writes 'HE LEFT ME' on the mirror.",
        ("Medicine Cabinet", "The Librarian"): "Books are crammed in the medicine cabinet. No medicine remains.",
        ("Medicine Cabinet", "Nightmare"): "All the bottles are labeled with your name. 'TAKE UNTIL DEAD.'",
        ("Medicine Cabinet", "The Collector"): "Pills of every color and type. Collected from unknown sources.",
        ("Medicine Cabinet", "The Burned Man"): "Everything is melted together. The smell of chemicals burns.",
        ("Medicine Cabinet", "The Doll"): "Doll medicine bottles. 'FOR DOLLY' labels. Tiny syringes.",
        ("Medicine Cabinet", "The Hanged Man"): "Rope burn cream. Neck braces. Autopsy reports.",
        ("Medicine Cabinet", "The Mimic"): "Your prescriptions. Your dosages. But you don't take medication.",
        ("Medicine Cabinet", "The Nurse"): "The cabinet is organized perfectly. 'NURSE BRADLEY'S SUPPLY.'",
        
        # Dining Table messages
        ("Dining Table", "Bonnie"): "Scorch marks show where someone sat. Place settings are charred.",
        ("Dining Table", "Poltergeist"): "Plates and silverware fly across the room! The table flips!",
        ("Dining Table", "Weeping Lady"): "The table is set for a dinner that never happened. Soup bowls hold only tears.",
        ("Dining Table", "Shadow Stalker"): "Shadow figures sit at each chair. They watch you.",
        ("Dining Table", "Little Timmy"): "A child's place setting appears. A high chair materializes.",
        ("Dining Table", "The Butcher"): "The table is a butcher's block. Cleaver marks score the surface.",
        ("Dining Table", "Ethereal Bride"): "Wedding feast is set but rotted. Place cards read 'BRIDE' and 'GROOM (ABSENT).'",
        ("Dining Table", "The Librarian"): "Books are stacked as place settings. Eating here is forbidden.",
        ("Dining Table", "Nightmare"): "The food shows your fears. Your dead grandmother serves dinner.",
        ("Dining Table", "The Collector"): "Every piece of silverware is different. Stolen from different homes.",
        ("Dining Table", "The Burned Man"): "The table is on fire! No wait... the flames are memories.",
        ("Dining Table", "The Doll"): "Dolls are seated at each chair. The table is set for their tea party.",
        ("Dining Table", "The Hanged Man"): "A noose hangs above each chair. The centerpiece is rope.",
        ("Dining Table", "The Mimic"): "Photos of you are the place cards. Your face at every seat.",
        ("Dining Table", "The Nurse"): "Hospital trays instead of plates. 'PATIENT DIET' labels on each.",
        
        # Toilet messages
        ("Toilet", "Bonnie"): "Steam rises from the bowl. The water is scalding hot.",
        ("Toilet", "Poltergeist"): "The lid slams up and down! Water sprays everywhere!",
        ("Toilet", "Weeping Lady"): "The bowl overflows with tears. It never stops filling.",
        ("Toilet", "Shadow Stalker"): "The bowl is filled with darkness. It seems to go down forever.",
        ("Toilet", "Little Timmy"): "A toy boat floats in the bowl. It sails in circles.",
        ("Toilet", "The Butcher"): "The water is thick and red. Something clogs the drain.",
        ("Toilet", "Ethereal Bride"): "Wedding rings fill the bowl. Thrown away in anger.",
        ("Toilet", "The Librarian"): "Torn book pages float in the bowl. 'BANNED' is watermarked on each.",
        ("Toilet", "Nightmare"): "Your face stares up from the water. It's drowning.",
        ("Toilet", "The Collector"): "Coins fill the bowl. Thrown in like a wishing well.",
        ("Toilet", "The Burned Man"): "The water boils. Steam scalds the air.",
        ("Toilet", "The Doll"): "Doll heads bob in the water. Their eyes are open.",
        ("Toilet", "The Hanged Man"): "Rope spirals down into the drain. It's attached to something below.",
        ("Toilet", "The Mimic"): "Your reflection ripples in the water. It doesn't match your movements.",
        ("Toilet", "The Nurse"): "Medical waste floats in the bowl. 'BIOHAZARD' warnings everywhere.",
        
        # Window messages  
        ("Window", "Bonnie"): "The glass is cracked from heat. Outside, you see flames that aren't there.",
        ("Window", "Poltergeist"): "The window slams open and shut! The glass cracks then repairs!",
        ("Window", "Weeping Lady"): "Rain streams down the inside of the glass. But it's not raining.",
        ("Window", "Shadow Stalker"): "The window shows only darkness. Day or night, it's always black outside.",
        ("Window", "Little Timmy"): "A child waves from outside the window. You're on the second floor.",
        ("Window", "The Butcher"): "Bloody handprints cover the glass. From the outside.",
        ("Window", "Ethereal Bride"): "A bride stands outside, staring in. She's been waiting for decades.",
        ("Window", "The Librarian"): "'SILENCE' is written in the frost. The letters appear on their own.",
        ("Window", "Nightmare"): "The window shows your fears. Whatever you're most afraid of, it's out there.",
        ("Window", "The Collector"): "Items are displayed on the windowsill. They weren't there before.",
        ("Window", "The Burned Man"): "The window is too hot to touch. Smoke fills the view.",
        ("Window", "The Doll"): "Dolls are pressed against the glass from outside. Watching.",
        ("Window", "The Hanged Man"): "A silhouette hangs outside the window. It swings gently.",
        ("Window", "The Mimic"): "You see yourself standing outside, trying to get in.",
        ("Window", "The Nurse"): "The window shows a hospital room. It's yours. You're in the bed.",
        
        # Outdoor objects - Old Swing Set
        ("Old Swing Set", "Little Timmy"): "The swing moves on its own. A child's laughter echoes.",
        ("Old Swing Set", "The Twins"): "Both swings move in perfect synchronization. They're giggling.",
        ("Old Swing Set", "The Doll"): "A porcelain doll sits on the swing. It wasn't there before.",
        ("Old Swing Set", "Shadow Stalker"): "A dark figure sits on the swing. It has no face.",
        ("Old Swing Set", "The Gardener"): "Vines are wrapping around the chains. Growing fast.",
        ("Old Swing Set", "Nightmare"): "The swing holds a version of yourself as a child. Dead.",
        
        # Dead Tree
        ("Dead Tree", "The Hanged Man"): "Multiple nooses hang from every branch. All swinging.",
        ("Dead Tree", "The Gardener"): "The tree is blooming with black flowers. They smell of death.",
        ("Dead Tree", "Shadow Stalker"): "The tree's shadow moves independently. It reaches for you.",
        ("Dead Tree", "Little Timmy"): "Carved into the bark: 'TIMMY WAS HERE.' The carving is fresh.",
        ("Dead Tree", "The Witch"): "Symbols are carved all over the trunk. The tree bleeds sap.",
        ("Dead Tree", "Nightmare"): "Every branch holds a body. They all have your face.",
        
        # Garden Statue
        ("Garden Statue", "Weeping Lady"): "The statue weeps real tears. An endless stream down stone cheeks.",
        ("Garden Statue", "The Artist"): "The statue changes poses when you're not looking.",
        ("Garden Statue", "The Collector"): "Objects have been placed as offerings at its feet.",
        ("Garden Statue", "Nightmare"): "The statue has YOUR face. It's screaming silently.",
        ("Garden Statue", "The Gardener"): "Moss and vines cover the statue like a shroud.",
        ("Garden Statue", "Shadow Stalker"): "The statue casts a shadow even in complete darkness.",
        
        # Rose Bushes
        ("Rose Bushes", "The Gardener"): "The roses are blood red and alive. Thorns reach for you.",
        ("Rose Bushes", "Weeping Lady"): "White roses drip with tears. The petals fall like sobs.",
        ("Rose Bushes", "The Butcher"): "The roses grow from buried bones. You can see them.",
        ("Rose Bushes", "Ethereal Bride"): "A bridal bouquet lies among the thorns, perfectly preserved.",
        ("Rose Bushes", "The Witch"): "The roses glow faintly with unholy light.",
        
        # Compost Pile
        ("Compost Pile", "The Gardener"): "Something is growing in the compost. It has hands.",
        ("Compost Pile", "The Butcher"): "Bones protrude from the pile. Human bones.",
        ("Compost Pile", "Shadow Stalker"): "The pile moves on its own. Something lives inside.",
        ("Compost Pile", "The Gravedigger"): "Freshly turned earth. Something was just buried here.",
        
        # Tool Rack
        ("Tool Rack", "The Gardener"): "The tools are coated in fresh blood. They were just used.",
        ("Tool Rack", "The Butcher"): "Meat hooks hang among the garden tools. Still dripping.",
        ("Tool Rack", "Shadow Stalker"): "A tool is missing. You hear scraping sounds behind you.",
        ("Tool Rack", "The Hanged Man"): "Rope coils among the tools. It ties itself into nooses.",
        
        # Patio Table
        ("Patio Table", "The Servant"): "Tea has been served. It's still warm. Who poured it?",
        ("Patio Table", "Ethereal Bride"): "A wedding reception layout. Champagne still bubbles.",
        ("Patio Table", "Shadow Stalker"): "Something sits at the table. You can only see it from the corner of your eye.",
        ("Patio Table", "The Collector"): "Strange items are arranged on the table. A collection of victims.",
        
        # Wind Chimes
        ("Wind Chimes", "The Musician"): "The chimes play a melody. It's hauntingly beautiful.",
        ("Wind Chimes", "The Twins"): "The chimes spell out letters. H-E-L-P.",
        ("Wind Chimes", "Nightmare"): "The chimes make a sound like screaming.",
        ("Wind Chimes", "Poltergeist"): "The chimes spin violently! The sound is deafening!",
        
        # Fertilizer Bags
        ("Fertilizer Bags", "The Gardener"): "The bags are labeled 'SPECIAL FERTILIZER.' They smell wrong.",
        ("Fertilizer Bags", "The Butcher"): "Some bags are leaking. It's not fertilizer.",
        ("Fertilizer Bags", "Shadow Stalker"): "A bag moves on its own. Something is inside.",
        ("Fertilizer Bags", "The Gravedigger"): "Lime bags are stacked here. Lots of them.",
        
        # Sliding Glass Door
        ("Sliding Glass Door", "Shadow Stalker"): "A dark figure stands on the other side. It waves.",
        ("Sliding Glass Door", "The Mimic"): "Your reflection doesn't match your movements.",
        ("Sliding Glass Door", "Little Timmy"): "Child's handprints cover the glass. They appear as you watch.",
        ("Sliding Glass Door", "The Gardener"): "Vines are trying to grow through the glass.",
        ("Sliding Glass Door", "Nightmare"): "What's on the other side isn't your backyard.",
        ("Sliding Glass Door", "Poltergeist"): "The door slides open and closed on its own.",
    }
    
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
        self.affected_by_ghost = None  # Which ghost affected it
        self.affect_timer = 0  # How long the effect lasts
        
    def apply_ghost_effect(self, behavior, ghost_name=None):
        """Apply a ghost behavior effect to this object"""
        self.ghost_affected = True
        self.affected_by_behavior = behavior
        self.affected_by_ghost = ghost_name
        self.affect_timer = 30.0  # Effect lasts 30 seconds
        
    def update(self, dt):
        """Update object state"""
        if self.affect_timer > 0:
            self.affect_timer -= dt
            if self.affect_timer <= 0:
                self.ghost_affected = False
                self.affected_by_behavior = None
                self.affected_by_ghost = None
        
    def get_description(self, ghost=None, flashlight_on=False):
        """Get the appropriate description based on state"""
        # If ghost affected this object, show affected description
        if self.ghost_affected:
            # Check for unique ghost+object message first
            ghost_name = self.affected_by_ghost
            if ghost_name:
                key = (self.name, ghost_name)
                if key in self.GHOST_OBJECT_MESSAGES:
                    return self.GHOST_OBJECT_MESSAGES[key]
            
            # Then check for behavior-specific description
            if self.affected_by_behavior and self.affected_by_behavior in self.affected_descriptions:
                return self.affected_descriptions[self.affected_by_behavior]
            
            # Finally use generic affected description
            return self._get_generic_affected_description()
        
        # If using flashlight and ghost-specific description exists
        if flashlight_on and ghost and ghost.name in self.ghost_descriptions:
            return self.ghost_descriptions[ghost.name]
            
        return self.zoom_description if self.zoom_description else self.description
    
    def _get_generic_affected_description(self):
        """Get a generic description based on the behavior that affected it"""
        behavior = self.affected_by_behavior
        if not behavior:
            return f"Something is wrong with the {self.name}. It feels... different."
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
    
    def apply_ghost_behavior_to_object(self, behavior, ghost_name=None):
        """Apply a ghost behavior to a random object in this room"""
        if not self.objects:
            return None
        # Pick a random object
        obj = random.choice(self.objects)
        obj.apply_ghost_effect(behavior, ghost_name)
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
            connections={"left": ROOM_ENTRANCE, "right": ROOM_KITCHEN, "up": ROOM_BEDROOM, "down": ROOM_BACKYARD},
            base_color=(85, 75, 70),
            description="A once-cozy living room. A cold fireplace dominates one wall. A sliding glass door leads to the backyard."
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
        self.add_object(InteractiveObject(
            "Sliding Glass Door",
            (550, 480, 180, 120),
            "A sliding glass door leading to the backyard. Handprints smear the glass.",
            "examine",
            "Through the dirty glass, you see the overgrown backyard. Something moves in the shadows."
        ))
        # Hidden clues
        self.add_hidden_clue(550, 550, "IT BURNS", "The Burned Man")
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


# ============== OUTDOOR ROOMS ==============

class BackyardRoom(Room):
    """The backyard area - accessed from living room via sliding glass door"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_BACKYARD,
            display_name="Backyard",
            connections={"left": ROOM_LIVING_ROOM, "right": ROOM_GARDEN, "up": ROOM_PATIO, "down": ROOM_TOOLSHED},
            base_color=(40, 60, 40),  # Dark grass color
            description="A neglected backyard overgrown with weeds. The moon casts long shadows across the dead grass."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Sliding Glass Door",
            (50, 200, 100, 250),
            "A sliding glass door leading back inside. Handprints smear the glass.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Old Swing Set",
            (400, 280, 200, 200),
            "A rusted swing set. One swing moves slowly on its own.",
            "examine",
            "The swing creaks rhythmically. You hear a child's laughter..."
        ))
        self.add_object(InteractiveObject(
            "Dead Tree",
            (800, 150, 150, 350),
            "A massive dead oak tree. Something hangs from a high branch.",
            "zoom",
            "Looking closer, you see rope marks worn into the branch. A noose dangles in the moonlight."
        ))
        self.add_object(InteractiveObject(
            "Abandoned Grill",
            (1000, 350, 100, 120),
            "An old charcoal grill. The smell of burned meat lingers.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(500, 450, "BURIED HERE", "The Gardener")
        self.add_hidden_clue(850, 500, "HELP US", "The Twins")
    
    def draw_base(self, surface):
        # Night sky
        pygame.draw.rect(surface, (10, 15, 30), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.3))
        # Stars
        star_positions = [(100, 50), (300, 80), (500, 40), (700, 90), (900, 60), (1100, 70)]
        for x, y in star_positions:
            pygame.draw.circle(surface, (200, 200, 220), (x, y), 2)
        # Moon
        pygame.draw.circle(surface, (220, 220, 200), (1100, 80), 40)
        pygame.draw.circle(surface, (10, 15, 30), (1090, 70), 35)  # Crescent
        # Grass/ground
        pygame.draw.rect(surface, (30, 50, 30), (0, SCREEN_HEIGHT * 0.3, SCREEN_WIDTH, SCREEN_HEIGHT * 0.7))
        # Grass texture
        for i in range(0, SCREEN_WIDTH, 20):
            height = 10 + (i % 30)
            pygame.draw.line(surface, (40, 70, 40), (i, SCREEN_HEIGHT * 0.6), (i + 5, SCREEN_HEIGHT * 0.6 - height), 2)
        # Fence in background
        for i in range(0, SCREEN_WIDTH, 60):
            pygame.draw.rect(surface, (60, 40, 30), (i, int(SCREEN_HEIGHT * 0.25), 10, 80))
        pygame.draw.rect(surface, (50, 35, 25), (0, int(SCREEN_HEIGHT * 0.28), SCREEN_WIDTH, 8))
    
    def draw_details(self, surface):
        # Sliding glass door (to house)
        pygame.draw.rect(surface, (40, 40, 50), (50, 200, 100, 250))
        pygame.draw.rect(surface, (60, 70, 90), (55, 205, 90, 240))
        pygame.draw.line(surface, (80, 80, 90), (100, 205), (100, 445), 2)
        # Light from inside
        pygame.draw.rect(surface, (100, 90, 60), (55, 205, 90, 240))
        
        # Swing set
        pygame.draw.rect(surface, (100, 60, 40), (450, 280, 10, 200))  # Left pole
        pygame.draw.rect(surface, (100, 60, 40), (590, 280, 10, 200))  # Right pole
        pygame.draw.rect(surface, (100, 60, 40), (440, 280, 170, 10))  # Top bar
        # Swings
        pygame.draw.line(surface, (80, 80, 80), (480, 290), (480, 380), 2)  # Chain
        pygame.draw.line(surface, (80, 80, 80), (500, 290), (500, 380), 2)
        pygame.draw.rect(surface, (60, 40, 30), (470, 380, 40, 10))  # Seat
        # Moving swing
        swing_offset = 20 if (self.effect_frame // 30) % 2 == 0 else -20
        pygame.draw.line(surface, (80, 80, 80), (550 + swing_offset, 290), (550, 400), 2)
        pygame.draw.line(surface, (80, 80, 80), (570 + swing_offset, 290), (570, 400), 2)
        pygame.draw.rect(surface, (60, 40, 30), (540, 400, 40, 10))
        
        # Dead tree
        pygame.draw.rect(surface, (60, 45, 35), (850, 150, 50, 350))  # Trunk
        # Branches
        pygame.draw.line(surface, (50, 40, 30), (875, 200), (750, 150), 8)
        pygame.draw.line(surface, (50, 40, 30), (875, 180), (950, 100), 8)
        pygame.draw.line(surface, (50, 40, 30), (875, 250), (1000, 200), 6)
        # Noose
        pygame.draw.line(surface, (120, 100, 80), (780, 150), (780, 220), 3)
        pygame.draw.circle(surface, (120, 100, 80), (780, 240), 20, 3)
        
        # Grill
        pygame.draw.ellipse(surface, (40, 40, 45), (1000, 350, 100, 60))
        pygame.draw.rect(surface, (35, 35, 40), (1010, 400, 80, 50))
        pygame.draw.rect(surface, (60, 50, 40), (1040, 450, 20, 30))


class GardenRoom(Room):
    """The overgrown garden - home of The Gardener ghost"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_GARDEN,
            display_name="Garden",
            connections={"left": ROOM_BACKYARD},
            base_color=(35, 55, 35),
            description="An overgrown garden with dead plants and wilted flowers. Something moves among the thorns."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Rose Bushes",
            (200, 300, 200, 150),
            "Dead rose bushes with blackened thorns.",
            "examine",
            "Among the dead roses, you find a single fresh bloom. Blood red."
        ))
        self.add_object(InteractiveObject(
            "Garden Statue",
            (600, 250, 100, 200),
            "A weathered angel statue. Its face has been worn away.",
            "zoom",
            "The statue's hands are positioned as if reaching for something. Or someone."
        ))
        self.add_object(InteractiveObject(
            "Compost Pile",
            (900, 350, 150, 100),
            "A rotting compost pile. Something is buried underneath.",
            "examine",
            "Digging reveals old bones. Too large to be animal bones..."
        ))
        self.add_object(InteractiveObject(
            "Garden Shed Key",
            (1100, 400, 50, 50),
            "A rusted key hanging from a hook.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(400, 500, "THEY NEVER LEFT", "The Gardener")
        self.add_hidden_clue(750, 350, "FERTILIZER", None)
    
    def draw_base(self, surface):
        # Night sky
        pygame.draw.rect(surface, (10, 15, 30), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.3))
        # Ground
        pygame.draw.rect(surface, (25, 45, 25), (0, SCREEN_HEIGHT * 0.3, SCREEN_WIDTH, SCREEN_HEIGHT * 0.7))
        # Dirt patches
        for x in range(100, SCREEN_WIDTH, 200):
            pygame.draw.ellipse(surface, (60, 45, 35), (x, SCREEN_HEIGHT * 0.6, 120, 60))
    
    def draw_details(self, surface):
        # Rose bushes
        for i in range(5):
            x = 200 + i * 40
            pygame.draw.ellipse(surface, (30, 50, 30), (x, 300 + (i % 2) * 20, 50, 80))
            # Thorns
            pygame.draw.line(surface, (80, 60, 40), (x + 25, 320), (x + 40, 310), 2)
        # One red rose
        pygame.draw.circle(surface, (150, 30, 30), (300, 340), 8)
        
        # Angel statue
        pygame.draw.rect(surface, (150, 150, 160), (640, 400, 40, 50))  # Base
        pygame.draw.ellipse(surface, (160, 160, 170), (610, 280, 100, 150))  # Body
        pygame.draw.circle(surface, (170, 170, 180), (660, 270), 30)  # Head
        # Wings
        pygame.draw.ellipse(surface, (180, 180, 190), (580, 300, 40, 80))
        pygame.draw.ellipse(surface, (180, 180, 190), (700, 300, 40, 80))
        # Worn face
        pygame.draw.rect(surface, (140, 140, 150), (650, 260, 20, 20))
        
        # Compost pile
        pygame.draw.ellipse(surface, (60, 50, 40), (900, 350, 150, 100))
        pygame.draw.ellipse(surface, (50, 40, 30), (920, 360, 110, 70))
        # Bones peeking out
        pygame.draw.line(surface, (200, 195, 180), (950, 400), (970, 420), 3)


class PatioRoom(Room):
    """The patio area with outdoor furniture"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_PATIO,
            display_name="Patio",
            connections={"down": ROOM_BACKYARD},
            base_color=(80, 70, 65),
            description="A stone patio with broken furniture. The wind chimes ring without wind."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Patio Table",
            (400, 300, 250, 150),
            "A wrought iron table with four chairs. One chair is always pulled out.",
            "examine",
            "Tea cups sit on the table, still warm. But no one is here..."
        ))
        self.add_object(InteractiveObject(
            "Wind Chimes",
            (800, 150, 80, 150),
            "Wind chimes that ring in the still air.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Potted Plants",
            (100, 350, 150, 100),
            "Dead potted plants in cracked pots.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Outdoor Fireplace",
            (1000, 200, 150, 250),
            "A stone fireplace. Cold ashes remain.",
            "examine"
        ))
    
    def draw_base(self, surface):
        # Night sky
        pygame.draw.rect(surface, (10, 15, 30), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT * 0.25))
        # Stone patio
        for y in range(int(SCREEN_HEIGHT * 0.25), SCREEN_HEIGHT, 60):
            for x in range(0, SCREEN_WIDTH, 80):
                color = (75, 70, 65) if (x + y) % 160 == 0 else (85, 80, 75)
                pygame.draw.rect(surface, color, (x, y, 78, 58))
    
    def draw_details(self, surface):
        # Patio table
        pygame.draw.ellipse(surface, (50, 50, 55), (400, 300, 250, 100))  # Table top
        pygame.draw.rect(surface, (40, 40, 45), (510, 380, 30, 100))  # Table leg
        # Chairs
        chair_positions = [(350, 350), (600, 350), (420, 420), (530, 420)]
        for i, (cx, cy) in enumerate(chair_positions):
            pygame.draw.rect(surface, (50, 50, 55), (cx, cy, 40, 50))
            # One chair pulled out
            if i == 2:
                pygame.draw.rect(surface, (50, 50, 55), (cx - 30, cy + 20, 40, 50))
        # Tea cups
        pygame.draw.ellipse(surface, (200, 200, 210), (450, 320, 30, 20))
        pygame.draw.ellipse(surface, (200, 200, 210), (520, 330, 30, 20))
        
        # Wind chimes
        pygame.draw.rect(surface, (100, 80, 60), (820, 100, 40, 10))
        chime_offset = 5 if (self.effect_frame // 20) % 2 == 0 else -5
        for i in range(5):
            pygame.draw.line(surface, (180, 180, 190), (810 + i * 12 + chime_offset, 110), 
                           (810 + i * 12, 110 + 30 + i * 10), 2)
        
        # Stone fireplace
        pygame.draw.rect(surface, (100, 90, 85), (1000, 200, 150, 250))
        pygame.draw.rect(surface, (40, 35, 30), (1020, 280, 110, 150))
        pygame.draw.rect(surface, (110, 100, 95), (990, 180, 170, 25))


class ToolshedRoom(Room):
    """A creepy toolshed with rusty implements"""
    
    def __init__(self):
        super().__init__(
            name=ROOM_TOOLSHED,
            display_name="Tool Shed",
            connections={"up": ROOM_BACKYARD},
            base_color=(60, 50, 45),
            description="A cramped tool shed filled with rusty implements. Something scratches at the walls."
        )
    
    def setup_room(self):
        self.add_object(InteractiveObject(
            "Tool Rack",
            (100, 150, 200, 300),
            "A rack of garden tools. The shovel has dried mud... and something else.",
            "examine",
            "The shovel's blade has scratch marks. Like someone was trying to dig out."
        ))
        self.add_object(InteractiveObject(
            "Workbench",
            (400, 300, 250, 100),
            "A cluttered workbench covered in rust and old blood.",
            "zoom",
            "Among the tools, you find photographs of the previous owners. All scratched out."
        ))
        self.add_object(InteractiveObject(
            "Fertilizer Bags",
            (800, 350, 150, 120),
            "Stacked bags of fertilizer. Some are strangely lumpy.",
            "examine"
        ))
        self.add_object(InteractiveObject(
            "Locked Cabinet",
            (1050, 200, 100, 200),
            "A padlocked metal cabinet. Something rattles inside.",
            "examine"
        ))
        # Hidden clues
        self.add_hidden_clue(300, 450, "DIG DEEPER", "The Gardener")
        self.add_hidden_clue(600, 380, "BONES", "The Butcher")
    
    def draw_base(self, surface):
        # Wooden walls
        for x in range(0, SCREEN_WIDTH, 40):
            color = (55, 45, 40) if x % 80 == 0 else (60, 50, 45)
            pygame.draw.rect(surface, color, (x, 0, 38, SCREEN_HEIGHT))
        # Floor
        pygame.draw.rect(surface, (50, 40, 35), (0, SCREEN_HEIGHT * 0.6, SCREEN_WIDTH, SCREEN_HEIGHT * 0.4))
    
    def draw_details(self, surface):
        # Tool rack
        pygame.draw.rect(surface, (80, 60, 50), (100, 150, 200, 20))
        pygame.draw.rect(surface, (80, 60, 50), (100, 250, 200, 20))
        pygame.draw.rect(surface, (80, 60, 50), (100, 350, 200, 20))
        # Tools
        # Shovel
        pygame.draw.rect(surface, (100, 80, 60), (120, 170, 10, 150))
        pygame.draw.rect(surface, (120, 120, 130), (110, 320, 30, 40))
        # Rake
        pygame.draw.rect(surface, (100, 80, 60), (180, 170, 8, 120))
        pygame.draw.rect(surface, (100, 100, 110), (160, 290, 50, 5))
        # Hoe
        pygame.draw.rect(surface, (100, 80, 60), (240, 180, 8, 100))
        pygame.draw.rect(surface, (110, 110, 120), (230, 275, 30, 20))
        
        # Workbench
        pygame.draw.rect(surface, (70, 55, 45), (400, 300, 250, 20))
        pygame.draw.rect(surface, (60, 45, 35), (410, 320, 30, 100))
        pygame.draw.rect(surface, (60, 45, 35), (610, 320, 30, 100))
        # Blood stains
        pygame.draw.ellipse(surface, (80, 30, 30), (500, 290, 60, 20))
        
        # Fertilizer bags
        for i in range(3):
            pygame.draw.rect(surface, (150, 130, 100), (800 + i * 20, 350 - i * 30, 80, 60))
        
        # Locked cabinet
        pygame.draw.rect(surface, (80, 80, 90), (1050, 200, 100, 200))
        pygame.draw.rect(surface, (70, 70, 80), (1055, 205, 90, 190))
        pygame.draw.circle(surface, (150, 130, 50), (1100, 300), 10)  # Lock
        
        # Single hanging light
        pygame.draw.line(surface, (60, 60, 60), (640, 0), (640, 100), 2)
        if self.lights_on:
            light_color = (180, 160, 80) if random.random() > 0.3 else (100, 90, 50)
        else:
            light_color = (80, 70, 40)
        pygame.draw.circle(surface, light_color, (640, 110), 15)


def create_all_rooms():
    """Create and return a dictionary of all rooms for the haunted house"""
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
        # Outdoor rooms
        ROOM_BACKYARD: BackyardRoom(),
        ROOM_GARDEN: GardenRoom(),
        ROOM_PATIO: PatioRoom(),
        ROOM_TOOLSHED: ToolshedRoom(),
    }
    return rooms


def create_rooms_for_location(location_id):
    """Create rooms for a specific location"""
    # For now, return haunted house rooms
    # This can be expanded later with more location-specific rooms
    return create_all_rooms()
