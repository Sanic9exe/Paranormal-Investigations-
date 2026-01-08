"""
Ghost hunting equipment for Paranormal Investigations
"""

import pygame
import random
import math
from constants import *


class Equipment:
    """Base class for ghost hunting equipment"""
    
    def __init__(self, name, icon_char):
        self.name = name
        self.icon_char = icon_char
        self.active = False
        self.cooldown = 0
        self.reading = None
        
    def update(self, dt, ghost_nearby, ghost_distance, ghost=None):
        """Update equipment state"""
        if self.cooldown > 0:
            self.cooldown -= dt
            
    def get_display_value(self):
        """Get the value to display"""
        return str(self.reading) if self.reading else "---"
        
    def draw_ui(self, surface, rect, font):
        """Draw the equipment UI"""
        pass


class Flashlight(Equipment):
    """Flashlight with battery"""
    
    def __init__(self):
        super().__init__("Flashlight", "F")
        self.battery = FLASHLIGHT_BATTERY_MAX
        self.flickering = False
        self.flicker_timer = 0
        
    def update(self, dt, ghost_nearby=False, ghost_distance=0, ghost=None):
        super().update(dt, ghost_nearby, ghost_distance, ghost)
        
        if self.active:
            # Drain battery faster when ghost is nearby
            drain_multiplier = FLASHLIGHT_GHOST_DRAIN_MULTIPLIER if ghost_nearby else 1.0
            self.battery -= FLASHLIGHT_DRAIN_RATE * dt * drain_multiplier
            self.battery = max(0, self.battery)
            
            # Flickering when low battery or ghost nearby
            if self.battery < FLASHLIGHT_FLICKER_THRESHOLD or ghost_nearby:
                self.flicker_timer += dt
                self.flickering = math.sin(self.flicker_timer * 20) > 0.3
            else:
                self.flickering = False
                
            # Turn off when empty
            if self.battery <= 0:
                self.active = False
                
    def recharge(self, amount=20):
        """Recharge the battery"""
        self.battery = min(FLASHLIGHT_BATTERY_MAX, self.battery + amount)
        
    def get_display_value(self):
        return f"{int(self.battery)}%"
        
    def draw_beam(self, surface, mouse_pos, darkness_level=200):
        """Draw the flashlight beam with cone shape"""
        if not self.active or self.battery <= 0:
            return
            
        # Create darkness overlay
        darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        actual_darkness = darkness_level if not self.flickering else darkness_level + 50
        darkness.fill((0, 0, 0, min(255, actual_darkness)))
        
        mx, my = mouse_pos
        
        # Calculate beam parameters based on battery
        battery_factor = self.battery / FLASHLIGHT_BATTERY_MAX
        outer_radius = int(FLASHLIGHT_OUTER_RADIUS * (0.5 + 0.5 * battery_factor))
        
        # Create gradient flashlight with cone effect
        if not self.flickering or random.random() > 0.3:
            for r in range(outer_radius, 0, -5):
                alpha = int(actual_darkness * (r / outer_radius) * battery_factor)
                # Vary the alpha based on flicker state
                if self.flickering:
                    alpha = int(alpha * (0.7 + random.random() * 0.3))
                pygame.draw.circle(darkness, (0, 0, 0, actual_darkness - alpha), (mx, my), r)
        
        surface.blit(darkness, (0, 0))
        
        # Draw light glow effect
        if self.battery > 10:
            glow = pygame.Surface((100, 100), pygame.SRCALPHA)
            glow_alpha = int(50 * battery_factor)
            if not self.flickering:
                pygame.draw.circle(glow, (255, 255, 200, glow_alpha), (50, 50), 40)
                surface.blit(glow, (mx - 50, my - 50))


