"""
Particle system for atmospheric effects in Paranormal Investigations
"""

import pygame
import random
import math
from constants import *


class Particle:
    """A single particle"""
    
    def __init__(self, x, y, particle_type):
        self.x = x
        self.y = y
        self.type = particle_type
        self.lifetime = 0
        self.max_lifetime = 3.0
        self.alpha = 255
        self.size = 2
        self.vx = 0
        self.vy = 0
        
        self._init_by_type()
        
    def _init_by_type(self):
        """Initialize particle properties based on type"""
        if self.type == PARTICLE_DUST:
            self.size = random.randint(1, 3)
            self.vx = random.uniform(-10, 10)
            self.vy = random.uniform(-5, 15)
            self.max_lifetime = random.uniform(3, 8)
            self.color = (180, 170, 150)
            
        elif self.type == PARTICLE_FOG:
            self.size = random.randint(30, 60)
            self.vx = random.uniform(-20, 20)
            self.vy = random.uniform(-5, 5)
            self.max_lifetime = random.uniform(5, 10)
            self.color = (150, 150, 160)
            self.alpha = 30
            
        elif self.type == PARTICLE_RAIN:
            self.size = random.randint(10, 20)
            self.vx = random.uniform(-5, 5)
            self.vy = random.uniform(300, 500)
            self.max_lifetime = 2.0
            self.color = (100, 120, 150)
            
        elif self.type == PARTICLE_ORBS:
            self.size = random.randint(5, 15)
            self.vx = random.uniform(-30, 30)
            self.vy = random.uniform(-50, -20)
            self.max_lifetime = random.uniform(2, 4)
            self.color = (200, 220, 255)
            self.alpha = 150
            
        elif self.type == PARTICLE_BREATH:
            self.size = random.randint(8, 20)
            self.vx = random.uniform(-5, 5)
            self.vy = random.uniform(-30, -10)
            self.max_lifetime = random.uniform(1, 2)
            self.color = (200, 230, 255)
            self.alpha = 100
            
    def update(self, dt):
        """Update particle position and state"""
        self.lifetime += dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        
        # Type-specific updates
        if self.type == PARTICLE_DUST:
            # Slow floating effect
            self.vx += random.uniform(-5, 5) * dt
            self.vy += random.uniform(-2, 2) * dt
            
        elif self.type == PARTICLE_FOG:
            # Swirling motion
            self.vx += math.sin(self.lifetime * 2) * 10 * dt
            
        elif self.type == PARTICLE_ORBS:
            # Gentle floating
            self.vx += math.sin(self.lifetime * 3) * 20 * dt
            self.vy += math.cos(self.lifetime * 2) * 10 * dt
            
        # Fade based on lifetime
        life_ratio = self.lifetime / self.max_lifetime
        if life_ratio > 0.7:
            self.alpha = int(255 * (1 - (life_ratio - 0.7) / 0.3))
            
        return self.lifetime < self.max_lifetime
        
    def draw(self, surface):
        """Draw the particle"""
        if self.alpha <= 0:
            return
            
        if self.type == PARTICLE_RAIN:
            # Draw as line for rain
            end_y = self.y + self.size
            color = (*self.color, min(255, self.alpha))
            rain_surf = pygame.Surface((4, self.size + 10), pygame.SRCALPHA)
            pygame.draw.line(rain_surf, color, (2, 0), (2, self.size), 1)
            surface.blit(rain_surf, (int(self.x), int(self.y)))
            
        elif self.type in [PARTICLE_FOG, PARTICLE_ORBS, PARTICLE_BREATH]:
            # Draw as translucent circle
            size = int(self.size)
            particle_surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            color = (*self.color, min(255, self.alpha))
            pygame.draw.circle(particle_surf, color, (size, size), size)
            surface.blit(particle_surf, (int(self.x - size), int(self.y - size)))
            
        else:
            # Draw as small dot for dust
            color = (*self.color, min(255, self.alpha))
            particle_surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(particle_surf, color, (self.size, self.size), self.size)
            surface.blit(particle_surf, (int(self.x - self.size), int(self.y - self.size)))


