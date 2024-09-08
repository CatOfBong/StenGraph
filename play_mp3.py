import pygame
import time
import threading
import os

def play_mp3():
    def play_music():
        pygame.init()
        pygame.mixer.init()

        # Construct the path to the MP3 file
        mp3_path = "your_file.mp3"

        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()

        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

        pygame.mixer.quit()
        pygame.quit()

    # Start playing the music in a separate thread
    music_thread = threading.Thread(target=play_music)
    music_thread.start()