class EMFReader(Equipment):
    """EMF Reader to detect ghost activity"""
    
    def __init__(self):
        super().__init__("EMF Reader", "E")
        self.level = 0
        self.spike_timer = 0
        self.base_level = 0
        self.false_positive_timer = 0
        
    def update(self, dt, ghost_nearby=False, ghost_distance=100, ghost=None):
        super().update(dt, ghost_nearby, ghost_distance, ghost)
        
        if self.active:
            # Base EMF noise
            self.base_level = random.randint(0, 1)
            
            # False positive timer decay
            if self.false_positive_timer > 0:
                self.false_positive_timer -= dt
            
            # Random false positives (balance change)
            if not ghost_nearby and random.random() < EMF_FALSE_POSITIVE_CHANCE * dt:
                self.false_positive_timer = 0.8
                self.level = random.randint(2, 4)  # False spike
            
            # Ghost proximity affects reading
            elif ghost_nearby and ghost_distance < 300:
                # Closer = higher reading
                proximity_factor = 1 - (ghost_distance / 300)
                ghost_level = int(EMF_LEVEL_5 * proximity_factor)
                self.level = max(self.base_level, ghost_level)
                
                # Random spikes
                if random.random() < 0.05:
                    self.spike_timer = 0.5
                    self.level = EMF_LEVEL_5
            elif self.false_positive_timer <= 0:
                self.level = self.base_level
                
            # Handle spike decay
            if self.spike_timer > 0:
                self.spike_timer -= dt
            else:
                self.level = max(self.base_level, self.level - 1)
                
            self.reading = self.level
        else:
            self.reading = None
            
    def get_display_value(self):
        if self.reading is None:
            return "OFF"
        return f"EMF: {self.reading}"
        
    def draw_ui(self, surface, rect, font):
        """Draw EMF meter UI"""
        if not self.active:
            return
            
        # Background
        bg = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        bg.fill((20, 30, 20, 200))
        surface.blit(bg, rect)
        
        # Title
        title = font.render("EMF", True, GREEN)
        surface.blit(title, (rect.x + 5, rect.y + 5))
        
        # Level indicators
        for i in range(5):
            color = GREEN if i < self.level else DARK_GRAY
            if i == 4 and self.level == 5:
                color = RED  # Level 5 is red (ghost!)
            bar_rect = pygame.Rect(rect.x + 10 + i * 15, rect.y + 30, 12, 20)
            pygame.draw.rect(surface, color, bar_rect)


class Thermometer(Equipment):
    """Digital thermometer to detect cold spots"""
    
    def __init__(self):
        super().__init__("Thermometer", "T")
        self.temperature = TEMP_NORMAL_MAX
        self.target_temp = TEMP_NORMAL_MAX
        
    def update(self, dt, ghost_nearby=False, ghost_distance=100, ghost=None):
        super().update(dt, ghost_nearby, ghost_distance, ghost)
        
        if self.active:
            # Calculate target temperature
            if ghost_nearby and ghost_distance < 200:
                # Ghost makes it cold
                proximity = 1 - (ghost_distance / 200)
                self.target_temp = TEMP_FREEZING + (TEMP_COLD_MAX - TEMP_FREEZING) * (1 - proximity)
            else:
                # Return to normal
                self.target_temp = random.uniform(TEMP_NORMAL_MIN, TEMP_NORMAL_MAX)
                
            # Gradually move toward target - slower response (balance change)
            diff = self.target_temp - self.temperature
            self.temperature += diff * dt * TEMP_CHANGE_SPEED
            
            # Add some noise
            self.temperature += random.uniform(-0.5, 0.5)
            
            self.reading = self.temperature
        else:
            self.reading = None
            
    def get_display_value(self):
        if self.reading is None:
            return "OFF"
        return f"{self.reading:.1f}°F"
        
    def is_freezing(self):
        """Check if temperature indicates ghost"""
        return self.reading is not None and self.reading < TEMP_COLD_MIN
        
    def draw_ui(self, surface, rect, font):
        """Draw thermometer UI"""
        if not self.active:
            return
            
        # Background
        bg = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        bg.fill((20, 20, 30, 200))
        surface.blit(bg, rect)
        
        # Temperature display
        if self.reading:
            if self.reading < TEMP_COLD_MIN:
                color = CYAN  # Freezing!
            elif self.reading < TEMP_COLD_MAX:
                color = BLUE  # Cold
            else:
                color = WHITE  # Normal
                
            temp_text = font.render(f"{self.reading:.1f}°F", True, color)
            surface.blit(temp_text, (rect.x + 5, rect.y + 5))
            
            # Freezing warning
            if self.reading < TEMP_FREEZING:
                warn = font.render("FREEZING!", True, CYAN)
                surface.blit(warn, (rect.x + 5, rect.y + 30))


