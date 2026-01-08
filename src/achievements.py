"""
Achievement system for Paranormal Investigations
"""

import pygame
import json
import os
from constants import *


class Achievement:
    """A single achievement"""
    
    def __init__(self, id, name, description, icon, secret=False):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon  # Emoji or character
        self.secret = secret  # Hidden until unlocked
        self.unlocked = False
        self.unlock_time = None
        
    def to_dict(self):
        """Convert to dictionary for saving"""
        return {
            'id': self.id,
            'unlocked': self.unlocked,
            'unlock_time': self.unlock_time
        }
        
    def from_dict(self, data):
        """Load from dictionary"""
        if data.get('id') == self.id:
            self.unlocked = data.get('unlocked', False)
            self.unlock_time = data.get('unlock_time')


class AchievementManager:
    """Manages all achievements"""
    
    ACHIEVEMENTS = [
        Achievement(
            ACHIEVEMENT_FIRST_GHOST,
            "First Contact",
            "Successfully identify your first ghost",
            "👻"
        ),
        Achievement(
            ACHIEVEMENT_SPEED_RUN,
            "Speed Demon",
            "Identify a ghost in under 60 seconds",
            "⚡"
        ),
        Achievement(
            ACHIEVEMENT_NO_FLASHLIGHT,
            "Fearless",
            "Win without using the flashlight",
            "🌑"
        ),
        Achievement(
            ACHIEVEMENT_ALL_EVIDENCE,
            "Evidence Collector",
            "Collect all 6 types of evidence in one game",
            "🔍"
        ),
        Achievement(
            ACHIEVEMENT_SURVIVOR,
            "Survivor",
            "Escape 10 ghosts",
            "🏃"
        ),
        Achievement(
            ACHIEVEMENT_NIGHTMARE_WIN,
            "Nightmare Slayer",
            "Win on Nightmare difficulty",
            "💀"
        ),
        Achievement(
            "ghost_hunter",
            "Ghost Hunter",
            "Identify 5 different ghost types",
            "🎯"
        ),
        Achievement(
            "explorer",
            "Explorer",
            "Visit all 10 rooms in one game",
            "🗺️"
        ),
        Achievement(
            "brave_soul",
            "Brave Soul",
            "Win using only flashlight - no other equipment",
            "😱"
        ),
        Achievement(
            "perfect_game",
            "Perfect Investigation",
            "Win without any wrong guesses",
            "⭐"
        ),
        Achievement(
            "equipment_master",
            "Equipment Master",
            "Use all equipment types in one game",
            "🔧",
            secret=True
        ),
        Achievement(
            "death_defier",
            "Death Defier",
            "Get killed 10 times... and keep playing",
            "☠️",
            secret=True
        ),
    ]
    
    def __init__(self):
        self.achievements = {a.id: a for a in self.ACHIEVEMENTS.copy()}
        self.pending_notifications = []
        self.notification_timer = 0
        self.current_notification = None
        
        # Statistics for tracking
        self.stats = {
            'ghosts_identified': 0,
            'ghosts_escaped': 0,
            'deaths': 0,
            'games_played': 0,
            'ghost_types_found': set(),
            'fastest_time': float('inf'),
        }
        
        # Try to load saved achievements
        self.load()
        
    def unlock(self, achievement_id):
        """Unlock an achievement"""
        if achievement_id in self.achievements:
            achievement = self.achievements[achievement_id]
            if not achievement.unlocked:
                achievement.unlocked = True
                achievement.unlock_time = pygame.time.get_ticks()
                self.pending_notifications.append(achievement)
                self.save()
                return True
        return False
        
    def check_achievements(self, game_data):
        """Check if any achievements should be unlocked based on game data"""
        # First ghost
        if game_data.get('victory') and self.stats['ghosts_identified'] == 0:
            self.unlock(ACHIEVEMENT_FIRST_GHOST)
            
        # Speed run
        if game_data.get('victory') and game_data.get('time_taken', 999) < 60:
            self.unlock(ACHIEVEMENT_SPEED_RUN)
            
        # No flashlight
        if game_data.get('victory') and not game_data.get('used_flashlight', True):
            self.unlock(ACHIEVEMENT_NO_FLASHLIGHT)
            
        # All evidence
        if len(game_data.get('evidence_collected', set())) >= 6:
            self.unlock(ACHIEVEMENT_ALL_EVIDENCE)
            
        # Survivor
        if game_data.get('victory'):
            self.stats['ghosts_escaped'] += 1
            if self.stats['ghosts_escaped'] >= 10:
                self.unlock(ACHIEVEMENT_SURVIVOR)
                
        # Nightmare win
        if game_data.get('victory') and game_data.get('difficulty') == DIFFICULTY_NIGHTMARE:
            self.unlock(ACHIEVEMENT_NIGHTMARE_WIN)
            
        # Ghost hunter
        if game_data.get('victory'):
            ghost_name = game_data.get('ghost_name')
            if ghost_name:
                self.stats['ghost_types_found'].add(ghost_name)
                if len(self.stats['ghost_types_found']) >= 5:
                    self.unlock('ghost_hunter')
                    
        # Explorer
        if len(game_data.get('rooms_visited', set())) >= 10:
            self.unlock('explorer')
            
        # Brave soul - win with only flashlight equipment used
        equipment_used = game_data.get('equipment_used', set())
        if game_data.get('victory') and len(equipment_used) == 1 and 'flashlight' in str(equipment_used).lower():
            self.unlock('brave_soul')
            
        # Perfect game
        if game_data.get('victory') and game_data.get('wrong_guesses', 0) == 0:
            self.unlock('perfect_game')
            
        # Equipment master
        if len(game_data.get('equipment_used', set())) >= 5:
            self.unlock('equipment_master')
            
        # Death defier
        if not game_data.get('victory'):
            self.stats['deaths'] += 1
            if self.stats['deaths'] >= 10:
                self.unlock('death_defier')
                
        # Update statistics
        if game_data.get('victory'):
            self.stats['ghosts_identified'] += 1
            time_taken = game_data.get('time_taken', float('inf'))
            if time_taken < self.stats['fastest_time']:
                self.stats['fastest_time'] = time_taken
                
        self.stats['games_played'] += 1
        self.save()
        
    def update(self, dt):
        """Update notification display"""
        if self.current_notification:
            self.notification_timer -= dt
            if self.notification_timer <= 0:
                self.current_notification = None
                
        if not self.current_notification and self.pending_notifications:
            self.current_notification = self.pending_notifications.pop(0)
            self.notification_timer = 4.0  # Show for 4 seconds
            
    def draw_notification(self, surface, font):
        """Draw achievement notification"""
        if not self.current_notification:
            return
            
        achievement = self.current_notification
        
        # Slide in animation
        slide_progress = min(1, (4.0 - self.notification_timer) / 0.5)
        if self.notification_timer < 0.5:
            slide_progress = self.notification_timer / 0.5
            
        x_offset = int((1 - slide_progress) * 300)
        
        # Background
        notif_width = 300
        notif_height = 80
        x = SCREEN_WIDTH - notif_width - 20 + x_offset
        y = 20
        
        bg = pygame.Surface((notif_width, notif_height), pygame.SRCALPHA)
        bg.fill((40, 40, 60, 230))
        surface.blit(bg, (x, y))
        pygame.draw.rect(surface, (255, 215, 0), (x, y, notif_width, notif_height), 2)
        
        # Icon
        icon_font = pygame.font.Font(None, 48)
        icon = icon_font.render(achievement.icon, True, WHITE)
        surface.blit(icon, (x + 10, y + 15))
        
        # Title
        title = font.render("Achievement Unlocked!", True, (255, 215, 0))
        surface.blit(title, (x + 60, y + 10))
        
        # Name
        name = font.render(achievement.name, True, WHITE)
        surface.blit(name, (x + 60, y + 35))
        
        # Description
        small_font = pygame.font.Font(None, 18)
        desc = small_font.render(achievement.description, True, GRAY)
        surface.blit(desc, (x + 60, y + 55))
        
    def draw_achievements_list(self, surface, fonts, scroll_offset=0):
        """Draw full achievements list"""
        x = 100
        y = 120 - scroll_offset
        
        for achievement in self.ACHIEVEMENTS:
            if y > 80 and y < SCREEN_HEIGHT - 100:
                # Background
                bg_color = (50, 60, 50) if achievement.unlocked else (40, 40, 50)
                pygame.draw.rect(surface, bg_color, (x, y, 500, 60), border_radius=5)
                
                if achievement.unlocked:
                    pygame.draw.rect(surface, (100, 200, 100), (x, y, 500, 60), 2, border_radius=5)
                    
                # Icon
                icon_font = pygame.font.Font(None, 36)
                if achievement.unlocked or not achievement.secret:
                    icon = icon_font.render(achievement.icon, True, WHITE)
                else:
                    icon = icon_font.render("?", True, GRAY)
                surface.blit(icon, (x + 15, y + 15))
                
                # Name
                if achievement.unlocked or not achievement.secret:
                    name_color = WHITE if achievement.unlocked else GRAY
                    name = fonts['medium'].render(achievement.name, True, name_color)
                    desc = fonts['small'].render(achievement.description, True, GRAY)
                else:
                    name = fonts['medium'].render("???", True, GRAY)
                    desc = fonts['small'].render("Secret achievement", True, DARK_GRAY)
                    
                surface.blit(name, (x + 60, y + 8))
                surface.blit(desc, (x + 60, y + 32))
                
                # Checkmark if unlocked
                if achievement.unlocked:
                    check = fonts['large'].render("✓", True, GREEN)
                    surface.blit(check, (x + 460, y + 12))
                    
            y += 70
            
    def get_completion_percentage(self):
        """Get percentage of achievements unlocked"""
        total = len(self.achievements)
        unlocked = sum(1 for a in self.achievements.values() if a.unlocked)
        return (unlocked / total) * 100 if total > 0 else 0
        
    def save(self):
        """Save achievements to file"""
        data = {
            'achievements': [a.to_dict() for a in self.achievements.values()],
            'stats': {
                'ghosts_identified': self.stats['ghosts_identified'],
                'ghosts_escaped': self.stats['ghosts_escaped'],
                'deaths': self.stats['deaths'],
                'games_played': self.stats['games_played'],
                'ghost_types_found': list(self.stats['ghost_types_found']),
                'fastest_time': self.stats['fastest_time'] if self.stats['fastest_time'] != float('inf') else None,
            }
        }
        
        try:
            with open('achievements.json', 'w') as f:
                json.dump(data, f)
        except Exception:
            pass  # Silently fail if can't save
            
    def load(self):
        """Load achievements from file"""
        try:
            if os.path.exists('achievements.json'):
                with open('achievements.json', 'r') as f:
                    data = json.load(f)
                    
                # Load achievement states
                for ach_data in data.get('achievements', []):
                    if ach_data['id'] in self.achievements:
                        self.achievements[ach_data['id']].from_dict(ach_data)
                        
                # Load stats
                stats = data.get('stats', {})
                self.stats['ghosts_identified'] = stats.get('ghosts_identified', 0)
                self.stats['ghosts_escaped'] = stats.get('ghosts_escaped', 0)
                self.stats['deaths'] = stats.get('deaths', 0)
                self.stats['games_played'] = stats.get('games_played', 0)
                self.stats['ghost_types_found'] = set(stats.get('ghost_types_found', []))
                fastest = stats.get('fastest_time')
                self.stats['fastest_time'] = fastest if fastest else float('inf')
        except Exception:
            pass  # Start fresh if can't load
