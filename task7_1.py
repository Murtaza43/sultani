import pygame
import keyboard
import os

# Initializing mixer
pygame.mixer.init()

# Full path to the folder containing your mp3 file
MUSIC_FOLDER = r"D:\Lessons\VS Code\Python"
tracks = ["gm.mp3"]  # List of your songs manually

current_track = 0
is_playing = False
paused = False

def load_track(index):
    path = os.path.join(MUSIC_FOLDER, tracks[index])
    pygame.mixer.music.load(path)
    print(f"Loaded: {tracks[index]}")

def play_music():
    global is_playing
    if not is_playing:
        pygame.mixer.music.play()
        is_playing = True
        print("Playing")

def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    print("Stopped")

# Load the only track
load_track(current_track)

print("\n🎵 Music Player Controls:")
print("  [p] Play/Pause")
print("  [s] Stop")
print("  [Esc] Exit\n")

while True:
    try:
        if keyboard.is_pressed('p'):
            if not is_playing:
                play_music()
                paused = False
            elif paused:
                pygame.mixer.music.unpause()
                paused = False
                print("Resumed")
            else:
                pygame.mixer.music.pause()
                paused = True
                print("Paused")
            keyboard.wait('p')  # Wait until released

        elif keyboard.is_pressed('s'):
            stop_music()
            paused = False
            keyboard.wait('s')

        elif keyboard.is_pressed('esc'):
            stop_music()
            print("Exiting...")
            break

    except:
        break