class SpiritBox(Equipment):
    """Spirit box for ghost communication"""
    
    RESPONSES = [
        "BEHIND", "HERE", "CLOSE", "LEAVE", "DIE", "HELP",
        "DEATH", "HATE", "KILL", "ATTACK", "RUN", "HIDE",
        "COLD", "DARK", "AFRAID", "ALONE", "HURT", "PAIN"
    ]
    
    def __init__(self):
        super().__init__("Spirit Box", "S")
        self.scanning = False
        self.response = None
        self.response_timer = 0
        self.static_offset = 0
        self.scan_frequency = 0
        self.response_cooldown = 0  # Cooldown between responses
        
    def update(self, dt, ghost_nearby=False, ghost_distance=100, ghost=None):
        super().update(dt, ghost_nearby, ghost_distance, ghost)
        
        if self.active:
            self.scanning = True
            self.scan_frequency += dt * 50
            self.static_offset = random.randint(-2, 2)
            
            # Response decay
            if self.response_timer > 0:
                self.response_timer -= dt
            else:
                self.response = None
                
            # Response cooldown (balance change)
            if self.response_cooldown > 0:
                self.response_cooldown -= dt
                
            # Random ghost responses - with cooldown
            if ghost_nearby and ghost_distance < 250 and self.response_cooldown <= 0:
                if random.random() < 0.01:  # 1% chance per frame when close
                    self.response = random.choice(self.RESPONSES)
                    self.response_timer = 2.0
                    self.response_cooldown = SPIRIT_BOX_RESPONSE_COOLDOWN  # 5s cooldown
        else:
            self.scanning = False
            self.response = None
            
    def get_display_value(self):
        if not self.active:
            return "OFF"
        if self.response:
            return self.response
        return "SCANNING..."
        
    def draw_ui(self, surface, rect, font):
        """Draw spirit box UI"""
        if not self.active:
            return
            
        # Background with static effect
        bg = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        static_color = 30 + random.randint(-10, 10)
        bg.fill((static_color, static_color, static_color + 10, 200))
        surface.blit(bg, rect)
        
        # Frequency display
        freq_text = font.render(f"{87.5 + (self.scan_frequency % 20):.1f} FM", True, GREEN)
        surface.blit(freq_text, (rect.x + 5, rect.y + 5))
        
        # Response or static
        if self.response:
            response_text = font.render(self.response, True, WHITE)
            x_offset = self.static_offset
            surface.blit(response_text, (rect.x + 5 + x_offset, rect.y + 30))
        else:
            static_text = font.render("~~~", True, GRAY)
            surface.blit(static_text, (rect.x + 5, rect.y + 30))


class UVLight(Equipment):
    """UV Light to reveal fingerprints and ghost traces"""
    
    def __init__(self):
        super().__init__("UV Light", "U")
        self.fingerprints = []
        self.reveal_timer = 0
        
    def update(self, dt, ghost_nearby=False, ghost_distance=100, ghost=None):
        super().update(dt, ghost_nearby, ghost_distance, ghost)
        
        if self.active and ghost_nearby:
            self.reveal_timer += dt
            # Reveal fingerprints over time
            if self.reveal_timer > 2 and len(self.fingerprints) < 5:
                if random.random() < 0.1:
                    x = random.randint(200, SCREEN_WIDTH - 200)
                    y = random.randint(150, SCREEN_HEIGHT - 200)
                    self.fingerprints.append((x, y, random.uniform(0, 360)))
        else:
            self.reveal_timer = 0
            
    def draw_effect(self, surface, mouse_pos):
        """Draw UV light effect and revealed fingerprints"""
        if not self.active:
            return
            
        mx, my = mouse_pos
        
        # UV light glow
        uv_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        
        # Purple tint in lit area
        pygame.draw.circle(uv_surface, (100, 50, 200, 50), (mx, my), 180)
        pygame.draw.circle(uv_surface, (150, 100, 255, 30), (mx, my), 120)
        
        surface.blit(uv_surface, (0, 0))
        
        # Draw fingerprints only in UV light radius
        for fx, fy, angle in self.fingerprints:
            dist = math.sqrt((fx - mx) ** 2 + (fy - my) ** 2)
            if dist < 150:
                alpha = int(255 * (1 - dist / 150))
                self.draw_fingerprint(surface, fx, fy, angle, alpha)
                
    def draw_fingerprint(self, surface, x, y, angle, alpha):
        """Draw a glowing fingerprint"""
        fp_surface = pygame.Surface((60, 80), pygame.SRCALPHA)
        color = (150, 100, 255, alpha)
        
        # Draw fingerprint lines
        for i in range(8):
            y_offset = i * 8 + 10
            wave = math.sin(angle + i * 0.5) * 5
            pygame.draw.arc(fp_surface, color, (10 + wave, y_offset, 40, 10), 0, 3.14, 2)
            
        surface.blit(fp_surface, (x - 30, y - 40))


