"""
Main game class for Paranormal Investigations
"""

import pygame
import random
import math
import time
from constants import *
from ghosts import get_random_ghost, get_all_ghosts, Ghost
from rooms import create_all_rooms
from ui import Button, Notebook, GhostBook, IdentifyMenu, ZoomView


class Game:
    """Main game class"""
    
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize fonts
        self.fonts = {
            'small': pygame.font.Font(None, FONT_SMALL),
            'medium': pygame.font.Font(None, FONT_MEDIUM),
            'large': pygame.font.Font(None, FONT_LARGE),
            'title': pygame.font.Font(None, FONT_TITLE),
        }
        
        # Game state
        self.state = STATE_MENU
        self.previous_state = None
        self.difficulty = DIFFICULTY_NORMAL
        
        # Game objects
        self.rooms = None
        self.current_room = None
        self.haunting_ghost = None
        self.all_ghosts = get_all_ghosts()
        
        # UI elements
        self.notebook = None
        self.ghost_book = None
        self.identify_menu = None
        self.zoom_view = None
        
        # Settings (must be set before create_menu_buttons)
        self.graphics_quality = "High"
        self.show_hints = True
        
        # Menu buttons
        self.menu_buttons = []
        self.settings_buttons = []
        self.difficulty_buttons = []
        self.pause_buttons = []
        self.create_menu_buttons()
        
        # Game mechanics
        self.flashlight_on = False
        self.mouse_pos = (0, 0)
        self.game_start_time = 0
        self.ghost_arrived = False
        self.ghost_arrival_time = 0
        self.grace_period = 0
        self.guesses_remaining = 2
        self.aggression = 0
        self.time_limit = 0
        self.last_behavior_time = 0
        self.active_effects = []
        self.blind_effect = 0
        self.jumpscare_ghost = None
        self.jumpscare_timer = 0
        
        # Lightning effect
        self.lightning_active = False
        self.lightning_timer = 0
        
        # Camera shake
        self.camera_shake = 0
        self.shake_offset = (0, 0)
        
    def create_menu_buttons(self):
        """Create all menu buttons"""
        center_x = SCREEN_WIDTH // 2
        
        # Main menu buttons
        self.menu_buttons = [
            Button((center_x - 100, 300, 200, 50), "Start Game", self.fonts['medium'],
                  lambda: self.set_state(STATE_DIFFICULTY)),
            Button((center_x - 100, 370, 200, 50), "Settings", self.fonts['medium'],
                  lambda: self.set_state(STATE_SETTINGS)),
            Button((center_x - 100, 440, 200, 50), "Credits", self.fonts['medium'],
                  lambda: self.set_state(STATE_CREDITS)),
            Button((center_x - 100, 510, 200, 50), "Quit", self.fonts['medium'],
                  self.quit_game),
        ]
        
        # Settings buttons
        self.settings_buttons = [
            Button((center_x - 100, 250, 200, 50), f"Graphics: {self.graphics_quality}", 
                  self.fonts['medium'], self.toggle_graphics),
            Button((center_x - 100, 320, 200, 50), f"Hints: {'On' if self.show_hints else 'Off'}", 
                  self.fonts['medium'], self.toggle_hints),
            Button((center_x - 100, 450, 200, 50), "Back", self.fonts['medium'],
                  lambda: self.set_state(STATE_MENU)),
        ]
        
        # Difficulty buttons
        self.difficulty_buttons = [
            Button((center_x - 100, 250, 200, 50), "Easy", self.fonts['medium'],
                  lambda: self.start_game(DIFFICULTY_EASY)),
            Button((center_x - 100, 320, 200, 50), "Normal", self.fonts['medium'],
                  lambda: self.start_game(DIFFICULTY_NORMAL)),
            Button((center_x - 100, 390, 200, 50), "Hard", self.fonts['medium'],
                  lambda: self.start_game(DIFFICULTY_HARD)),
            Button((center_x - 100, 460, 200, 50), "Nightmare", self.fonts['medium'],
                  lambda: self.start_game(DIFFICULTY_NIGHTMARE)),
            Button((center_x - 100, 550, 200, 50), "Back", self.fonts['medium'],
                  lambda: self.set_state(STATE_MENU)),
        ]
        
        # Pause menu buttons
        self.pause_buttons = [
            Button((center_x - 100, 300, 200, 50), "Resume", self.fonts['medium'],
                  self.resume_game),
            Button((center_x - 100, 370, 200, 50), "Main Menu", self.fonts['medium'],
                  lambda: self.set_state(STATE_MENU)),
        ]
        
    def toggle_graphics(self):
        """Toggle graphics quality"""
        qualities = ["Low", "Medium", "High"]
        idx = qualities.index(self.graphics_quality)
        self.graphics_quality = qualities[(idx + 1) % len(qualities)]
        self.settings_buttons[0].text = f"Graphics: {self.graphics_quality}"
        
    def toggle_hints(self):
        """Toggle hint display"""
        self.show_hints = not self.show_hints
        self.settings_buttons[1].text = f"Hints: {'On' if self.show_hints else 'Off'}"
        
    def set_state(self, new_state):
        """Change game state"""
        self.previous_state = self.state
        self.state = new_state
        
    def start_game(self, difficulty):
        """Start a new game with given difficulty"""
        self.difficulty = difficulty
        settings = DIFFICULTY_SETTINGS[difficulty]
        
        # Reset game state
        self.rooms = create_all_rooms()
        self.current_room = self.rooms[ROOM_ENTRANCE]
        self.haunting_ghost = get_random_ghost()
        self.haunting_ghost.reset()
        
        # Initialize UI
        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.notebook = Notebook(screen_rect)
        self.ghost_book = GhostBook(screen_rect, self.all_ghosts)
        self.identify_menu = IdentifyMenu(screen_rect, self.all_ghosts, self.fonts['medium'])
        self.zoom_view = ZoomView(screen_rect)
        
        # Set up game mechanics
        self.guesses_remaining = settings['guesses']
        self.grace_period = random.randint(*settings['grace_period'])
        self.time_limit = self.haunting_ghost.time_limit * settings['time_multiplier']
        self.aggression = self.haunting_ghost.base_aggression
        
        self.game_start_time = time.time()
        self.ghost_arrived = False
        self.ghost_arrival_time = 0
        self.last_behavior_time = 0
        self.active_effects = []
        self.blind_effect = 0
        self.flashlight_on = False
        self.lightning_active = False
        
        self.state = STATE_PLAYING
        
    def resume_game(self):
        """Resume the game from pause"""
        self.state = STATE_PLAYING
        
    def quit_game(self):
        """Quit the game"""
        self.running = False
        
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
                self.update_hover()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.handle_click(event.pos)
                elif event.button == 4:  # Scroll up
                    self.handle_scroll(-30)
                elif event.button == 5:  # Scroll down
                    self.handle_scroll(30)
                    
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
                
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event)
                
    def update_hover(self):
        """Update hover states"""
        if self.state == STATE_MENU:
            for btn in self.menu_buttons:
                btn.update(self.mouse_pos)
        elif self.state == STATE_SETTINGS:
            for btn in self.settings_buttons:
                btn.update(self.mouse_pos)
        elif self.state == STATE_DIFFICULTY:
            for btn in self.difficulty_buttons:
                btn.update(self.mouse_pos)
        elif self.state == STATE_PAUSED:
            for btn in self.pause_buttons:
                btn.update(self.mouse_pos)
        elif self.state == STATE_PLAYING:
            if self.current_room:
                self.current_room.update_hover(self.mouse_pos)
        elif self.state == STATE_IDENTIFY:
            if self.identify_menu:
                self.identify_menu.update(self.mouse_pos)
                
    def handle_click(self, pos):
        """Handle mouse click"""
        if self.state == STATE_MENU:
            for btn in self.menu_buttons:
                if btn.handle_click(pos):
                    return
                    
        elif self.state == STATE_SETTINGS:
            for btn in self.settings_buttons:
                if btn.handle_click(pos):
                    return
                    
        elif self.state == STATE_DIFFICULTY:
            for btn in self.difficulty_buttons:
                if btn.handle_click(pos):
                    return
                    
        elif self.state == STATE_PAUSED:
            for btn in self.pause_buttons:
                if btn.handle_click(pos):
                    return
                    
        elif self.state == STATE_PLAYING:
            # Check for room navigation
            self.handle_room_navigation(pos)
            # Check for object interaction
            self.handle_object_interaction(pos)
            
        elif self.state == STATE_IDENTIFY:
            result = self.identify_menu.handle_click(pos)
            if result:
                self.check_ghost_identification(result)
                
        elif self.state == STATE_ZOOM:
            self.state = STATE_PLAYING
            
        elif self.state in [STATE_GAME_OVER, STATE_VICTORY]:
            self.set_state(STATE_MENU)
            
        elif self.state == STATE_NOTEBOOK:
            pass  # Notebook handles its own clicks
            
        elif self.state == STATE_GHOST_BOOK:
            # Check for page navigation
            if self.ghost_book:
                if pos[0] < SCREEN_WIDTH // 3:
                    self.ghost_book.prev_page()
                elif pos[0] > SCREEN_WIDTH * 2 // 3:
                    self.ghost_book.next_page()
                    
        elif self.state == STATE_CREDITS:
            self.set_state(STATE_MENU)
            
    def handle_room_navigation(self, pos):
        """Handle clicking on room edges to navigate"""
        if not self.current_room:
            return
            
        connections = self.current_room.connections
        
        # Left edge
        if pos[0] < EDGE_SIZE and connections.get("left"):
            self.current_room = self.rooms[connections["left"]]
            return
        # Right edge
        if pos[0] > SCREEN_WIDTH - EDGE_SIZE and connections.get("right"):
            self.current_room = self.rooms[connections["right"]]
            return
        # Top edge
        if pos[1] < EDGE_SIZE and connections.get("up"):
            self.current_room = self.rooms[connections["up"]]
            return
        # Bottom edge
        if pos[1] > SCREEN_HEIGHT - EDGE_SIZE and connections.get("down"):
            self.current_room = self.rooms[connections["down"]]
            return
            
    def handle_object_interaction(self, pos):
        """Handle clicking on interactive objects"""
        if not self.current_room:
            return
            
        obj = self.current_room.get_object_at(pos)
        if obj:
            if obj.interaction_type == "toggle":
                obj.state = not obj.state
                self.notebook.add_note(f"Toggled {obj.name}")
            elif obj.interaction_type == "examine":
                self.notebook.add_note(f"Examined {obj.name}")
            elif obj.interaction_type == "zoom":
                self.zoom_view.set_object(obj)
                self.state = STATE_ZOOM
                self.notebook.add_note(f"Zoomed in on {obj.name}")
                
    def handle_scroll(self, amount):
        """Handle scroll wheel"""
        if self.state == STATE_IDENTIFY and self.identify_menu:
            self.identify_menu.scroll(amount)
        elif self.state == STATE_GHOST_BOOK and self.ghost_book:
            self.ghost_book.scroll_offset += amount
            
    def handle_keydown(self, event):
        """Handle key press"""
        key = event.key
        
        # Global shortcuts
        if key == pygame.K_ESCAPE:
            if self.state == STATE_PLAYING:
                self.state = STATE_PAUSED
            elif self.state in [STATE_PAUSED, STATE_NOTEBOOK, STATE_GHOST_BOOK, 
                               STATE_IDENTIFY, STATE_ZOOM]:
                self.state = STATE_PLAYING
            elif self.state in [STATE_SETTINGS, STATE_CREDITS, STATE_DIFFICULTY]:
                self.state = STATE_MENU
                
        if self.state == STATE_PLAYING:
            if key == pygame.K_f:
                self.flashlight_on = not self.flashlight_on
            elif key == pygame.K_n:
                self.state = STATE_NOTEBOOK
                self.notebook.editing = True
            elif key == pygame.K_g:
                self.state = STATE_GHOST_BOOK
            elif key == pygame.K_i:
                self.state = STATE_IDENTIFY
            elif key == pygame.K_p:
                self.state = STATE_PAUSED
                
        elif self.state == STATE_NOTEBOOK:
            if self.notebook.editing:
                if key == pygame.K_RETURN:
                    if self.notebook.current_input:
                        self.notebook.add_note(self.notebook.current_input)
                        self.notebook.current_input = ""
                elif key == pygame.K_BACKSPACE:
                    self.notebook.current_input = self.notebook.current_input[:-1]
                elif event.unicode and len(self.notebook.current_input) < 60:
                    self.notebook.current_input += event.unicode
                    
        elif self.state == STATE_GHOST_BOOK:
            if key == pygame.K_LEFT:
                self.ghost_book.prev_page()
            elif key == pygame.K_RIGHT:
                self.ghost_book.next_page()
                
    def handle_keyup(self, event):
        """Handle key release"""
        pass
        
    def check_ghost_identification(self, selected_ghost):
        """Check if player correctly identified the ghost"""
        if selected_ghost.name == self.haunting_ghost.name:
            # Correct!
            self.state = STATE_VICTORY
        else:
            # Wrong guess
            self.guesses_remaining -= 1
            self.aggression += 0.2
            self.blind_effect = 2.0  # 2 seconds of blind effect
            
            if self.guesses_remaining <= 0:
                # Game over - jumpscare
                self.jumpscare_ghost = self.haunting_ghost
                self.jumpscare_timer = 3.0
                self.state = STATE_JUMPSCARE
            else:
                self.state = STATE_PLAYING
                self.camera_shake = 0.5
                
    def update(self, dt):
        """Update game state"""
        if self.state == STATE_PLAYING:
            self.update_gameplay(dt)
        elif self.state == STATE_JUMPSCARE:
            self.jumpscare_timer -= dt
            if self.jumpscare_timer <= 0:
                self.state = STATE_GAME_OVER
                
        # Update camera shake
        if self.camera_shake > 0:
            self.camera_shake -= dt
            self.shake_offset = (
                random.randint(-5, 5) if self.camera_shake > 0 else 0,
                random.randint(-5, 5) if self.camera_shake > 0 else 0
            )
        else:
            self.shake_offset = (0, 0)
            
        # Update blind effect
        if self.blind_effect > 0:
            self.blind_effect -= dt
            
    def update_gameplay(self, dt):
        """Update gameplay mechanics"""
        current_time = time.time()
        elapsed = current_time - self.game_start_time
        
        # Check for ghost arrival
        if not self.ghost_arrived and elapsed >= self.grace_period:
            self.ghost_arrived = True
            self.ghost_arrival_time = current_time
            self.lightning_active = True
            self.lightning_timer = 0.5
            
        # Update lightning
        if self.lightning_active:
            self.lightning_timer -= dt
            if self.lightning_timer <= 0:
                self.lightning_active = False
                
        # Ghost behaviors
        if self.ghost_arrived:
            time_since_arrival = current_time - self.ghost_arrival_time
            
            # Increase aggression over time
            settings = DIFFICULTY_SETTINGS[self.difficulty]
            self.aggression = min(1.0, self.haunting_ghost.base_aggression + 
                                 (time_since_arrival / self.time_limit) * settings['aggression_rate'])
            
            # Trigger behaviors
            behavior_interval = max(5, 30 - self.aggression * 25)
            if current_time - self.last_behavior_time > behavior_interval:
                self.trigger_ghost_behavior()
                self.last_behavior_time = current_time
                
            # Check for time limit
            if time_since_arrival >= self.time_limit:
                self.jumpscare_ghost = self.haunting_ghost
                self.jumpscare_timer = 3.0
                self.state = STATE_JUMPSCARE
                
    def trigger_ghost_behavior(self):
        """Trigger a random ghost behavior"""
        behavior = self.haunting_ghost.get_random_behavior()
        self.active_effects.append({
            'type': behavior,
            'start_time': time.time(),
            'duration': random.uniform(2, 5)
        })
        
        # Some behaviors cause camera shake
        if behavior in ['slam_doors', 'throw_objects', 'violent_door_slams']:
            self.camera_shake = 0.3
            
    def draw(self):
        """Draw the current game state"""
        # Apply camera shake
        self.screen.fill(BLACK)
        
        if self.state == STATE_MENU:
            self.draw_menu()
        elif self.state == STATE_SETTINGS:
            self.draw_settings()
        elif self.state == STATE_CREDITS:
            self.draw_credits()
        elif self.state == STATE_DIFFICULTY:
            self.draw_difficulty()
        elif self.state == STATE_PLAYING:
            self.draw_gameplay()
        elif self.state == STATE_PAUSED:
            self.draw_gameplay()
            self.draw_pause()
        elif self.state == STATE_NOTEBOOK:
            self.draw_gameplay()
            self.draw_notebook()
        elif self.state == STATE_GHOST_BOOK:
            self.draw_gameplay()
            self.draw_ghost_book()
        elif self.state == STATE_IDENTIFY:
            self.draw_gameplay()
            self.draw_identify()
        elif self.state == STATE_ZOOM:
            self.draw_gameplay()
            self.draw_zoom()
        elif self.state == STATE_JUMPSCARE:
            self.draw_jumpscare()
        elif self.state == STATE_GAME_OVER:
            self.draw_game_over()
        elif self.state == STATE_VICTORY:
            self.draw_victory()
            
        pygame.display.flip()
        
    def draw_menu(self):
        """Draw main menu"""
        # Background
        self.screen.fill(MENU_BG)
        
        # Title
        title_text = self.fonts['title'].render("Paranormal", True, WHITE)
        title_text2 = self.fonts['title'].render("Investigations", True, RED)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        self.screen.blit(title_text2, (SCREEN_WIDTH // 2 - title_text2.get_width() // 2, 170))
        
        # Subtitle
        subtitle = self.fonts['medium'].render("Can you identify the ghost before it's too late?", 
                                              True, GRAY)
        self.screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 250))
        
        # Buttons
        for btn in self.menu_buttons:
            btn.draw(self.screen)
            
        # Version
        version = self.fonts['small'].render("v1.0", True, DARK_GRAY)
        self.screen.blit(version, (10, SCREEN_HEIGHT - 25))
        
    def draw_settings(self):
        """Draw settings menu"""
        self.screen.fill(MENU_BG)
        
        title = self.fonts['title'].render("Settings", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        # Note about sound
        note = self.fonts['small'].render("Note: Sound is not yet implemented", True, GRAY)
        self.screen.blit(note, (SCREEN_WIDTH // 2 - note.get_width() // 2, 180))
        
        for btn in self.settings_buttons:
            btn.draw(self.screen)
            
    def draw_credits(self):
        """Draw credits screen"""
        self.screen.fill(MENU_BG)
        
        title = self.fonts['title'].render("Credits", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        credits = [
            "Paranormal Investigations",
            "",
            "A ghost hunting experience",
            "",
            "Created with Python and Pygame",
            "",
            "Click anywhere to return"
        ]
        
        y = 200
        for line in credits:
            text = self.fonts['medium'].render(line, True, WHITE if line else GRAY)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y))
            y += 40
            
    def draw_difficulty(self):
        """Draw difficulty selection"""
        self.screen.fill(MENU_BG)
        
        title = self.fonts['title'].render("Select Difficulty", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        # Difficulty descriptions
        descriptions = {
            0: "3 guesses, more time, slower aggression",
            1: "2 guesses, standard time and aggression",
            2: "1 guess, less time, faster aggression", 
            3: "1 guess, minimal time, extreme aggression"
        }
        
        for i, btn in enumerate(self.difficulty_buttons[:-1]):
            btn.draw(self.screen)
            if i < len(descriptions):
                desc = self.fonts['small'].render(descriptions[i], True, GRAY)
                self.screen.blit(desc, (btn.rect.right + 20, btn.rect.centery - 8))
        
        self.difficulty_buttons[-1].draw(self.screen)  # Back button
        
    def draw_gameplay(self):
        """Draw main gameplay"""
        # Create offset surface for camera shake
        offset_x, offset_y = self.shake_offset
        
        if self.current_room:
            self.current_room.draw(self.screen, self.fonts['medium'])
            
        # Draw ghost effects
        self.draw_ghost_effects()
        
        # Draw flashlight
        if self.flashlight_on:
            self.draw_flashlight()
            
        # Draw blind effect
        if self.blind_effect > 0:
            self.draw_blind_effect()
            
        # Draw lightning
        if self.lightning_active:
            self.draw_lightning()
            
        # Draw HUD
        self.draw_hud()
        
        # Draw hints
        if self.show_hints:
            self.draw_hints()
            
    def draw_ghost_effects(self):
        """Draw active ghost effects"""
        current_time = time.time()
        remaining_effects = []
        
        for effect in self.active_effects:
            elapsed = current_time - effect['start_time']
            if elapsed < effect['duration']:
                remaining_effects.append(effect)
                self.draw_effect(effect['type'], elapsed / effect['duration'])
                
        self.active_effects = remaining_effects
        
    def draw_effect(self, effect_type, progress):
        """Draw a specific ghost effect"""
        alpha = int(255 * (1 - progress))
        
        if effect_type in ['flicker_lights', 'darken_room']:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, min(200, alpha)))
            self.screen.blit(overlay, (0, 0))
            
        elif effect_type in ['cold_spots', 'cold_breath']:
            # Blue tint
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((100, 150, 255, min(100, alpha // 2)))
            self.screen.blit(overlay, (0, 0))
            
        elif effect_type == 'visual_distortion':
            # Wavy effect would go here
            pass
            
    def draw_flashlight(self):
        """Draw flashlight effect"""
        # Create darkness overlay
        darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        darkness.fill((0, 0, 0, 200))
        
        # Cut out flashlight area
        mx, my = self.mouse_pos
        
        # Create gradient flashlight
        for r in range(FLASHLIGHT_OUTER_RADIUS, 0, -5):
            alpha = int(200 * (r / FLASHLIGHT_OUTER_RADIUS))
            pygame.draw.circle(darkness, (0, 0, 0, 200 - alpha), (mx, my), r)
            
        self.screen.blit(darkness, (0, 0))
        
    def draw_blind_effect(self):
        """Draw temporary blindness effect"""
        alpha = int(255 * min(1.0, self.blind_effect))
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, alpha))
        self.screen.blit(overlay, (0, 0))
        
    def draw_lightning(self):
        """Draw lightning flash"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 200))
        self.screen.blit(overlay, (0, 0))
        
    def draw_hud(self):
        """Draw heads-up display"""
        # Time remaining (if ghost has arrived)
        if self.ghost_arrived:
            time_remaining = self.time_limit - (time.time() - self.ghost_arrival_time)
            minutes = int(time_remaining // 60)
            seconds = int(time_remaining % 60)
            time_text = f"Time: {minutes:02d}:{seconds:02d}"
            time_color = RED if time_remaining < 60 else YELLOW if time_remaining < 180 else WHITE
            time_surf = self.fonts['medium'].render(time_text, True, time_color)
            self.screen.blit(time_surf, (SCREEN_WIDTH - 150, 10))
            
            # Aggression meter
            aggr_text = self.fonts['small'].render("Aggression:", True, WHITE)
            self.screen.blit(aggr_text, (SCREEN_WIDTH - 150, 40))
            bar_rect = pygame.Rect(SCREEN_WIDTH - 150, 60, 100, 15)
            pygame.draw.rect(self.screen, DARK_GRAY, bar_rect)
            fill_width = int(100 * self.aggression)
            fill_color = (int(255 * self.aggression), int(255 * (1 - self.aggression)), 0)
            pygame.draw.rect(self.screen, fill_color, 
                           (bar_rect.x, bar_rect.y, fill_width, bar_rect.height))
        else:
            # Grace period countdown
            remaining = self.grace_period - (time.time() - self.game_start_time)
            if remaining > 0:
                wait_text = self.fonts['small'].render("Investigating...", True, GRAY)
                self.screen.blit(wait_text, (SCREEN_WIDTH - 150, 10))
                
        # Guesses remaining
        guesses_text = self.fonts['medium'].render(f"Guesses: {self.guesses_remaining}", True,
                                                  RED if self.guesses_remaining == 1 else WHITE)
        self.screen.blit(guesses_text, (10, 10))
        
        # Flashlight indicator
        fl_text = "Flashlight: ON" if self.flashlight_on else "Flashlight: OFF"
        fl_color = YELLOW if self.flashlight_on else GRAY
        fl_surf = self.fonts['small'].render(fl_text, True, fl_color)
        self.screen.blit(fl_surf, (10, 40))
        
        # Controls hint
        controls = "N: Notes | G: Ghost Book | I: Identify | F: Flashlight | ESC: Pause"
        controls_surf = self.fonts['small'].render(controls, True, DARK_GRAY)
        self.screen.blit(controls_surf, (SCREEN_WIDTH // 2 - controls_surf.get_width() // 2, 
                                        SCREEN_HEIGHT - 25))
        
    def draw_hints(self):
        """Draw gameplay hints"""
        if self.current_room:
            # Highlight interactive objects
            for obj in self.current_room.objects:
                if obj.hovered:
                    hint = self.fonts['small'].render(f"Click: {obj.name}", True, WHITE)
                    self.screen.blit(hint, (obj.rect.centerx - hint.get_width() // 2,
                                           obj.rect.top - 20))
                                           
    def draw_pause(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        title = self.fonts['title'].render("PAUSED", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        
        for btn in self.pause_buttons:
            btn.draw(self.screen)
            
    def draw_notebook(self):
        """Draw notebook overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        self.notebook.draw(self.screen, self.fonts['medium'])
        
    def draw_ghost_book(self):
        """Draw ghost book overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        self.ghost_book.draw(self.screen, self.fonts)
        
    def draw_identify(self):
        """Draw identification menu"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        self.identify_menu.draw(self.screen, self.guesses_remaining)
        
    def draw_zoom(self):
        """Draw zoom view"""
        self.zoom_view.draw(self.screen, self.fonts['large'])
        
    def draw_jumpscare(self):
        """Draw jumpscare"""
        self.screen.fill(BLACK)
        
        if self.jumpscare_ghost:
            # Draw scary ghost face
            center_x = SCREEN_WIDTH // 2
            center_y = SCREEN_HEIGHT // 2
            
            # Flash effect
            if random.random() > 0.3:
                self.screen.fill(self.jumpscare_ghost.color)
                
            # Big scary ghost representation
            ghost_color = self.jumpscare_ghost.color
            pygame.draw.circle(self.screen, ghost_color, (center_x, center_y - 50), 150)
            
            # Scary eyes
            pygame.draw.circle(self.screen, WHITE, (center_x - 60, center_y - 80), 40)
            pygame.draw.circle(self.screen, WHITE, (center_x + 60, center_y - 80), 40)
            pygame.draw.circle(self.screen, RED, (center_x - 60, center_y - 80), 25)
            pygame.draw.circle(self.screen, RED, (center_x + 60, center_y - 80), 25)
            
            # Scary mouth
            pygame.draw.ellipse(self.screen, BLACK, (center_x - 80, center_y, 160, 100))
            
            # Ghost name
            name = self.fonts['title'].render(self.jumpscare_ghost.name, True, WHITE)
            self.screen.blit(name, (center_x - name.get_width() // 2, SCREEN_HEIGHT - 150))
            
    def draw_game_over(self):
        """Draw game over screen"""
        self.screen.fill((30, 0, 0))
        
        title = self.fonts['title'].render("GAME OVER", True, RED)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        
        if self.jumpscare_ghost:
            ghost_text = self.fonts['large'].render(f"The ghost was: {self.jumpscare_ghost.name}",
                                                   True, WHITE)
            self.screen.blit(ghost_text, (SCREEN_WIDTH // 2 - ghost_text.get_width() // 2, 320))
            
        hint = self.fonts['medium'].render("Click anywhere to return to menu", True, GRAY)
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 500))
        
    def draw_victory(self):
        """Draw victory screen"""
        self.screen.fill((0, 30, 0))
        
        title = self.fonts['title'].render("INVESTIGATION COMPLETE", True, GREEN)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        
        if self.haunting_ghost:
            ghost_text = self.fonts['large'].render(
                f"You correctly identified: {self.haunting_ghost.name}!", True, WHITE)
            self.screen.blit(ghost_text, (SCREEN_WIDTH // 2 - ghost_text.get_width() // 2, 320))
            
        # Stats
        time_text = self.fonts['medium'].render(
            f"Guesses remaining: {self.guesses_remaining}", True, WHITE)
        self.screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, 400))
        
        hint = self.fonts['medium'].render("Click anywhere to return to menu", True, GRAY)
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 500))
        
    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            
            self.handle_events()
            self.update(dt)
            self.draw()
            
        pygame.quit()
