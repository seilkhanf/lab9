import pygame
import os
from pygame import mixer

class CustomMusicPlayer:
    def __init__(self, folder_path):
        pygame.init()
        mixer.init()
        self.music_folder = folder_path
        self.music_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav'))]
        self.current_track_index = 0
        self.isPlaying = False

    def load_music(self):
        pygame.mixer.music.load(os.path.join(self.music_folder, self.music_files[self.current_track_index]))

    def play_music(self):
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.music_files)
        self.load_music()
        if self.isPlaying:
            self.play_music()

    def prev_track(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.music_files)
        self.load_music()
        if self.isPlaying:
            self.play_music()

    def run(self):
        self.load_music()

        while True:
            user_input = input('  ')
                
            if user_input == 's':
                self.stop_music()
            elif user_input == ' ':
                self.play_music()
                self.isPlaying = True
            elif user_input == 'n':
                self.next_track()
            elif user_input == 'p':
                self.prev_track()
            elif user_input == 'q':
                pygame.quit()
                exit()

if __name__ == "__main__":
    custom_player = CustomMusicPlayer("C:\\Users\\Daniyar\\Desktop\\pp2\\music")
    custom_player.run()
    
    pygame.quit()
    exit()