class EquipmentManager:
    """Manages all ghost hunting equipment"""
    
    def __init__(self, equipment_slots=2):
        self.flashlight = Flashlight()
        self.emf_reader = EMFReader()
        self.thermometer = Thermometer()
        self.spirit_box = SpiritBox()
        self.uv_light = UVLight()
        
        self.all_equipment = [
            self.flashlight,
            self.emf_reader,
            self.thermometer,
            self.spirit_box,
            self.uv_light
        ]
        
        self.active_equipment = self.flashlight
        self.current_index = 0
        
        # Equipment slot limit (balance change)
        self.equipment_slots = equipment_slots
        self.equipped_items = [self.flashlight]  # Start with flashlight equipped
        
    def set_equipment_slots(self, slots):
        """Set the number of equipment slots allowed"""
        self.equipment_slots = slots
        # Trim equipped items if needed
        while len(self.equipped_items) > slots:
            removed = self.equipped_items.pop()
            removed.active = False
            
    def can_equip(self, equipment):
        """Check if equipment can be equipped"""
        if equipment in self.equipped_items:
            return True
        return len(self.equipped_items) < self.equipment_slots
        
    def equip_item(self, equipment):
        """Equip an item if there's room"""
        if equipment in self.equipped_items:
            return True
        if len(self.equipped_items) < self.equipment_slots:
            self.equipped_items.append(equipment)
            return True
        return False
        
    def unequip_item(self, equipment):
        """Unequip an item"""
        if equipment in self.equipped_items:
            equipment.active = False
            self.equipped_items.remove(equipment)
            return True
        return False
        
    def switch_equipment(self, direction=1):
        """Switch to next/previous equipment"""
        self.current_index = (self.current_index + direction) % len(self.all_equipment)
        self.active_equipment = self.all_equipment[self.current_index]
        
    def toggle_current(self):
        """Toggle current equipment on/off"""
        equip = self.active_equipment
        
        if equip.active:
            # Turn off
            equip.active = False
        else:
            # Check if we can equip it
            if self.can_equip(equip):
                self.equip_item(equip)
                equip.active = True
            # If we can't, we need to swap - turn off oldest equipped item
            elif len(self.equipped_items) >= self.equipment_slots:
                # Find an active item to swap out
                for old_equip in self.equipped_items:
                    if old_equip != self.flashlight:  # Never auto-unequip flashlight
                        self.unequip_item(old_equip)
                        self.equip_item(equip)
                        equip.active = True
                        break
        
    def update(self, dt, ghost_nearby, ghost_distance, ghost=None):
        """Update all equipment"""
        for equip in self.all_equipment:
            equip.update(dt, ghost_nearby, ghost_distance, ghost)
            
    def draw_equipment_bar(self, surface, font):
        """Draw the equipment selection bar"""
        bar_width = 300
        bar_height = 60
        x = SCREEN_WIDTH - bar_width - 20
        y = SCREEN_HEIGHT - bar_height - 20
        
        # Background
        bg = pygame.Surface((bar_width, bar_height), pygame.SRCALPHA)
        bg.fill(EQUIPMENT_BG)
        surface.blit(bg, (x, y))
        pygame.draw.rect(surface, GRAY, (x, y, bar_width, bar_height), 2)
        
        # Equipment slots indicator
        slots_text = font.render(f"Slots: {len(self.equipped_items)}/{self.equipment_slots}", True, YELLOW)
        surface.blit(slots_text, (x + 5, y - 35))
        
        # Equipment slots
        slot_width = bar_width // len(self.all_equipment)
        for i, equip in enumerate(self.all_equipment):
            slot_x = x + i * slot_width
            
            # Highlight active selection
            if equip == self.active_equipment:
                pygame.draw.rect(surface, (80, 80, 100), 
                               (slot_x, y, slot_width, bar_height))
                               
            # Equipment icon - color based on equipped status
            if equip.active:
                color = GREEN
            elif equip in self.equipped_items:
                color = YELLOW  # Equipped but not active
            elif self.can_equip(equip):
                color = WHITE  # Can be equipped
            else:
                color = DARK_GRAY  # Cannot equip (slots full)
                
            icon = font.render(equip.icon_char, True, color)
            surface.blit(icon, (slot_x + slot_width // 2 - icon.get_width() // 2, y + 5))
            
            # Status
            if equip.active:
                status = font.render(equip.get_display_value()[:8], True, color)
                surface.blit(status, (slot_x + 5, y + 35))
                
        # Instructions
        help_text = font.render("Q/E: Switch | SPACE: Toggle", True, GRAY)
        surface.blit(help_text, (x, y - 20))
