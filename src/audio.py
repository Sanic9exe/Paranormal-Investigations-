"""
Audio and sound management for Paranormal Investigations
Note: This provides a sound framework. Actual audio files would need to be added.
Visual sound indicators are shown when sounds would play.
"""

import pygame
import random
import math
from constants import *


class SoundIndicator:
    """Visual indicator when a sound plays (since actual audio may not be available)"""
    
    def __init__(self, text, x, y, color, duration=2.0):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.duration = duration
        self.lifetime = 0
        self.alpha = 255
        
    def update(self, dt):
        """Update indicator"""
        self.lifetime += dt
        self.y -= 20 * dt  # Float upward
        
        # Fade out in last 30%
        life_ratio = self.lifetime / self.duration
        if life_ratio > 0.7:
            self.alpha = int(255 * (1 - (life_ratio - 0.7) / 0.3))
            
        return self.lifetime < self.duration
        
    def draw(self, surface, font):
        """Draw the indicator"""
        if self.alpha <= 0:
            return
            
        # Create text with sound icon
        text_surf = font.render(f"🔊 {self.text}", True, self.color)
        text_surf.set_alpha(self.alpha)
        surface.blit(text_surf, (int(self.x), int(self.y)))


class AudioManager:
    """Manages game audio and visual sound indicators"""
    
    def __init__(self):
        self.sound_enabled = True
        self.music_enabled = True
        self.volume = 0.7
        
        # Visual indicators for sounds
        self.indicators = []
        
        # Ambient sound timers
        self.ambient_timer = 0
        self.ambient_interval = 10  # Seconds between ambient sounds
        
        # Sound categories and their visual representations
        self.sound_colors = {
            'ambient': GRAY,
            'ghost': PURPLE,
            'player': WHITE,
            'ui': CYAN,
            'danger': RED,
            'discovery': GREEN,
        }
        
        # Track what sounds are "playing"
        self.active_ambients = set()
        
        # Try to initialize pygame mixer
        self.mixer_available = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            self.mixer_available = True
        except Exception:
            pass
            
    def play_sound(self, sound_name, category='ambient', x=None, y=None):
        """Play a sound (shows visual indicator)"""
        if not self.sound_enabled:
            return
            
        # Position for indicator
        if x is None:
            x = SCREEN_WIDTH // 2
        if y is None:
            y = SCREEN_HEIGHT - 100
            
        color = self.sound_colors.get(category, WHITE)
        
        # Create visual indicator
        self.indicators.append(SoundIndicator(sound_name, x, y, color))
        
    def play_ambient(self, ambient_type):
        """Play an ambient sound"""
        ambients = {
            'creak': "Floor creaking...",
            'wind': "Wind howling...",
            'thunder': "Thunder rumbles...",
            'whisper': "Whispers...",
            'footsteps': "Distant footsteps...",
            'door': "Door creaking...",
            'breathing': "Heavy breathing...",
            'heartbeat': "Heartbeat...",
            'static': "Static noise...",
            'music_box': "Music box playing...",
        }
        
        if ambient_type in ambients:
            self.play_sound(ambients[ambient_type], 'ambient')
            self.active_ambients.add(ambient_type)
            
    def play_ghost_sound(self, sound_type, ghost_name=None):
        """Play a ghost-related sound"""
        ghost_sounds = {
            'moan': "Ghostly moan...",
            'scream': "Terrifying scream!",
            'laugh': "Eerie laughter...",
            'cry': "Crying sounds...",
            'whisper': f"'{ghost_name}' whispers...",
            'growl': "Threatening growl...",
            'slam': "DOOR SLAM!",
            'scratch': "Scratching sounds...",
            'chains': "Chains rattling...",
            'child': "Child's voice...",
        }
        
        if sound_type in ghost_sounds:
            text = ghost_sounds[sound_type]
            if ghost_name and '{ghost_name}' not in text:
                text = f"[{ghost_name}] {text}"
            self.play_sound(text, 'ghost', SCREEN_WIDTH // 2, 150)
            
    def play_ui_sound(self, sound_type):
        """Play UI sound"""
        ui_sounds = {
            'click': "Click",
            'open': "Open",
            'close': "Close",
            'success': "Success!",
            'fail': "Failed!",
            'equip': "Equipped",
            'beep': "Beep",
        }
        
        if sound_type in ui_sounds:
            self.play_sound(ui_sounds[sound_type], 'ui', SCREEN_WIDTH - 150, 50)
            
    def play_danger_sound(self, danger_type):
        """Play danger/warning sound"""
        danger_sounds = {
            'heartbeat': "♥ Heartbeat racing...",
            'warning': "⚠ Warning!",
            'hunt': "🎯 GHOST HUNTING!",
            'death': "💀 You died...",
        }
        
        if danger_type in danger_sounds:
            self.play_sound(danger_sounds[danger_type], 'danger', SCREEN_WIDTH // 2, 80)
            
    def update(self, dt, ghost_nearby=False):
        """Update audio manager"""
        # Update indicators
        self.indicators = [i for i in self.indicators if i.update(dt)]
        
        # Ambient sound timer
        self.ambient_timer += dt
        if self.ambient_timer >= self.ambient_interval:
            self.ambient_timer = 0
            self._play_random_ambient(ghost_nearby)
            
    def _play_random_ambient(self, ghost_nearby):
        """Play a random ambient sound"""
        if random.random() < 0.3:  # 30% chance
            if ghost_nearby:
                # Ghost-related ambients
                choices = ['whisper', 'breathing', 'footsteps', 'creak']
            else:
                # Normal ambients
                choices = ['creak', 'wind', 'door']
                
            self.play_ambient(random.choice(choices))
            
    def draw_indicators(self, surface, font):
        """Draw all sound indicators"""
        for indicator in self.indicators:
            indicator.draw(surface, font)
            
    def set_volume(self, volume):
        """Set master volume"""
        self.volume = max(0, min(1, volume))
        if self.mixer_available:
            try:
                pygame.mixer.music.set_volume(self.volume)
            except Exception:
                pass


class Soundtrack:
    """Manages background music and ambient tracks"""
    
    def __init__(self, audio_manager):
        self.audio = audio_manager
        self.current_track = None
        self.intensity = 0  # 0 = calm, 1 = tense
        
    def set_intensity(self, intensity):
        """Set music intensity (0-1)"""
        self.intensity = max(0, min(1, intensity))
        
    def update(self, ghost_nearby, time_remaining):
        """Update soundtrack based on game state"""
        # Calculate intensity
        ghost_factor = 0.5 if ghost_nearby else 0
        time_factor = max(0, 1 - time_remaining / 180) * 0.3  # More tense as time runs out
        
        self.intensity = ghost_factor + time_factor
        
    def get_intensity_description(self):
        """Get description of current music intensity"""
        if self.intensity < 0.2:
            return "Calm ambience"
        elif self.intensity < 0.5:
            return "Uneasy tension"
        elif self.intensity < 0.8:
            return "Rising dread"
        else:
            return "Terror!"