class ParticleSystem:
    """Manages all particles in the game"""
    
    def __init__(self):
        self.particles = []
        self.max_particles = 200
        self.enabled = True
        
        # Particle spawn rates
        self.dust_rate = 0.1  # Particles per second
        self.fog_rate = 0.05
        self.rain_rate = 0  # Only during rain
        self.orb_rate = 0  # Only when ghost nearby
        
        self.spawn_timers = {
            PARTICLE_DUST: 0,
            PARTICLE_FOG: 0,
            PARTICLE_RAIN: 0,
            PARTICLE_ORBS: 0,
        }
        
    def set_weather(self, weather_type):
        """Set the current weather condition"""
        if weather_type == "rain":
            self.rain_rate = 2.0
            self.dust_rate = 0
        elif weather_type == "foggy":
            self.fog_rate = 0.2
            self.rain_rate = 0
        else:
            self.rain_rate = 0
            self.dust_rate = 0.1
            self.fog_rate = 0.05
            
    def set_ghost_nearby(self, nearby, distance=100):
        """Set whether ghost is nearby for orb effects"""
        if nearby and distance < 200:
            self.orb_rate = 0.3 * (1 - distance / 200)
        else:
            self.orb_rate = 0
            
    def spawn_breath(self, x, y):
        """Spawn cold breath particles (for cold spots)"""
        for _ in range(3):
            if len(self.particles) < self.max_particles:
                p = Particle(x + random.randint(-20, 20), y, PARTICLE_BREATH)
                self.particles.append(p)
                
    def spawn_burst(self, x, y, particle_type, count=10):
        """Spawn a burst of particles at a location"""
        for _ in range(count):
            if len(self.particles) < self.max_particles:
                p = Particle(
                    x + random.randint(-30, 30),
                    y + random.randint(-30, 30),
                    particle_type
                )
                self.particles.append(p)
                
    def update(self, dt):
        """Update all particles"""
        if not self.enabled:
            return
            
        # Update existing particles
        self.particles = [p for p in self.particles if p.update(dt)]
        
        # Spawn new particles based on rates
        self._spawn_by_rate(PARTICLE_DUST, self.dust_rate, dt)
        self._spawn_by_rate(PARTICLE_FOG, self.fog_rate, dt)
        self._spawn_by_rate(PARTICLE_RAIN, self.rain_rate, dt)
        self._spawn_by_rate(PARTICLE_ORBS, self.orb_rate, dt)
        
    def _spawn_by_rate(self, particle_type, rate, dt):
        """Spawn particles based on rate"""
        if rate <= 0 or len(self.particles) >= self.max_particles:
            return
            
        self.spawn_timers[particle_type] += dt
        spawn_interval = 1.0 / rate if rate > 0 else float('inf')
        
        while self.spawn_timers[particle_type] >= spawn_interval:
            self.spawn_timers[particle_type] -= spawn_interval
            
            # Random spawn position
            if particle_type == PARTICLE_RAIN:
                x = random.randint(0, SCREEN_WIDTH)
                y = -20
            elif particle_type == PARTICLE_FOG:
                x = random.randint(-50, SCREEN_WIDTH + 50)
                y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
            elif particle_type == PARTICLE_ORBS:
                x = random.randint(100, SCREEN_WIDTH - 100)
                y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - 100)
            else:
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)
                
            self.particles.append(Particle(x, y, particle_type))
            
    def draw(self, surface):
        """Draw all particles"""
        if not self.enabled:
            return
            
        for particle in self.particles:
            particle.draw(surface)
            
    def clear(self):
        """Clear all particles"""
        self.particles.clear()


class AmbientEffects:
    """Manages ambient atmospheric effects"""
    
    def __init__(self):
        self.lightning_active = False
        self.lightning_timer = 0
        self.lightning_intensity = 0
        
        self.screen_shake = 0
        self.shake_offset = (0, 0)
        
        self.vignette_intensity = 0.3
        self.vignette_pulse = 0
        
        self.creepy_events = []
        self.event_cooldown = 0
        
    def trigger_lightning(self, duration=0.3):
        """Trigger a lightning flash"""
        self.lightning_active = True
        self.lightning_timer = duration
        self.lightning_intensity = 255
        
    def trigger_shake(self, intensity=0.5):
        """Trigger screen shake"""
        self.screen_shake = intensity
        
    def add_creepy_event(self, event_type, data=None):
        """Add a creepy ambient event"""
        self.creepy_events.append({
            'type': event_type,
            'data': data,
            'timer': 3.0
        })
        
    def update(self, dt):
        """Update ambient effects"""
        # Lightning
        if self.lightning_active:
            self.lightning_timer -= dt
            self.lightning_intensity = int(255 * (self.lightning_timer / 0.3))
            if self.lightning_timer <= 0:
                self.lightning_active = False
                
        # Screen shake
        if self.screen_shake > 0:
            self.screen_shake -= dt * 2
            shake_amount = int(self.screen_shake * 10)
            self.shake_offset = (
                random.randint(-shake_amount, shake_amount),
                random.randint(-shake_amount, shake_amount)
            )
        else:
            self.shake_offset = (0, 0)
            
        # Vignette pulse
        self.vignette_pulse += dt
        self.vignette_intensity = 0.2 + math.sin(self.vignette_pulse * 2) * 0.05
        
        # Creepy events
        self.creepy_events = [e for e in self.creepy_events if e['timer'] > 0]
        for event in self.creepy_events:
            event['timer'] -= dt
            
        # Random ambient events
        self.event_cooldown -= dt
        if self.event_cooldown <= 0:
            self.event_cooldown = random.uniform(10, 30)
            # Could trigger random creepy sounds here
            
    def draw_lightning(self, surface):
        """Draw lightning flash"""
        if self.lightning_active and self.lightning_intensity > 0:
            flash = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            flash.fill((255, 255, 255, min(255, self.lightning_intensity)))
            surface.blit(flash, (0, 0))
            
    def draw_vignette(self, surface):
        """Draw vignette effect (darkened edges)"""
        vignette = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        
        # Create radial gradient vignette
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        max_dist = math.sqrt(center_x ** 2 + center_y ** 2)
        
        # Draw concentric rectangles for vignette (faster than per-pixel)
        for i in range(10):
            ratio = i / 10
            alpha = int(255 * self.vignette_intensity * ratio * ratio)
            rect_size = 1 - ratio
            x = int(center_x * (1 - rect_size))
            y = int(center_y * (1 - rect_size))
            w = int(SCREEN_WIDTH * rect_size)
            h = int(SCREEN_HEIGHT * rect_size)
            
            if w > 0 and h > 0:
                border = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                pygame.draw.rect(border, (0, 0, 0, alpha), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
                pygame.draw.rect(border, (0, 0, 0, 0), (x, y, w, h))
                surface.blit(border, (0, 0))
                break  # Only draw outermost layer for performance
