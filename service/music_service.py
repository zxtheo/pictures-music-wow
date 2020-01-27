#music_service
from pysine import sine
import time

def play_music(music_score):
    for note in music_score:
        sine(frequency=note.pitch, duration=note.length)
        # time.sleep(0.1)