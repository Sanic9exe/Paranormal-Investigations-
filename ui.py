"""
UI components for Paranormal Investigations
"""

import pygame
import math
from constants import *


class Button:
    """A clickable button"""
    
    def __init__(self, rect, text, font, callback=None, color=BUTTON_COLOR, 
                 hover_color=BUTTON_HOVER, text_color=WHITE):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.callback = callback
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hovered = False
        self.enabled = True
        
    def update(self, mouse_pos):
        """Update button hover state"""
        self.hovered = self.rect.collidepoint(mouse_pos) and self.enabled
        
    def draw(self, surface):
        """Draw the button"""
        color = self.hover_color if self.hovered else self.color
        if not self.enabled:
            color = DARK_GRAY
            
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, WHITE if self.hovered else GRAY, self.rect, 2, border_radius=8)
        
        text_surf = self.font.render(self.text, True, self.text_color if self.enabled else GRAY)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def handle_click(self, pos):
        """Handle click event"""
        if self.enabled and self.rect.collidepoint(pos) and self.callback:
            self.callback()
            return True
        return False


class ScrollablePanel:
    """A scrollable panel for content"""
    
    def __init__(self, rect, content_height):
        self.rect = pygame.Rect(rect)
        self.content_height = content_height
        self.scroll_offset = 0
        self.max_scroll = max(0, content_height - self.rect.height)
        self.scrollbar_dragging = False
        
    def scroll(self, amount):
        """Scroll the panel"""
        self.scroll_offset = max(0, min(self.max_scroll, self.scroll_offset + amount))
        
    def get_scrollbar_rect(self):
        """Get the scrollbar rectangle"""
        if self.content_height <= self.rect.height:
            return None
        bar_height = max(30, self.rect.height * self.rect.height / self.content_height)
        bar_y = self.rect.y + (self.scroll_offset / self.max_scroll) * (self.rect.height - bar_height) if self.max_scroll > 0 else self.rect.y
        return pygame.Rect(self.rect.right - 15, bar_y, 10, bar_height)
        
    def draw_scrollbar(self, surface):
        """Draw the scrollbar"""
        scrollbar = self.get_scrollbar_rect()
        if scrollbar:
            pygame.draw.rect(surface, DARK_GRAY, 
                           (self.rect.right - 15, self.rect.y, 10, self.rect.height), 
                           border_radius=5)
            pygame.draw.rect(surface, GRAY, scrollbar, border_radius=5)


