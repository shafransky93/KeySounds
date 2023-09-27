#!/usr/bin/env python

from package_installer import check_and_install_packages

# List of required packages
required_packages = [
    "pygame",
    "keyboard",
]

if __name__ == "__main__":
    check_and_install_packages(required_packages)

import keyboard
import pygame

# Initialize pygame
pygame.mixer.init()

# Define the sound file you want to play (replace with your own sound file)
sound_file = "pew-pew-.mp3"

# Load the sound
sound = pygame.mixer.Sound(sound_file)

# Function to play the sound
def play_sound(e):
    sound.play()

# Register a callback for key presses
keyboard.on_press(play_sound)

# Wait for key presses
keyboard.wait()
