#!/usr/bin/env python3
"""
Paranormal Investigations - A first-person haunted house ghost hunting game
Main entry point for the game
"""

import pygame
import sys
from game import Game

def main():
    """Main entry point for the game."""
    pygame.init()
    
    # Set up display
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Paranormal Investigations")
    
    # Create and run the game
    game = Game(screen)
    game.run()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