class Notebook:
    """The player's notebook for observations"""
    
    def __init__(self, screen_rect):
        self.rect = pygame.Rect(screen_rect.width // 4, screen_rect.height // 8,
                               screen_rect.width // 2, screen_rect.height * 3 // 4)
        self.notes = []
        self.current_page = 0
        self.max_lines = 15
        self.cursor_pos = 0
        self.current_input = ""
        self.editing = False
        
    def add_note(self, text):
        """Add a note to the notebook"""
        self.notes.append(text)
        
    def get_current_page_notes(self):
        """Get notes for current page"""
        start = self.current_page * self.max_lines
        end = start + self.max_lines
        return self.notes[start:end]
    
    def draw(self, surface, font):
        """Draw the notebook"""
        # Notebook background
        pygame.draw.rect(surface, (240, 230, 210), self.rect, border_radius=10)
        pygame.draw.rect(surface, SEPIA, self.rect, 3, border_radius=10)
        
        # Spiral binding
        for i in range(10):
            y = self.rect.y + 40 + i * 55
            pygame.draw.circle(surface, DARK_GRAY, (self.rect.x + 30, y), 8)
            pygame.draw.circle(surface, (200, 190, 170), (self.rect.x + 30, y), 5)
        
        # Title
        title = font.render("Investigation Notes", True, SEPIA)
        surface.blit(title, (self.rect.centerx - title.get_width() // 2, self.rect.y + 15))
        
        # Lines
        small_font = pygame.font.Font(None, 20)
        for i, note in enumerate(self.get_current_page_notes()):
            y = self.rect.y + 60 + i * 35
            pygame.draw.line(surface, (200, 190, 170), 
                           (self.rect.x + 50, y + 25), (self.rect.right - 30, y + 25), 1)
            text = small_font.render(note, True, DARK_GRAY)
            surface.blit(text, (self.rect.x + 55, y + 5))
        
        # Current input
        if self.editing:
            input_y = self.rect.y + 60 + len(self.get_current_page_notes()) * 35
            pygame.draw.line(surface, (200, 190, 170),
                           (self.rect.x + 50, input_y + 25), (self.rect.right - 30, input_y + 25), 1)
            input_text = small_font.render(self.current_input + "|", True, BLACK)
            surface.blit(input_text, (self.rect.x + 55, input_y + 5))
        
        # Page number
        page_text = small_font.render(f"Page {self.current_page + 1}", True, SEPIA)
        surface.blit(page_text, (self.rect.centerx - page_text.get_width() // 2, self.rect.bottom - 30))
        
        # Instructions
        inst_text = small_font.render("Type to add notes. Press Enter to save. ESC to close.", True, GRAY)
        surface.blit(inst_text, (self.rect.centerx - inst_text.get_width() // 2, self.rect.bottom - 50))


class GhostBook:
    """The ghost encyclopedia"""
    
    def __init__(self, screen_rect, ghosts):
        self.rect = pygame.Rect(screen_rect.width // 8, screen_rect.height // 8,
                               screen_rect.width * 3 // 4, screen_rect.height * 3 // 4)
        self.ghosts = ghosts
        self.current_page = 0
        self.scroll_offset = 0
        
    def next_page(self):
        """Go to next ghost"""
        if self.current_page < len(self.ghosts) - 1:
            self.current_page += 1
            self.scroll_offset = 0
            
    def prev_page(self):
        """Go to previous ghost"""
        if self.current_page > 0:
            self.current_page -= 1
            self.scroll_offset = 0
            
    def draw_ghost_sketch(self, surface, ghost, rect):
        """Draw a sketch-like representation of the ghost"""
        center_x = rect.centerx
        center_y = rect.centery
        
        # Background for sketch
        pygame.draw.rect(surface, (250, 245, 230), rect)
        pygame.draw.rect(surface, SEPIA, rect, 2)
        
        sketch_data = ghost.sketch_data
        ghost_type = sketch_data.get("type", "humanoid")
        features = sketch_data.get("features", [])
        
        # Draw based on type
        if ghost_type == "humanoid":
            # Head
            pygame.draw.circle(surface, ghost.color, (center_x, center_y - 50), 30, 3)
            # Body
            pygame.draw.line(surface, ghost.color, (center_x, center_y - 20), 
                           (center_x, center_y + 40), 3)
            # Arms
            pygame.draw.line(surface, ghost.color, (center_x, center_y), 
                           (center_x - 40, center_y + 20), 3)
            pygame.draw.line(surface, ghost.color, (center_x, center_y), 
                           (center_x + 40, center_y + 20), 3)
            # Legs
            pygame.draw.line(surface, ghost.color, (center_x, center_y + 40), 
                           (center_x - 20, center_y + 80), 3)
            pygame.draw.line(surface, ghost.color, (center_x, center_y + 40), 
                           (center_x + 20, center_y + 80), 3)
            
            # Special features
            if "three_arms" in features:
                pygame.draw.line(surface, ghost.color, (center_x, center_y - 10),
                               (center_x - 30, center_y - 40), 3)
            if "dress" in features:
                pygame.draw.polygon(surface, ghost.color,
                                  [(center_x - 30, center_y + 20), (center_x + 30, center_y + 20),
                                   (center_x + 40, center_y + 80), (center_x - 40, center_y + 80)], 3)
            if "cleaver" in features:
                pygame.draw.rect(surface, (100, 100, 110), 
                               (center_x + 45, center_y + 10, 30, 20), 2)
            if "long_hair" in features:
                for i in range(-3, 4):
                    pygame.draw.line(surface, ghost.color,
                                   (center_x + i * 8, center_y - 30),
                                   (center_x + i * 10, center_y + 30), 2)
                                   
        elif ghost_type == "amorphous":
            # Swirling mass
            for i in range(5):
                radius = 40 - i * 5
                pygame.draw.circle(surface, ghost.color, 
                                 (center_x + i * 3, center_y + i * 2), radius, 2)
            # Eyes
            pygame.draw.circle(surface, RED, (center_x - 15, center_y - 10), 8)
            pygame.draw.circle(surface, RED, (center_x + 15, center_y - 10), 8)
            
        elif ghost_type == "child":
            # Smaller figure
            pygame.draw.circle(surface, ghost.color, (center_x, center_y - 30), 25, 3)
            pygame.draw.line(surface, ghost.color, (center_x, center_y - 5),
                           (center_x, center_y + 30), 3)
            pygame.draw.line(surface, ghost.color, (center_x, center_y + 10),
                           (center_x - 25, center_y + 20), 3)
            pygame.draw.line(surface, ghost.color, (center_x, center_y + 10),
                           (center_x + 25, center_y + 20), 3)
            # Ball
            if "ball" in features:
                pygame.draw.circle(surface, RED, (center_x + 40, center_y + 50), 15, 3)
                
        elif ghost_type == "shifting":
            # Multiple overlapping forms
            for i in range(3):
                offset = (i - 1) * 15
                pygame.draw.ellipse(surface, ghost.color,
                                  (center_x - 30 + offset, center_y - 50 + abs(offset),
                                   60, 100), 2)
            # Multiple eyes
            for x, y in [(-20, -20), (20, -20), (0, 0), (-15, 20), (15, 20)]:
                pygame.draw.circle(surface, WHITE, (center_x + x, center_y + y), 6)
                pygame.draw.circle(surface, BLACK, (center_x + x, center_y + y), 3)
        
        # Sketch lines for effect
        for _ in range(10):
            import random
            x1 = rect.x + random.randint(10, rect.width - 10)
            y1 = rect.y + random.randint(10, rect.height - 10)
            pygame.draw.line(surface, (230, 220, 200), (x1, y1), (x1 + 5, y1 + 3), 1)
    
    def draw(self, surface, fonts):
        """Draw the ghost book"""
        # Book background
        pygame.draw.rect(surface, (80, 60, 40), self.rect, border_radius=15)
        pygame.draw.rect(surface, (60, 45, 30), self.rect, 4, border_radius=15)
        
        # Inner pages
        inner_rect = self.rect.inflate(-30, -30)
        pygame.draw.rect(surface, (250, 240, 220), inner_rect, border_radius=10)
        
        if self.current_page < len(self.ghosts):
            ghost = self.ghosts[self.current_page]
            
            # Left page - Sketch
            sketch_rect = pygame.Rect(inner_rect.x + 20, inner_rect.y + 60, 
                                     inner_rect.width // 2 - 40, inner_rect.height - 120)
            self.draw_ghost_sketch(surface, ghost, sketch_rect)
            
            # Right page - Information
            info_x = inner_rect.x + inner_rect.width // 2 + 20
            info_y = inner_rect.y + 30
            
            # Name
            name_text = fonts['large'].render(ghost.name, True, SEPIA)
            surface.blit(name_text, (info_x, info_y))
            info_y += 50
            
            # Description
            words = ghost.description.split()
            lines = []
            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                if fonts['small'].size(test_line)[0] < inner_rect.width // 2 - 50:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word + " "
            lines.append(current_line)
            
            for line in lines[:6]:
                text = fonts['small'].render(line, True, DARK_GRAY)
                surface.blit(text, (info_x, info_y))
                info_y += 22
            
            info_y += 20
            
            # Behaviors
            behavior_title = fonts['medium'].render("Known Behaviors:", True, SEPIA)
            surface.blit(behavior_title, (info_x, info_y))
            info_y += 30
            
            for i, behavior in enumerate(ghost.behaviors[:5]):
                behavior_text = f"• {behavior.replace('_', ' ').title()}"
                text = fonts['small'].render(behavior_text, True, DARK_GRAY)
                surface.blit(text, (info_x + 10, info_y))
                info_y += 22
            
            # Aggression indicator
            info_y += 20
            aggr_title = fonts['medium'].render("Base Aggression:", True, SEPIA)
            surface.blit(aggr_title, (info_x, info_y))
            info_y += 25
            
            # Aggression bar
            bar_rect = pygame.Rect(info_x, info_y, 200, 20)
            pygame.draw.rect(surface, GRAY, bar_rect, border_radius=5)
            fill_width = int(200 * ghost.base_aggression)
            fill_color = (int(255 * ghost.base_aggression), int(255 * (1 - ghost.base_aggression)), 0)
            pygame.draw.rect(surface, fill_color, 
                           (info_x, info_y, fill_width, 20), border_radius=5)
        
        # Page title
        title = fonts['large'].render("Ghost Encyclopedia", True, SEPIA)
        surface.blit(title, (inner_rect.centerx - title.get_width() // 2, inner_rect.y + 10))
        
        # Navigation
        nav_text = fonts['small'].render(f"Ghost {self.current_page + 1} of {len(self.ghosts)} - Use Arrow Keys or Click Edges", 
                                        True, GRAY)
        surface.blit(nav_text, (inner_rect.centerx - nav_text.get_width() // 2, inner_rect.bottom - 30))
        
        # Navigation arrows
        if self.current_page > 0:
            pygame.draw.polygon(surface, SEPIA, 
                              [(inner_rect.x + 30, inner_rect.centery),
                               (inner_rect.x + 50, inner_rect.centery - 20),
                               (inner_rect.x + 50, inner_rect.centery + 20)])
        if self.current_page < len(self.ghosts) - 1:
            pygame.draw.polygon(surface, SEPIA,
                              [(inner_rect.right - 30, inner_rect.centery),
                               (inner_rect.right - 50, inner_rect.centery - 20),
                               (inner_rect.right - 50, inner_rect.centery + 20)])


class IdentifyMenu:
    """Menu for identifying the ghost"""
    
    def __init__(self, screen_rect, ghosts, font):
        self.rect = pygame.Rect(screen_rect.width // 4, screen_rect.height // 8,
                               screen_rect.width // 2, screen_rect.height * 3 // 4)
        self.ghosts = ghosts
        self.font = font
        self.selected = None
        self.buttons = []
        self.scroll_offset = 0
        self.create_buttons()
        
    def create_buttons(self):
        """Create ghost selection buttons"""
        self.buttons = []
        small_font = pygame.font.Font(None, 24)
        for i, ghost in enumerate(self.ghosts):
            y = self.rect.y + 80 + i * 50
            btn = Button(
                (self.rect.x + 30, y, self.rect.width - 60, 40),
                ghost.name,
                small_font
            )
            self.buttons.append((btn, ghost))
            
    def draw(self, surface, guesses_left):
        """Draw the identify menu"""
        # Background
        pygame.draw.rect(surface, (30, 30, 40), self.rect, border_radius=15)
        pygame.draw.rect(surface, (100, 80, 60), self.rect, 3, border_radius=15)
        
        # Title
        title = self.font.render("Identify the Ghost", True, WHITE)
        surface.blit(title, (self.rect.centerx - title.get_width() // 2, self.rect.y + 20))
        
        # Guesses remaining
        guesses_text = self.font.render(f"Guesses Remaining: {guesses_left}", True, 
                                       RED if guesses_left == 1 else YELLOW)
        surface.blit(guesses_text, (self.rect.centerx - guesses_text.get_width() // 2, 
                                   self.rect.y + 50))
        
        # Ghost buttons (scrollable area)
        clip_rect = pygame.Rect(self.rect.x, self.rect.y + 80, 
                               self.rect.width, self.rect.height - 140)
        surface.set_clip(clip_rect)
        
        for btn, ghost in self.buttons:
            adjusted_rect = btn.rect.copy()
            adjusted_rect.y -= self.scroll_offset
            if clip_rect.colliderect(adjusted_rect):
                temp_btn = Button(adjusted_rect, btn.text, btn.font)
                temp_btn.hovered = btn.hovered
                if ghost == self.selected:
                    pygame.draw.rect(surface, (80, 120, 80), adjusted_rect, border_radius=8)
                temp_btn.draw(surface)
        
        surface.set_clip(None)
        
        # Confirm button
        if self.selected:
            confirm_rect = pygame.Rect(self.rect.centerx - 80, self.rect.bottom - 50, 160, 40)
            pygame.draw.rect(surface, GREEN, confirm_rect, border_radius=8)
            pygame.draw.rect(surface, WHITE, confirm_rect, 2, border_radius=8)
            confirm_text = self.font.render("Confirm", True, BLACK)
            surface.blit(confirm_text, (confirm_rect.centerx - confirm_text.get_width() // 2,
                                       confirm_rect.centery - confirm_text.get_height() // 2))
        
        # Instructions
        small_font = pygame.font.Font(None, 20)
        inst = small_font.render("Click a ghost to select, then confirm. Press ESC to cancel.", True, GRAY)
        surface.blit(inst, (self.rect.centerx - inst.get_width() // 2, self.rect.bottom - 20))
        
    def update(self, mouse_pos):
        """Update button hover states"""
        adjusted_pos = (mouse_pos[0], mouse_pos[1] + self.scroll_offset)
        for btn, ghost in self.buttons:
            btn.update(adjusted_pos)
            
    def handle_click(self, pos):
        """Handle click events"""
        # Check ghost buttons
        adjusted_pos = (pos[0], pos[1] + self.scroll_offset)
        for btn, ghost in self.buttons:
            if btn.rect.collidepoint(adjusted_pos):
                self.selected = ghost
                return None
        
        # Check confirm button
        if self.selected:
            confirm_rect = pygame.Rect(self.rect.centerx - 80, self.rect.bottom - 50, 160, 40)
            if confirm_rect.collidepoint(pos):
                return self.selected
        
        return None
        
    def scroll(self, amount):
        """Scroll the ghost list"""
        max_scroll = max(0, len(self.ghosts) * 50 - (self.rect.height - 140))
        self.scroll_offset = max(0, min(max_scroll, self.scroll_offset + amount))


class ZoomView:
    """Zoomed view of an object"""
    
    def __init__(self, screen_rect):
        self.rect = pygame.Rect(screen_rect.width // 6, screen_rect.height // 6,
                               screen_rect.width * 2 // 3, screen_rect.height * 2 // 3)
        self.obj = None
        self.description = ""
        
    def set_object(self, obj):
        """Set the object to zoom on"""
        self.obj = obj
        self.description = obj.zoom_description if obj.zoom_description else obj.description
        
    def draw(self, surface, font):
        """Draw the zoom view"""
        # Darkened background
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))
        
        # Main panel
        pygame.draw.rect(surface, (40, 35, 30), self.rect, border_radius=15)
        pygame.draw.rect(surface, (100, 80, 50), self.rect, 3, border_radius=15)
        
        if self.obj:
            # Title
            title = font.render(self.obj.name, True, CREAM)
            surface.blit(title, (self.rect.centerx - title.get_width() // 2, self.rect.y + 20))
            
            # Object representation (larger rectangle)
            obj_rect = pygame.Rect(self.rect.x + 50, self.rect.y + 70, 
                                  self.rect.width - 100, self.rect.height - 200)
            pygame.draw.rect(surface, (60, 55, 50), obj_rect, border_radius=10)
            
            # Draw a larger version of object interaction
            center_text = font.render("[ Examining... ]", True, GRAY)
            surface.blit(center_text, (obj_rect.centerx - center_text.get_width() // 2,
                                      obj_rect.centery - center_text.get_height() // 2))
            
            # Description
            small_font = pygame.font.Font(None, 22)
            words = self.description.split()
            lines = []
            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                if small_font.size(test_line)[0] < self.rect.width - 60:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word + " "
            lines.append(current_line)
            
            y = self.rect.bottom - 100
            for line in lines[-4:]:
                text = small_font.render(line, True, CREAM)
                surface.blit(text, (self.rect.x + 30, y))
                y += 22
        
        # Close instruction
        small_font = pygame.font.Font(None, 20)
        close_text = small_font.render("Click anywhere or press ESC to close", True, GRAY)
        surface.blit(close_text, (self.rect.centerx - close_text.get_width() // 2, 
                                 self.rect.bottom - 25))
