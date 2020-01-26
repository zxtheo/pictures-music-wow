#music_service
import winsound, time
from pysine import sine

def play_music(music_score):
    for note in music_score:
        sine(frequency=note.pitch, duration=note.length)
        # time.sleep(note.rest/1000)

def test(pitch, length):
    winsound.Beep(pitch, length)
